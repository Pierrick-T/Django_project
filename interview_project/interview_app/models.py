from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)

class PhysicalPort(models.Model):
    # Add the Many to one relation here
    location = models.CharField(max_length=30)
