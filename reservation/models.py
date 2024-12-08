from django.db import models
from table.models import Table
# Create your models here.

class Reservation(models.Model):
    date = models.DateField()
    time = models.TimeField()
    table = models.ForeignKey(Table,on_delete=models.CASCADE)
    