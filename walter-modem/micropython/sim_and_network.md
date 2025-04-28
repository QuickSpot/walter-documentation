## Methods Overview

- [getNetworkRegState](#getnetworkregstate)
- [getRSSI](#getrssi)
- [getSignalQuality](#getsignalquality)
- [getCellInformation](#getcellinformation)
- [getRAT](#getrat)
- [setRAT](#setrat)
- [getRadioBands](#getradiobands)
- [getSimState](#getsimstate)
- [unlockSim](#unlocksim)
- [setNetworkSelectionMode](#setnetworkselectionmode)

## Enums Overview

- [WalterModemNetworkRegState](#waltermodemnetworkregstate)
- [WalterModemSQNMONIReportsType](#waltermodemsqnmonireportstype)
- [WalterModemRat](#waltermodemrat)
- [WalterModemNetworkSelMode](#waltermodemnetworkselmode)
- [WalterModemOperatorFormat](#waltermodemoperatorformat)

---

## Methods

### `getNetworkRegState`

Get the network registration state.
This is buffered by the library and thus instantly available.

#### Example

```py
if modem.get_network_reg_state() in (
    WalterModemNetworkRegState.REGISTERED_HOME,
    WalterModemNetworkRegState.REGISTERED_ROAMING
):
    # ...
```

#### Returns

[`WalterModemNetworkRegState`](#waltermodemnetworkregstate) \
The current modem registration state

---

### `getRSSI`

Retrieves the RSSI information.

#### Example

```py
modem_rsp = ModemRsp()

if await modem.get_rssi(rps=modem_rsp):
    print(modem_rsp.rssi)
else:
    print('Failed to get modem RSSI')

```

#### Params

| Param | Description                             | Default  |
| ----- | --------------------------------------- | -------- |
| `rsp` | Reference to a modem response instance. | **None** |

#### Returns

`bool`
True on success, False otherwise.

---

### `getSignalQuality`

Retrieves information about the serving and neighbouring cells,
including operator, cell ID, RSSI, and RSRP.

#### Example

```py
modem_rsp = ModemRsp()

if await modem.get_signal_quality(rps=modem_rsp):
    print(f'rsrp: {modem_rsp.signal_quality.rsrp}')
    print(f'rsrq: {modem_rsp.signal_quality.rsrq}')
else:
    print('Failed to get signal quality')

```

#### Params

| Param | Description                             | Default  |
| ----- | --------------------------------------- | -------- |
| `rsp` | Reference to a modem response instance. | **None** |

#### Returns

`bool`
True on success, False otherwise.

---

### `getCellInformation`

Retrieves the modem's identity details, including IMEI, IMEISV, and SVN.

#### Example

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

#### Params

| Param          | Description                                                                | Default                                        |
| -------------- | -------------------------------------------------------------------------- | ---------------------------------------------- |
| `reports_type` | The [type of cell information](#waltermodemsqnmonireportstype) to retreive | **WalterModemSQNMONIReportsType.SERVING_CELL** |
| `rsp`          | Reference to a modem response instance.                                    | **None**                                       |

#### Returns

`bool`
True on success, False otherwise.

---

### `getRAT`

Retrieves the Radio Access Technology (RAT) for the modem.

#### Example

```py
modem_rsp = ModemRsp()

if await modem.get_rat(rps=modem_rsp):
    print(modem_rsp.rat)
else:
    print('Failed to get modem RAT')
```

#### Params

| Param | Description                             | Default  |
| ----- | --------------------------------------- | -------- |
| `rsp` | Reference to a modem response instance. | **None** |

#### Returns

`bool`
True on success, False otherwise.

---

### `setRAT`

Sets the Radio Access Technology (RAT) for the modem.

#### Example

```py
if not await modem.set_rat(WalterModemRat.LTEM):
    print('Failed to set RAT to LTEM')
```

#### Params

| Param | Description                             | Default  |
| ----- | --------------------------------------- | -------- |
| `rat` | The new [RAT](#waltermodemrat)          |          |
| `rsp` | Reference to a modem response instance. | **None** |

#### Returns

`bool`
True on success, False otherwise.

---

### `getRadioBands`

Retrieves the radio bands the modem is configured to use for network connection.

#### Example

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

#### Params

| Param | Description                             | Default  |
| ----- | --------------------------------------- | -------- |
| `rsp` | Reference to a modem response instance. | **None** |

#### Returns

`bool`
True on success, False otherwise.

---

### `getSimState`

Retrieves the state of the SIM card.

#### Example

```py
modem_rsp = ModemRsp()

if await modem.get_sim_state(rps=modem_rsp):
    print(WalterModemSimState.get_value_name(modem_rsp.sim_state))
else:
    print('Failed to get SIM state')
```

#### Params

| Param | Description                             | Default  |
| ----- | --------------------------------------- | -------- |
| `rsp` | Reference to a modem response instance. | **None** |

#### Returns

`bool`
True on success, False otherwise.

---

### `unlockSim`

Sets the SIM card's PIN code.

> [!NOTE]
> The modem must be in FULL or NO_RF operational state.

#### Example

```py
if not await modem.unlock_sim():
    print('Failed to unlock SIM')
```

#### Params

| Param | Description                                      | Default  |
| ----- | ------------------------------------------------ | -------- |
| `pin` | The PIN code of the SIM card or NULL for no pin. | **None** |
| `rsp` | Reference to a modem response instance.          | **None** |

#### Returns

`bool`
True on success, False otherwise.

---

### `setNetworkSelectionMode`

Sets the network selection mode for Walter.

> [!NOTE]
> This command is only available when the modem is in the fully operational state.

#### Example

```py
if not await modem.set_network_selection_mode(WalterModemNetworkSelMode.AUTOMATIC):
    print('Failed to set network selection mode to automatic')
```

#### Params

| Param             | Description                                                                            | Default                                         |
| ----------------- | -------------------------------------------------------------------------------------- | ----------------------------------------------- |
| `mode`            | The [network selection mode](#setnetworkselectionmode).                                | **WalterModemNetworkSelMode.AUTOMATIC**         |
| `operator_name`   | The network operator name in case manual selection has been chosen.                    | **""**                                          |
| `operator_format` | The [format](#waltermodemoperatorformat) in which the network operator name is passed. | **WalterModemOperatorFormat.LONG_ALPHANUMERIC** |
| `rsp`             | Reference to a modem response instance.                                                | **None**                                        |

#### Returns

`bool`
True on success, False otherwise.

---

## Enums

### `WalterModemNetworkRegState`

Modem network registration states.

> **NOT_SEARCHING** = `0` \
> **REGISTERED_HOME** = `1` \
> **SEARCHING** = `2` \
> **DENIED** = `3` \
> **UNKNOWN** = `4` \
> **REGISTERED_ROAMING** = `5` \
> **REGISTERED_SMS_ONLY_HOME** = `6` \
> **REGISTERED_SMS_ONLY_ROAMING** = `7` \
> **ATTACHED_EMERGENCY_ONLY** = `8` \
> **REGISTERED_CSFB_NOT_PREFERRED_HOME** = `9` \
> **REGISTERED_CSFB_NOT_PREFERRED_ROAMING** = `10` \
> **REGISTERED_TEMP_CONN_LOSS** = `80` \

### `WalterModemSQNMONIReportsType`

SQNMONI cell information reporting scopes.

> **SERVING_CELL** = `0` \
> Reports only the serving cell. \
> **INTRA_FREQUENCY_CELLS** = `1` \
> Reports cells on the same frequency. \
> **INTER_FREQUENCY_CELLS** = `2` \
> Reports cells on different frequencies. \
> **ALL_CELLS** = `7` \
> Reports all available cells. \
> **SERVING_CELL_WITH_CINR** = `9` \
> Reports the serving cell with CINR (Carrier-to-Interference-plus-Noise Ratio).

### `WalterModemRat`

Types of 3GPP access technologies supported by Walter.

> **LTEM** = `0` \  
> LTE-M (Long-Term Evolution for Machines). \
> **NBIOT** = `1` \
> NB-IoT (Narrowband Internet of Things). \
> **AUTO** = `2` \
> Automatic selection of access technology.

### `WalterModemNetworkSelMode`

Support network selection modes.

> **AUTOMATIC** = `0` \
> Automatically selects a network. \
> **MANUAL** = `1` \
> Manually selects a network. \
> **UNREGISTER** = `2` \
> Disconnects from the network. \
> **MANUAL_AUTO_FALLBACK** = `4` \
> Manual selection with automatic fallback.

### `WalterModemOperatorFormat`

Supported netowrk operator formats.

> **LONG_ALPHANUMERIC** = `0` \
> Full operator name (e.g., "Vodafone UK"). \
> **SHORT_ALPHANUMERIC** = `1` \
> Short operator name (e.g., "Vodafone"). \
> **NUMERIC** = `2` \
> Numeric operator code (e.g., "23415").
