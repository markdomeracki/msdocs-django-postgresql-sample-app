# Generated by Django 4.1.5 on 2023-02-01 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_csv', '0004_rename_project_screen_project_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screen',
            name='project_id',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
