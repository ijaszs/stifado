from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib import messages
from core.models import Restaurant,Product
from core.forms import CustomUserCreationForm
from django.http import JsonResponse
from .models import Cart
# home page views
def index(request):
    #Retrieve all the restaurants
    restaurants = Restaurant.objects.all()
    products = Product.objects.all()
    context =  { 'restaurants': restaurants,
                'products': products
                }
    return render(request, "index.html", context)





# signup views
def register_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "You have successfully registered Welcome!")
            return redirect('index') 
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})


# Product list page views
def product_list(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    products = Product.objects.filter(restaurant=restaurant)
    product_count = products.count()

    return render(request, "product_list.html", {'products': products, 'product_count': product_count, 'restaurant': restaurant})



# checkout page views
def checkout(request):
    products = Product.objects.all()
    return render(request,"checkout.html",{'products': products}) 

# serch prodect views
def search_views(request):
    if request.method == "POST":
        search = request.POST.get('searched', '')
        products = Product.objects.filter(name__contains=search)
        return render(request, "search_view.html", {'search': search, 'products': products})
    else:
        return render(request, "search_view.html", {})





def cart(request):
    products = Product.objects.all()
    return render(request,"cart.html",{'products': products}) 







