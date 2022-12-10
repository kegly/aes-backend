from django.db import models
from tags.models import Tag
from user_core.models import Student


# Create your models here.
class CV(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_images', blank=True, max_length=255)
    job = models.CharField(max_length=50, blank=True, null=True)
    salary = models.CharField(max_length=50, blank=True, null=True)
    about_me = models.CharField(max_length=512, blank=True, null=True)
    work_places = models.CharField(max_length=512, blank=True, null=True)
    skills = models.ManyToManyField(Tag, blank=True, null=True, related_name='cv')
    education = models.CharField(max_length=512, blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    contacts = models.CharField(max_length=128, blank=True, null=True)
    pet_projects = models.URLField(max_length=200, blank=True, null=True)

    @property
    def rating(self):
        return 0
