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