## Methods Overview

- [reset](#reset)
- [checkComm](#checkcomm)
- [getClock](#getclock)
- [configCmeErrorReports](#configcmeerrorreports)
- [configCeregReports](#configceregreports)
- [getOpState](#getopstate)
- [setOpState](#setopstate)

## Enums Overview

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

if await modem.get_clock(rps=modem_rsp):
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

### `configCmeErrorReports`

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

| Param          | Description                             | Default                                    |
| -------------- | --------------------------------------- | ------------------------------------------ |
| `reports_type` | The CME error report type.              | **WalterModemCMEErrorReportsType.NUMERIC** |
| `rsp`          | Reference to a modem response instance. | **None**                                   |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

### `configCeregReports`

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

| Param          | Description                             | Default                                    |
| -------------- | --------------------------------------- | ------------------------------------------ |
| `reports_type` | The CEREG status reports type.          | **WalterModemCEREGReportsType.ENABLED** |
| `rsp`          | Reference to a modem response instance. | **None**                                   |

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

if await modem.get_op_state(rps=modem_rsp):
    print(modem_rsp.op_state)
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

| Param      | Description                             | Default  |
| ---------- | --------------------------------------- | -------- |
| `op_state` | The new operational state of the modem. |          |
| `rsp`      | Reference to a modem response instance. | **None** |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---
