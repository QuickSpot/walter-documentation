## Methods Overview

- [gnssConfig](#gnssconfig)
- [gnssGetAssistanceStatus](#gnssgetassistancestatus)
- [gnssUpdateAssistance](#gnssupdateassistance)
- [gnssPerformAction](#gnssperformaction)
- [gnssSetUTCTime](#gnsssetutctime)
- [gnssGetUTCTime](#gnssgetutctime)

## Enums Overview

- [WalterModemGNSSLocMode](#waltermodemgnsslocmode)
- [WalterModemGNSSSensMode](#waltermodemgnsssensmode)
- [WalterModemGNSSAcqMode](#waltermodemgnssacqmode)
- [WalterModemGNSSAction](#waltermodemgnssaction)
- [WalterModemGNSSFixStatus](#waltermodemgnssfixstatus)
- [WalterModemGNSSAssistanceType](#waltermodemgnssassistancetype)

---

## Methods

### `gnssConfig`

This function will configure the GNSS receiver.

The settings are persistent over reboots but may need to be set again after a modem firmware upgrade.
Between fixes, this function can be used to change the sensitivity mode.

> [!TIP]
> It is recommended to run this function at least once before GNSS is used.  
> In our findings, calling config again after a valid fix has been acquired
> reduces the time it would take for consecutive fixin within a range of 100km.

#### Params

| Param      | Description                                                      | Default                                           |
| ---------- | ---------------------------------------------------------------- | ------------------------------------------------- |
| `sensMode` | The sensitivity mode.                                            | **WALTER_MODEM_GNSS_SENS_MODE_HIGH**              |
| `acqMode`  | The acquisition mode.                                            | **WALTER_MODEM_GNSS_ACQ_MODE_COLD_WARM_START**    |
| `locMode`  | The GNSS location mode.                                          | **WALTER_MODEM_GNSS_LOC_MODE_ON_DEVICE_LOCATION** |
| `rsp`      | Optional modem response structure to save the result.            | **NULL**                                          |
| `cb`       | Optional callback function, if set this function will not block. | **NULL**                                          |
| `args`     | Optional argument to pass to the callback.                       | **NULL**                                          |

#### Returns

`bool`  
True on success, false on error.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.gnssConfig()) {
    Serial.println("Info: GNSS configured");
} else {
    Serial.println("Error: Failed to configure GNSS");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (modem.gnssConfig()) {
    ESP_LOGI("gnss_docs_demo", "GNSS configured");
} else {
    ESP_LOGE("gnss_docs_demo", "Failed to configure GNSS");
}

// ...
```

<!-- tabs:end -->

---

### `gnssGetAssistanceStatus`

Get the current GNSS assistance data status.

This function retrieves the status of the assistance data currently loaded in the GNSS subsystem.

#### Params

| Param  | Description                                                      | Default  |
| ------ | ---------------------------------------------------------------- | -------- |
| `rsp`  | Optional modem response structure to save the result.            | **NULL** |
| `cb`   | Optional callback function, if set this function will not block. | **NULL** |
| `args` | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on success, false on error.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.gnssGetAssistanceStatus(&rsp)) {
    // Data can be found under: rsp.data.gnssAssistance
} else {
    Serial.println("Error: Failed to get GNSS assistance status");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.gnssGetAssistanceStatus(&rsp)) {
    // Data can be found under: rsp.data.gnssAssistance
} else {
    Serial.println("Error: Failed to get GNSS assistance status");
}

// ...
```

<!-- tabs:end -->

---

### `gnssUpdateAssistance`

Update the GNSS assistance data.

This function will connect to the cloud to download the requested type of assistance data
and update the GNSS subsystem with this data.

> [!TIP]
> The most efficient type of assistance data is real-time ephemeris.

#### Params

| Param  | Description                                                      | Default                                                  |
| ------ | ---------------------------------------------------------------- | -------------------------------------------------------- |
| `type` | The type of GNSS assistance data to update.                      | **WALTER_MODEM_GNSS_ASSISTANCE_TYPE_REALTIME_EPHEMERIS** |
| `rsp`  | Optional modem response structure to save the result.            | **NULL**                                                 |
| `cb`   | Optional callback function, if set this function will not block. | **NULL**                                                 |
| `args` | Optional argument to pass to the callback.                       | **NULL**                                                 |

#### Returns

`bool`  
True on success, false on error.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.gnssUpdateAssistance(WALTER_MODEM_GNSS_ASSISTANCE_TYPE_ALMANAC)) {
    Serial.println("Info: GNSS assistance updated");
} else {
    Serial.println("Error: Failed to update GNSS assistance");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (modem.gnssUpdateAssistance(WALTER_MODEM_GNSS_ASSISTANCE_TYPE_ALMANAC)) {
    ESP_LOGI("gnss_docs_demo", "GNSS assistance updated");
} else {
    ESP_LOGE("gnss_docs_demo", "Failed to update GNSS assistance");
}

// ...
```

<!-- tabs:end -->

---

### `gnssPerformAction`

Perform a GNSS action.

This function programs the GNSS subsystem to perform a specified action.

#### Params

| Param    | Description                                                      | Default                                     |
| -------- | ---------------------------------------------------------------- | ------------------------------------------- |
| `action` | The action for the GNSS subsystem to perform.                    | **WALTER_MODEM_GNSS_ACTION_GET_SINGLE_FIX** |
| `rsp`    | Optional modem response structure to save the result.            | **NULL**                                    |
| `cb`     | Optional callback function, if set this function will not block. | **NULL**                                    |
| `args`   | Optional argument to pass to the callback.                       | **NULL**                                    |

#### Returns

`bool`  
True on success, false on error.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.gnssPerformAction()) {
    Serial.println("Info: Requested GNSS fix");
} else {
    Serial.println("Error: Failed to request GNSS fix");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (modem.gnssPerformAction()) {
    ESP_LOGI("gnss_docs_demo", "Requested GNSS fix");
} else {
    ESP_LOGE("gnss_docs_demo", "Failed to request GNSS fix");
}

// ...
```

<!-- tabs:end -->

---

### `gnssSetUTCTime`

Sets the UTC time for GNSS usage.

#### Params

| Param       | Description                                                      | Default  |
| ----------- | ---------------------------------------------------------------- | -------- |
| `epochTime` | Unix timestamp for UTC time (see getClock).                      |          |
| `rsp`       | Optional modem response structure to save the result.            | **NULL** |
| `cb`        | Optional callback function, if set this function will not block. | **NULL** |
| `args`      | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on success, false on error.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

uint64_t epochTime = 1693560000;

if (modem.gnssSetUTCTime(epochTime)) {
    Serial.println("Info: GNSS UTC time set");
} else {
    Serial.println("Error: Failed to set GNSS UTC time");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

uint64_t epochTime = 1693560000;

if (modem.gnssSetUTCTime(epochTime)) {
    ESP_LOGI("gnss_docs_demo", "GNSS UTC time set");
} else {
    ESP_LOGE("gnss_docs_demo", "Failed to set GNSS UTC time");
}

// ...
```

<!-- tabs:end -->

---

### `gnssGetUTCTime`

Gets the UTC time for GNSS usage.

> [!NOTE]  
> The UTC time can be found in the clock portion of the response data (`rsp`).

#### Params

| Param  | Description                                                      | Default  |
| ------ | ---------------------------------------------------------------- | -------- |
| `rsp`  | Optional modem response structure to save the result.            | **NULL** |
| `cb`   | Optional callback function, if set this function will not block. | **NULL** |
| `args` | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on success, false on error.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.gnssGetUTCTime(&rsp)) {
   // Data can be found in the lockc portion of the rsp object.
} else {
    Serial.println("Error: Failed to get GNSS UTC time");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.gnssGetUTCTime(&rsp)) {
    // Data can be found in the lockc portion of the rsp object.
} else {
    ESP_LOGE("gnss_docs_demo", "Failed to get GNSS UTC time");
}

// ...
```

<!-- tabs:end -->

---

## Enums

### `WalterModemGNSSLocMode`

The GNSS location modus. When set to 'on-device location' the GNSS subsystem will compute
position and speed and estimate the error on these parameters.

> **WALTER_MODEM_GNSS_LOC_MODE_ON_DEVICE_LOCATION** = `0`  

### `WalterModemGNSSSensMode`

The possible sensitivity settings use by Walter's GNSS receiver.
This sets the amount of time that the receiver is actually on.

More sensitivity requires more power.

> **WALTER_MODEM_GNSS_SENS_MODE_LOW** = `1`  
> **WALTER_MODEM_GNSS_SENS_MODE_MEDIUM** = `2`  
> **WALTER_MODEM_GNSS_SENS_MODE_HIGH** = `3`  

### `WalterModemGNSSAcqMode`

The possible GNSS acquisition modes.

When no ephemerides are available and/or the time is not known
cold start will be used automatically.

> **WALTER_MODEM_GNSS_ACQ_MODE_COLD_WARM_START** = `0`  
> Walter has no clue where on earth it is.  
> **WALTER_MODEM_GNSS_ACQ_MODE_HOT_START** = `1`  
> Walter must know where it is within 100km.

### `WalterModemGNSSAction`

The supported actions that Walter's GNSS can execute.

> **WALTER_MODEM_GNSS_ACTION_GET_SINGLE_FIX** = `0`  
> **WALTER_MODEM_GNSS_ACTION_CANCEL** = `1`  

### `WalterModemGNSSFixStatus`

The possible GNSS fix statuses.

> **WALTER_MODEM_GNSS_FIX_STATUS_READY** = `0`  
> **WALTER_MODEM_GNSS_FIX_STATUS_STOPPED_BY_USER** = `1`  
> **WALTER_MODEM_GNSS_FIX_STATUS_NO_RTC** = `2`  
> **WALTER_MODEM_GNSS_FIX_STATUS_LTE_CONCURRENCY** = `3`  

### `WalterModemGNSSAssistanceType`

Types of GNSS assistance data used to improve positioning performance.

> **WALTER_MODEM_GNSS_ASSISTANCE_TYPE_ALMANAC** = `0`  
> Long-term orbital data providing coarse satellite positions and health status.  
> **WALTER_MODEM_GNSS_ASSISTANCE_TYPE_REALTIME_EPHEMERIS** = `1`  
> Real-time satellite position and velocity data for immediate accuracy.  
> **WALTER_MODEM_GNSS_ASSISTANCE_TYPE_PREDICTED_EPHEMERIS** = `2`  
> Forecasted satellite position data for faster cold starts without a live connection.  
