import os
from os.path import join, dirname
from datetime import datetime, time


from dotenv import load_dotenv
import MySQLdb

from sensor import Sensor
from weather import Weather
from temperature_db import TemperatureDB
from sms import TemperatureSMS

# Load the configuration file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Instantiate the objects
sensor = Sensor()
db = TemperatureDB()
weather = Weather(os.environ.get("OPENWEATHERMAP_API_KEY"), os.environ.get("OPENWEATHERMAP_PLACE_ID"))
sms = TemperatureSMS()

# Get temperature readings
inside = sensor.get_fahrenheit()
outside = weather.get_fahrenheit()

# Save to the database
db.insert_data('inside', inside)
db.insert_data('outside', outside)


now = datetime.now()
now_time = now.time()


# Need a way to do this only once. As is it will keep sending this each time it runs
# if now_time >= time(8,00) and now_time <= time(20,30):
#     if inside > outside and outside > 60:
#         sms.send_message("")





print "Indoor Temperature: " + str(inside) + "F"
print "Outdoor Temperature: " + str(outside) + "F"

db.close()


