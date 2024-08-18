from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vin = models.CharField(max_length=100)
    imei = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    renter_name = models.CharField(max_length=100, blank=True, null=True)
    monthly_limit = models.IntegerField()
    oil_change = models.IntegerField()
    financial = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100)
    final_odometer = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="car_images/")

    def __str__(self):
        return f"Image for {self.car.name}"
