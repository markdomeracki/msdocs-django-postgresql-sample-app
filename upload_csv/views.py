import csv

import numpy as np
import requests
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import Project, Screen, Plate, Sample, ResultsFolder, Well
from django.core.files.storage import FileSystemStorage
from os.path import exists
import os
import pandas as pd

from .serializer import UploadSerializer, ResultsFolderSerializer

fs = FileSystemStorage(location='temp/')


class ResultsFolderView(generics.ListCreateAPIView):
    queryset = ResultsFolder.objects.all()
    serializer_class = ResultsFolderSerializer


class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response('Get API')

    def create(self, request):
        path = []
        paths = ResultsFolder.objects.all()
        for x in paths:
            path.append(x.file_path)

        result_folder = path[0]
        print(result_folder)
        file_uploaded = request.FILES.get('file_upload')
        if exists('temp/temp.csv'):
            os.remove('temp/temp.csv')

        file_name = fs.save(
            "temp.csv", file_uploaded
        )
        tmp_file = fs.path(file_name)
        df_combo = prepare_combo_csv(tmp_file, result_folder)

        df_project = get_project_table(df_combo)
        Project.objects.bulk_create(
            Project(**vals) for vals in df_project.to_dict('records')
        )

        df_screen = get_screen_table(df_combo)
        Screen.objects.bulk_create(
            Screen(**vals) for vals in df_screen.to_dict('records')
        )

        df_plate = get_plate_table(df_combo)
        Plate.objects.bulk_create(
            Plate(**vals) for vals in df_plate.to_dict('records')
        )
        # TODO Create a well insert statement

        df_sample = get_sample_table(df_combo)
        Sample.objects.bulk_create(
            Sample(**vals) for vals in df_sample.to_dict('records')
        )

        df_well = get_well_table(df_combo)
        Well.objects.bulk_create(
            Well(**vals) for vals in df_well.to_dict('records')
        )

        content_type = file_uploaded.content_type
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)


def prepare_combo_csv(combo_path, result_folder):
    '''
    Reads a combo.csv from combo_path, extracts important
    info from the result_folder path, transforms data and
    reformats column names to a useable format to create the
    subsequent tables.
    '''
    # read input file
    df_combo = pd.read_csv(combo_path, index_col=0)

    # get path folders
    path = os.path.normpath(result_folder)
    path_folders = path.split(os.sep)
    screen_type = os.path.basename(path).lower()

    # add PROG and PROJ from path
    df_combo['PROG'] = [s for s in path_folders if s.startswith('PROG')][0]
    df_combo['PROJ'] = [s for s in path_folders if s.startswith('PROJ')][0]

    # add screen_type
    df_combo['screen_type'] = screen_type
    # add plate ID
    df_combo['plate_id'] = df_combo['Project'] + "/" + df_combo['Plate']
    # set well_ID
    df_combo['well_id'] = ["well_" + str(x + 1) for x in np.arange(len(df_combo))]
    df_combo['sample_name'] = df_combo['Plate']

    # rename columns
    df_combo.rename(columns={'PROJ': 'project_id',
                             'exp datetime': 'screening_start_date',
                             'PROG': 'project_type',
                             'Project': 'screen_id',
                             'conc': 'concentration',
                             'plate-type': 'plate_type'}, inplace=True)
    # lowercase all columns
    df_combo.columns = [col.lower() for col in df_combo.columns]
    return df_combo


def get_project_table(df_combo) -> pd.DataFrame:
    # returns project table from df_combo
    df_project = df_combo.copy()

    # only get sample plates
    df_project = df_project[df_project['plate_type'] == 'sample']
    df_project = df_project[df_project['plate'].str.contains('pentanol') == False]

    def f(x):
        d = {}
        d['sample_count'] = int(x['plate'].nunique())
        d['screening_start_date'] = x['screening_start_date'].min()
        return pd.Series(d, index=['sample_count', 'screening_start_date'])

    # get sample counts for each project
    df_project = df_project.groupby(['project_id', 'project_type'])[['plate', 'screening_start_date']].apply(
        f).reset_index()
    # reset index
    df_project.reset_index(drop=True, inplace=True)
    # reorder columns
    df_project = df_project[['project_id', 'project_type', 'screening_start_date', 'sample_count']]
    return df_project


def get_screen_table(df_combo) -> pd.DataFrame:
    # returns screen table from df_combo

    df_screen = df_combo.copy()
    # get unique projects
    df_screen.drop_duplicates('screen_id', inplace=True)
    df_screen.reset_index(drop=True, inplace=True)

    # select columns
    df_screen = df_screen[['screen_id', 'screen_type', 'screening_start_date', 'project_id']]
    return df_screen


def get_plate_table(df_combo) -> pd.DataFrame:
    # returns plate table from df_combo

    df_plate = df_combo.copy()

    # get unique plate_ids
    df_plate.drop_duplicates(['plate_id', 'plate_type'], inplace=True)
    df_plate.reset_index(drop=True, inplace=True)

    # select columns
    df_plate = df_plate[['plate_id', 'screening_start_date', 'plate_type', 'screen_id']]
    return df_plate


def get_well_table(df_combo) -> pd.DataFrame:
    # returns wells table from df_combo
    df_well = df_combo.copy()

    return df_well


def get_sample_table(df_combo) -> pd.DataFrame:
    # returns sample table from df_combo
    df_sample = df_combo.copy()

    # get only sample records
    df_sample = df_sample[df_sample['plate_type'] == 'sample']
    df_sample = df_sample[df_sample['plate'].str.contains('pentanol') == False]

    # select/order columns
    df_sample = df_sample[['sample_name', 'screening_start_date', 'concentration', 'well_id', 'plate_id']]
    df_sample.reset_index(drop=True, inplace=True)
    return df_sample
