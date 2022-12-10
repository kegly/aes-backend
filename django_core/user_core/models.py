from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_hr = models.BooleanField(default=False)
    email_confirmed = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['username', 'is_student']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return str(self.user)


class HR(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return str(self.user)
