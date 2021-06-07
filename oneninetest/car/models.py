from django.db import models

# Create your models here.
class Car(models.Model):
    carname = models.CharField(max_length=100)
    ownername = models.CharField(max_length=100)

    def __str__(self):
        return self.carname
        
class Carshop(models.Model):
    carname = models.CharField(max_length=100)
    quantity = models.IntegerField()
    car_price = models.IntegerField()
    def __str__(self):
        return self.carname

class Carrepair(models.Model):
    carname = models.CharField(max_length=100)
    ownername = models.CharField(max_length=50)
    startdate = models.DateField(blank=True)
    def __str__(self):
        return self.carname