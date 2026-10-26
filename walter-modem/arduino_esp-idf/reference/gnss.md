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
- [WMGNSSFixStatus](#wmgnssfixstatus)
- [WMGNSSAssistanceType](#wmgnssassistancetype)

## Structs Overview

- [WMGNSSFixEvent](#wmgnssfixevent)
- [WMGNSSSat](#wmgnsssat)
- [WMGNSSAssistance](#wmgnssassistance)

---

## Methods

### `gnssConfig`

This function will configure the GNSS receiver.

The settings are persistent over reboots but may need to be set again after a modem firmware upgrade.
Between fixes, this function can be used to change the sensitivity mode.

> [!TIP]
> It is recommended to run this function at least once before GNSS is used.  
> In our findings, calling config again after a valid fix has been acquired
> reduces the time it would take for consecutive fixes within a range of 100km.

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
The result is stored in `rsp.data.gnssAssistance`, an array of [WMGNSSAssistance](#wmgnssassistance)
with one entry per [WMGNSSAssistanceType](#wmgnssassistancetype), indexed by that type.

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
    for (int i = 0; i < WALTER_MODEM_GNSS_ASSISTANCE_TYPE_COUNT; i++) {
        WMGNSSAssistance *assistance = &rsp.data.gnssAssistance[i];
        Serial.printf("Info: Assistance type %d: available=%d, update in %lds, expires in %lds\n",
                      assistance->type, assistance->available,
                      (long) assistance->timeToUpdate, (long) assistance->timeToExpire);
    }
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
    for (int i = 0; i < WALTER_MODEM_GNSS_ASSISTANCE_TYPE_COUNT; i++) {
        WMGNSSAssistance *assistance = &rsp.data.gnssAssistance[i];
        ESP_LOGI("gnss_docs_demo", "Assistance type %d: available=%d, update in %lds, expires in %lds",
                 assistance->type, assistance->available,
                 (long) assistance->timeToUpdate, (long) assistance->timeToExpire);
    }
} else {
    ESP_LOGE("gnss_docs_demo", "Failed to get GNSS assistance status");
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

> [!NOTE]
> This function returns as soon as the modem has accepted the request, not when the download is done.
> The modem reports that the assistance data was updated with a `WALTER_MODEM_GNSS_EVENT_ASSISTANCE` event,
> see [setGNSSEventHandler](/walter-modem/arduino_esp-idf/reference/event_handlers.md#setgnsseventhandler).

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

> [!NOTE]
> This function returns as soon as the modem has accepted the action, it does not wait for a fix.
> The fix is delivered as a [WMGNSSFixEvent](#wmgnssfixevent) through a `WALTER_MODEM_GNSS_EVENT_FIX` event,
> see [setGNSSEventHandler](/walter-modem/arduino_esp-idf/reference/event_handlers.md#setgnsseventhandler).
> Check the `status` of the fix: only `WALTER_MODEM_GNSS_FIX_STATUS_READY` means a fix was obtained.

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

| Param       | Description                                                                                                | Default  |
| ----------- | ---------------------------------------------------------------------------------------------------------- | -------- |
| `epochTime` | Unix timestamp for UTC time (see [getClock](/walter-modem/arduino_esp-idf/reference/general.md#getclock)). |          |
| `rsp`       | Optional modem response structure to save the result.                                                      | **NULL** |
| `cb`        | Optional callback function, if set this function will not block.                                           | **NULL** |
| `args`      | Optional argument to pass to the callback.                                                                 | **NULL** |

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
> The UTC time is stored as a Unix timestamp in `rsp.data.clock.epochTime`.
> When the modem has no GNSS clock yet, this function returns false and `epochTime` is set to 0.

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
    Serial.print("Info: GNSS UTC time: ");
    Serial.println(rsp.data.clock.epochTime);
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
    ESP_LOGI("gnss_docs_demo", "GNSS UTC time: %lld", (long long) rsp.data.clock.epochTime);
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
> Position and speed are computed on the device.

### `WalterModemGNSSSensMode`

The possible sensitivity settings used by Walter's GNSS receiver.
This sets the amount of time that the receiver is actually on.

More sensitivity requires more power.

> **WALTER_MODEM_GNSS_SENS_MODE_LOW** = `1`  
> Lowest sensitivity, lowest power consumption.  
> **WALTER_MODEM_GNSS_SENS_MODE_MEDIUM** = `2`  
> Medium sensitivity and power consumption.  
> **WALTER_MODEM_GNSS_SENS_MODE_HIGH** = `3`  
> Highest sensitivity, highest power consumption.

### `WalterModemGNSSAcqMode`

The possible GNSS acquisition modes.

When no ephemerides are available and/or the time is not known
cold start will be used automatically.

> **WALTER_MODEM_GNSS_ACQ_MODE_COLD_WARM_START** = `0`  
> Use when Walter's position is unknown (cold or warm start).  
> **WALTER_MODEM_GNSS_ACQ_MODE_HOT_START** = `1`  
> Use when Walter's position is known within 100km.

### `WalterModemGNSSAction`

The supported actions that Walter's GNSS can execute.

> **WALTER_MODEM_GNSS_ACTION_GET_SINGLE_FIX** = `0`  
> Start acquiring a single fix.  
> **WALTER_MODEM_GNSS_ACTION_CANCEL** = `1`  
> Stop the ongoing fix acquisition.

### `WMGNSSFixStatus`

The possible GNSS fix statuses.

> **WALTER_MODEM_GNSS_FIX_STATUS_READY** = `0`  
> A fix was obtained.  
> **WALTER_MODEM_GNSS_FIX_STATUS_STOPPED_BY_USER** = `1`  
> The fix acquisition was cancelled with `WALTER_MODEM_GNSS_ACTION_CANCEL`.  
> **WALTER_MODEM_GNSS_FIX_STATUS_NO_RTC** = `2`  
> No fix because the GNSS clock is not set, see [gnssSetUTCTime](#gnsssetutctime).  
> **WALTER_MODEM_GNSS_FIX_STATUS_LTE_CONCURRENCY** = `3`  
> No fix because the receiver could not run alongside LTE activity.

### `WMGNSSAssistanceType`

Types of GNSS assistance data used to improve positioning performance.

> **WALTER_MODEM_GNSS_ASSISTANCE_TYPE_ALMANAC** = `0`  
> Long-term orbital data providing coarse satellite positions and health status.  
> **WALTER_MODEM_GNSS_ASSISTANCE_TYPE_REALTIME_EPHEMERIS** = `1`  
> Real-time satellite position and velocity data for immediate accuracy.  
> **WALTER_MODEM_GNSS_ASSISTANCE_TYPE_PREDICTED_EPHEMERIS** = `2`  
> Forecasted satellite position data for faster cold starts without a live connection.  
> **WALTER_MODEM_GNSS_ASSISTANCE_TYPE_COUNT** = `3`  
> The number of assistance types, used as the size of `rsp.data.gnssAssistance`.

---

## Structs

### `WMGNSSFixEvent`

A GNSS fix, delivered with a `WALTER_MODEM_GNSS_EVENT_FIX` event
(see [setGNSSEventHandler](/walter-modem/arduino_esp-idf/reference/event_handlers.md#setgnsseventhandler)).

| Field                 | Type                                | Description                                               |
| --------------------- | ----------------------------------- | --------------------------------------------------------- |
| `status`              | [WMGNSSFixStatus](#wmgnssfixstatus) | The status of the fix.                                    |
| `fixId`               | `uint8_t`                           | The id of the fix, always in [0-9].                       |
| `timestamp`           | `int64_t`                           | The time of the fix as a Unix timestamp.                  |
| `timeToFix`           | `uint32_t`                          | The number of milliseconds used to get the fix.           |
| `estimatedConfidence` | `double`                            | The estimated horizontal confidence of the fix in meters. |
| `latitude`            | `double`                            | The latitude of the fix.                                  |
| `longitude`           | `double`                            | The longitude of the fix.                                 |
| `height`              | `double`                            | The height above sea level.                               |
| `northSpeed`          | `double`                            | The speed in northern direction in meters per second.     |
| `eastSpeed`           | `double`                            | The speed in eastern direction in meters per second.      |
| `downSpeed`           | `double`                            | The downwards speed in meters per second.                 |
| `satCount`            | `uint8_t`                           | The number of received satellites.                        |
| `sats`                | [WMGNSSSat](#wmgnsssat)[]           | The received satellites, the first `satCount` are valid.  |

### `WMGNSSSat`

A satellite received during a GNSS fix.

| Field            | Type      | Description                                                                        |
| ---------------- | --------- | ---------------------------------------------------------------------------------- |
| `satNo`          | `uint8_t` | The number of the satellite.                                                       |
| `signalStrength` | `uint8_t` | The CN0 signal strength in dB/Hz. The minimum required signal strength is 30dB/Hz. |

### `WMGNSSAssistance`

The status of one type of GNSS assistance data, see [gnssGetAssistanceStatus](#gnssgetassistancestatus).

| Field          | Type                                          | Description                                                                        |
| -------------- | --------------------------------------------- | ---------------------------------------------------------------------------------- |
| `type`         | [WMGNSSAssistanceType](#wmgnssassistancetype) | The type of assistance data this entry is about.                                   |
| `available`    | `bool`                                        | True when this type of assistance data is available.                               |
| `lastUpdate`   | `int32_t`                                     | The number of seconds since the last update of this type of assistance data.       |
| `timeToUpdate` | `int32_t`                                     | The number of seconds before this data should be updated to keep GNSS performance. |
| `timeToExpire` | `int32_t`                                     | The number of seconds after which this data expires and can no longer be used.     |
