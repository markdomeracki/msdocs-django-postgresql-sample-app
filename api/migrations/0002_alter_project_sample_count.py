# Generated by Django 4.1.5 on 2023-01-23 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='sample_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
