from Sensor import Sensor
from Weather import Weather
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

#sensor = Sensor()
weather = Weather(os.environ.get("OPENWEATHERMAP_API_KEY"), os.environ.get("OPENWEATHERMAP_PLACE_ID"))
#print sensor.get_fahrenheit()
print weather.get_temperature()

