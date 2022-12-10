from rest_framework import viewsets
from .serializers import StudentSerializer, CompanySerializer
from .models import Student, Company

from django.db.models import QuerySet
from rest_framework.viewsets import ReadOnlyModelViewSet


class StudentView(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    http_method_names = ['get', 'post', 'patch']


class CompanyView(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    http_method_names = ['get', 'post']
