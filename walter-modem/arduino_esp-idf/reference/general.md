## Methods Overview

- [begin](#begin)
- [tickleWatchdog](#ticklewatchdog)
- [sendCmd](#sendcmd)
- [softReset](#softreset)
- [reset](#reset)
- [checkComm](#checkcomm)
- [sleep](#sleep)
- [configCMEErrorReports](#configcmeerrorreports)
- [configCEREGReports](#configceregreports)
- [getIdentity](#getidentity)
- [getClock](#getclock)

## Enums Overview

- [WalterModemState](#waltermodemstate)
- [WalterModemRspDataType](#waltermodemrspdatatype)
- [WalterModemCMEErrorReportsType](#waltermodemcmeerrorreportstype)
- [WalterModemCMEError](#waltermodemcmeerror)

---

## Methods

### `begin`

Initialize the modem.

This function initializes the modem and must be called before using the modem device.

> [!NOTE]
> It can only be called once; subsequent calls have no effect.

#### Params

<!-- tabs:start -->

##### **Arduino**

| Param             | Description                                                    | Default |
| ----------------- | -------------------------------------------------------------- | ------- |
| `uart`            | The hardware serial used to talk to the modem.                 |         |
| `watchdogTimeout` | Timeout in seconds before auto-reboot; minimum is 300 seconds. | **0**   |

##### **ESP-IDF**

| Param             | Description                                                    | Default |
| ----------------- | -------------------------------------------------------------- | ------- |
| `uartNo`          | The UART number of the hardware used to talk to the modem.     |         |
| `watchdogTimeout` | Timeout in seconds before auto-reboot; minimum is 300 seconds. | **0**   |

<!-- tabs:end -->

#### Returns

`bool`  
True on success, false on error.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (WalterModem::begin(&Serial2)) {
    Serial.println("Info: Modem initialization OK");
} else {
    Serial.println("Error: Modem initialization ERROR");
    return;
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (WalterModem::begin(UART_NUM_1)) {
    ESP_LOGI("general_docs_demo", "Successfully initialized modem");
} else {
    ESP_LOGE("general_docs_demo", "Could not initialize modem");
    return;
}

// ...
```

<!-- tabs:end -->

---

### `tickleWatchdog`

Tickle watchdog.

This function will reset the watchdog timer.
It must be called regularly and before the configured timeout expires.

---

### `sendCmd`

Send an AT command.

This function sends an AT command to the modem.
The necessary carriage return and line feed characters will be added automatically to the given command.

#### Params

| Param      | Description                                                      | Default  |
| ---------- | ---------------------------------------------------------------- | -------- |
| `atCmd`    | The AT command to send.                                          |          |
| `atCmdRsp` | The expected AT command response.                                | **OK**   |
| `rsp`      | Optional modem response structure to save the result in.         | **NULL** |
| `cb`       | Optional callback function, if set this function will not block. | **NULL** |
| `args`     | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.sendCmd("ATI")) {
    Serial.println("Info: Success");
} else {
    Serial.println("Error: Failed");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (modem.sendCmd("ATI")) {
    ESP_LOGI("general_docs_docs_demo", "Success");
} else {
    ESP_LOGE("general_docs_docs_demo", "Failed");
}

// ...
```

<!-- tabs:end -->

---

### `softReset`

Software reset the modem and wait for it to reset.

This function is required when switching from RAT (Radio Access Technology).

> [!WARNING]
> The function will fail if the modem does not reset.

#### Params

| Param  | Description                                                      | Default  |
| ------ | ---------------------------------------------------------------- | -------- |
| `rsp`  | Optional modem response structure to save the result.            | **NULL** |
| `cb`   | Optional callback function, if set this function will not block. | **NULL** |
| `args` | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.softReset()) {
    Serial.println("Info: Modem soft reset");
} else {
    Serial.println("Error: Modem soft reset failed");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (modem.softReset()) {
    ESP_LOGI("general_docs_docs_demo", "Modem soft reset");
} else {
    ESP_LOGE("general_docs_docs_demo", "Modem soft reset failed");
}

// ...
```

<!-- tabs:end -->
---

### `reset`

Physically reset the modem and wait for it to start.

All connections will be lost when this function is called.

> [!WARNING]
> The function will fail if the modem does not start after the reset.

#### Params

| Param  | Description                                                      | Default  |
| ------ | ---------------------------------------------------------------- | -------- |
| `rsp`  | Optional modem response structure to save the result.            | **NULL** |
| `cb`   | Optional callback function, if set this function will not block. | **NULL** |
| `args` | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.reset()) {
    Serial.println("Info: Modem reset");
} else {
    Serial.println("Error: Modem Reset failed");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (modem.reset()) {
    ESP_LOGI("general_docs_docs_demo", "Modem reset");
} else {
    ESP_LOGE("general_docs_docs_demo", "Modem Reset failed");
}

// ...
```

<!-- tabs:end -->

---

### `checkComm`

Check communication between the ESP32 and the modem.

This function sends the 'AT' command and verifies if the modem responds with 'OK'.

#### Params

| Param  | Description                                                      | Default  |
| ------ | ---------------------------------------------------------------- | -------- |
| `rsp`  | Optional modem response structure to save the result.            | **NULL** |
| `cb`   | Optional callback function, if set this function will not block. | **NULL** |
| `args` | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on success, false if communication failed.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.checkComm()) {
    Serial.println("Info: Comm OK");
} else {
    Serial.println("Error: Comm ERROR");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (modem.checkComm()) {
    ESP_LOGI("general_docs_docs_demo", "Comm OK");
} else {
    ESP_LOGE("general_docs_docs_demo", "Comm ERROR");
}

// ...
```

<!-- tabs:end -->

---

### `sleep`

Put Walter to deep or light sleep.

This function will put Walter into deep sleep or light sleep for a given duration.

Typical power consumption is approximately 1mA in light sleep and 9.5µA in deep sleep.
The function immediately affects the ESP32-S3, but the modem may be delayed or prevented from entering deep sleep.

> [!NOTE]
> Deep sleep causes the ESP32 to restart program execution;
> the modem library saves state such as PDP context and socket state in RTC memory.
> After waking from deep sleep, any initialization must be redone.
>
> Deep sleep is typically used together with PSM and/or eDRX.

#### Params

| Param        | Description                        | Default   |
| ------------ | ---------------------------------- | --------- |
| `sleepTime`  | Duration of deep sleep in seconds. | **0**     |
| `lightSleep` | If true, only light sleep is used. | **false** |

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

modem.sleep(600);

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

modem.sleep(600);

// ...
```

<!-- tabs:end -->

---

### `configCMEErrorReports`

Configure the CME error reports.

This function sets the CME error reports type.

> [!NOTE]
> By default, the library enables numeric error reports.
> Changing this setting may cause errors to be reported incorrectly.

#### Params

| Param  | Description                                                      | Default                                    |
| ------ | ---------------------------------------------------------------- | ------------------------------------------ |
| `type` | The CME error reports type to set.                               | **WALTER_MODEM_CME_ERROR_REPORTS_NUMERIC** |
| `rsp`  | Optional modem response structure to save the result.            | **NULL**                                   |
| `cb`   | Optional callback function, if set this function will not block. | **NULL**                                   |
| `args` | Optional argument to pass to the callback.                       | **NULL**                                   |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.configCMEErrorReports()) {
    Serial.println("Info: CME error reports configured");
} else {
    Serial.println("Error: Failed to configure CME error reports");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (modem.configCMEErrorReports()) {
    ESP_LOGI("general_docs_docs_demo", "CME error reports configured");
} else {
    ESP_LOGE("general_docs_docs_demo", "Failed to configure CME error reports");
}

// ...
```

<!-- tabs:end -->

---

### `configCEREGReports`

Configure the CEREG status reports.

This function sets the CEREG status report type.

> [!NOTE]
> By default, the library enables CEREG status reports with minimal operational info.
> Changing this setting may cause the library to not work correctly.

#### Params

| Param  | Description                                                      | Default                                |
| ------ | ---------------------------------------------------------------- | -------------------------------------- |
| `type` | The CEREG status reports type to set.                            | **WALTER_MODEM_CEREG_REPORTS_ENABLED** |
| `rsp`  | Optional modem response structure to save the result.            | **NULL**                               |
| `cb`   | Optional callback function, if set this function will not block. | **NULL**                               |
| `args` | Optional argument to pass to the callback.                       | **NULL**                               |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.configCEREGReports()) {
    Serial.println("Info: CEREG reports configured");
} else {
    Serial.println("Error: Failed to configure CEREG reports");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (modem.configCEREGReports()) {
    ESP_LOGI("general_docs_docs_demo", "CEREG reports configured");
} else {
    ESP_LOGE("general_docs_docs_demo", "Failed to configure CEREG reports");
}

// ...
```

<!-- tabs:end -->

---

### `getIdentity`

Get the identity of the modem (IMEI, IMEISV, SVN).

This function retrieves the:

- IMEI (International Mobile Equipment Identity)
- IMEISV (IMEI with Software Version)
- SVN (Software Version Number) from the modem.

#### Params

| Param  | Description                                                      | Default  |
| ------ | ---------------------------------------------------------------- | -------- |
| `rsp`  | Optional modem response structure to save the result.            | **NULL** |
| `cb`   | Optional callback function, if set this function will not block. | **NULL** |
| `args` | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.getIdentity(&rsp)) {
    Serial.println("Info: Identity information:");
    Serial.print("-> imei: ");
    Serial.println(rsp.data.identity.imei);
    Serial.print("-> imeisv: ");
    Serial.println(rsp.data.identity.imeisv);
    Serial.print("-> svn: ");
    Serial.println(rsp.data.identity.svn);
} else {
    Serial.println("Error: Failed to get identity");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.getIdentity(&rsp)) {
    ESP_LOGI("general_docs_docs_demo", "Identity information:");
    ESP_LOGI("general_docs_docs_demo", "-> imei: %s", rsp.data.identity.imei);
    ESP_LOGI("general_docs_docs_demo", "-> imeisv: %s", rsp.data.identity.imeisv);
    ESP_LOGI("general_docs_docs_demo", "-> svn: %s", rsp.data.identity.svn)
} else {
    ESP_LOGE("general_docs_docs_demo", "Error: Failed to get identity");
}

// ...
```

<!-- tabs:end -->

---

### `getClock`

Get the current modem time and date.

This function retrieves the current time and date from the modem.

#### Params

| Param  | Description                                                      | Default  |
| ------ | ---------------------------------------------------------------- | -------- |
| `rsp`  | Optional modem response structure to save the result.            | **NULL** |
| `cb`   | Optional callback function, if set this function will not block. | **NULL** |
| `args` | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.getClock(&rsp)) {
    Serial.println("Info: Clock information:");
    Serial.print("-> epoch time: ");
    Serial.println(rsp.data.clock.epochTime);
    Serial.print("-> timezone offset: ");
    Serial.println(rsp.data.clock.timeZoneOffset);
} else {
    Serial.println("Error: Failed to get clock information");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.getClock(&rsp)) {
    ESP_LOGI("general_docs_docs_demo", "Clock information:");
    ESP_LOGI("general_docs_docs_demo", "-> epoch time: %s", rsp.data.clock.epochTime);
    ESP_LOGI("general_docs_docs_demo", "-> timezone offset: %s", rsp.data.clock.timeZoneOffset);
} else {
    ESP_LOGE("general_docs_docs_demo", "Error: Failed to get clock information");
}

// ...
```

<!-- tabs:end -->

---

## Enums

### `WalterModemState`

The possible state codes returned by modem functions and operational components.

> **WALTER_MODEM_STATE_OK** = `0`  
> Operation completed successfully.  
> **WALTER_MODEM_STATE_ERROR** = `1`  
> A general or unspecified error occurred.  
> **WALTER_MODEM_STATE_TIMEOUT** = `2`  
> Operation timed out before completion.  
> **WALTER_MODEM_STATE_NO_MEMORY** = `3`  
> Memory allocation failed or resources exhausted.  
> **WALTER_MODEM_STATE_NO_FREE_PDP_CONTEXT** = `4`  
> No free PDP context available.  
> **WALTER_MODEM_STATE_NO_SUCH_PDP_CONTEXT** = `5`  
> Requested PDP context does not exist.  
> **WALTER_MODEM_STATE_NO_FREE_SOCKET** = `6`  
> No free socket could be allocated.  
> **WALTER_MODEM_STATE_NO_SUCH_SOCKET** = `7`  
> Referenced socket does not exist.  
> **WALTER_MODEM_STATE_NO_SUCH_PROFILE** = `8`  
> Specified profile could not be found.  
> **WALTER_MODEM_STATE_NOT_EXPECTING_RING** = `9`  
> An unexpected ring was received.  
> **WALTER_MODEM_STATE_AWAITING_RING** = `10`  
> Waiting for an incoming ring.  
> **WALTER_MODEM_STATE_AWAITING_RESPONSE** = `11`  
> Awaiting a response to a previous command.  
> **WALTER_MODEM_STATE_BUSY** = `12`  
> Modem is busy with another operation.  
> **WALTER_MODEM_STATE_NO_DATA** = `13`  
> No data available when expected.  

### `WalterModemRspDataType`

The different implemented response data types.

> **WALTER_MODEM_RSP_DATA_TYPE_NO_DATA** = `0`  
> No data available.  
> **WALTER_MODEM_RSP_DATA_TYPE_OPSTATE** = `1`  
> Modem operational state.  
> **WALTER_MODEM_RSP_DATA_TYPE_RAT** = `2`  
> Radio access technology type.  
> **WALTER_MODEM_RSP_DATA_TYPE_RSSI** = `3`  
> Received Signal Strength Indicator.  
> **WALTER_MODEM_RSP_DATA_TYPE_SIGNAL_QUALITY** = `4`  
> Signal quality metric.  
> **WALTER_MODEM_RSP_DATA_TYPE_CELL_INFO** = `5`  
> Cellular network information.  
> **WALTER_MODEM_RSP_DATA_TYPE_SIM_STATE** = `6`  
> SIM card state.  
> **WALTER_MODEM_RSP_DATA_TYPE_SIM_CARD_ID** = `7`  
> SIM card identifier.  
> **WALTER_MODEM_RSP_DATA_TYPE_SIM_CARD_IMSI** = `8`  
> SIM card IMSI number.  
> **WALTER_MODEM_RSP_DATA_TYPE_CME_ERROR** = `9`  
> CME error code.  
> **WALTER_MODEM_RSP_DATA_TYPE_PDP_CTX_ID** = `10`  
> PDP context identifier.  
> **WALTER_MODEM_RSP_DATA_TYPE_BANDSET_CFG_SET** = `11`  
> Bandset configuration status.  
> **WALTER_MODEM_RSP_DATA_TYPE_PDP_ADDR** = `12`  
> PDP context IP address.  
> **WALTER_MODEM_RSP_DATA_TYPE_SOCKET_ID** = `13`  
> Socket identifier.  
> **WALTER_MODEM_RSP_DATA_TYPE_GNSS_ASSISTANCE_DATA** = `14`  
> GNSS assistance data.  
> **WALTER_MODEM_RSP_DATA_TYPE_GNSS_UTC_TIME** = `15`  
> GNSS UTC time information.  
> **WALTER_MODEM_RSP_DATA_TYPE_CLOCK** = `16`  
> Modem internal clock data.  
> **WALTER_MODEM_RSP_DATA_TYPE_IDENTITY** = `17`  
> Modem identity data.  
> **WALTER_MODEM_RSP_DATA_TYPE_BLUECHERRY** = `18`  
> BlueCherry specific response data.  
> **WALTER_MODEM_RSP_DATA_TYPE_HTTP_RESPONSE** = `19`  
> HTTP response data.  
> **WALTER_MODEM_RSP_DATA_TYPE_COAP** = `20`  
> CoAP message data.  
> **WALTER_MODEM_RSP_DATA_TYPE_MQTT** = `21`  
> MQTT message data.

### `WalterModemCMEErrorReportsType`

The CME error reporting methods.

> **WALTER_MODEM_CME_ERROR_REPORTS_OFF** = `0`  
> Error reporting disabled.  
> **WALTER_MODEM_CME_ERROR_REPORTS_NUMERIC** = `1`  
> Errors reported as numeric codes.  
> **WALTER_MODEM_CME_ERROR_REPORTS_VERBOSE** = `2`  
> Errors reported as human-readable strings.

### `WalterModemCMEError`

All supported CME error codes.

> **WALTER_MODEM_CME_EQUIPMENT_FAILURE** = `0`  
> Equipment failure occurred.  
> **WALTER_MODEM_CME_NO_CONNECTION** = `1`  
> No connection to phone adapter.  
> **WALTER_MODEM_CME_PHONE_ADAPTER_LINK_RESERVED** = `2`  
> Phone adapter link is reserved.  
> **WALTER_MODEM_CME_OPERATION_NOT_ALLOWED** = `3`  
> Operation not allowed.  
> **WALTER_MODEM_CME_OPERATION_NOT_SUPPORTED** = `4`  
> Operation not supported.  
> **WALTER_MODEM_CME_PH_SIM_PIN_REQUIRED** = `5`  
> Phone-to-SIM PIN required.  
> **WALTER_MODEM_CME_PH_FSIM_PIN_REQUIRED** = `6`  
> Phone-to-first-SIM PIN required.  
> **WALTER_MODEM_CME_PH_FSIM_PUK_REQUIRED** = `7`  
> Phone-to-first-SIM PUK required.  
> **WALTER_MODEM_CME_SIM_NOT_INSERTED** = `10`  
> SIM card not inserted.  
> **WALTER_MODEM_CME_SIM_PIN_REQUIRED** = `11`  
> SIM PIN required.  
> **WALTER_MODEM_CME_SIM_PUK_REQUIRED** = `12`  
> SIM PUK required.  
> **WALTER_MODEM_CME_SIM_FAILURE** = `13`  
> SIM failure occurred.  
> **WALTER_MODEM_CME_SIM_BUSY** = `14`  
> SIM is busy.  
> **WALTER_MODEM_CME_SIM_WRONG** = `15`  
> SIM card wrong.  
> **WALTER_MODEM_CME_INCORRECT_PASSWORD** = `16`  
> Incorrect password entered.  
> **WALTER_MODEM_CME_SIM_PIN2_REQUIRED** = `17`  
> SIM PIN2 required.  
> **WALTER_MODEM_CME_SIM_PUK2_REQUIRED** = `18`  
> SIM PUK2 required.  
> **WALTER_MODEM_CME_MEMORY_FULL** = `20`  
> Memory is full.  
> **WALTER_MODEM_CME_INVALID_INDEX** = `21`  
> Invalid index specified.  
> **WALTER_MODEM_CME_NOT_FOUND** = `22`  
> Requested item not found.  
> **WALTER_MODEM_CME_MEMORY_FAILURE** = `23`  
> Memory failure occurred.  
> **WALTER_MODEM_CME_TEXT_STRING_TOO_LONG** = `24`  
> Text string too long.  
> **WALTER_MODEM_CME_INVALID_CHARS_IN_TEXT_STRING** = `25`  
> Invalid characters in text string.  
> **WALTER_MODEM_CME_DIAL_STRING_TOO_LONG** = `26`  
> Dial string too long.  
> **WALTER_MODEM_CME_INVALID_CHARS_IN_DIAL_STRING** = `27`  
> Invalid characters in dial string.  
> **WALTER_MODEM_CME_NO_NETWORK_SERVICE** = `30`  
> No network service available.  
> **WALTER_MODEM_CME_NETWORK_TIMEOUT** = `31`  
> Network timed out.  
> **WALTER_MODEM_CME_NETWORK_NOT_ALLOWED_EMERGENCY_CALS_ONLY** = `32`  
> Network not allowed, emergency calls only.  
> **WALTER_MODEM_CME_NETWORK_PERSONALISATION_PIN_REQUIRED** = `40`  
> Network personalization PIN required.  
> **WALTER_MODEM_CME_NETWORK_PERSONALISATION_PUK_REQUIRED** = `41`  
> Network personalization PUK required.  
> **WALTER_MODEM_CME_NETWORK_SUBSET_PERSONALISATION_PIN_REQUIRED** = `42`  
> Network subset personalization PIN required.  
> **WALTER_MODEM_CME_NETWORK_SUBSET_PERSONALISATION_PUK_REQUIRED** = `43`  
> Network subset personalization PUK required.  
> **WALTER_MODEM_CME_SERVICE_PROVIDER_PERSONALISATION_PIN_REQUIRED** = `44`  
> Service provider personalization PIN required.  
> **WALTER_MODEM_CME_SERVICE_PROVIDER_PERSONALISATION_PUK_REQUIRED** = `45`  
> Service provider personalization PUK required.  
> **WALTER_MODEM_CME_CORPORATE_PERSONALISATION_PIN_REQUIRED** = `46`  
> Corporate personalization PIN required.  
> **WALTER_MODEM_CME_CORPORATE_PERSONALISATION_PUK_REQUIRED** = `47`  
> Corporate personalization PUK required.  
> **WALTER_MODEM_CME_HIDDEN_KEY_REQUIRED** = `48`  
> Hidden key required.  
> **WALTER_MODEM_CME_EAP_METHOD_NOT_SUPPORTED** = `49`  
> EAP method not supported.  
> **WALTER_MODEM_CME_INCORRECT_PARAMETERS** = `50`  
> Incorrect parameters provided.  
> **WALTER_MODEM_CME_SYSTEM_FAILURE** = `60`  
> System failure occurred.  
> **WALTER_MODEM_CME_UNKNOWN_ERROR** = `100`  
> Unknown error occurred.  
> **WALTER_MODEM_CME_UPGRADE_FAILED_GENERAL_ERROR** = `528`  
> Upgrade failed due to general error.  
> **WALTER_MODEM_CME_UPGRADE_FAILED_CORRUPTED_IMAGE** = `529`  
> Upgrade failed due to corrupted image.  
> **WALTER_MODEM_CME_UPGRADE_FAILED_INVALID_SIGNATURE** = `530`  
> Upgrade failed due to invalid signature.  
> **WALTER_MODEM_CME_UPGRADE_FAILED_NETWORK_ERROR** = `531`  
> Upgrade failed due to network error.  
> **WALTER_MODEM_CME_UPGRADE_FAILED_ALREADY_IN_PROGRESS** = `532`  
> Upgrade already in progress.  
> **WALTER_MODEM_CME_UPGRADE_CANCEL_FAILED_NO_UPGRADE_IN_PROGRESS** = `533`  
> Cancel failed; no upgrade in progress.  
> **WALTER_MODEM_CME_HW_CONFIG_FAILED_GENERAL_ERROR** = `540`  
> Hardware configuration failed (general error).  
> **WALTER_MODEM_CME_HW_CONFIG_FAILED_INVALID_FUNCTION** = `541`  
> Hardware configuration failed (invalid function).  
> **WALTER_MODEM_CME_HW_CONFIG_FAILED_INVALID_FUNCTION_PARAM** = `542`  
> Hardware configuration failed (invalid function parameter).  
> **WALTER_MODEM_CME_HW_CONFIG_FAILED_PINS_ALREADY_ASSIGNED** = `543`  
> Hardware configuration failed (pins already assigned).
