from django.db import models
from .shift import ShiftTypes
from django.contrib.auth.models import User
# Create your models here.


class Staff(models.Model):
    name = models.CharField(max_length=30, blank=True)
    surname = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True, null=True,blank=True)
    password =models.CharField(max_length=30, null=True, blank=True)
    Shift_type= models.CharField(max_length=8,choices=ShiftTypes, blank=True)
    ShiftStartTime = models.IntegerField(null=True, blank=True)
    ShiftEndTime = models.CharField(max_length=10, null=True, blank=True)
    OverTime = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return f"{self.name} {self.surname} {self.ShiftStartTime} {self.ShiftEndTime} {self.Shift_Type} {self.OverTime}"

    