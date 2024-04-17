from django.shortcuts import render

# Create your views here.
def home(request):  
    return render(request,"home.html",{}) 

def payout(request):  
    return render(request,"payout.html",{}) 

def settings(request):  
    return render(request,"settings.html",{}) 


def message(request):  
    return render(request,"message.html",{}) 