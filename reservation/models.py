from django.db import models
from table.models import Table
from django.contrib.auth.models import User
from django import forms
# Create your models here.

class Reservation(models.Model):
    date = models.DateField()
    time = models.TimeField()
    table = models.ForeignKey(Table,on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    