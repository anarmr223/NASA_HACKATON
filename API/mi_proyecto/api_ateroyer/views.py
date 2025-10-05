from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from datetime import date
from . import controller
from . import cacheObj
# Create your views here.

apiKey = "DEMO_KEY" 
cacheItem = cacheObj.cacheObj()

today = date.today().strftime("%Y-%m-%d")
class test(APIView):
    def get(self, request): 
        today = date.today().strftime("%Y-%m-%d")

        url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={today}&api_key={apiKey}"

        r = requests.get(url)  
        data = r.json()

        return Response(data)
    
class ateroids(APIView):
    def get(self, request):

        format_data=cacheItem.request()
        asteroid_data = [asteroid.to_dict() for asteroid in format_data]
        return Response(asteroid_data)