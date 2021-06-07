from django.db import models

# Create your models here.
class Owner(models.Model):
    vehicleOwned = models.CharField(max_length=100)
    ownername = models.CharField(max_length=100)
    ownerAddress = models.CharField(max_length=100)
    vehicle_price = models.IntegerField()

    def __str__(self):
        return self.ownername

class Vehicle(models.Model):
    vehicle_name = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100)
    vehicle_company = models.CharField(max_length=100)
    vehicle_purchase_date = models.DateField(blank=True)

    def __str__(self):
        return self.vehicle_name