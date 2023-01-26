from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
import pandas as pd


from . serializer import UploadSerializer


class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response('Get API')

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        print(pd.read_csv(file_uploaded))
        content_type = file_uploaded.content_type
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)
