from django.db import models


class ProjectCsv(models.Model):
    project_id = models.CharField(primary_key=True, max_length=50)
    project_type = models.CharField(max_length=50)
    screening_start_date = models.CharField(max_length=50)
    sample_count = models.IntegerField()

    # project = {
    #     'project_id': '2',
    #     'Project_type': '2',
    #     'screening_start_date': '2',
    #     'sample_count': '2',
    # }
