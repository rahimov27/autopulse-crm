# Generated by Django 4.2.14 on 2024-07-18 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autopulse_app', '0009_car_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_image',
            field=models.ImageField(upload_to='car_images/'),
        ),
    ]
