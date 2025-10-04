#from django.test import TestCase

from controller import formatData
from asteroide import Asteroid
from datetime import date, datetime
import requests
import json

apiKey = "DEMO_KEY" 

today = date.today().strftime("%Y-%m-%d")

url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={today}&api_key={apiKey}"

with open("../prueba/data.json", "r") as f:
    data = json.load(f)

asteroides = formatData(data)

for a in asteroides:
    print(f"Nombre: {a.name}, ID: {a.id}, Masa: {a.mass}, Posición: ({a.x}, {a.y}, {a.z}), latitud: ({a.latitude}), altitud: ({a.altitude})")
