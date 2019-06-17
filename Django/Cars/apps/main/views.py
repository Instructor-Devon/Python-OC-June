from django.shortcuts import render, redirect
from .models import Driver, Car
# Create your views here.
def index(request):
    context = {
        "drivers": Driver.objects.all(),
        "cars": Car.objects.all()
    }
    return render(request, "main/index.html", context)

def create_car(request):

    print(request.POST)

    Car.objects.create(make = request.POST["make"], model = request.POST["model"], top_speed = request.POST["speed"], driver_id = request.POST["driver"])

    return redirect("/")