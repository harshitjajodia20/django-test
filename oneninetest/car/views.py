from django.shortcuts import render,redirect
from .models import Carshop,Carrepair,Car
# Create your views here.

def car(request):
    if request.method == 'POST':
        table = request.POST['table']
        print(table)
        if(table == 'Carrepair'):
            data = Carrepair.objects.using('car_db').all().order_by('-id')[:10]
            print(data.values()[0])
            context = {
                "Carrepair":data
            }
            return render(request,'car.html',context)
        
        if(table == 'Car'):
            data = Car.objects.using('car_db').all().order_by('-id')[:10]
            print(data.values()[0])
            context = {
                "Car":data
            }
            return render(request,'car.html',context)
        if(table == 'Carshop'):
            data = Carshop.objects.using('car_db').all().order_by('-id')[:10]
            print(data.values()[0])
            context = {
                "Carshop":data
            }
            return render(request,'car.html',context)
        return redirect('car')
    else:    
        return render(request,'car.html')
