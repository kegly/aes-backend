from django.db import models
from user_core.models import Student, HR
from projects.models import Project
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify


# Create your models here.
class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    is_approved = models.BooleanField(default=False)

    # _hr = models.IntegerField(max_length=20, db_column='hr')
    owner = models.ForeignKey(HR, on_delete=models.CASCADE, blank=True, null=True)

    #
    #
    #
    # @receiver(pre_save)
    # def set_owner(sender, instance, *args, **kwargs):
    #     instance.owner = slugify(instance.project.owner)
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        self.owner = self.project.owner

    def __str__(self):
        return self.project.name

    class Meta:
        verbose_name = "Заявка в проект"
        verbose_name_plural = "Заявки в проект"
