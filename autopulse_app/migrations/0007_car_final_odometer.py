# Generated by Django 4.2.14 on 2024-07-17 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autopulse_app', '0006_car_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='final_odometer',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
