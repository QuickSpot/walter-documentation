## Troubleshooting

### I'm unable to flash Walter. How do I force the module into flash mode?

Walter utilizes the ESP32-S3's built-in USB-to-serial peripheral.
However, if the chip has been flashed with software
that disables this functionality or if the firmware is stuck
in a high-frequency boot loop, you may encounter issues
when attempting to flash the Walter module.

To resolve this, you can force Walter into flashing mode
by pulling `GPIO0` to ground before powering it on.
This will prevent the chip from booting its current firmware,
allowing it to remain in a waiting state
for new firmware to be downloaded over USB-C or serial.

### Why does Walter keep restarting?

Common causes include:

1. Insufficient power supply
   - ensure stable power through USB-C or external power
2. Network connectivity issues
   - implement proper error handling
3. Memory issues
   - check for memory leaks in your application
4. Buffer overflows
   - particularly in areas with poor signal strength

### How do I enable debug logging?

Set the Arduino IDE debug level to "Debug" in board settings, or in code:

```cpp
modem.setDebug(true);
```

### Serial Monitor issues with sleep mode?

The Arduino IDE serial monitor may not reconnect properly after sleep mode.
This is due to the fact that Walter uses the USB-Serial hardware
that is built-in into the ESP32-S3,
this converter is powered off in deep sleep which effectively
disconnects the Walter module from the host computer during deep sleep.
Not all software can handle this correctly, possible solutions are:

1. Use Visual Studio Code with the
   [Serial Monitor extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-serial-monitor)
2. Use an external USB-to-UART converter
