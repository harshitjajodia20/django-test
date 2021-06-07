from django.shortcuts import render,redirect
from .models import Vehicle,Owner
# Create your views here.
def vehicle(request):
    if request.method == 'POST':
        table = request.POST['table']
        print(table)
        if(table == 'Vehicle'):
            data = Vehicle.objects.using('owner_db').all().order_by('-id')[:10]
            context = {
                "Vehicle":data
            }
            return render(request,'vehicle.html',context)
        
        if(table == 'Owner'):
            data = Owner.objects.using('owner_db').all().order_by('-id')[:10]
            context = {
                "Owner":data
            }
            return render(request,'vehicle.html',context)
        return redirect('vehicle')
    else:    
        return render(request,'vehicle.html')
        