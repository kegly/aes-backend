from django.db import models
from user_core.models import User, HR, Company
from teams.models import Team
from tags.models import Tag


class Project(models.Model):
    """
    Model for a project
    """
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(HR, blank=True, null=True, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='projects', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    group = models.ForeignKey(Team, related_name='projects', on_delete=models.CASCADE, blank=True, null=True)
    is_draft = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True, related_name='project')
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
