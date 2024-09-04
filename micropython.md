## TL;DR

If you have already set up the Micropython toolchain and want to quickly start
with Walter you can download our Micropython library and run some examples. All
source code is available on Github: 
https://github.com/QuickSpot/walter-micropython

## Preparing the toolchain

In this guide, we assume a recent Debian-based linux distribution is used.
Most steps will work correctly on Windows as well. If not, the difference will
be indicated in the guide.

Make sure a recent version of Python 3.x is installed on your development system.

Install a serial communication tool such as minicom.

On Debian based systems, these commands may do the trick if these packages
are not yet installed. Warning: if Python 3 is already installed, do not
try to install it as a different version might be installed next to the existing
installation, which would create a confusing situation.

```
apt update
apt install python3 pip3
apt install minicom
```

It is recommended to create a working directory or git repository for your
tests so we don't make a mess in our home directory. Hypothetically:

```
cd
mkdir walter_micropython_tests
cd walter_micropython_tests
```

### On Windows

On Windows, Putty is a reliable lightweight serial communication tool.
Wherever minicom is mentioned, please use Putty and the correct COM port
(see below).

## Connecting Walter to your system

After plugging in Walter, a device node will automatically be created.
Before plugging in, retrieve the list of dev nodes that are already present,
so we can later figure out which one belongs to Walter.

```
ls /dev/ttyACM*
```

When no other devices are currently plugged in, this list will usually be empty.

Now plug in Walter. You can optionally check for any kernel messages that confirm
Walter was detected correctly by linux:

```
sudo dmesg
```

Now retrieve the list of serial device nodes once more. Walter should now
appear in the list with its associated device node on linux.

```
ls /dev/ttyACM*
```

In this setup guide we shall assume `/dev/ttyACM0`, which will normally be the name
of the dev node if you have no other devices connected. Please replace with the
name on your system if it is a different dev node on your system.

Let's test if we can communicate:

```
minicom -b 115200 -D /dev/ttyACM0
```

Walter should be talking to you. You can leave minicom by pressing Ctrl-A followed
by Q (quit).

If communication fails, one typical reason is your user is not member of the `dialout`
group. In that case, run this command to add your user to this group:

```
sudo adduser USERNAME dialout
```

(Replace `USERNAME` by the login of your user account.)

Log out and in again to make sure the group membership is applied, and test again
using minicom.

If communication is still not possible, you can try the following hack to give
all users write and read access to the serial device.

