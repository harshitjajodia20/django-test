from django.shortcuts import render,redirect
from accounts.models import Accounts
# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        servername = request.POST['servername']
        server = Accounts.objects.all().filter(username=username, password=password, servername=servername)
        if server:
            server=server.values()[0]
            db=server['servername']
            #print(db)
            if db == 'car_db':
                #print('here i found car')
                return redirect('car') 
            if db == 'bike_db':
                #print('here i found bike')
                return redirect('bike')
            if db == 'owner_db':
                #print('here i found owner')
                return redirect('vehicle')
            return redirect('index')
        else:
            print('wrong credentials')
            return redirect('index')
    else:     
        return render(request,'index.html')
