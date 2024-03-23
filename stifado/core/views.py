from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django import forms
import requests
import json



# Create your views here.

def index(request):
    #location api
    res = requests.get('http://ip-api.com/json/24.48.0.1')
    location_data_one = res.text
    location_data = json.loads(location_data_one)
    #prodect items
    


    return render(request,"index.html",{'location_data':location_data})




#longin form 
# def login_user(request): 
#   if request.method == "POST":
#      username = request.POST["username"]
#      password = request.POST["password"]
#      user = authenticate(request, username=username, password=password)
#      if user is not None:
#         login(request, user)
#         messages.success(request,("You have been loged in"))
#         return redirect('index')
#         # Redirect to a success page.
#      else:
#         messages.success(request,("Thair was an error login try again.."))
#         return redirect('login')
#   else:# Return an 'invalid login' error message.
#     return render(request, 'login.html', {})
#logout user 


# def logout_user(request):
#     if request.method == "POST":
#      logout(request)
#     return redirect('index')


#signup user
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


#cart views
def cart(request):
    return render(request,"cart.html") 


#prodect list page views
def prodect_list(request):
    return render(request,"prodect_list.html") 



   