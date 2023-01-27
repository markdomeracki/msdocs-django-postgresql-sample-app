from django.db import models


# TODO 	OR	conc	Firefly	Renilla	Normalized	Project	Plate	Row	Column	Renilla_bgnorm	Firefly_bgnorm
#  Background_Subtracted	Background_Divided	plate-type	exp datetime

class ComboCSVData(models.Model):
    OR = models.CharField(max_length=100)
    conc = models.CharField(max_length=100)
    Project = models.CharField(max_length=100)
    Plate = models.CharField(max_length=100)
    Row = models.CharField(max_length=100)
    Plate_type = models.CharField(max_length=100)
    Exp_datetime = models.CharField(max_length=100)  # TODO Will need to figure this out.
    Column = models.FloatField()
    Renilla_bgnorm = models.FloatField()
    Firefly_bgnorm = models.FloatField()
    Background_Subtracted = models.FloatField()
    Background_Divided = models.FloatField()
    Firefly = models.FloatField()
    Renilla = models.FloatField()
    Normalized = models.FloatField()
