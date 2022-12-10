from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from teams.models import Team


class Rating(models.Model):
    """
    A rating is a number between 1 and 5
    """
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='ratings')

    def __str__(self):
        return str(self.rating)
