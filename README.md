# Walter Documentation

## Introduction

This repository contains all information and documentation about Walter and
additional motherboards for Walter. Walter is a board designed by
[DPTechnics](https://www.dptechnics.com) which combines an 
[ESP32-S3](https://www.espressif.com/en/products/socs/esp32-s3) and
a [Sequans Monarch 2](https://www.sequans.com/products/monarch-2-gm02sp) in a
small form factor IoT module. This gives Walter a vast amount of wireless
connectivity options such as:
- Bluetooth Low Energy 5.0
- 1T1R WiFi b/g/n
- LTE Cat-M1 (LTE-M)
- LTE Cat-NB1 (NB-IoT rel. 13)
- LTE Cat-NB2 (NB-IoT rel. 14), ready for rel. 15
- GNSS receiver (GPS and Galileo)

Besides these you get all the goodies from the ESP32-S3 chip such as  SPI, I2S,
I2C, PWM, RMT, ADC, UART, SD/MMC host and TWAI. 

We design and manufacture Walter in Belgium and guarantee that the board will be
available for a minimum of 10 years. This makes Walter a solid choice to design
your next LPWAN IoT product with.

All documentation for Walter is open source and we welcome all contributions are
more than welcome.

## Structure

We strive the support as many software platforms as possible and we have thus
created the following documentation structure:
  - common: this directory contains documentation which is independant from the 
            chosen software toolchain.
  - arduino: this directory contains documentation which is specific to using
             Walter with the Arduino toolchain.
  - toit: this directory contains documentation which is specific to using
             Walter with the Toit toolchain.
  - esp-idf: this directory contains documentation which is specific to using
             Walter with the Espressif IDF toolchain.
  - micropython: this directory contains documentation which is specific to
                 using Walter with the MicroPython toolchain.

## Getting started

Every toolchain has it's own getting started guide but a common guide which
doesn't involve any programming can be found in
[common/getting-started.md](common/getting-started.md).