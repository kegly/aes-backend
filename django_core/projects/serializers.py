from .models import Project
from rest_framework import serializers
from tags.models import Tag


class RetrieveProjectSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(read_only=True, slug_field='name', many=True)

    class Meta:
        model = Project
        fields = (
            'id', 'name', 'image', 'description', 'group', 'is_draft', 'created_at', 'updated_at',
            'tags', 'company')


class ProjectSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all(), required=False)

    class Meta:
        model = Project
        fields = (
            'id', 'name', 'image', 'description', 'group', 'is_draft', 'created_at', 'updated_at',
            'tags', 'company')
