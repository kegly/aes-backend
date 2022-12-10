from django.shortcuts import render
from .serializers import CVSerializer
from .models import CV
from rest_framework import viewsets


# Create your views here.


class CVView(viewsets.ModelViewSet):
    serializer_class = CVSerializer
    queryset = CV.objects.all()
    http_method_names = ['get', 'post', 'patch']
