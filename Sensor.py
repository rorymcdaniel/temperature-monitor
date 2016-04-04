import time
import struct

class Sensor:

    def __init__(self):
        self.temp = 0

    def _read_temp(self):
        ldusb = open("/dev/ldusb0")
        raw = ldusb.read(8)
        ldusb.close()
        data = list(struct.unpack("<BBHHH", raw))
        return data

    def get_celcius(self):
        data = self._read_temp()
        # Average together the three temperature samples and apply transform: C = Average/126.74 - 5.4
        cel = (data[2] + data[3] + data[4]) / 3 / 126.74 - 5.4
        return cel

    def get_fahrenheit(self):
        cel = self.get_celcius()
        fahr = (9.0 / 5.0 * cel) + 32.0
        # Adjusted temperature factor determined empirically
        fahr_adj = fahr * 1.16
        return fahr_adj

