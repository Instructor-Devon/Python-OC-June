from django.shortcuts import render, HttpResponse
from datetime import datetime
# Create your views here.
def index(request):
    print(request)

    context = {
        "users": ["Devon", "Howard", "Marco"],
        "time": datetime.now()
    }
    return render(request, "index.html", context)

def test(request, my_val):
    return HttpResponse("Over here " + my_val)