from django.urls import include, path
from . import views

urlpatterns = [
    path('create/project', views.Project.as_view()),
    path('create/screen', views.Screen.as_view()),
    path('create/plate', views.Plate.as_view()),
    path('create/receptor', views.Receptor.as_view()),
    path('create/well', views.Well.as_view())
]
