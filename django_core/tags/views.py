from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Tag
from .serializers import TagSerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
