from django.shortcuts import render,redirect
from .models import Bike,Bikeshop,Bikerepair
# Create your views here.
def bike(request):
    if request.method == 'POST':
        table = request.POST['table']
        print(table)
        if(table == 'Bikerepair'):
            data = Bikerepair.objects.using('bike_db').all().order_by('-id')[:10]
            context = {
                "Bikerepair":data
            }
            return render(request,'bike.html',context)
        
        if(table == 'Bike'):
            data = Bike.objects.using('bike_db').all().order_by('-id')[:10]
            context = {
                "Bike":data
            }
            return render(request,'bike.html',context)
        if(table == 'Bikeshop'):
            data = Bikeshop.objects.using('bike_db').all().order_by('-id')[:10]
            context = {
                "Bikeshop":data
            }
            return render(request,'bike.html',context)
        return redirect('bike')
    else:    
        return render(request,'bike.html')
        