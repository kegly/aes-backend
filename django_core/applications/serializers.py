from rest_framework import serializers
from user_core.models import Student
from projects.models import Project
from .models import Application
from django.core.mail import send_mail
from django_core.settings import EMAIL_HOST_USER
from user_core.serializers import StudentSerializer


class ApplicationSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    student = StudentSerializer()

    class Meta:
        model = Application
        fields = ('id', 'is_approved', 'student', 'project', 'owner')
