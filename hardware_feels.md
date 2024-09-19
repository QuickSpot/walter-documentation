## Board overview

![drawing](./img/walter-feels-transparent-01.png)

Walter Feels is a reference design of a carrier board for Walter that can also
be used as the basis of an IoT gateway. This carrier board has the following 
functionality:

 - Wide input range (2.5 - 26 V) MPPT power input
 - Single- to multi-cell and multi-chemistry (LiFePo, Li-Ion, Lead) battery
   charger. The board operates on voltages as low as 2.5V
 - I²C battery and power management (Analog Devices LTC4015)
 - MicroSD card slot
 - Sensors: temperature, humidity, barometric pressure, and 6 DoF IMU,
 - Sensor connectors: Sensirion SCD30 absolute CO₂ sensor (not included)
 - Multiple interfaces, including RS232, RS485, SDI-12, and CAN bus
 - 3.3, 5, and 12 V output
 - Two GPIO pins directly from the Walter board
 - I2C connector for other external sensors
 - Compatible with Takachi PFF13-4-13W housing for indoor applications

## MPPT power input

*MPPT* stands for Maximum Power Point Tracking, it is a technique used with
variable power sources to maximize energy extraction as conditions vary. This 
input is ideally suited to connect a renewable energy source such as a solar
panel or wind generator. The input accepts any voltage between 2.5V and 26V. 

> Solar panel voltages are specified under load. When there is almost no load
> the output voltage can get much higher which could damage the Walter Feels 
> board. You must make sure that the *Voc* or *open-circuit voltage* rating of
> the panel doesn't exceed 26V

## Battery configuration

Walter Feels' power management IC is the
[Analog Devices LTC4015](https://www.analog.com/en/products/ltc4015.html) which 
supports the following battery chemistry and cell combinations:
 - Li-Ion/Polymer: up to 9 cells
 - LiFePO4: up to 9 cells
 - Lead-Acid (Liquid, Gel, AGM): 3, 6 or 12 cells

The LTC4015 must be configured for the correct battery chemistry and cell count
before the charger will engage. To do this you need to close the correct solder
jumpers. The following table shows the configuration required to configure the 
cell count of the connected battery:

| Cell count | CELLS0 | CELLS1 | CELLS2 |
|:----------:|:------:|:------:|--------|
| 1          | H      | L      | L      |
| 2          | L      | H      | L      |
| 3          | H      | H      | L      |
| 4          | Z      | L      | L      |
| 5          | L      | Z      | L      |
| 6          | Z      | H      | L      |
| 7          | H      | Z      | L      |
| 8          | Z      | Z      | L      |
| 9          | L      | L      | H      |
| 12         | H      | H      | H      |

Legend:
 - H: close the ON jumper, leave OFF jumper open.
 - L: close the OFF jumper, leave ON jumper open.
 - Z: leave ON and OFF jumper open.

The below table gives an overview of the possible chemistries and how to
configure them. If you choose the *programmable* option you must make sure to
adopt your firmware to correctly configure charging parameters in the LTC4015.

|           Chemistry           | CHEM0 | CHEM1 |
|:-----------------------------:|:-----:|:-----:|
| Li-Ion programmable           | L     | L     |
| Li-Ion 4.2V/cell fixed        | H     | H     |
| Li-Ion 4.1V/cell fixed        | Z     | L     |
| Li-Ion 4.0V/cell fixed        | L     | Z     |
| LiFePO4 programmable          | H     | L     |
| LiFePO4 fixed fast charge     | Z     | H     |
| LiFePO4 fixed standard charge | H     | Z     |
| Lead-Acid fixed               | Z     | Z     |
| Lead-Acid programmable        | L     | H     |

Legend:
 - H: close the ON jumper, leave OFF jumper open.
 - L: close the OFF jumper, leave ON jumper open.
 - Z: leave ON and OFF jumper open.