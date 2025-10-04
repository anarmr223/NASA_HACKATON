from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from datetime import date
import controller
# Create your views here.

apiKey = "DEMO_KEY" 

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

        url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={today}&api_key={apiKey}"

        response = requests.get(url)
        data = response.json()

        format_data= controller.formatData(data)

        return Response(format_data)