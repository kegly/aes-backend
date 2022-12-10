from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student

from django.db.models import QuerySet
from rest_framework.viewsets import ReadOnlyModelViewSet


class StudentView(viewsets.ModelViewSet):
    serializer_class = StudentSerializer

    queryset = Student.objects.all()
    http_method_names = ['get', 'post', 'patch']


