from django.db import models
from django.utils import timezone

class user(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    Password= models.CharField(max_length=24)
    shif = models.DateTimeField()
    