```
sudo chmod 777 /dev/ttyACM0```
```

In that case, please configure your system appropriately to make this hack
unnecessary. If not, you will need to execute the chmod command every time
you plug in Walter because the permissions will be reset on every reconnect.

### On Windows

Use Device Manager to find your serial ports (COM1, COM2, ...).
Watch the serial devices while you plug in Walter. The newly assigned COM
port will appear in the list shortly after connecting. Remember this port name,
and replace `/dev/ttyACM0` with this COM port throughout the rest of this
guide.

Good to know: on Windows, the port may occasionally not appear.
In that case, please reboot. This time the port should appear correctly.

## Install esptool.py

You can choose whether to install the python dependencies for managing MicroPython
under your own user account or systemwide. This guide assumes we are installing
everything under our regular user account, which works fine out of the box.

Open a terminal and install esptool.py using pip3:

```
pip3 install esptool
```

Optionally you can read the documentation for esptool at
https://docs.espressif.com/projects/esptool/en/latest/esp32/
although it is not essential to complete this guide.

### On Windows

Sometimes the pip3 command will not have permission to install esptool correctly.
In that case, please run the command inside a command prompt invoked with
administrator privilege.

## Install MicroPython using esptool

Look specifically for the ESP32S3 release, which has SPIRAM support.
This release currently lives at https://micropython.org/download/ESP32_GENERIC_S3/ .

The setup process is described on the download page, and summarized briefly below.

First download the MicroPython image to be installed on your Walter.
please use the regular firmware, not the one with Octal-SPIRAM support,
since the ESP32S3 on Walter has Quad-SPIRAM. Download the latest release
and use the file with the `.bin` extension.

The version we are currently using for tests is `ESP32_GENERIC_S3-20231005-v1.21.0.bin`
and is included in the QuickSpot MicroPython library repository for your convenience.

Please replace below by the actual filename that you downloaded.

Now we shall perform the steps described on the webpage:

1. Erase the entire flash to start with a clean slate:

```
esptool.py --chip esp32s3 --port /dev/ttyACM0 erase_flash
```

2. Upload the MicroPython image to Walter:

```
esptool.py --chip esp32s3 --port /dev/ttyACM0 write_flash -z 0 ESP32_GENERIC_S3-20231005-v1.21.0.bin
```

## Install the ampy tool to manage the MicroPython scripts installed on Walter

Ampy is a tool provided by AdaFruit, which works fine with Walter.

```
pip3 install adafruit-ampy
``` 

Using Ampy you can upload, download and delete scripts or list the installed
scripts. Let's test Ampy.

Retrieve the list of files:

```
ampy --port /dev/ttyACM0 ls
```

After a fresh install, the only script will be `boot.py`, which is mandatory
and executed at boot time, so the output of this command should be:

```
/boot.py
```

We will use ampy later on in this guide to manage a few demo scripts.
For now we can proceed, but if you wish to get more familiar with ampy already,
check the documentation at https://learn.adafruit.com/micropython-basics-loading-modules/import-code .

## Play around with the default script

So far we have not modified anything yet. Let's take a look at the `boot.py`
file that was already installed.

```
ampy --port /dev/ttyACM0 ls
ampy --port /dev/ttyACM0 get boot.py
```

The file contents will be printed on your console. At the time of writing,
the script was basically empty because there were only a few lines in
comment. In that case, MicroPython will simply provide an interactive
Python REPL shell. Let's communicate with it before changing anything
to `boot.py` just yet.

```
minicom -b 115200 -D /dev/ttyACM0
```

This time Walter will not be talking to you like when we were testing with
minicom earlier, because it is waiting for your Python instruction to
parse and evaluate. Let's play around a bit over the serial connection:

```
print('hello world')
#output:
#hello world

import random
dir(random)
# output:
# ['__class__', '__init__', '__name__', '__dict__', 'choice', 'getrandbits', 'randint', 'random']

help(random)
#output:
#object <module 'urandom'> is of type module
#  __name__ -- urandom
#  __init__ -- <function>
#  getrandbits -- <function>
#  seed -- <function>
#  randrange -- <function>
#  randint -- <function>
#  choice -- <function>
#  random -- <function>
#  uniform -- <function>

random.randint(1,10)

#possible output:
7
```

When you press Ctrl-D, the interactive MicroPython instance will interpret it as
end of file and shut down. In response, the board will soft reboot, which only
takes an instant. Python is immediately restarted.

## First hello world script

Let's write a boot.py script that keeps printing hello world followed by
a random int between 0 and 10. Put this in `boot.py` on your development
machine. In this guide we assume we are still in the `walter_micropython_tests`
folder.

```
import time
import random

while True:
    print('hello world - %d' % random.randint(0, 10))
    time.sleep(1)
```

Use Ampy to upload the new `boot.py` file:

```
ampy --port /dev/ttyACM0 put boot.py
```

You can verify that the file was indeed written correctly by simply getting it
again:

```
ampy --port /dev/ttyACM0 get boot.py
```

Now let's test the script. Start minicom again.

```
minicom -b 115200 -D /dev/ttyACM0
```

Note that Walter has not rebooted, and the interactive python environment we were
playing around with in step 6 is still running. Press Ctrl-D to send end-of-file,
after which Walter will reboot, and your script should now start emitting its output:

```
hello world - 7
hello world - 8
hello world - 6
hello world - 10
hello world - 1
hello world - 8
hello world - 5
hello world - 8
hello world - 1
hello world - 6
hello world - 5
hello world - 0
hello world - 0
hello world - 9
... and so on ...
```

Later on, if a script is running, you may also need to press Ctrl-C to interrupt it,
before pressing Ctrl-D to shutdown MicroPython and reboot, but right now, no
script is running yet so this step is not necessary.

## Demo script to interface with Pytrack

Pytrack is a popular GPS companion board for the well-known Pycom board. 
Walter is backwards compatible with Pycom, and scripts written for Pytrack
will work out of the box without any modifications. Here is an example.

We will use the `gnssl76l.py` module, which is simply another Python
script installed next to `boot.py`. This module interprets I2C data and
converts it into readable form. It was written by Mika Tuupola
and available here: https://github.com/tuupola/micropython-gnssl76l

We provide it in this repo for convenience. Please download this file:

```python
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
```

Now let's disconnect Walter and attach it to the Pytrack companion board.

After connecting again, upload `gnssl76l.py` to Walter:

```
ampy --port /dev/ttyACM0 put gnssl76l.py
```

Now we shall install our demo `boot.py` that interfaces with Pytrack.
The GPS demo is called `boot_gps.py` in our repository. Please download this file
to your development system:

```python
import utime
from gnssl76l import GNSSL76L
import machine

