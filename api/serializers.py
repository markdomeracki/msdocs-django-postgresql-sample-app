from rest_framework import serializers
from .models import Project, Screen, Plate, Receptor, Sample, Well

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['project_id', 'project_type', 'screening_start_date', 'sample_count']


class ScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screen
        fields = ['screen_id', 'screen_type', 'control_type', 'created_at']


class PlateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plate
        fields = ['plate_id', 'created_at', 'plate_type']


class ReceptorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receptor
        fields = ['receptor_id', 'full_name', 'variant', 'ar_name', 'allele_sequence', 'gene_name']


class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = ['sample_name', 'created_at', 'concentration', 'well', 'plate', 'sample_id']


class WellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Well
        fields = '__all__'

