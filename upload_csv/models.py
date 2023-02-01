from django.db import models


class ComboCSVData(models.Model):
    ar = models.CharField(max_length=100)
    concentration = models.CharField(max_length=100)
    # Firefly = models.DecimalField(max_digits=10, decimal_places=3)
    Project = models.CharField(max_length=100)
    # Plate = models.CharField(max_length=100)
    # Row = models.CharField(max_length=100)
    # Plate_type = models.CharField(max_length=100)
    # Exp_datetime = models.CharField(max_length=100)  # TODO Will need to figure this out.
    # Column = models.FloatField()
    # Renilla_bgnorm = models.FloatField()
    # Firefly_bgnorm = models.FloatField()
    # Background_Subtracted = models.FloatField()
    # Background_Divided = models.FloatField()
    # Renilla = models.FloatField()
    # Normalized = models.FloatField()


class Project(models.Model):
    project_id = models.TextField(db_column='project_ID', primary_key=True)
    project_type = models.TextField(blank=True, null=True)
    screening_start_date = models.TextField(blank=True, null=True)
    sample_count = models.FloatField(blank=True, null=True)


class Screen(models.Model):
    screen_id = models.TextField(db_column='screen_ID', primary_key=True)
    screen_type = models.TextField(blank=True, null=True)
    screening_start_date = models.TextField(blank=True, null=True)
    project_id = models.CharField(max_length=100)


class Plate(models.Model):
    plate_id = models.CharField(max_length=100)
    screening_start_date = models.CharField(max_length=100)
    plate_type = models.CharField(max_length=100)
    screen_id = models.CharField(max_length=100)


# class Well(models.Model): # TODO Will need to get these columns
#     sample_name = models.CharField(max_length=100)
#     screening_start_date = models.CharField(max_length=100)


class Sample(models.Model):
    sample_name = models.CharField(max_length=100)
    screening_start_date = models.CharField(max_length=100)
    concentration = models.CharField(max_length=100)
    well_id = models.CharField(max_length=100)
    plate_id = models.CharField(max_length=100)
