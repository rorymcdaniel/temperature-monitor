import urllib
import urllib2
import os

class TemperatureSMS:


    def __init__(self):
        self.url = "http://textbelt.com/text"


    def send_message(self, message):
        values = {'number': os.environ.get('TO_PHONE_NUMBER'),
                  'message': message}
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)

