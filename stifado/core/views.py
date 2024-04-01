from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib import messages
from . models import Restaurant,Product
from .forms import CustomUserCreationForm

def index(request):
    #Retrieve all the restaurants
    restaurants = Restaurant.objects.all()
    products = Product.objects.all()
    context =  { 'restaurants': restaurants,
                'products': products
                }
    return render(request, "index.html", context)


# Product list page views
def product_list(request, id):
    # Retreiving products
    products = Product.objects.filter(restaurant__id=id)
    # Retreiving restaurants count
    restaurant = get_object_or_404(Restaurant, id=id)
    products = Product.objects.filter(restaurant=restaurant)
    product_count = products.count()

    return render(request,"product_list.html", {'products': products, 'product_count': product_count})


# Cart views
def cart(request):
    products = Product.objects.all()
    return render(request,"cart.html",{'products': products}) 


def register_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "You have successfully registered. Welcome!")
            return redirect('index') 
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})


def checkout(request):
    products = Product.objects.all()
    return render(request,"checkout.html",{'products': products}) 