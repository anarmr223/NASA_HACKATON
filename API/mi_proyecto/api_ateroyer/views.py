from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from datetime import date
import controller
from cacheObj import cacheObj
# Create your views here.

apiKey = "DEMO_KEY" 
cacheItem = cacheObj()

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

        return Response(format_data)