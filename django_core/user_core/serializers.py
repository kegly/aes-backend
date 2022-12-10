from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer, UserSerializer, UserDeleteSerializer
from rest_framework import serializers
from .models import Student, Company, HR

User = get_user_model()


class BaseUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class BaseUserSerializer(UserSerializer):
    student = StudentSerializer()

    class Meta(UserSerializer.Meta):
        model = User
        fields = ('id', 'username', 'is_student', 'is_hr', 'student')


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class HRSerializer(serializers.ModelSerializer):
    class Meta:
        model = HR
        fields = '__all__'
