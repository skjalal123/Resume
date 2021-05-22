from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.utils import timezone
# Create your models here.


class Academic(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
        )
    degree = models.CharField(
        max_length=100
        )
    year = models.IntegerField(
        default=2020
        )
    college = models.CharField(
        max_length=100
        )
    board = models.CharField(        max_length=100
        )
    percentage = models.FloatField(
        default=0
        )

class CareerObjective(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
        )
    objective = models.TextField()

class ExtraCurriculam(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
        )
    certificate = models.CharField(
        max_length=200
        )
    offered_By = models.CharField(
        max_length=50
        )
    year = models.DurationField()

class Experience(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
        )
    company_name = models.CharField(
        max_length=100
        )
    role = models.CharField(
        max_length=100
    )
    starting_date = models.DateField(
        default=timezone.now()
        )
    currently_Working = models.BooleanField(
        default=False
    )
    end_date = models.DateField(
        default=timezone.now(),
        blank=True
    )
    Description = models.TextField()

class Skill(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    languages = models.CharField(
        max_length=25
    )
    Version = models.CharField(
        max_length=25
    )

class Interested_Area(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    Interested = models.CharField(
        max_length=25
        )

class Project(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    project_name = models.CharField(
        max_length=100
        )
    gitUrl = models.URLField(
        blank=True
    )
    Description = models.TextField()

class Hobby(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    Interested = models.CharField(
        max_length=25
        )