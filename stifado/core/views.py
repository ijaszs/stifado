from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from . models import Restaurant,Product

def index(request):
    #Retrieve all the restaurants
    restaurants = Restaurant.objects.all()
   
    return render(request, "index.html", { 'restaurants': restaurants})


# Product list page views
def product_list(request):
    # Retreiving products
    products = Product.objects.all()
    return render(request,"product_list.html", {'products': products}) 


# Cart views
def cart(request):
    return render(request,"cart.html") 



def register_user(request):
    form = UserCreationForm()
    if request.method == "POST":
       form = UserCreationForm(request.POST)
       if form.is_valid():
          form.save()
          username = form.cleaned_data['username']
          password = form.cleaned_data['password1']
          user = authenticate(request, username=username, password=password)
          login(request,user)
          messages.success(request,("You have successfully registered  welcome !"))
          return redirect ('index')

    return render(request, 'register.html', {'form': form})