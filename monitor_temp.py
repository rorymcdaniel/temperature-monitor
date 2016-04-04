import os
from os.path import join, dirname

from dotenv import load_dotenv

from sensor import Sensor
from weather import Weather

# This assumes that .env is in the same directory.
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

sensor = Sensor()
weather = Weather(os.environ.get("OPENWEATHERMAP_API_KEY"), os.environ.get("OPENWEATHERMAP_PLACE_ID"))
print "Indoor Temperature: " + sensor.get_fahrenheit()
print "Outdoor Temperature: " + str(weather.get_fahrenheit()) + "F"

