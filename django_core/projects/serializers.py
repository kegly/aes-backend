from .models import Project
from rest_framework import serializers
from tags.models import Tag
from user_core.models import Company


class RetrieveProjectSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(read_only=True, slug_field='name', many=True)
    company = serializers.SlugRelatedField(read_only=True, slug_field='name')
    owner = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Project
        fields = (
            'id', 'name', 'owner', 'image', 'description', 'group', 'is_draft', 'created_at', 'updated_at',
            'tags', 'company', 'is_premium')


class ProjectSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all(), required=False)
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(), required=False)
    owner = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(), required=False)

    class Meta:
        model = Project
        fields = (
            'id', 'name', 'owner', 'image', 'description', 'group', 'is_draft', 'created_at', 'updated_at',
            'tags', 'company', 'is_premium')
