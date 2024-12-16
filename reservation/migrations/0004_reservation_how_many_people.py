# Generated by Django 4.2.16 on 2024-12-15 23:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_reservation_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='how_many_people',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]
