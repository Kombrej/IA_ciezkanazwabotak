from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    shift= models.TimeField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
