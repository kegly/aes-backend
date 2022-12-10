from django.contrib.auth.models import AbstractUser
from django.db import models
from tags.models import Tag


class User(AbstractUser):
    """
    A user is a person that has an account on the website
    """
    is_student = models.BooleanField(default=False)
    is_hr = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['email', 'is_student', 'is_hr']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Student(models.Model):
    class GENDER(models.TextChoices):
        male = 'male', 'male'
        female = 'female', 'female'

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, choices=GENDER.choices, default=GENDER.male)
    language = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"


class HR(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return str(self.user)
