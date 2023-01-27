import csv

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import ComboCSVData
from django.core.files.storage import FileSystemStorage
from os.path import exists
import os
import pandas as pd

from .serializer import UploadSerializer

fs = FileSystemStorage(location='temp/')


class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response('Get API')

    def create(self, request):
        data_list = []
        file_uploaded = request.FILES.get('file_uploaded')
        print(exists('temp/temp.csv'))
        if exists('temp/temp.csv'):
            os.remove('temp/temp.csv')

        file_name = fs.save(
            "temp.csv", file_uploaded
        )
        tmp_file = fs.path(file_name)
        add_data_from_csv(tmp_file)

        content_type = file_uploaded.content_type
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)


def add_data_from_csv(file):
    with open(file) as f:
        reader = csv.reader(f)

        for row in reader:
            print(row)

            or_ = ComboCSVData(
                OR=row[1],
                conc=row[2],
                Firefly=row[3],
                Renilla=row[4],
                Normalized=row[5],
                Project=row[6],
                Plate=row[7],
                Row=row[8],
                Column=row[9],
                Renilla_bgnorm=row[10],
                Firefly_bgnorm=row[11],
                Background_Subtracted=row[12],
                Background_Divided=[13],
                Plate_type=row[14],
                Exp_datetime=row[15],

            )
            or_.save()

# def add_data_from_csv(file):
#     temp_data = pd.read_csv(file)
#     data = [
#         ComboCSVData(
#             OR=temp_data['OR']
#         )
#         for row in temp_data['id']
#
#     ]
#     ComboCSVData.objects.bulk_create(data)
