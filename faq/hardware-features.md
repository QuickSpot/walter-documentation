## Hardware Features

### How do I enable the 3.3V output?

The 3V3 OUT (pin 26) is software controllable and the output is not enabled by
default. You need to enable the 3.3V in your code:

- Set GPIO0 LOW to enable 3.3V output
- Set GPIO0 HIGH to disable 3.3V output

### Does Walter support CAN bus?

Yes, but it requires an external CAN transceiver *(e.g., SN65HVD232)*
to convert TTL levels to CAN bus levels.
The ESP32-S3's built-in TWAI peripheral is used for CAN communication.

### Can Walter monitor input voltage?

Yes, you can monitor the VIN voltage using the AT+SQNVMON command.
The Sequans modem is directly connected to VIN,
while the ESP32-S3 uses a DC-DC converter for stable 3.3V.
