from rest_framework import generics, permissions
from .serializers import *
from django.shortcuts import render
from .models import *


class Project(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class Screen(generics.CreateAPIView):
    queryset = Screen.objects.all()
    serializer_class = ScreenSerializer
    permission_classes = [permissions.IsAuthenticated]


class Plate(generics.CreateAPIView):
    queryset = Plate.objects.all()
    serializer_class = PlateSerializer
    permission_classes = [permissions.IsAuthenticated]


class Receptor(generics.CreateAPIView):
    queryset = Receptor.objects.all()
    serializer_class = ReceptorSerializer
    permission_classes = [permissions.IsAuthenticated]


class Well(generics.CreateAPIView):
    queryset = Well.objects.all()
    serializer_class = WellSerializer
    permission_classes = [permissions.IsAuthenticated]

