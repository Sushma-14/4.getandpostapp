from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'input.html')
def add(request):
    if request.method == "GET":
        x = request.GET["t1"]
        y = request.GET["t2"]
        z=x+y
        return HttpResponse("the sum is " + str(z))
    else:
        x = request.POST["t1"]
        y = request.POST["t2"]
        z=x + y
        return HttpResponse("the sum is " + str(z))