from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

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

def authViews(request):
    if request.method == "POST":
     form = UserCreationForm(request.post or None)
     if form.is_valid():
         form.save()
    else:
     form = UserCreationForm()
    return render(request,"registration/signup.html",{"form":form}) 
