from django.db import models
from user_core.models import Student
from projects.models import Project


# Create your models here.
class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.project.name

    class Meta:
        verbose_name = "Заявка в проект"
        verbose_name_plural = "Заявки в проект"
