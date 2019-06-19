from django.shortcuts import render, redirect, HttpResponse
from django.contrib.messages import error
from .models import User

# Create your views here.
def index(request):
    return render(request, "home/index.html")

def login(request):
    if request.method == "POST":
        print(request.POST)
    return redirect("/")

def register(request):
    if request.method == "POST":
        errors = User.objects.validate_registration(request.POST)
        if errors:
            for err in errors:
                error(request, err)
        else:
            new_id = User.objects.register_user(request.POST)
            request.session["user_id"] = new_id
    return redirect("/")
