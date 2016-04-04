# Indoor/Outdoor Temperature Monitor
This module compares the indoor and outdoor temperatures in order to determine when you need to open the windows
in summer. It utilizes a Go Temp USB thermometer and the openweathermap.org API

## This is under active development and as of yet is not fully functional
Eventually this will either store observations in a database locally or use an external service.

### Required modules
* requests
* python-dotenv


    sudo pip install requests
    sudo pip install python-dotenv

At the moment, this only works on Linux. It does not work on OS X or Windows.
