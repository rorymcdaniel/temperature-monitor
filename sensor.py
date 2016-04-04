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
        c = (data[2] + data[3] + data[4]) / 3 / 126.74 - 5.4
        return c

    def get_fahrenheit(self):
        c = self.get_celcius()
        f = (9.0 / 5.0 * c) + 32.0
        return f

