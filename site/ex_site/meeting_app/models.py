from django.db import models

# Create your models here.

class Human(models.Model):
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

class Customer(models.Model):
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)


