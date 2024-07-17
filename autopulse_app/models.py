from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    vin = models.CharField(max_length=100)
    imei = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    renter_name = models.CharField(max_length=100)
    monthly_limit = models.IntegerField()
    oil_change = models.IntegerField()
    financial = models.IntegerField()
    STATUS_CHOICES = [("ready", "Ready"), ("leased", "Leased"), ("repair", "In Repair")]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="ready")
    car_rented_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Car model: {self.name}, Renter name: {self.renter_name}"
