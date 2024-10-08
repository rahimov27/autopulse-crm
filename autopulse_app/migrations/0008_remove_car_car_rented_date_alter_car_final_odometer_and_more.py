# Generated by Django 4.2.14 on 2024-07-18 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autopulse_app', '0007_car_final_odometer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='car_rented_date',
        ),
        migrations.AlterField(
            model_name='car',
            name='final_odometer',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='financial',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='renter_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='status',
            field=models.CharField(max_length=100),
        ),
    ]
