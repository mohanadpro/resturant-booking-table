# Generated by Django 4.2.16 on 2024-12-06 21:02

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
