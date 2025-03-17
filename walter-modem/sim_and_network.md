## Methods Overview

- [getNetworkRegState](#getnetworkregstate)
- [getRssi](#getrssi)
- [getSignalQuality](#getsignalquality)
- [getCellInformation](#getcellinformation)
- [getRat](#getrat)
- [setRat](#setrat)
- [getRadioBands](#getradiobands)
- [getSimState](#getsimstate)
- [unlockSim](#unlocksim)
- [setNetworkSelectionMode](#setnetworkselectionmode)

## Enums Overview

---

## Methods

### `getNetworkRegState`

Get the network registration state.
This is buffered by the library and thus instantly available.

#### Example

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

```py
if modem.get_network_reg_state() in (
    WalterModemNetworkRegState.REGISTERED_HOME,
    WalterModemNetworkRegState.REGISTERED_ROAMING
):
    # ...
```

<!-- tabs:end -->

#### Returns

`WalterModemNetworkRegState` \
The current modem registration state

---

### `getRssi`

Retrieves the RSSI information.

#### Example

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

```py
modem_rsp = ModemRsp()

if await modem.get_rssi(rps=modem_rsp):
    print(modem_rsp.rssi)
else:
    print('Failed to get modem RSSI')

```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

| Param | Description                             | Default  |
| ----- | --------------------------------------- | -------- |
| `rsp` | Reference to a modem response instance. | **None** |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

### `getSignalQuality`

Retrieves information about the serving and neighbouring cells,
including operator, cell ID, RSSI, and RSRP.

#### Example

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

```py
modem_rsp = ModemRsp()

if await modem.get_signal_quality(rps=modem_rsp):
    print(modem_rsp.signal_quality.rsrp)
else:
    print('Failed to get signal quality')

```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

| Param | Description                             | Default  |
| ----- | --------------------------------------- | -------- |
| `rsp` | Reference to a modem response instance. | **None** |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

### `getCellInformation`

Retrieves the modem's identity details, including IMEI, IMEISV, and SVN.

#### Example

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

```py
modem_rsp = ModemRsp()

if await modem.get_cell_information(rps=modem_rsp):
    print(f'net name: {modem_rsp.cell_information.net_name}')
    print(f'cid: {modem_rsp.cell_information.cid}')
    print(f'band: {modem_rsp.cell_information.band}')
    # ...
else:
    print('Failed to get cell information')
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

| Param          | Description                              | Default                                        |
| -------------- | ---------------------------------------- | ---------------------------------------------- |
| `reports_type` | The type of cell information to retreive | **WalterModemSQNMONIReportsType.SERVING_CELL** |
| `rsp`          | Reference to a modem response instance.  | **None**                                       |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

### `getRat`

Retrieves the Radio Access Technology (RAT) for the modem.

#### Example

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

```py
modem_rsp = ModemRsp()

if await modem.get_rat(rps=modem_rsp):
    print(modem_rsp.rat)
else:
    print('Failed to get modem RAT')
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

| Param | Description                             | Default  |
| ----- | --------------------------------------- | -------- |
| `rsp` | Reference to a modem response instance. | **None** |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

### `setRat`

Sets the Radio Access Technology (RAT) for the modem.

#### Example

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

```py
if not await modem.set_rat(WalterModemRat.LTEM):
    print('Failed to set RAT to LTEM')
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

| Param | Description                             | Default  |
| ----- | --------------------------------------- | -------- |
| `rat` | The new RAT                             |          |
| `rsp` | Reference to a modem response instance. | **None** |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

### `getRadioBands`

Retrieves the radio bands the modem is configured to use for network connection.

#### Example

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

```py
modem_rsp = ModemRsp()

if await modem.get_radio_bands(rps=modem_rsp):
    for band_sel in modem_rsp.band_sel_cfg_list:
        print(f'net_operator: {band_sel.net_operator} (rat: {band_sel.rat})')

        print('bands:')
        for band in band_sel:
            print(f'  {band}')
    # ...
else:
    print('Failed to get radio bands')
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

| Param | Description                             | Default  |
| ----- | --------------------------------------- | -------- |
| `rsp` | Reference to a modem response instance. | **None** |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

### `getSimState`

Retrieves the state of the SIM card.

#### Example

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

```py
modem_rsp = ModemRsp()

if await modem.get_sim_state(rps=modem_rsp):
    print(WalterModemSimState.get_value_name(modem_rsp.sim_state))
else:
    print('Failed to get SIM state')
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

| Param | Description                             | Default  |
| ----- | --------------------------------------- | -------- |
| `rsp` | Reference to a modem response instance. | **None** |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

### `unlockSim`

Sets the SIM card's PIN code.

> [!NOTE]
> The modem must be in FULL or NO_RF operational state.

#### Example

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

```py
if not await modem.unlock_sim():
    print('Failed to unlock SIM')
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

| Param | Description                                      | Default  |
| ----- | ------------------------------------------------ | -------- |
| `pin` | The PIN code of the SIM card or NULL for no pin. | **None** |
| `rsp` | Reference to a modem response instance.          | **None** |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

### `setNetworkSelectionMode`

Sets the network selection mode for Walter.

> [!NOTE]
> This command is only available when the modem is in the fully operational state.

#### Example

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

```py
if not await modem.set_network_selection_mode(WalterModemNetworkSelMode.AUTOMATIC):
    print('Failed to set network selection mode to automatic')
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

| Param             | Description                                                         | Default                                         |
| ----------------- | ------------------------------------------------------------------- | ----------------------------------------------- |
| `mode`            | The network selection mode.                                         | **WalterModemNetworkSelMode.AUTOMATIC**         |
| `operator_name`   | The network operator name in case manual selection has been chosen. | **""**                                          |
| `operator_format` | The format in which the network operator name is passed.            | **WalterModemOperatorFormat.LONG_ALPHANUMERIC** |
| `rsp`             | Reference to a modem response instance.                             | **None**                                        |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---
