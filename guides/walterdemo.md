## QuickSpot WalterDemo data protocol

The Walter demo server at `walterdemo.quickspot.io:1999` accepts UDP packets
containing binary sensor data.  
This guide specifies the supported packet formats for data transmission.

## Support Packet Lengths

The server accepts packets with these exact byte lengths:
**8, 14, 15, 18, 20, 23, 24, 27, 29, 30, 37, 39, 51, 71 bytes.**  
All packets begin with a 6-byte device MAC address, followed by sensor data in
a format specific to the packet length.

## Packet Formats

- [8-Byte Packet: Counter](#_8-byte-packet-counter)
- [14-Byte Packet: Environmental Sensors](#_14-byte-packet-environmental-sensors)
- [15-Byte Packet: GPS Position](#_15-byte-packet-gps-position)
- [18-Byte Packet: Single Sensor & GPS](#_18-byte-packet-single-sensor--gps)
- [20-Byte Packet: Audio & Cellular Network](#_20-byte-packet-audio--cellular-network)
- [23-Byte Packet: Environmental & GPS](#_23-byte-packet-environmental--gps)
- [24-Byte Packet: Counter, Sensor, Celinfo & RAT](#_24-byte-packet-counter-sensor-celinfo--rat)
- [27-Byte Packet: Air Quality, Environmental & GPS](#_27-byte-packet-air-quality-environmental--gps)
- [29-Byte Packet: Positioning](#_29-byte-packet-positioning)
- [30-Byte Packet: Positioning & RAT](#_30-byte-packet-positioning--rat)
- [37/39-Byte Packet: Walter Feels](#_3739-byte-packet-walter-feels)
- [51-Byte Packet: Walter Feels, Cell Info & RAT](#_51-byte-packet-walter-feels-cell-info--rat)
- [71-Byte Packet: Environmental & Marine](#_71-byte-packet-environmental--marine)

### 8-Byte Packet: Counter

| Bytes | Field       | Type      |
| ----- | ----------- | --------- |
| `0-5` | MAC Address | Raw bytes |
| `6-7` | Counter     | uint16 BE |

### 14-Byte Packet: Environmental Sensors

| Bytes   | Field             | Type      | Note                      |
| ------- | ----------------- | --------- | ------------------------- |
| `0-5`   | MAC Address       | Raw bytes |                           |
| `6-7`   | Relative Humidity | uint16 BE | *value / 100 = %*         |
| `8-9`   | Temperature       | uint16 BE | *(value / 100) - 50 = °C* |
| `10-11` | Light Level       | uint16 BE | *value / 10 = lux*        |
| `12-13` | Ambient Pressure  | uint16 BE | *value / 10 = hPa*        |

### 15-Byte Packet: GPS Position

| Bytes   | Field           | Type       | Note      |
| ------- | --------------- | ---------- | --------- |
| `0-5`   | MAC Address     | Raw bytes  |           |
| `6`     | Satellite Count | uint8      |           |
| `7-10`  | Latitude        | float32 LE | *Degrees* |
| `11-14` | Longitde        | float32 LE | *Degrees* |

### 18-Byte Packet: Single Sensor & GPS

| Bytes   | Field           | Type       | Note                                   |
| ------- | --------------- | ---------- | -------------------------------------- |
| `0-5`   | MAC Address     | Raw bytes  |                                        |
| `6`     | Sensor Type     | uint8      | *2 = temperature*                      |
| `7-8`   | Sensor Value    | uint16 BE  | *Temperature: (value / 100) - 50 = °C* |
| `9`     | Satellite Count | uint8      |                                        |
| `10-13` | Latitude        | float32 LE |                                        |
| `14-17` | Longitude       | float32 LE |                                        |

### 20-Byte Packet: Audio & Cellular Network

| Bytes   | Field       | Type      | Note                                        |
| ------- | ----------- | --------- | ------------------------------------------- |
| `0-5`   | MAC Address | Raw bytes |                                             |
| `6`     | Audio Level | uint8     | *dB*                                        |
| `7`     | Audio Min   | uint8     | *dB*                                        |
| `8`     | Audio Max   | uint8     | *dB*                                        |
| `9-10`  | MCC         | uint16 BE | *Mobile Country Code*                       |
| `11-12` | MNC         | uint16 BE | *Mobile Network Code*                       |
| `13-14` | TAC         | uint16 BE | *Tracking Area Code*                        |
| `15-18` | Cell ID     | uint32 BE |                                             |
| `19`    | RSRP        | uint8     | *Signal strength (positive value for -dBm)* |

### 23-Byte Packet: Environmental & GPS

| Bytes   | Field             | Type       | Note                      |
| ------- | ----------------- | ---------- | ------------------------- |
| `0-5`   | MAC Address       | Raw bytes  |                           |
| `6-7`   | Relative Humidity | uint16 BE  | *value / 100 = %*         |
| `8-9`   | Temperature       | uint16 BE  | *(value / 100) - 50 = °C* |
| `10-11` | Light Level       | uint16 BE  | *value / 10 = lux*        |
| `12-13` | Ambient Pressure  | uint16 BE  | *value / 10 = hPa*        |
| `14`    | Satellite Count   | uint8      |                           |
| `15-18` | Latitude          | float32 LE | *Degrees*                 |
| `19-22` | Longitude         | float32 LE | *Degrees*                 |

### 24-Byte Packet: Counter, Sensor, Celinfo & RAT

| Bytes   | Field       | Type      | Note                                  |
| ------- | ----------- | --------- | ------------------------------------- |
| `0-5`   | MAC Address | Raw bytes |                                       |
| `6-7`   | Counter     | uint16 BE |                                       |
| `8-9`   | Temperature | uint16 BE | *(value / 100) - 50 = °C*             |
| `10-11` | MCC         | uint16 BE | *Mobile Country Code*                 |
| `12-13` | MNC         | uint16 BE | *Mobile Network Code*                 |
| `14-15` | TAC         | uint16 BE | *Tracking Area Code*                  |
| `16-19` | Cell ID     | uint32 BE |                                       |
| `20`    | RSRP        | uint8     | *Signal strength (positive for -dBm)* |
| `21`    | RSRQ        | uint8     | *Signal strength (positive for -dBm)* |
| `22`    | RAT         | uint8     | *Radio Access Technology*             |

### 27-Byte Packet: Air Quality, Environmental & GPS

| Bytes   | Field             | Type       | Note                      |
| ------- | ----------------- | ---------- | ------------------------- |
| `0-5`   | MAC Address       | Raw bytes  |                           |
| `6-7`   | PM1.0             | uint16 BE  | *value / 100 = µg/m³*     |
| `8-9`   | PM2.5             | uint16 BE  | *value / 100 = µg/m³*     |
| `10-11` | PM4.0             | uint16 BE  | *value / 100 = µg/m³*     |
| `12-13` | PM10              | uint16 BE  | *value / 100 = µg/m³*     |
| `14-15` | Temperature       | uint16 BE  | *(value / 100) - 50 = °C* |
| `16-17` | Relative Humidity | uint16 BE  | *value / 100 = %*         |
| `18`    | Satellite Count   | uint8      |                           |
| `19-22` | Latitude          | float32 LE |                           |
| `23-26` | Longitude         | float32 LE |                           |

### 29-Byte Packet: Positioning

| Bytes   | Field           | Type       | Note                                        |
| ------- | --------------- | ---------- | ------------------------------------------- |
| `0-5`   | MAC Address     | Raw bytes  |                                             |
| `6`     | Sensor Type     | uint8      | *2 = temperature*                           |
| `7-8`   | Sensor Value    | uint16 BE  | *Temperature: (value / 100) - 50 = °C*      |
| `9`     | Satellite Count | uint8      |                                             |
| `10-13` | Latitude        | float32 LE |                                             |
| `14-17` | Longitude       | float32 LE |                                             |
| `18-19` | MCC             | uint16 BE  | *Movile Country Code*                       |
| `20-21` | MNC             | uint16 BE  | *Mobile Network Code*                       |
| `22-23` | TAC             | uint16 BE  | *Tracking Area Code*                        |
| `24-27` | Cell ID         | uint32 BE  |                                             |
| `28`    | RSRP            | uint8      | *Signal strength (positive value for -dBm)* |

### 30-Byte Packet: Positioning & RAT

| Bytes   | Field           | Type       | Note                                   |
| ------- | --------------- | ---------- | -------------------------------------- |
| `0-5`   | MAC Address     | Raw bytes  |                                        |
| `6`     | Sensor Type     | uint8      | *2 = temperature*                      |
| `7-8`   | Sensor Value    | uint16 BE  | *Temperature: (value / 100) - 50 = °C* |
| `9`     | Satellite Count | uint8      |                                        |
| `10-13` | Latitude        | float32 LE |                                        |
| `14-17` | Longitude       | float32 LE |                                        |
| `18-19` | MCC             | uint16 BE  | *Mobile Country Code*                  |
| `20-21` | MNC             | uint16 BE  | *Mobile Network Code*                  |
| `22-23` | TAC             | uint16 BE  | *Tracking Area Code*                   |
| `24-27` | Cell ID         | uint32 BE  |                                        |
| `28`    | RSRP            | uint8      | *Signal strength (positive for -dBm)*  |
| `29`    | RAT             | uint8      | *Radio Access Technology*              |

### 37/39-Byte Packet: Walter Feels

| Bytes   | Field           | Type      | Note               |
| ------- | --------------- | --------- | ------------------ |
| `0-5`   | MAC Address     | Raw bytes |                    |
| `6-7`   | Temperature     | int16 BE  | *value / 100 = °C* |
| `8-9`   | Humidity        | uint16 BE | *value / 100 = %*  |
| `10-11` | Pressure        | uint16 BE | *value / 10 = hPa* |
| `12-13` | CO2             | uint16 BE | *Raw value*        |
| `14-15` | Charge Mode     | uint16 BE | *Raw Value*        |
| `16-17` | Charger State   | uint16 BE | *Raw Value*        |
| `18-19` | Input Voltage   | uint16 BE | *value / 1000 = V* |
| `20-21` | Input Current   | int16 BE  | *value / 1000 = A* |
| `22-23` | Battery Voltage | uint16 BE | *value / 1000 = V* |
| `24-25` | Battery Voltage | uint16 BE | *value / 1000 = V* |
| `26-27` | Battery Current | int16 BE  | *value / 1000 = A* |

37-Byte variant remainder:

| Bytes   | Field           | Type       |
| ------- | --------------- | ---------- |
| `28`    | Satellite Count | uint8      |
| `29-32` | Latitude        | float32 LE |
| `33-36` | Longitude       | float32 LE |

39-Byte variant remainder:

| Bytes   | Field              | Type       | Note              |
| ------- | ------------------ | ---------- | ----------------- |
| `28-29` | Battery Percentage | uint16 BE  | *value / 100 = %* |
| `30`    | Satellite Count    | uint8      |                   |
| `31-34` | Latitude           | float32 LE |                   |
| `35-38` | Longitude          | float32 LE |                   |

### 51-Byte Packet: Walter Feels, Cell Info & RAT

| Bytes   | Field           | Type       | Note                                  |
| ------- | --------------- | ---------- | ------------------------------------- |
| `0-5`   | MAC Address     | Raw bytes  |                                       |
| `6-7`   | Temperature     | int16 BE   | *value / 100 = °C*                    |
| `8-9`   | Humidity        | uint16 BE  | *value / 100 = %*                     |
| `10-11` | Pressure        | uint16 BE  | *value / 10 = hPa*                    |
| `12-13` | CO2             | uint16 BE  | *Raw value*                           |
| `14-15` | Charge Mode     | uint16 BE  | *Raw value*                           |
| `16-17` | Charger State   | uint16 BE  | *Raw value*                           |
| `18-19` | Input Voltage   | uint16 BE  | *value / 1000 = V*                    |
| `20-21` | Input Current   | int16 BE   | *value / 1000 = A*                    |
| `22-23` | System Voltage  | uint16 BE  | *value / 1000 = V*                    |
| `24-25` | Battery Voltage | uint16 BE  | *value / 1000 = V*                    |
| `26-27` | Battery Current | int16 BE   | *value / 1000 = A*                    |
| `28`    | -               | Padding    | *(from earlier packets)*              |
| `29-30` | Satellite Count | uint8      |                                       |
| `31-34` | Latitude        | float32 LE |                                       |
| `35-38` | Longitude       | float32 LE |                                       |
| `39-40` | MCC             | uint16 BE  | *Mobile Country Code*                 |
| `41-42` | MNC             | uint16 BE  | *Mobile Network Code*                 |
| `43-44` | TAC             | uint16 BE  | *Tracking Area Code*                  |
| `45-48` | Cell ID         | uint32 BE  |                                       |
| `49`    | RSRP            | uint8      | *Signal strength (positive for -dBm)* |
| `50`    | RAT             | uint8      | *Radio Access Technology*             |

### 71-Byte Packet: Environmental & Marine

| Bytes   | Field                | Type       | Note               |
| ------- | -------------------- | ---------- | ------------------ |
| `0-5`   | MAC Address          | Raw bytes  |                    |
| `6-7`   | Temperature          | int16 BE   | *value / 100 = °C* |
| `8-9`   | Humidity             | uint16 BE  | *value / 100 = %*  |
| `10-11` | Pressure             | uint16 BE  | *value / 10 = hPa* |
| `12-13` | CO2                  | uint16 BE  | *Raw value*        |
| `14-15` | Charge Mode          | uint16 BE  | *Raw Value*        |
| `16-17` | Charger State        | uint16 BE  | *Raw Value*        |
| `18-19` | Input Voltage        | uint16 BE  | *value / 1000 = V* |
| `20-21` | Input Current        | int16 BE   | *value / 1000 = A* |
| `22-23` | Battery Voltage      | uint16 BE  | *value / 1000 = V* |
| `24-25` | Battery Voltage      | uint16 BE  | *value / 1000 = V* |
| `26-27` | Battery Current      | int16 BE   | *value / 1000 = A* |
| `28-29` | Battery Percentage   | uint16 BE  | *value / 100 = %*  |
| `30`    | Satellite Count      | uint8      |                    |
| `31-34` | Latitude             | float32 LE |                    |
| `35-38` | Longitude            | float32 LE |                    |
| `39-42` | Water Tubidity       | float32 LE |                    |
| `43-46` | Water Conductivity   | float32 LE |                    |
| `47-50` | Oxygen Concentration | float32 LE |                    |
| `51-54` | Oxygen Saturation    | float32 LE |                    |
| `55-58` | Water Temperature    | float32 LE |                    |
| `59-62` | Water Pressure       | float32 LE |                    |
| `53-66` | Sensor Temperature   | float32 LE |                    |
| `57-70` | Sound Velocity       | float32 LE |                    |
