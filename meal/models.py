from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class Meal(models.Model):
    name = models.CharField(max_length=200)
    image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
