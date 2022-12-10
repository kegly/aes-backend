from django.db import models
from user_core.models import User
from teams.models import Team


class Project(models.Model):
    """
    Model for a project
    """
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='projects', blank=True, null=True)
    description = models.TextField()
    group = models.ForeignKey(Team, related_name='projects', on_delete=models.CASCADE)
    is_draft = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
