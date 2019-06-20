from django.shortcuts import render, redirect
from .models import Book 
from datetime import datetime
# Create your views here.
def index(req):
    return render(req, "main/index.html")

def add(req):
    # check for future date!
    print(req.POST["the_date"])
    to_dt = datetime.strptime(req.POST["the_date"], "%Y-%m-%d")
    now = datetime.now()
    if to_dt > now:
        print("date is in the future!!!")
    else:
        print("date ok to store in db")
    
    # Book.objects.create(title="Dummy", pub_date=req.POST["the_date"])
    return redirect("/")
