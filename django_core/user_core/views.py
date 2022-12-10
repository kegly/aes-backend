from rest_framework import viewsets
from .serializers import StudentSerializer, CompanySerializer, HRSerializer
from .models import Student, Company, HR

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


class HRView(viewsets.ModelViewSet):
    serializer_class = HRSerializer
    queryset = HR.objects.all()
    http_method_names = ['get', 'post', 'patch']

