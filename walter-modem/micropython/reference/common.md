## Methods Overview

- [reset](#reset)
- [check_comm](#check_comm)
- [get_clock](#get_clock)
- [config_cme_error_reports](#config_cme_error_reports)
- [config_cereg_reports](#config_cereg_reports)

## Enums Overview

- [WalterModemCMEErrorReportsType](#waltermodemcmeerrorreportstype)
- [WalterModemCEREGReportsType](#waltermodemceregreportstype)
- [WalterModemOpState](#waltermodemopstate)

---

## Methods

### `reset`

Physically reset the modem and wait for it to start.
All connections will be lost when this function is called.

> [!NOTE]
> The function will fail when the modem doesn't start after the reset.

#### Example

```py
if not await modem.reset():
    print('Failed to reset modem')
```

#### Params

| Param | Description                             | Default  |
| ----- | --------------------------------------- | -------- |
| `rsp` | Reference to a modem response instance. | **None** |

#### Returns

`bool`
True on success, False otherwise.

---

### `soft_reset`

Perform a soft reset on the modem, wait for it to complete.

> [!NOTE]
> The method will fail when the modem doesn't reset.

#### Example

```py
if not await modem.soft_reset():
    print('Failed to soft reset modem')
```

#### Returns

`bool`
True on success, False otherwise.

---

### `check_comm`

Sends the 'AT' command to check if the modem responds with 'OK',
verifying communication between the ESP32S3 and the modem.

#### Example

```py
if await modem.check_comm():
    print('Modem communication successfull')
```

#### Params

| Param | Description                             | Default  |
| ----- | --------------------------------------- | -------- |
| `rsp` | Reference to a modem response instance. | **None** |

#### Returns

`bool`
True on success, False otherwise.

---

### `get_clock`

Retrieves the current time and date from the modem.

#### Example

```py
modem_rsp = ModemRsp()

if await modem.get_clock(rsp=modem_rsp):
    print(modem_rsp.clock)
else:
    print('Failed to get modem clock')

```

#### Params

| Param | Description                             | Default  |
| ----- | --------------------------------------- | -------- |
| `rsp` | Reference to a modem response instance. | **None** |

#### Returns

`bool`
True on success, False otherwise.

---

### `config_cme_error_reports`

Configures the CME error report type.
By default, errors are enabled and numeric.

> [!WARNING]
> Changing this may affect error reporting.

#### Example

```py
if not await modem.config_cme_error_reports(reports_type=WalterModemCMEErrorReportsType.VERBOSE):
    print('Failed to configure CME error reports')
```

#### Params

| Param          | Description                                                   | Default                                    |
| -------------- | ------------------------------------------------------------- | ------------------------------------------ |
| `reports_type` | The [CME error report type](#waltermodemcmeerrorreportstype). | **WalterModemCMEErrorReportsType.NUMERIC** |
| `rsp`          | Reference to a modem response instance.                       | **None**                                   |

#### Returns

`bool`
True on success, False otherwise.

---

### `config_cereg_reports`

Configures the CEREG status report type.
By default, reports are enabled with minimal operational info.

> [!WARNING]
> Changing this may affect library functionality.

#### Example

```py
if not await modem.config_cereg_reports(reports_type=WalterModemCEREGReportsType.ENABLED):
    print('Failed to config CEREg reports')
```

#### Params

| Param          | Description                                                    | Default                                 |
| -------------- | -------------------------------------------------------------- | --------------------------------------- |
| `reports_type` | The [CEREG status reports type](#waltermodemceregreportstype). | **WalterModemCEREGReportsType.ENABLED** |
| `rsp`          | Reference to a modem response instance.                        | **None**                                |

#### Returns

`bool`
True on success, False otherwise.

---

## Enums

### `WalterModemCMEErrorReportsType`

Modem CME error reporting methods.

> **OFF** = `0` \
> No error reporting. \
> **NUMERIC** = `1` \
> Numeric error codes for reporting. \
> **VERBOSE** = `2` \
> Detailed verbose error messages.

### `WalterModemCEREGReportsType`

CEREG unsolicited reporting methods.

> **OFF** = `0` \
> No unsolicited reporting. \
> **ENABLED** = `1` \
> Unsolicited reporting enabled. \
> **ENABLED_WITH_LOCATION** = `2` \
> Unsolicited reporting with location information. \
> **ENABLED_WITH_LOCATION_EMM_CAUSE** = `3` \
> Unsolicited reporting with location and EMM cause. \
> **ENABLED_UE_PSM_WITH_LOCATION** = `4` \
> Unsolicited reporting with UE PSM and location. \
> **ENABLED_UE_PSM_WITH_LOCATION_EMM_CAUSE** = `5` \
> Unsolicited reporting with UE PSM, location, and EMM cause.

### `WalterModemOpState`

Modem operational modes.

> **MINIMUM** = `0` \
> Minimal operational mode. \
> **FULL** = `1` \
> Full operational mode. \
> **NO_RF** = `4` \
> No RF (Radio Frequency) operation. \
> **MANUFACTURING** = `5` \
> Manufacturing mode for testing and diagnostics.
