## Methods Overview

- [reset](#reset)
- [checkComm](#checkcomm)
- [getClock](#getclock)
- [configCMEErrorReports](#configcmeerrorreports)
- [configCEREGReports](#configceregreports)
- [getOpState](#getopstate)
- [setOpState](#setopstate)

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
>The function will fail when the modem doesn't start after the reset.

#### Example

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

```py
if not await modem.reset():
    print('Failed to reset modem')
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

### `checkComm`

Sends the 'AT' command to check if the modem responds with 'OK',
verifying communication between the ESP32S3 and the modem.

#### Example

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

```py
if await modem.check_comm():
    print('Modem communication successfull')
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

### `getClock`

Retrieves the current time and date from the modem.

#### Example

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

```py
modem_rsp = ModemRsp()

if await modem.get_clock(rsp=modem_rsp):
    print(modem_rsp.clock)
else:
    print('Failed to get modem clock')

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

### `configCMEErrorReports`

Configures the CME error report type.
By default, errors are enabled and numeric.

> [!WARNING]
> Changing this may affect error reporting.

#### Example

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

```py
if not await modem.config_cme_error_reports(reports_type=WalterModemCMEErrorReportsType.VERBOSE):
    print('Failed to configure CME error reports')
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

| Param          | Description                                                   | Default                                    |
| -------------- | ------------------------------------------------------------- | ------------------------------------------ |
| `reports_type` | The [CME error report type](#waltermodemcmeerrorreportstype). | **WalterModemCMEErrorReportsType.NUMERIC** |
| `rsp`          | Reference to a modem response instance.                       | **None**                                   |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

### `configCEREGReports`

Configures the CEREG status report type.
By default, reports are enabled with minimal operational info.

> [!WARNING]
> Changing this may affect library functionality.

#### Example

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

```py
if not await modem.config_cereg_reports(reports_type=WalterModemCEREGReportsType.ENABLED):
    print('Failed to config CEREg reports')
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

| Param          | Description                                                    | Default                                 |
| -------------- | -------------------------------------------------------------- | --------------------------------------- |
| `reports_type` | The [CEREG status reports type](#waltermodemceregreportstype). | **WalterModemCEREGReportsType.ENABLED** |
| `rsp`          | Reference to a modem response instance.                        | **None**                                |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

### `getOpState`

Retrieves the modem's current operational state.

#### Example

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

```py
modem_rsp = ModemRsp()

if await modem.get_op_state(rsp=modem_rsp):
    print(WalterModemOpState.get_value_name(modem_rsp.op_state))
else:
    print('Failed to get modem op state')

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

### `setOpState`

Sets the operational state of the modem.

#### Example

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

```py
if not await modem.set_op_state(op_state=WalterModemOpState.FULL):
    print('Failed to set modem op state')
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

| Param      | Description                                                    | Default  |
| ---------- | -------------------------------------------------------------- | -------- |
| `op_state` | The new [operational state](#waltermodemopstate) of the modem. |          |
| `rsp`      | Reference to a modem response instance.                        | **None** |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

## Enums

### `WalterModemCMEErrorReportsType`

Modem CME error reporting methods.

<!-- tabs:start -->

#### **Arduino**

#### **ESP-IDF**

#### **Micropython**

> **OFF** = `0` \
> No error reporting. \
> **NUMERIC** = `1` \
> Numeric error codes for reporting. \
> **VERBOSE** = `2` \
> Detailed verbose error messages.

<!-- tabs:end -->

### `WalterModemCEREGReportsType`

CEREG unsolicited reporting methods.

<!-- tabs:start -->

#### **Arduino**

#### **ESP-IDF**

#### **Micropython**

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

<!-- tabs:end -->

### `WalterModemOpState`

Modem operational modes.

<!-- tabs:start -->

#### **Arduino**

#### **ESP-IDF**

#### **Micropython**

> **MINIMUM** = `0` \
> Minimal operational mode. \
> **FULL** = `1` \
> Full operational mode. \
> **NO_RF** = `4` \
> No RF (Radio Frequency) operation. \
> **MANUFACTURING** = `5` \
> Manufacturing mode for testing and diagnostics.

<!-- tabs:end -->
