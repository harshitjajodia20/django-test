from django.contrib import admin
from .models import Bike,Bikerepair,Bikeshop
# Register your models here.

admin.site.register(Bike)
admin.site.register(Bikerepair)
admin.site.register(Bikeshop)