from rest_framework.serializers import Serializer, FileField
from rest_framework import serializers
from .models import ResultsFolder


class UploadSerializer(Serializer):
    file_uploaded = FileField()

    class Meta:
        fields = ['file_upload']


class ResultsFolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultsFolder
        fields = '__all__'


