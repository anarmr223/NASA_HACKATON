import os
import json
import requests
from datetime import datetime, date
from django.conf import settings

from .controller import formatData


class cacheObj:
    def __init__(self):
        # Inicializamos vacío, sin cargar datos aún
        self._cache = None
        self._fechaCache = None

    @property
    def cache(self):
        return self._cache
    
    @cache.setter
    def cache(self, cache):
        self._cache = cache

    @property
    def fechaCache(self):
        return self._fechaCache
    
    @fechaCache.setter
    def fechaCache(self, fechaCache):
        self._fechaCache = fechaCache

    def request(self):
        """ Devuelve el cache si está al día, si no lo actualiza """
        hoy = datetime.now().date()
        if self._fechaCache != hoy:
            self.actualizarCache()
        return self._cache
    
    def actualizarCache(self):
        apiKey = "DEMO_KEY" 
        today = date.today().strftime("%Y-%m-%d")

        url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={today}&api_key={apiKey}"

        #llamada a la api
        response = requests.get(url)
        data = response.json()

        #pruebas
        #file_path = os.path.join(settings.BASE_DIR, "prueba", "data.json")
        #with open(file_path, "r") as file:
        #    data = json.load(file) 

        self._cache = formatData(data)
        self._fechaCache = datetime.now().date()

    def __str__(self):
        return f"cache: {self.cache}, tiempo exp: {self.fechaCache}"
