## Methods Overview

- [configGnss](#configgnss)
- [getGnnsAssistanceStatus](#getgnssassistancestatus)
- [updateGnssAssistance](#updategnssassistance)
- [performGnssAction](#performgnssaction)
- [waitForGnssFix](#waitforgnssfix)

## Enums Overview

---

## Methods

### `configGnss`

Configures Walter's GNSS receiver with persistent settings that
may need to be reset after a modem firmware upgrade.
Can also adjust sensitivity mode between fixes.

> [!TIP]
> Recommended to run at least once before using GNSS.

#### Example

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

```py
if not await modem.config_gnss():
    print('Failed to configure GNSS subsystem')
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

| Param       | Description                                        | Default                                       |
| ----------- | -------------------------------------------------- | --------------------------------------------- |
| `sens_mode` | The [sensitivity mode](#waltermodemgnsssensmode).  | **WalterModemGNSSSensMode.HIGH**              |
| `acq_mode`  | The [acquisition mode](#waltermodemgnssacqmode).   | **WalterModemGNSSAcqMode.COLD_WARM_START**    |
| `loc_mode`  | The [GNSS location mode](#waltermodemgnsslocmode). | **WalterModemGNSSLocMode.ON_DEVICE_LOCATION** |
| `rsp`       | Reference to a modem response instance             | **None**                                      |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

### `getGnssAssistanceStatus`

Retrieves the status of the assistance data
currently loaded in the GNSS subsystem.

#### Example

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

```py
if not await modem.get_gnss_assistance_status(rsp=modem_rsp):
    print('Failed to request GNSS assistance status')
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

| Param | Description                            | Default  |
| ----- | -------------------------------------- | -------- |
| `rsp` | Reference to a modem response instance | **None** |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

### `updateGnssAssistance`

Connects to the cloud to download and update the GNSS subsystem
with the requested assistance data.

Real-time ephemeris is the most efficient type.

#### Example

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

```py
if not await modem.update_gnss_assistance():
    print('Failed to update almanac data')
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

| Param  | Description                                                                   | Default                                              |
| ------ | ----------------------------------------------------------------------------- | ---------------------------------------------------- |
| `type` | The [type of GNSS assistance data](#waltermodemgnssassistancetype) to update. | **WalterModemGNSSAssistanceType.REALTIME_EPHEMERIS** |
| `rsp`  | Reference to a modem response instance                                        | **None**                                             |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

### `performGnssAction`

Programs the GNSS subsystem to perform a specified action.

#### Example

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

```py
if not await modem.perform_gnss_action(
    action=WalterModemGNSSAction.GET_SINGLE_FIX,
    rsp=modem_rsp
):
    print('Failed to request GNSS fix',
          WalterModemCMEError.get_value_name(modem_rsp.cme_error))
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

| Param    | Description                                                             | Default                                  |
| -------- | ----------------------------------------------------------------------- | ---------------------------------------- |
| `action` | The [action for the GNSS subsystem](#waltermodemgnssaction) to perform. | **WalterModemGNSSAction.GET_SINGLE_FIX** |
| `rsp`    | Reference to a modem response instance.                                 | **None**                                 |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

### `waitForGnssFix`

Waits for a gnss fix before then returning it.

#### Example

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

```py
gnss_fix = await modem.wait_for_gnss_fix()
```

<!-- tabs:end -->

#### Returns

`ModemGNSSFix`

---

## Enums

### `WalterModemGNSSSensMode`

The possible sensitivity settings use by Walter's GNSS receiver.
This sets the amount of time that the receiver is actually on.

More sensitivity requires more power.

<!-- tabs:start -->

#### **Arduino**

#### **ESP-IDF**

#### **Micropython**

> **LOW** = `1` \
> **MEDIUM** = `2` \
> **HIGH** = `3`

<!-- tabs:end -->

### `WalterModemGNSSAcqMode`

The possible GNSS acquisition modes.

When no ephemerides are available and/or the time is not known
cold start will be used automatically.

<!-- tabs:start -->

#### **Arduino**

#### **ESP-IDF**

#### **Micropython**

> **COLD_WARM_START** = `0` \
> Walter has no clue where he is on earth. \
> **HOT_START** = `1` \
> Walter must know where he is within 100km.

<!-- tabs:end -->

### `WalterModemGNSSLocMode`

The GNSS location modus.

<!-- tabs:start -->

#### **Arduino**

#### **ESP-IDF**

#### **Micropython**

> **ON_DEVICE_LOCATION** = `0` \
> The GNSS sybsystem will compute
> position and speed and estimate the error on these parameters.

<!-- tabs:end -->

### `WalterModemGNSSAssistanceType`

Types of GNSS assistance data used to improve positioning performance.

<!-- tabs:start -->

#### **Arduino**

#### **ESP-IDF**

#### **Micropython**

> **ALMANAC** = `0` \
> Long-term orbital data providing coarse satellite positions and health status. \
> **REALTIME_EPHEMERIS** = `1` \
> Real-time satellite position and velocity data for immediate accuracy. \
> **PREDICTED_EPHEMERIS** = `2` \
> Forecasted satellite position data for faster cold starts without a live connection.

<!-- tabs:end -->

### `WalterModemGNSSAction`

Supported actions that Walter's GNSS can execute.

<!-- tabs:start -->

#### **Arduino**

#### **ESP-IDF**

#### **Micropython**

> **GET_SINGLE_FIX** = `0` \
> **CANCEL** = `1`

<!-- tabs:end -->
