from datetime import date
import datetime

import requests

from controller import formatData
class cacheObj():
    def __init__(self):
        cache=self.actualizarCache()
        fechaCache=datetime.now()

    @property
    def cache(self):
        return self.cache
    
    @cache.setter
    def cache(self, cache):
        self.cache=cache

    @property
    def fechaCache(self):
        return self.cacheHorizon
    
    @fechaCache.setter
    def fechaCache(self, fechaCache):
        self.fechaCache=fechaCache

    def request(self):
        if self.fechaCache!=datetime.now():
            self.fechaCache=datetime.now()
            self.actualizarCache()
        return self.cache
    
    def actualizarCache(self):

        apiKey = "DEMO_KEY" 

        today = date.today().strftime("%Y-%m-%d")

        url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={today}&api_key={apiKey}"

        response = requests.get(url)
        data = response.json()

        self.cache=formatData(data)




    