from django.shortcuts import render
from .serializers import CVSerializer, RetrieveCVSerializer
from .models import CV
from rest_framework import viewsets
from .filters import CVFilter
from django.db.models import QuerySet
from rest_framework.viewsets import ReadOnlyModelViewSet


# Create your views here.


class CVView(viewsets.ModelViewSet):
    serializer_class = CVSerializer
    queryset = CV.objects.all()
    http_method_names = ['get', 'post', 'patch']

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'list':
            return RetrieveCVSerializer
        else:
            return CVSerializer


class CVFilterViewSet(ReadOnlyModelViewSet):
    queryset = CV.objects.all()
    filterset_class = CVFilter
    serializer_class = RetrieveCVSerializer

    def filter_queryset(self, queryset: QuerySet) -> QuerySet:
        queryset = super().filter_queryset(queryset)
        return queryset
