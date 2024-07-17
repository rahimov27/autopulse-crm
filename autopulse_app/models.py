from django.db import models


# Create your models here.
class Car(models.Model):
    vin = models.CharField(max_length=100)
    imei = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    renter_name = models.CharField(max_length=100)
    mountly_limit = models.IntegerField()
    oil_change = models.IntegerField()
    financial = models.IntegerField()
    STATUS_CHOICES = [("ready", "Ready"), ("leased", "Leased"), ("repair", "In Repair")]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="ready")
    car_rented_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Car model:{self.name}, Renter name:{self.renter_name}"
