from django.shortcuts import render
from django.db.models import QuerySet
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Project
from .filters import ProjectFilter
from .serializers import RetrieveProjectSerializer, ProjectSerializer
from rest_framework import viewsets


# Create your views here.
class ProjectFilterViewSet(ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    filterset_class = ProjectFilter
    serializer_class = RetrieveProjectSerializer

    def filter_queryset(self, queryset: QuerySet) -> QuerySet:
        queryset = super().filter_queryset(queryset)
        return queryset


class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    http_method_names = ['get', 'post', 'patch']

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'list':
            return RetrieveProjectSerializer
        else:
            return ProjectSerializer
