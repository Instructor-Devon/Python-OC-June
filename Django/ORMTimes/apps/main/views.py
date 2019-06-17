from django.shortcuts import render, HttpResponse
from .models import User

# Create your views here.
# 
def index(request):
    all_users = User.objects.all()

    
    context = {
        "users": all_users
    }

    return render(request, "main/index.html", context)