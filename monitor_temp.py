import os
from os.path import join, dirname

from dotenv import load_dotenv
from twilio.rest import TwilioRestClient
import MySQLdb


from sensor import Sensor
from weather import Weather

# This assumes that .env is in the same directory.
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

conn = MySQLdb.connect(passwd=os.environ.get("MYSQL_PASS"), user=os.environ.get("MYSQL_USER"), db=os.environ.get("MYSQL_DBNAME"), host=os.environ.get("MYSQL_HOST"))

x = conn.cursor()

def insert_data(location, temperature):
    try:
        x.execute("""INSERT INTO observations (location, temperature )VALUES (%s,%s)""", (location, temperature))
        conn.commit()
    except Exception:
        conn.rollback()



sensor = Sensor()

weather = Weather(os.environ.get("OPENWEATHERMAP_API_KEY"), os.environ.get("OPENWEATHERMAP_PLACE_ID"))

inside = sensor.get_fahrenheit()
outside = weather.get_fahrenheit()

insert_data('inside', inside)
insert_data('outside', outside)

print "Indoor Temperature: " + str(inside) + "F"
print "Outdoor Temperature: " + str(outside) + "F"


client = TwilioRestClient(os.environ.get('TWILIO_ACCOUNT_SID'), os.environ.get('TWILIO_AUTH_TOKEN'))

message = client.messages.create(body="The temperature outside is lower than the temperature inside. Open the windows!",
    to=os.environ.get("TO_PHONE_NUMBER"),    # Replace with your phone number
    from_=os.environ.get("FROM_PHONE_NUMBER")) # Replace with your Twilio number
print message.sid

conn.close()


