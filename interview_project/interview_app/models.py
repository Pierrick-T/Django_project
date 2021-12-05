from django.db import models

# Create your models here.

class PhysicalPort(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location
class User(models.Model):
    physicalport = models.ForeignKey(PhysicalPort, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name