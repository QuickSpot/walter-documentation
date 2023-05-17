# This file is part of MicroPython GNSSL76L driver
# Copyright (c) 2017 Mika Tuupola
#
# Licensed under the MIT license:
#   http://www.opensource.org/licenses/mit-license.php
#
# Project home:
#   https://github.com/tuupola/micropython-gnssl76l

"""
MicroPython Quectel GNSS L76-L (GPS) I2C driver
"""

import utime
from machine import I2C, Pin

class GNSSL76L:
    def __init__(self, i2c=None, address=0x10):
        if i2c is None:
            self.i2c = I2C(scl=Pin(8), sda=Pin(9))
        else:
            self.i2c = i2c

        self.address = address

    def read(self, chunksize=255):
        data = self.i2c.readfrom(self.address, chunksize)
        while data[-2:] != b"\x0a\x0a":
            utime.sleep_ms(2)
            data = data + self.i2c.readfrom(self.address, chunksize)

        return data.replace(b"\x0a", b"").replace(b"\x0d", b"\x0d\x0a")

    def sentences(self):
        return self.read().splitlines()