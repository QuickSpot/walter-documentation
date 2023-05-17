#
# This file is part of MicroPython LIS2HH12 driver
# Copyright (c) 2017-2018 Mika Tuupola
#
# Licensed under the MIT license:
#   http://www.opensource.org/licenses/mit-license.php
#
# Project home:
#   https://github.com/tuupola/micropython-lis2hh12
#

"""
MicroPython I2C driver for LIS2HH12 3-axis accelerometer
"""

import ustruct # pylint: disable=import-error
from machine import I2C, Pin # pylint: disable=import-error
from micropython import const # pylint: disable=import-error

__version__ = "0.3.0-dev"

_TEMP_L = const(0x0b)
_TEMP_H = const(0x0c)
_WHO_AM_I = const(0x0f) # 0b01000001 = 0x41
_CTRL1 = const(0x20)
_CTRL2 = const(0x21)
_CTRL3 = const(0x22)
_CTRL4 = const(0x23)
_CTRL5 = const(0x24)
_CTRL6 = const(0x25)
_CTRL7 = const(0x26)
_OUT_X_L = const(0x28)
_OUT_X_H = const(0x29)
_OUT_Y_L = const(0x2a)
_OUT_Y_H = const(0x2b)
_OUT_Z_L = const(0x2c)
_OUT_Z_H = const(0x2d)

# CTRL1
_ODR_MASK = const(0b01110000)
ODR_OFF = const(0b00000000)
ODR_10HZ  = const(0b00010000)
ODR_50HZ  = const(0b00100000)
ODR_100HZ = const(0b00110000)
ODR_200HZ = const(0b01000000)
ODR_400HZ = const(0b01010000)
ODR_800HZ = const(0b01100000)

# CTRL4
_FS_MASK = const(0b00110000)
FS_2G = const(0b00000000)
FS_4G = const(0b00100000)
FS_8G = const(0b00110000)

_SO_2G = 0.061 # 0.061 mg / digit
_SO_4G = 0.122 # 0.122 mg / digit
_SO_8G = 0.244 # 0.244 mg / digit

SF_G = 0.001 # 1 mg = 0.001 g
SF_SI = 0.00980665 # 1 mg = 0.00980665 m/s2

class LIS2HH12:
    """Class which provides interface to LIS2HH12 3-axis accelerometer."""
    def __init__(self, i2c=None, address=0x1e, odr=ODR_100HZ, fs=FS_2G, sf=SF_SI):
        if i2c is None:
            self.i2c = I2C(scl=Pin(8), sda=Pin(9))
        else:
            self.i2c = i2c

        self.address = address

        if 0x41 != self.whoami:
            raise RuntimeError("LIS2HH12 not found in I2C bus.")

        self._sf = sf
        self._odr(odr)
        self._fs(fs)

    @property
    def acceleration(self):
        """
        Acceleration measured by the sensor. By default will return a
        3-tuple of X, Y, Z axis acceleration values in m/s^2. Will
        return values in g if constructor was provided `sf=SF_G`
        parameter.

        On ESP32 currently takes aproximately 4.6ms to return full
        3-tuple reading.
        """
        so = self._so
        sf = self._sf

        x = self._register_word(_OUT_X_L) * so * sf
        y = self._register_word(_OUT_Y_L) * so * sf
        z = self._register_word(_OUT_Z_L) * so * sf
        return (x, y, z)

    @property
    def whoami(self):
        """ Value of the whoami register. """
        return self._register_char(_WHO_AM_I)

    def _register_word(self, register, value=None):
        if value is None:
            data = self.i2c.readfrom_mem(self.address, register, 2)
            return ustruct.unpack("<h", data)[0]
        data = ustruct.pack("<h", value)
        return self.i2c.writeto_mem(self.address, register, data)

    def _register_char(self, register, value=None):
        if value is None:
            return self.i2c.readfrom_mem(self.address, register, 1)[0]
        data = ustruct.pack("<b", value)
        return self.i2c.writeto_mem(self.address, register, data)

    def _fs(self, value):
        char = self._register_char(_CTRL4)
        char &= ~_FS_MASK # clear FS bits
        char |= value
        self._register_char(_CTRL4, char)

        # Store the sensitivity multiplier
        if FS_2G == value:
            self._so = _SO_2G
        elif FS_4G == value:
            self._so = _SO_4G
        elif FS_8G == value:
            self._so = _SO_8G

    def _odr(self, value):
        char = self._register_char(_CTRL1)
        char &= ~_ODR_MASK # clear ODR bits
        char |= value
        self._register_char(_CTRL1, char)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        pass