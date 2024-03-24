from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages


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


