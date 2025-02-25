## TL;DR

If you have already set up the Arduino development environment and want to
quickly start with Walter you can download our Arduino library and run some
examples. All source code is available on Github: 
https://github.com/QuickSpot/walter-arduino

## Configure the Arduino IDE

The library is designed to be used with the Arduino IDE or any variant such as
the VSCode plugins. You need to start by installing the ESP32 core for Arduino
using the official documentation. After installation of the most recent ESP32
core you must select the following settings in de IDE:

 - Board: ESP32S3 Dev Module
 - Upload Speed: 921600
 - USB Mode: Hardware CDC and JTAG
 - USB CDC On Boot: Enabled
 - USB Firmware MSC On Boot: Disabled
 - USB DFU On Boot: Disabled
 - Upload Mode: UART0 / Hardware CDC
 - CPU Frequency: 240MHz (WiFi)
 - Flash Mode: QIO 80MHz
 - Flash Size: 16MB (128Mb)
 - Partition Scheme: 16M Flash (2MB APP/12.5MB FATFS) (must be this partition scheme to make modem firmware updates possible)
 - Core Debug Level: Anything that goes for you
 - PSRAM: QSPI PSRAM
 - Arduino Runs On: Core 1
 - Events Run On: Core 1
 - Erase All Flash Before Sketch Upload: Enabled
 - JTAG Adapter: Integrated USB JTAG
 - Zigbee Mode: Disabled

You now need to clone the [walter-arduino](https://github.com/QuickSpot/walter-arduino)
library into the `libraries` directory of your Arduino IDE. The location of this
directory depends on your OS and installation, typical locations are:

 - Windows: `%USERPROFILE%\Documents\Arduino\libraries`
 - Mac OSX: `~/Documents/Arduino/libraries`
 - Linux: `~/sketchbook/libraries`

That's it, you can now run any of the examples and connect to the internet.