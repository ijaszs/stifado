from django.shortcuts import render
import requests
import json

from ..models import Restaurant


def index(request):
   # Location API
    res = requests.get('http://ip-api.com/json/24.48.0.1')
    location_data_one = res.text
    location_data = json.loads(location_data_one)

    #Retrieve all the restaurants
    restaurants = Restaurant.objects.all()
   
    return render(request, "index.html", {'location_data':location_data, 'restaurants': restaurants})
 