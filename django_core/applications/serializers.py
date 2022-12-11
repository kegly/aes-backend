from rest_framework import serializers
from user_core.models import Student
from projects.models import Project
from .models import Application
from django.core.mail import send_mail
from django_core.settings import EMAIL_HOST_USER
from user_core.serializers import StudentSerializer
from projects.serializers import ProjectSerializer


class ApplicationSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()
    student = StudentSerializer()

    class Meta:
        model = Application
        fields = ('id', 'is_approved', 'student', 'project', 'owner')
