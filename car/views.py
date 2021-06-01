from car.models import Car
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
def home(req):
    cars=Car.objects.all()
    print(cars)
    return render(req,'car/homepage.html',{"cars":cars})
# Create your views here.
def registercar(request):
    if request.method=="GET":
        return render(request,'car/register.html')
    else:
        print(request.POST.keys())
        mycar=Car()
        mycar.company=request.POST.get("company")
        mycar.about=request.POST.get("about")
        mycar.modelno=request.POST.get("modelno")
        mycar.millage=request.POST.get("millage")
        mycar.engine=request.POST.get("engine")
        mycar.power=request.POST.get("power")
        mycar.price=request.POST.get("price")
        mycar.carimage=request.FILES["image"]
        if request.POST.get("sport"):
            mycar.isSport=True
        if request.POST.get("nitro"):
            mycar.nitro=True
        if request.POST.get("autogear"):
            mycar.autogear=True
          
        if request.POST.get("autodrive"):
            mycar.autodrive=True
        mycar.save()  

        return render(request,'car/register.html',{"message":"car is registered"})

def detailspage(req,pk):
    car=Car.objects.get(pk=pk)
    return render(req,'car/detailcars.html',{"car":car})