from django.db import models
from user_core.models import User


class Team(models.Model):
    """
    A team is a group of users that work together on a project
    """
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='teams')

    def __str__(self):
        return self.name
