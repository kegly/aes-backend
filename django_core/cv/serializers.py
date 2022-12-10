from .models import CV
from rest_framework import serializers


class CVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = (
            'id', 'student', 'image', 'job', 'salary', 'about_me', 'work_places', 'skills', 'education', 'contacts',
            'phone_number', 'pet_projects', 'rating')
