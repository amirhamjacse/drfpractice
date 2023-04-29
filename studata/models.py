from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    name = models.CharField(
        max_length=232, null=True
    )
    roll = models.IntegerField(
        null=True
    )
    city = models.CharField(
        max_length=232, null=True
    )
