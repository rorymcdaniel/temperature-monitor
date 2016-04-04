import requests

class Weather:

    def __init__(self, api_key, location_id):
        self.url = "http://api.openweathermap.org/data/2.5/weather?id=" + location_id + "&appid=" + api_key
        self.temperature = ""

    def get_weather(self):
        r = requests.get(self.url)
        return r.json()


    def get_temperature(self):
        weather = self.get_weather()
        c = weather['main']['temp'] - 273.15
        self.temperature = c

