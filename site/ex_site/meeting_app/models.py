from django.db import models
from datetime import date, timedelta

# Create your models here.

class Human(models.Model):
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

class Customer(models.Model):
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

class DateEntry(models.Model):
    date_entry = models.DateField()
    time_entry = models.TimeField()
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    activate = models.BooleanField(default=False)


