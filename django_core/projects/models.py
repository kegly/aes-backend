from django.db import models
from user_core.models import User
from teams.models import Team
from tags.models import Tag


class Project(models.Model):
    """
    Model for a project
    """
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='projects', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    group = models.ForeignKey(Team, related_name='projects', on_delete=models.CASCADE, blank=True, null=True)
    is_draft = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True, related_name='project')

    def __str__(self):
        return self.name