# Set the 3v3 select pin as output.
pin = machine.Pin(0, machine.Pin.OUT)
# Set the pint to 0 for 3V3
pin.value(0)
# allow the system to
utime.sleep_ms(2000)

receiver = GNSSL76L()
while True:
    for sentence in receiver.sentences():
        print(sentence)

    print("\n")
    utime.sleep_ms(1000)
```

On the Walter board this file must be named `boot.py`, and by passing an extra
parameter to `amply` we can provide the destination filename:

```
ampy --port /dev/ttyACM0 put boot_gps.py boot.py
```

Connect to Walter once again using minicom:

```
minicom -b 115200 -D /dev/ttyACM0
```

Press Ctrl-D to leave the interactive prompt and reboot Walter,
or you can also simply unplug and reconnect Walter before starting minicom.

It should start spitting out GPS information. See the screenshot:

![alt text](/img/gps_readout.png)

Note that Walter also has its own GPS module onboard.
A demonstration script for communicating with the built-in GPS module will be
provided shortly.

## Demo script to interface with the accelerometer on Pytrack

Walter can communicate with the accelerometer on Pytrack over I2C through the
following pins:

 - sda pin 9
 - scl pin 8

In addition, pin 0 must to be set to output, and value 0 must written to it to select 3V3.

Like in step 8 we will use a helper module to interpret the I2C communication to
actual accelerometer information. Please download it here:

```python
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
```

Download our demo `boot_acc.py` file:

```python
import utime
from lis2hh12 import LIS2HH12
import machine

# Set the 3v3 select pin as output.
pin = machine.Pin(0, machine.Pin.OUT)
# Set the pint to 0 for 3V3
pin.value(0)
# allow the system to
utime.sleep_ms(2000)

sensor = LIS2HH12()

print("LIS2HH12 id: " + hex(sensor.whoami))

while True:
    print(sensor.acceleration)
    utime.sleep_ms(1000)
```

In `boot_acc.py` you will also recognize the pin setup as described above.

Use ampy to upload both files to Walter.

```
ampy --port /dev/ttyACM0 put boot_acc.py boot.py
ampy --port /dev/ttyACM0 put lis2hh12.py
```

Use minicom again to test.

```
minicom -b 115200 -D /dev/ttyACM0
```

Press Ctrl-D to restart Walter, after which our new boot.py will be invoked.
By wiggling around with the module, you will notice that the values indicate
movement.

Demo output:

![alt text](/img/acc_readout.png)

## Using the Walter Micropython library

Upload all the `.py` files to Walter's root directory using the aforementioned `ampy` tool.

 - `queue.py` which is a third-party `Queue` implementation that is missing in `uasyncio`, MicroPython's `asyncio` implementation -- cherry-picked from this great repo by Peter Hinch: https://github.com/peterhinch/micropython-async/blob/master/v3/docs/TUTORIAL.md
 - `_walter.py` which contains the constants and helper objects, separated from the main library because uploading everything as one single file to Walter would take quite long
 - `walter.py` which contains our library implementation
 - `boot.py` which contains your code - the repo contains whatever we were recently testing when committing; probably one of the examples

You can find examples in the `examples` folder.

We use asyncio coroutines for communicating with the modem, queueing commands and running your user code.

You can create your own coroutines, for example to wait for a
GNSS fix in the background instead of blocking the main coroutine.
You can simply create any extra tasks in your main routine passed to
the `modem.begin(main_routine)` call:

```
import uasyncio
import walter
import _walter

async def my_extra_task():
    # ...
    

async def main():
    # ...
    # ......

    uasyncio.create_task(my_extra_task())

    # ......
    # ...

modem = walter.Modem()
modem.begin(main)
```