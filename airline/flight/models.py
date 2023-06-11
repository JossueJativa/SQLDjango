from django.db import models

# Create your models here.
class Flight (models.Model):
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    duration = models.IntegerField()