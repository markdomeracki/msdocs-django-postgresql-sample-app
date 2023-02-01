import csv

import numpy as np
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import ComboCSVData, Project, Screen, Plate, Sample
from django.core.files.storage import FileSystemStorage
from os.path import exists
import os
import pandas as pd

from .serializer import UploadSerializer
# from module.aromyxapi.aromyxapi.Airtable import airtable

fs = FileSystemStorage(location='temp/')

class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response('Get API')

    def create(self, request):
        result_folder = 'out/PROG_025 - Commercial Projects/PROJ_025_49 Hanvon - Project 2 - 4 ' \
                        'samples/1xNTwDEtkaDPgE2jGt1jziIej8jqkrstt/Secondary '
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
        content_type = file_uploaded.content_type
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)


# def convert_AR_names(df_combo: pd.DataFrame) -> pd.DataFrame:
#     df_combo.rename(columns={'OR': 'AR'}, inplace=True)
#
#     receptor_dict = {}
#     for AR in df_combo['AR'].unique():
#         if AR[0:2] == 'AR':
#             if airtable.get_OR_from_AR(AR) != 'unmapped':
#                 receptor_dict[AR] = airtable.get_OR_from_AR(AR)
#             else:
#                 receptor_dict[AR] = AR
#         else:
#             receptor_dict[AR] = AR
#
#     # add receptor name column
#     df_combo['receptor_name'] = df_combo['AR']
#     df_combo.replace({'receptor_name': receptor_dict}, inplace=True)
#
#     # create dict to convert receptor names to ARs
#     AR_dict = {}
#     for receptor in df_combo['receptor_name'].unique():
#         if (receptor[0:3] == 'TAS') or (receptor[0:2] == 'OR'):
#             if airtable.get_AR_from_OR(receptor) != 'unmapped':
#                 AR_dict[receptor] = airtable.get_AR_from_OR(receptor)
#             else:
#                 AR_dict[receptor] = receptor
#         else:
#             AR_dict[receptor] = receptor
#
#     # replace convert ARs
#     df_combo.replace({'AR': AR_dict}, inplace=True)
#     return df_combo


def prepare_combo_csv(combo_path, result_folder):
    # read input file
    df_combo = pd.read_csv(combo_path, index_col=0)
    print(df_combo)

    # convert to/from AR_names
    # df_combo = convert_AR_names(df_combo)

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
    return df_combo


def get_project_table(df_combo) -> pd.DataFrame:
    # returns project table from df_combo
    df_project = df_combo.copy()

    # only get sample plates
    df_project = df_project[df_project['plate_type'] == 'sample']
    df_project = df_project[df_project['Plate'].str.contains('pentanol') == False]

    def f(x):
        d = {}
        d['sample_count'] = int(x['Plate'].nunique())
        d['screening_start_date'] = x['screening_start_date'].min()
        return pd.Series(d, index=['sample_count', 'screening_start_date'])
    df_project = df_project.groupby(['project_id', 'project_type'])[['Plate', 'screening_start_date']].apply(
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

    # select columns
    #     df_well = df_well[[]]
    return df_well


def get_sample_table(df_combo) -> pd.DataFrame:
    # returns sample table from df_combo
    df_sample = df_combo.copy()

    # get only sample records
    df_sample = df_sample[df_sample['plate_type'] == 'sample']
    df_sample = df_sample[df_sample['Plate'].str.contains('pentanol') == False]

    # select/order columns
    df_sample = df_sample[['sample_name', 'screening_start_date', 'concentration', 'well_id', 'plate_id']]
    df_sample.reset_index(drop=True, inplace=True)
    return df_sample


# df_combo = prepare_combo_csv(combo_path, result_folder)  # combo.csv


def add_data_from_csv(file):
    with open(file) as f:
        reader = csv.reader(f)

        for row in reader:

            or_ = ComboCSVData(
                ar=row[1],
                concentration=row[2],
                # Firefly=row[3],
                # Renilla=row[4],
                # Normalized=row[5],
                Project=row[6],
                # Plate=row[7],
                # Row=row[8],
                # Column=row[9],
                # Renilla_bgnorm=row[10],
                # Firefly_bgnorm=row[11],
                # Background_Subtracted=row[12],
                # Background_Divided=[13],
                # Plate_type=row[14],
                # Exp_datetime=row[15],

            )
            or_.save()
