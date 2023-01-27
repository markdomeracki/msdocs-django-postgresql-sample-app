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
