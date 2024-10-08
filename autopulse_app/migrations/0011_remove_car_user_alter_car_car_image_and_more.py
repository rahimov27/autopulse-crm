# Generated by Django 4.2.14 on 2024-07-18 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autopulse_app', '0010_alter_car_car_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='user',
        ),
        migrations.AlterField(
            model_name='car',
            name='car_image',
            field=models.ImageField(blank=True, null=True, upload_to='cars/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='final_odometer',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='renter_name',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
