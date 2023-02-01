# Generated by Django 4.1.5 on 2023-01-31 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_csv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComboCSVData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ar', models.CharField(max_length=100)),
                ('concentration', models.CharField(max_length=100)),
                ('Project', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.TextField(db_column='project_ID', primary_key=True, serialize=False)),
                ('project_type', models.TextField(blank=True, null=True)),
                ('screening_start_date', models.TextField(blank=True, null=True)),
                ('sample_count', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ProjectCsv',
        ),
    ]
