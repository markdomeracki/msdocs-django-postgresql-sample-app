# Generated by Django 4.1.5 on 2023-01-27 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_csv', '0003_rename_or_combocsvdata_ar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='combocsvdata',
            name='Firefly',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
