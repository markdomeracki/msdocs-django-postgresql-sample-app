# Generated by Django 4.1.5 on 2023-02-01 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_csv', '0005_alter_screen_project_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate_id', models.CharField(max_length=100)),
                ('screening_start_date', models.CharField(max_length=100)),
                ('plate_type', models.CharField(max_length=100)),
                ('screen_id', models.CharField(max_length=100)),
            ],
        ),
    ]