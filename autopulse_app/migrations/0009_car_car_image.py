# Generated by Django 4.2.14 on 2024-07-18 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autopulse_app', '0008_remove_car_car_rented_date_alter_car_final_odometer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_image',
            field=models.ImageField(default=1, upload_to='car_images/% Y/% m/% d/'),
            preserve_default=False,
        ),
    ]
