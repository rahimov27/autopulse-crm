# Generated by Django 4.2.14 on 2024-08-11 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autopulse_app', '0015_remove_car_car_image_carimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='CarImage',
        ),
    ]
