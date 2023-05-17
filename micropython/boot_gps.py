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