from django.db import models

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Plate(models.Model):
    plate_id = models.TextField(db_column='plate_ID', primary_key=True)  # Field name made lowercase.
    created_at = models.TextField(blank=True, null=True)
    plate_type = models.TextField(blank=True, null=True)
    screen_id = models.TextField(db_column='screen_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'plate'


class Project(models.Model):
    project_id = models.TextField(db_column='project_ID', primary_key=True)  # Field name made lowercase.
    project_type = models.TextField(blank=True, null=True)
    screening_start_date = models.TextField(blank=True, null=True)
    sample_count = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'project'


class Receptor(models.Model):
    receptor_id = models.TextField(db_column='receptor_ID', primary_key=True)  # Field name made lowercase.
    full_name = models.TextField(blank=True, null=True)
    variant = models.TextField(blank=True, null=True)
    ar_name = models.TextField(db_column='AR_name', blank=True, null=True)  # Field name made lowercase.
    allele_sequence = models.TextField(blank=True, null=True)
    gene_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'receptor'


class Sample(models.Model):
    sample_name = models.TextField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    concentration = models.FloatField(blank=True, null=True)
    well = models.ForeignKey('Well', models.DO_NOTHING, db_column='well_ID', blank=True,
                             null=True)  # Field name made lowercase.
    plate = models.ForeignKey(Plate, models.DO_NOTHING, db_column='plate_ID', blank=True,
                              null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'sample'


class Screen(models.Model):
    screen_id = models.TextField(db_column='screen_ID', primary_key=True)  # Field name made lowercase.
    screen_type = models.TextField(blank=True, null=True)
    control_type = models.TextField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    project = models.ForeignKey(Project, models.DO_NOTHING, db_column='project_ID', blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'screen'


class Well(models.Model):
    or_field = models.TextField(db_column='OR', blank=True,
                                null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    firefly = models.FloatField(db_column='Firefly', blank=True, null=True)  # Field name made lowercase.
    renilla = models.FloatField(db_column='Renilla', blank=True, null=True)  # Field name made lowercase.
    normalized = models.FloatField(db_column='Normalized', blank=True, null=True)  # Field name made lowercase.
    project = models.TextField(db_column='Project', blank=True, null=True)  # Field name made lowercase.
    plate = models.TextField(db_column='Plate', blank=True, null=True)  # Field name made lowercase.
    renilla_bgnorm = models.FloatField(db_column='Renilla_bgnorm', blank=True, null=True)  # Field name made lowercase.
    firefly_bgnorm = models.FloatField(db_column='Firefly_bgnorm', blank=True, null=True)  # Field name made lowercase.
    plate_type = models.TextField(db_column='plate-type', blank=True,
                                  null=True)  # Field renamed to remove unsuitable characters.
    background_subtracted = models.FloatField(db_column='Background_Subtracted', blank=True,
                                              null=True)  # Field name made lowercase.
    background_divided = models.FloatField(db_column='Background_Divided', blank=True,
                                           null=True)  # Field name made lowercase.
    control_type = models.TextField(blank=True, null=True)
    exp_datetime = models.TextField(db_column='exp datetime', blank=True,
                                    null=True)  # Field renamed to remove unsuitable characters.
    prog = models.TextField(db_column='PROG', blank=True, null=True)  # Field name made lowercase.
    proj = models.TextField(db_column='PROJ', blank=True, null=True)  # Field name made lowercase.
    row = models.TextField(db_column='Row', blank=True, null=True)  # Field name made lowercase.
    column = models.FloatField(db_column='Column', blank=True, null=True)  # Field name made lowercase.
    conc = models.FloatField(blank=True, null=True)
    ar = models.TextField(db_column='AR', blank=True, null=True)  # Field name made lowercase.
    plate_0 = models.ForeignKey(Plate, models.DO_NOTHING, db_column='plate_ID', blank=True,
                                null=True)  # Field name made lowercase. Field renamed because of name conflict.
    well_id = models.TextField(db_column='well_ID', primary_key=True)  # Field name made lowercase.
    screen_type = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'well'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)