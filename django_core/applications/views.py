from django.shortcuts import render
from .serializers import ApplicationSerializer
from .models import Application
from projects.models import Project
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .filters import ApplicationFilter
from django.db.models import QuerySet
from rest_framework.viewsets import ReadOnlyModelViewSet


# Create your views here.


class ApplicationView(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
    http_method_names = ['get', 'post', 'patch']


# Create your views here.

class ApplicationsFilterViewSet(ReadOnlyModelViewSet):
    queryset = Application.objects.all()
    filterset_class = ApplicationFilter
    serializer_class = ApplicationSerializer

    def filter_queryset(self, queryset: QuerySet) -> QuerySet:
        queryset = super().filter_queryset(queryset)
        return queryset
