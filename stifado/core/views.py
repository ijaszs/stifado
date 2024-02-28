from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html") 

def signup(request):
    return render(request,"signup.html") 

def cart(request):
    return render(request,"cart.html") 

def prodect_list(request):
    return render(request,"prodect_list.html") 
