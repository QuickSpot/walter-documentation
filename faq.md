## Hardware Features

### How do I enable the 3.3V output?
The 3V3 OUT (pin 26) is software controllable and the output is not enabled by 
default. You need to enable the 3.3V in your code:
- Set GPIO0 LOW to enable 3.3V output
- Set GPIO0 HIGH to disable 3.3V output

### Does Walter support CAN bus?
Yes, but it requires an external CAN transceiver (e.g., SN65HVD232) to convert TTL levels to CAN bus levels. The ESP32-S3's built-in TWAI peripheral is used for CAN communication.

### Can Walter monitor input voltage?
Yes, you can monitor the VIN voltage using the AT+SQNVMON command. The Sequans modem is directly connected to VIN, while the ESP32-S3 uses a DC-DC converter for stable 3.3V.

## GNSS/GPS

### Which GNSS antenna should I use?
The recommended antenna is the passive Taoglas FXP.611. Active antennas are not supported by the board.

### How sensitive is the built-in GNSS?
The Walter board's GNSS sensitivity varies by start condition:
- Cold start (no valid assistance): -146dBm
- Warm start (valid assistance, no position): -150.5dBm
- Hot start (valid assistance, position within 100km): -153.3dBm

### Why can't I get a GNSS fix indoors?
GNSS is not suited for indoor positioning, even with dedicated modules. While you might get a signal indoors, it will likely be noisy with degraded accuracy. Indoor reception is limited due to:
- Building materials blocking signals
- Window coatings (especially silver/metallic) interfering with reception
- Lower sensitivity compared to dedicated GNSS modules

For indoor applications, consider alternative positioning technologies such as 
Bluetooth beacons or WiFi scanning. Both are supported by Walter.

## Communication

### Does Walter support both LTE-M and NB-IoT?
Yes, Walter supports both LTE-M and NB-IoT. You can force the RAT (Radio Access Technology) using:
```cpp
modem.setRAT(WALTER_MODEM_RAT_LTEM) // for LTE-M
modem.setRAT(WALTER_MODEM_RAT_NBIOT) // for NB-IoT
```
Followed by `modem.reset()`.

### What protocols are supported?
Walter supports:
- CoAP + DTLS (recommended for low data usage as it's UDP-based)
- MQTT/MQTTS
- HTTP/HTTPS
- Raw UDP
- Raw TCP

### Can I force Walter to connect to a specific network?
Yes, you can manually set the network using AT commands. Example for Vodafone UK:
```
AT+SQNMODEACTIVE=2
AT^RESET
AT+CGDCONT=1,"IP","soracom.io"
AT+CFUN=1
AT+CGATT=0
AT+COPS=1,2,"23415"
```

### Should I use MQTT or CoAP?
A: CoAP is recommended over MQTT for lower data usage as it's UDP-based instead of TCP-based. If you are using NB-IoT you should not use TCP-based protocols. As this might sometimes work it is not guaranteed and will give bad results when you scale up.

### What should I do if I get CME ERROR 4?
CME ERROR 4 typically indicates a network-related issue. Common solutions:
1. Check if you're in an area with good coverage
2. Verify your SIM card is properly provisioned
3. Consider using an external antenna in areas with poor reception
4. Implement automatic reconnection logic in your code
5. Avoid reconnecting more than 3-6 times per hour to prevent network rejection

## Software Development

### Are there OTA (Over-The-Air) update options?
Yes, there are several options for OTA updates:
 - Using BlueCherry's OTA system with CoAP + DTLS
 - Using ESP-IDF's built-in OTA functionality
 - Using Zephyr's OTA capabilities
 - Custom implementation using CoAP or other protocols

### How do I get the current time?
After establishing an LTE connection, you can get the network time using the modem's getClock() function:
```cpp
if(modem.getClock(&rsp)) {
    if(rsp.data.clock > 0) {
        // rsp.data.clock contains UTC timestamp
    }
}
```

### Is the WalterModem library thread-safe?
No, thread locking is not implemented in the library and is left to the application level.

### Where can I find example code?
Examples can be found in:
- GitHub repository (https://github.com/QuickSpot/walter-arduino/tree/main/examples)
- QuickSpot documentation (https://www.quickspot.io/documentation)

### How do I enable debugging?
You can enable debug output in the Arduino IDE under Tools menu by setting the debug level to 'DEBUG'. This will show more detailed output including AT commands.

## Power Management

### How do I implement sleep mode in Walter?
The modem automatically enters its lowest power mode when:
1. It's disconnected from the network using `setOpState(WALTER_MODEM_OPSTATE_MINIMUM)`
2. It finishes a transmission and enters RRC idle mode with PSM or eDRX enabled

Example code for configuring power saving:
```cpp
// Enable PSM (Power Saving Mode)
modem.configPSM(WALTER_MODEM_PSM_ENABLE,"01101011", "00101010");

// or configure eDRX
modem.configEDRX();
```

### What happens when ESP32 goes into deep sleep?
When configuring PSM using `configPSM(WALTER_MODEM_PSM_ENABLE, "01101011", "00101010")`, the modem will automatically enter sleep mode when the conditions are met. You don't need to explicitly disconnect from the network. The `configPSM()` function only configures the behavior and doesn't immediately trigger sleep mode.

## Troubleshooting

### I'm unable to flash Walter. How do I force the module into flash mode?
Walter utilizes the ESP32-S3's built-in USB-to-serial peripheral. However, if the chip has been flashed with software that disables this functionality or if the firmware is stuck in a high-frequency boot loop, you may encounter issues when attempting to flash the Walter module.

To resolve this, you can force Walter into flashing mode by pulling `GPIO0` to ground before powering it on. This will prevent the chip from booting its current firmware, allowing it to remain in a waiting state for new firmware to be downloaded over USB-C or serial.

### Why does Walter keep restarting?
Common causes include:
1. Insufficient power supply - ensure stable power through USB-C or external power
2. Network connectivity issues - implement proper error handling
3. Memory issues - check for memory leaks in your application
4. Buffer overflows - particularly in areas with poor signal strength

### How do I enable debug logging?
Set the Arduino IDE debug level to "Debug" in board settings, or in code:
```cpp
modem.setDebug(true);
```
### Serial Monitor issues with sleep mode?
The Arduino IDE serial monitor may not reconnect properly after sleep mode. This is due to the fact that Walter uses the USB-Serial hardware that is built-in into the ESP32-S3, this converter is powered off in deep sleep which effectively disconnects the Walter module from the host computer during deep sleep. Not all software can handle this correctly, possible solutions are:
1. Use Visual Studio Code with the [Serial Monitor extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-serial-monitor)
2. Use an external USB-to-UART converter