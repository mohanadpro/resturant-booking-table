from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.

AREAS = ((0, "Near to fireplace"), (1, "Terrace"), (2, "Smoker"), (3,"Inside"), (4, "Second floor"))

class Reservation(models.Model):
    date = models.DateField()
    time = models.TimeField()
    area = models.IntegerField(choices=AREAS, default=0)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    have_kids = models.BooleanField(default=False)
    note = models.TextField(default='')
    