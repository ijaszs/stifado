from django.shortcuts import render

from ..models import Product


# Product list page views
def product_list(request):
    # Retreiving products
    products = Product.objects.all()
    return render(request,"product_list.html", {'products': products}) 


# Cart views
def cart(request):
    return render(request,"cart.html") 