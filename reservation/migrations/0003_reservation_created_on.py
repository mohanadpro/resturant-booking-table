# Generated by Django 4.2.16 on 2024-12-14 15:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_reservation_area_reservation_have_kids_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
