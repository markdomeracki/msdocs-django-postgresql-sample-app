from django.db import models


class ResultsFolder(models.Model):
    file_path = models.CharField(max_length=300)


class Project(models.Model):
    project_id = models.CharField(max_length=100)
    project_type = models.CharField(max_length=100)
    screening_start_date = models.DateTimeField()
    sample_count = models.FloatField()


class Screen(models.Model):
    screen_id = models.CharField(max_length=100)
    screen_type = models.CharField(max_length=100)
    screening_start_date = models.DateTimeField()
    project_id = models.CharField(max_length=100)


class Plate(models.Model):
    plate_id = models.CharField(max_length=100)
    screening_start_date = models.DateTimeField()
    plate_type = models.CharField(max_length=100)
    screen_id = models.CharField(max_length=100)


class Well(models.Model):
    ar = models.CharField(max_length=100)
    concentration = models.FloatField()
    firefly = models.FloatField()
    renilla = models.FloatField()
    normalized = models.FloatField()
    screen_id = models.CharField(max_length=100)
    plate = models.CharField(max_length=100)
    row = models.CharField(max_length=100)
    column = models.IntegerField()
    receptor_name = models.CharField(max_length=100)
    renilla_bgnorm = models.FloatField()
    firefly_bgnorm = models.FloatField()
    background_subtracted = models.FloatField()
    background_divided = models.FloatField()
    plate_type = models.CharField(max_length=100)
    screening_start_date = models.DateTimeField()
    project_type = models.CharField(max_length=100)
    project_id = models.CharField(max_length=100)
    screen_type = models.CharField(max_length=100)
    plate_id = models.CharField(max_length=100)
    well_id = models.CharField(max_length=100)
    sample_name = models.CharField(max_length=100)


class Sample(models.Model):
    sample_name = models.CharField(max_length=100)
    screening_start_date = models.DateTimeField()
    concentration = models.FloatField()
    well_id = models.CharField(max_length=100)
    plate_id = models.CharField(max_length=100)
