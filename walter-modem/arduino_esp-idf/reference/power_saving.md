## Methods Overview

- [configPSM](#configpsm)
- [configEDRX](#configedrx)
- [durationToTAU](#durationtotau)
- [durationToActiveTime](#durationtoactivetime)

## Enums Overview

- [WalterModemPSMMode](#waltermodempsmmode)
- [WalterModemEDRXMode](#waltermodemedrxmode)

---

## Methods

### `configPSM`

Configure Power Saving Mode Setting.

This function controls whether **PSM** (Power Saving Mode) should be applied,
and requests the Power Saving Mode settings for Walter.

> [!NOTE]
> The settings are only a request; the network may allocate different values,
> which are reported via unsolicited +CEREG results for Active Time and extended periodic TAU (T3412) values.

#### Params

| Param       | Description                                                      | Default                      |
| ----------- | ---------------------------------------------------------------- | ---------------------------- |
| `mode`      | Enable or disable the use of PSM.                                | **WALTER_MODEM_PSM_DISABLE** |
| `reqTAU`    | The requested extended periodic TAU value (`T3412`).             | **NULL**                     |
| `reqActive` | The requested Active Time value (`T3324`).                       | **NULL**                     |
| `rsp`       | Optional modem response structure to save the result.            | **NULL**                     |
| `cb`        | Optional callback function, if set this function will not block. | **NULL**                     |
| `args`      | Optional argument to pass to the callback.                       | **NULL**                     |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG(PSM_ACTIVE, const char *, "00000001");
CONFIG(PSM_TAU, const char *, "00000110");

// ...

if (modem.configPSM(WALTER_MODEM_PSM_ENABLE,PSM_TAU,PSM_ACTIVE)) {
    Serial.println("Info: PSM configured");
} else {
    Serial.println("Error: Failed to configure PSM");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG(PSM_ACTIVE, const char *, "00000001");
CONFIG(PSM_TAU, const char *, "00000110");

// ...

if (modem.configPSM(WALTER_MODEM_PSM_ENABLE,PSM_TAU,PSM_ACTIVE)) {
    ESP_LOGI("power_saving_docs_demo", "PSM configured");
} else {
    ESP_LOGE("power_saving_docs_demo", "Failed to configure PSM");
}

// ...
```

<!-- tabs:end -->

---

### `configEDRX`

Configure extended DRX Setting.

This function controls whether extended DRX (eDRX) should be applied
and configures the requested eDRX value and Paging Time Window (PTW).

eDRX is a power-saving feature that allows the device to extend its sleep cycles
by sleeping longer between paging checks at the cost of increased latency.

- `mode`: Enable or disable the use of eDRX.
- `reqEDRXVal`: The requested eDRX cycle length.
- `reqPtw`: The requested Paging Time Window during which the device listens for paging messages.

#### Params

| Param        | Description                                                         | Default                       |
| ------------ | ------------------------------------------------------------------- | ----------------------------- |
| `mode`       | Enable or disable the use of eDRX.                                  | **WALTER_MODEM_EDRX_DISABLE** |
| `reqEDRXVal` | The requested eDRX value specifying the sleep cycle length.         | **NULL**                      |
| `reqPtw`     | The requested Paging Time Window specifying listening duration.     | **NULL**                      |
| `rsp`        | Optional modem response structure to save the result.               | **NULL**                      |
| `cb`         | Optional callback function, if set will make function non-blocking. | **NULL**                      |
| `args`       | Optional argument to pass to the callback.                          | **NULL**                      |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.configEDRX()) {
    Serial.println("Info: eDRX configured");
} else {
    Serial.println("Error: Failed to configure eDRX");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (modem.configEDRX()) {
    ESP_LOGI("power_saving_docs_demo", "eDRX configured");
} else {
    ESP_LOGE("power_saving_docs_demo", "Failed to configure eDRX");
}

// ...
```

<!-- tabs:end -->

---

### `durationToTAU`

Encode a TAU duration for use in PSM configuration.

This function will encode a given duration into the nearest duration
that can be encoded according to the 3GPP specification for use in timer T3412 (TAU).

> [!WARNING]
> This function is an approximation because of the encoding used over the wire.

#### Params

| Param                     | Description                                                           | Default     |
| ------------------------- | --------------------------------------------------------------------- | ----------- |
| `seconds`                 | Duration in seconds.                                                  | **0**       |
| `minutes`                 | Duration in minutes.                                                  | **0**       |
| `hours`                   | Duration in hours.                                                    | **0**       |
| `actual_duration_seconds` | Optional pointer in which the actual requested duration can be saved. | **nullptr** |

#### Returns

`uint8_t`  
The interval encoded into the 3GPP standard format.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

Serial.println(modem.durationToTAU(0,30,1));

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

ESP_LOGI(modem.durationToTAU(0,30,1));

// ...
```

<!-- tabs:end -->

---

### `durationToActiveTime`

Convert a given duration of seconds and minutes to a reqActive approximation.

This function encodes a given duration into the nearest duration
that can be encoded according to the 3GPP specification for timer T3324 (Active Time).

It uses a multiplier internally for the approximation.

> [!WARNING]
> This function provides an approximation because it uses a multiplier internally.

#### Params

| Param                     | Description                                                     | Default     |
| ------------------------- | --------------------------------------------------------------- | ----------- |
| `seconds`                 | Duration in seconds.                                            | **0**       |
| `minutes`                 | Duration in minutes.                                            | **0**       |
| `actual_duration_seconds` | Optional pointer to save the actual requested duration encoded. | **nullptr** |

#### Returns

`uint8_t`  
The duration encoded into the 3GPP standard format.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

Serial.println(modem.durationToActiveTime(15,1));

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

ESP_LOGI(modem.durationToActiveTime(15,1));

// ...
```

<!-- tabs:end -->

---

## Enums

### `WalterModemPSMMode`

The supported Power Saving Mode (PSM) modes.

> **WALTER_MODEM_PSM_DISABLE** = `0`  
> Power Saving Mode disabled.  
> **WALTER_MODEM_PSM_ENABLE** = `1`  
> Power Saving Mode enabled.  
> **WALTER_MODEM_PSM_RESET** = `2`  
> Power Saving Mode reset.  

### `WalterModemEDRXMode`

The supported extended Discontinuous Reception (eDRX) modes.

> **WALTER_MODEM_EDRX_DISABLE** = `0`  
> eDRX disabled.  
> **WALTER_MODEM_EDRX_ENABLE** = `1`  
> eDRX enabled.  
> **WALTER_MODEM_EDRX_ENABLE_WITH_RESULT** = `2`  
> eDRX enabled with result notification.  
> **WALTER_MODEM_EDRX_RESET** = `3`  
> eDRX reset.
