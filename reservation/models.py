from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.safestring import mark_safe
# Create your models here.

AREAS = ((0, "Near to fireplace"),
         (1, "Terrace"), (2, "Smoker"),
         (3, "Inside"), (4, "Second floor"))


class Reservation(models.Model):
    date = models.DateField()
    time = models.TimeField()
    area = models.IntegerField(choices=AREAS, default=0)
    how_many_people = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(25),
            MinValueValidator(1)
        ])
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    have_kids = models.BooleanField(default=False)
    special_request = models.CharField(max_length=250, default=None, blank=True, null=True)
    note = models.TextField(default=None, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
