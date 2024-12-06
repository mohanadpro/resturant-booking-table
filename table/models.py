from django.db import models

# Create your models here.
class Table(models.Model):
    table_number = models.IntegerField()
    maximum_capability = models.IntegerField()