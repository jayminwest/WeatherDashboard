import requests
from datetime import datetime

"""
1. Enter location
2. Get the coords for that location
3. Call api using that location
4. Show the current forecast for the next week and show the historical median from years past
5. Print this out
6. Add a section for moisture as well

"""

OWM_API_KEY = ''

def get_current_weather(apiKey, cityName):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': cityName, 
        'appid': apiKey,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    return data

print(get_current_weather(OWM_API_KEY, "Sandpoint"))