from django.db import models

# Create your models here.
class Bike(models.Model):
    bikename = models.CharField(max_length=100)
    ownername = models.CharField(max_length=100)
    bike_price = models.CharField(max_length=100)
    def __str__(self):
        return self.bikename

class Bikeshop(models.Model):
    bikename = models.CharField(max_length=100)
    quantity = models.IntegerField()
    bike_price = models.IntegerField()
    def __str__(self):
        return self.bikename

class Bikerepair(models.Model):
    bikename = models.CharField(max_length=100)
    ownername = models.CharField(max_length=50)
    startdate = models.DateField(blank=True)
    def __str__(self):
        return self.bikename
