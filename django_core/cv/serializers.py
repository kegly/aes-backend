from .models import CV
from rest_framework import serializers
from tags.models import Tag


class CVSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField(read_only=True)
    skills = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all(), required=False)

    class Meta:
        model = CV
        fields = (
            'id', 'student', 'image', 'job', 'salary', 'about_me', 'work_places', 'skills', 'education', 'contacts',
            'phone_number', 'pet_projects', 'rating')


class RetrieveCVSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField(read_only=True)
    skills = serializers.SlugRelatedField(read_only=True, slug_field='name', many=True)

    class Meta:
        model = CV
        fields = (
            'id', 'student', 'image', 'job', 'salary', 'about_me', 'work_places', 'skills', 'education', 'contacts',
            'phone_number', 'pet_projects', 'rating')
