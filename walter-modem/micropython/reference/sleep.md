## Methods Overview

- [sleep](#sleep)
- [config_PSM](#config_psm)
- [config_EDRX](#config_edrx)

## Enums Overview

- [WalterModemPSMMode](#waltermodempsmmode)
- [WalterModemEDRXMODE](#waltermodemedrxmode)

---

## Methods

### `sleep`

This function will put Walter into deep sleep or light sleep for a given duration.

The typical power consumption is:
- **1mA** in light sleep
- **8µA** in deep sleep

> [!NOTE]
> Sleep applies to the ESP32-S3 only, the modem can remain active during sleep.\
> To reach the low power consumption described above,
> it is recommended to configure the power saving functions of the modem.

#### Example

```py
modem.sleep(sleep_time_ms=20000, persist_mqtt_subs=False)
```

#### Params

| Param               | Description                                                       | Default   |
| ------------------- | ----------------------------------------------------------------- | --------- |
| `sleep_time_ms`     | The time to sleep *(in ms)*                                       |           |
| `light_sleep`       | True to go to lightsleep, False to go to deepsleep.               | **False** |
| `persist_mqtt_subs` | Whether or not to persist the mqtt subscriptions after deepsleep. | **False** |

---

### `config_PSM`

Configure PSM on the modem.

> [!NOTE]
> What you get from the network may not be exactly the same as what was requested.

#### Example

```py
await modem.config_PSM(
    mode=WalterModemPSMMode.ENABLE_PSM,
    periodic_TAU_s=678
)
```

#### Params

| Param            | Description                                                                     | Default  |
| ---------------- | ------------------------------------------------------------------------------- | -------- |
| `mode`           | Enable, Disable or Disable & Reset. ([WalterModemPSMMode](#waltermodempsmmode)) |          |
| `periodic_TAU_s` | The Periodic TAU in seconds.                                                    | **None** |
| `active_time`    | The Active Time in seconds.                                                     | **None** |
| `rsp`            | Reference to a modem response instance.                                         | **None** |

#### Returns

`bool`
True on success, False otherwise

---

### `config_EDRX`

Configure eDRX on the modem.

> [!NOTE]
> What you get from the network may not be exactly the same as what was requested.

#### Example

```py
await modem.config_EDRX(
    mode=WalterModemEDRXMODE.ENABLE_EDRX,
    req_edrx_val='0101',
    req_ptw='0001'
)
```

#### Params

| Param          | Description                                                                       | Default  |
| -------------- | --------------------------------------------------------------------------------- | -------- |
| `mode`         | Enable, Disable or Disable & Reset. ([WalterModemEDRXMODE](#waltermodemedrxmode)) |          |
| `req_edrx_val` | String: a nibble                                                                  | **None** |
| `req_ptw`      | String: a nibble                                                                  | **None** |
| `rsp`          | Reference to a modem response instance.                                           | **None** |

#### Returns

`bool`
True on success, False otherwise

---

## Enums

### `WalterModemPSMMode`

Indication to disable or enable the use of PSM.

> **DISABLE_PSM** = `0` \
> **ENABLE_PSM** = `1` \
> **DISABLE_AND_DISCARD_ALL_PARAMS** = `2`\
> Sets manufacturer specific defaults if available.

### `WalterModemEDRXMODE`

Indication to disable or enable the use of eDRX.

> **DISABLE_EDRX** = `0` \
> **ENABLE_EDRX** = `1` \
> **ENABLE_EDRX_AND_UNSOLICITED_RESULT_CODE** = `2` \
> **DISABLE_AND_DISCARD_ALL_PARAMS** = `3`\
> Sets manufacturer specific defaults if available.
