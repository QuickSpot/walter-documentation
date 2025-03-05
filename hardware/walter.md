## Module overview

![drawing](img/walter-functionality-numbered-stroke.svg)

The Walter module has the following components:

 1. 5G LPWAN modem & GNSS receiver
 2. Reset button
 3. USB Type-C connector for power and programming
 4. 5G antenna connector
 5. GNSS antenna connector (**passive antenna only**)
 6. Integrated GNSS LNA + SAW filter
 7. 3.3V output switch
 8. Ultra low quiescent current DC-DC converter
 9. ESP32-S3 SoC with 16MiB flash and 2MiB PSRAM
 10. Wi-Fi and BLE antenna
 11. 2.54mm pin headers, breadboard friendly
 12. Test pads
 13. Nano SIM card slot

## Intended use

Walter is a small-form-factor IoT system-on-module (SoM) that combines a
powerful
[Espressif ESP32-S3](https://www.espressif.com/en/products/socs/esp32-s3)
system-on-chip (SoC) with a second-generation
[Sequans GM02SP](https://sequans.com/products/monarch-2-gm02sp/)
LTE-M/NB-IoT 5G modem and GNSS receiver. Its ESP32-S3 provides many built-in
peripherals as well, including UART, SPI, I²C, CAN, Wi-Fi b/g/n, and
Bluetooth 5. Walter is the only module that packs all of these connectivity
options into such a small package. While ideal for prototyping you can also use
Walter for production as it is fully certified (CE, UKCA, FCC, IC, RCM).

## Power

### Power input

Walter can be powered either by connecting a USB-C cable or via the VIN pin.
The module accepts any input voltage between 3.0V and 5.5V.

> **DO NOT** power Walter with both the USB-C connection and the VIN-pin! This
> can lead to seriously damaging the board and external peripherals connected to
> it! To minimize losses the USB-C power input and Vin input pin are directly
> connected to each other. If you want to debug your application through USB-C
> while Walter is plugged into a carrier board we advise you to modify a USB-C
> cable by cutting the power lead.

### 3.3V output

Walter contains a Texas Instruments TPS6208833 DC-DC Converter which takes power
from either the USB-C port or the VIN-pin and converts it to a regulated +3.3VDC
supply. The maximum load on the 3.3VDC output is 250mA.

## Pinout

![drawing](img/hardware_pinout.svg)

## Pin descriptions

| Pin |  Function  | ESP pin | Input/Output  | ADC      | RTC | Touch   | Description                                |
|:---:|:----------:|:-------:|---------------|----------|-----|---------|--------------------------------------------|
| 1   | RESET      | EN      | input         | No       | No  | No      | ESP32-S3 reset with 10k pull-up            |
| 2   | IO44/RX0   | RXD0    | bidirectional | No       | No  | No      | ESP32-S3 UART0 receive                     |
| 3   | IO43/TX0   | TXD0    | bidirectional | No       | No  | No      | ESP32-S3 UART0 transmit                    |
| 4   | DFU/3V3_EN | IO0     | bidirectional | No       | Yes | No      | DFU when low on boot and 3V3 output enable |
| 5   | IO12       | IO12    | bidirectional | ADC2_CH1 | Yes | TOUCH12 | General purpose I/O port                   |
| 6   | IO11       | IO11    | bidirectional | ADC2_CH0 | Yes | TOUCH11 | General purpose I/O port                   |
| 7   | IO13       | IO13    | bidirectional | ADC2_CH2 | Yes | TOUCH13 | General purpose I/O port                   |
| 8   | IO38       | IO38    | bidirectional | No       | No  | No      | General purpose I/O port                   |
| 9   | IO39       | IO39    | bidirectional | No       | No  | No      | General purpose I/O port                   |
| 10  | IO40       | IO40    | bidirectional | No       | No  | No      | General purpose I/O port                   |
| 11  | IO41       | IO41    | bidirectional | No       | No  | No      | General purpose I/O port                   |
| 12  | IO42       | IO42    | bidirectional | No       | No  | No      | General purpose I/O port                   |
| 13  | IO2        | IO2     | bidirectional | ADC1_CH1 | Yes | TOUCH2  | General purpose I/O port                   |
| 14  | IO1        | IO1     | bidirectional | ADC1_CH0 | Yes | TOUCH1  | General purpose I/O port                   |
| 15  | IO4        | IO4     | bidirectional | ADC1_CH3 | Yes | TOUCH4  | General purpose I/O port                   |
| 16  | IO5        | IO5     | bidirectional | ADC1_CH4 | Yes | TOUCH5  | General purpose I/O port                   |
| 17  | IO6        | IO6     | bidirectional | ADC1_CH5 | Yes | TOUCH6  | General purpose I/O port                   |
| 18  | IO7        | IO7     | bidirectional | ADC1_CH6 | Yes | TOUCH7  | General purpose I/O port                   |
| 19  | IO15       | IO15    | bidirectional | ADC2_CH4 | Yes | No      | General purpose I/O port                   |
| 20  | IO16       | IO16    | bidirectional | ADC2_CH5 | Yes | No      | General purpose I/O port                   |
| 21  | IO17       | IO17    | bidirectional | ADC2_CH6 | Yes | No      | General purpose I/O port                   |
| 22  | IO18       | IO18    | bidirectional | ADC2_CH7 | Yes | No      | General purpose I/O port                   |
| 23  | IO8        | IO8     | bidirectional | ADC1_CH7 | Yes | TOUCH8  | General purpose I/O port                   |
| 24  | IO9        | IO9     | bidirectional | ADC1_CH8 | Yes | TOUCH9  | General purpose I/O port                   |
| 25  | IO10       | IO10    | bidirectional | ADC1_CH9 | Yes | TOUCH10 | General purpose I/O port                   |
| 26  | 3V3 OUT    | N/A     | power output  | No       | No  | No      | General purpose I/O port                   |
| 27  | GND        | GND     | power ground  | No       | No  | No      | GND connection                             |
| 28  | VIN        | N/A     | power input   | No       | No  | No      | 3.0 - 5V power input port                  |

> The pins on Walter are designed to work in the 3.3V domain. If you want to
> connect 5V peripherals you must use a suitable level translation technique.

## Special functions and IO mux

One of the advantages of the ESP32-S3 in comparison to the older ESP32 is that
the pin multiplexer functionality has been significantly expanded. It is
therefore possible to select any of the normal I/O pins for any digital
peripheral. If you want to process analog signals with any of the two built-in
ADCs you need to take into account the following limitations:

- ADC1 can use IO pins 1, 2, 4, 5, 6, 7, 8, 9, 10
- ADC2 can use IO pins 11, 12, 13, 15, 16, 17, 18

> [!note]
> The ADC2 peripheral is used by the ESP32-S3 if WiFi is enabled.
> While you can still use ADC2 with WiFi enabled it can fail as the WiFi radio has
> prioritized access to the ADC2 peripheral. We therefore recommend not to use
> ADC2 simultaneously with WiFi.

The ESP32-S3 has an ultra low power (ULP)
[RISC-V](https://en.wikipedia.org/wiki/RISC-V)
co-processor which can operate during deep-sleep. This co-processor can control
IO pins which are in the RTC domain. In the case of Walter the available RTC
IO pins are 0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18.

IO0 is a 'strapping pin' which means that the state of the pin at boot
determines module configuration. In case of IO0 there are two options described
in the below table. Once the application has booted the application uses IO0 to
switch on or off the 3.3V output pin in an active-low fashion. This means that
the 3.3V output pin is off by default on boot.

| State |                                 Function                                | Default |
|:-----:|:-----------------------------------------------------------------------:|:-------:|
| High  | Boot from SPI memory and run application                                | Yes     |
| Low   | Boot to bootloader for USB-Serial-JTAG, USB-OTG or UART firmware upload | No      |

The ESP32-S3 has a capacitive touch controller. This peripheral allows you to
use a conductive surface as a touch sensitive button. Not all pins can be used
for touch sensing because of the complex analog circuitry involved. On Walter
IO pins 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12 and 13 can be used for touch sensing.

## Internal pins

There are some internal connections between the ESP32-S3 and the Sequans Monarch
2. These pins are not routed to Walter's header pins but if you want to port
a new language to Walter you will need to know how the modem is connected. The
following table gives an overview of the internal pin connections:

| ESP32-S3 pin |  Description  |
|:------------:|:-------------:|
| IO19         | USB D-        |
| IO20         | USB D+        |
| IO46         | LTE_WAKE0     |
| IO48         | LTE UART0 TX  |
| IO14         | LTE UART0 RX  |
| IO21         | LTE UART0 RTS |
| IO47         | LTE UART0 CTS |
| IO45         | LTE RESET     |

## Test pins

![drawing](img/walter-testpoints.svg)

Walter contains 22 testpoints on the bottom of the board that serve multiple
purposes. You can use these pins for debugging, interfacing and/or flashing of
the Sequans GM02SP and the ESP32-S3-WROOM module.

| Test pin number |           Description          |
|:---------------:|:------------------------------:|
| 1               | Sequans GM02SP JTAG TDO        |
| 2               | Sequans GM02SP JTAG TCK        |
| 3               | Sequans GM02SP JTAG TRSTN      |
| 4               | Sequans GM02SP JTAG TMS        |
| 5               | Sequans GM02SP JTAG TDI        |
| 6               | Sequans GM02SP PS status       |
| 7               | Sequans GM02SP RES/FFF FFH     |
| 8               | Sequans GM02SP RX0             |
| 9               | Sequans GM02SP TX0             |
| 10              | Sequans GM02SP TX1             |
| 11              | Sequans GM02SP RX1             |
| 12              | Sequans GM02SP RX2             |
| 13              | Sequans GM02SP CTS0            |
| 14              | Sequans GM02SP RTS0            |
| 15              | Sequans GM02SP CTS1            |
| 16              | Sequans GM02SP RTS1            |
| 17              | Sequans GM02SP TX2             |
| 18              | Walter input power             |
| 19              | 3.3V output (not switched)     |
| 20              | Sequans GM02SP 1.8V output     |
| 21              | Ground                         |
| 22              | ESP32-S3 GPIO3 (strapping pin) |

## Sequans GM02SP UARTs

The Sequans GM02SP module has 3 hardware UART interfaces. Only UART0 is
connected to the ESP32-S3 Wroom Module on Walter as described in the
[internal pins](#internal-pins) section. Communication between the ESP32-S3
and the modem is possible with AT-commands. Please refer to the corresponding AT
[command reference manual](https://quickspot.io/docs/file/gm02s_at_commands.pdf)
of the Sequans GM02SP for all possible AT-commands.

The UARTs have the following functionality by default:

- UART0 (115200@8N1 with HW handshaking): used for AT commands.
- UART1 (921600@8N1 with HW handshaking): used for manual firmware updates
  and/or custom software installation.
- UART2 (115200@8N1 no HW handshaking): console log output.

Please note that any UART host should be connected as follows:

- RX <-> RX
- TX <-> TX
- RTS <-> RTS
- CTS <-> CTS

## Electrical characteristics

|         Parameter        | Units | Minimum rating | Typical rating | Maximum rating |
|:------------------------:|:-----:|:--------------:|----------------|----------------|
| DC supply voltage        | V     | 3.0            | 5.0            | 5.5            |
| Digital I/O voltage      | V     | 2.64           | 3.3            | 3.6            |
| Power consumption @ 3.3V | A     | -              | -              | 1.5            |
| 3.3V output current      | mA    | -              | -              | 250            |
| Deep sleep current       | µA    | -              | 9.8            | -              |
