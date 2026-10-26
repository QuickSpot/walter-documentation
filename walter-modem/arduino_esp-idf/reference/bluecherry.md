> [!NOTE]
> Since v1.6.0, BlueCherry has its own `WalterBlueCherry` class in `WalterBlueCherry.h`.
> The `modem.blueCherry*` methods have been removed.
>
> - **ESP-IDF:** enable `BLUECHERRY_ENABLE` in the BlueCherry menuconfig menu. It replaces
>   `WALTER_MODEM_ENABLE_BLUECHERRY`, and an existing `sdkconfig` keeps the old name silently,
>   so set the option again.
> - **Arduino:** enable PSRAM for the publish buffer. Without it, the library falls back to
>   internal RAM and logs a warning.

## Methods Overview

- [init](#init)
- [provision](#provision)
- [isProvisioned](#isprovisioned)
- [publish](#publish)
- [sync](#sync)
- [setAutoSync](#setautosync)
- [getState](#getstate)
- [setStateHandler](#setstatehandler)
- [setMsgHandler](#setmsghandler)
- [setOtaHandler](#setotahandler)
- [otaStartDownload](#otastartdownload)
- [otaInstall](#otainstall)
- [otaAbort](#otaabort)
- [otaMarkValid](#otamarkvalid)
- [otaRollbackRestart](#otarollbackrestart)
- [close](#close)
- [getOtaProgressPercentage](#getotaprogresspercentage)
- [getOtaProgressBytes](#getotaprogressbytes)
- [getOtaSize](#getotasize)

## Enums Overview

- [BlueCherryState](#bluecherrystate)
- [BlueCherryZtpDeviceIdType](#bluecherryztpdeviceidtype)
- [BlueCherryOtaError](#bluecherryotaerror)
- [BlueCherryOtaEvent](#bluecherryotaevent)

## Structs Overview

- [BlueCherryPublishBuffer](#bluecherrypublishbuffer)
- [BlueCherryOtaInfo](#bluecherryotainfo)

## Types Overview

- [blueCherryMsgHandler](#bluecherrymsghandler)
- [blueCherryStateHandler](#bluecherrystatehandler)
- [blueCherryOtaHandler](#bluecherryotahandler)

---

## Methods

### `init`

Initialize BlueCherry and start the synchronisation task.

`init` does no network I/O. The sync task connects once the modem is attached to a network.

> [!IMPORTANT]
> Call `init` after `modem.begin()`, on every boot, including after waking from deep sleep.

> [!TIP]
> Install the OTA handler with [setOtaHandler](#setotahandler) **before** calling `init`.

#### Params

| Param            | Description                                                                                                                                   | Default  |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `tls_profile_id` | The modem TLS profile to use. BlueCherry owns NVM slots 0, 5 and 6.                                                                           |          |
| `device_type_id` | The 8 character BlueCherry Type ID, required for provisioning only.                                                                           | **NULL** |
| `publish_buffer` | A [BlueCherryPublishBuffer](#bluecherrypublishbuffer) to queue outgoing messages in, or NULL to allocate the Kconfig default in internal RAM. | **NULL** |

#### Returns

`bool`
True on succes, false on error

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>
#include <WalterBlueCherry.h>

#define BC_TLS_PROFILE 1
#define BC_DEVICE_TYPE "walter01"

WalterModem modem;
WalterBlueCherry bc;

// ...

if (bc.init(BC_TLS_PROFILE, BC_DEVICE_TYPE)) {
    Serial.println("Info: BlueCherry initialized");
} else {
    Serial.println("Error: Failed to init BlueCherry");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>
#include <WalterBlueCherry.h>

#define BC_TLS_PROFILE 1
#define BC_DEVICE_TYPE "walter01"

WalterModem modem;
WalterBlueCherry bc;

// ...

if (bc.init(BC_TLS_PROFILE, BC_DEVICE_TYPE)) {
    ESP_LOGI("bluecherry_docs_demo", "BlueCherry initialized");
} else {
    ESP_LOGE("bluecherry_docs_demo", "Failed to init BlueCherry");
}

// ...
```

<!-- tabs:end -->

---

### `provision`

Upload the BlueCherry credentials to the modem.

The device certificate goes to NVM slot 5, the private key to slot 0 and the CA chain to slot 6.

> [!NOTE]
> This is only needed for manual provisioning. Zero-Touch Provisioning calls it itself when
> [init](#init) was given a `device_type_id`.

#### Params

| Param          | Description                            | Default |
| -------------- | -------------------------------------- | ------- |
| `cert_pem`     | The device certificate in PEM format.  |         |
| `priv_key_pem` | The device private key in PEM format.  |         |
| `ca_cert`      | The BlueCherry CA chain in PEM format. |         |

#### Returns

`bool`
True on succes, false on error

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterBlueCherry.h>

const char *device_cert = "-----BEGIN CERTIFICATE-----\r\n\
-----END CERTIFICATE-----\r\n";

const char *device_key = "-----BEGIN PRIVATE KEY-----\r\n\
-----END PRIVATE KEY-----\r\n";

const char *bc_ca_cert = "-----BEGIN CERTIFICATE-----\r\n\
-----END CERTIFICATE-----\r\n";

// ...

if (bc.provision(device_cert, device_key, bc_ca_cert)) {
    Serial.println("Info: BlueCherry credentials uploaded");
} else {
    Serial.println("Error: Failed to upload the BlueCherry credentials");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterBlueCherry.h>

const char *device_cert = "-----BEGIN CERTIFICATE-----\r\n\
-----END CERTIFICATE-----\r\n";

const char *device_key = "-----BEGIN PRIVATE KEY-----\r\n\
-----END PRIVATE KEY-----\r\n";

const char *bc_ca_cert = "-----BEGIN CERTIFICATE-----\r\n\
-----END CERTIFICATE-----\r\n";

// ...

if (bc.provision(device_cert, device_key, bc_ca_cert)) {
    ESP_LOGI("bluecherry_docs_demo", "BlueCherry credentials uploaded");
} else {
    ESP_LOGE("bluecherry_docs_demo", "Failed to upload the BlueCherry credentials");
}

// ...
```

<!-- tabs:end -->

---

### `isProvisioned`

Check whether the modem holds BlueCherry credentials.
Reads NVM slots 5, 6 and 0. The key itself is never readable back out of the modem.

> [!NOTE]
> This does not check if the credentials are valid, only that the BlueCherry slots are occupied.

#### Returns

`bool`
True when all three are present, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterBlueCherry.h>

// ...

if (bc.isProvisioned()) {
    Serial.println("Info: Provisioned");
} else {
    Serial.println("Info: Not provisioned");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterBlueCherry.h>

// ...

if (bc.isProvisioned()) {
    ESP_LOGI("bluecherry_docs_demo", "Provisioned");
} else {
    ESP_LOGI("bluecherry_docs_demo", "Not provisioned");
}

// ...
```

<!-- tabs:end -->

---

### `publish`

Queue a message for publication.

The message is only queued. It is sent to the cloud on the next [sync](#sync).

> [!NOTE]
> Messages longer than `BLUECHERRY_MAX_PUBLISH_LEN` (255 bytes) are rejected, not truncated.
> When the publish buffer is full, the call fails without dropping messages already queued.

#### Params

| Param   | Description                                                                    | Default |
| ------- | ------------------------------------------------------------------------------ | ------- |
| `topic` | The single byte topic index the cloud maps to an MQTT topic. 0x00 is reserved. |         |
| `len`   | The number of bytes in data, at most BLUECHERRY_MAX_PUBLISH_LEN.               |         |
| `data`  | The payload, which is copied.                                                  |         |

#### Returns

`bool`
True when queued, false on error.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterBlueCherry.h>

// ...

static const char msg[] = "Demo message";

if (bc.publish(0x84, sizeof(msg) - 1, (const uint8_t *)msg)) {
    Serial.println("Info: Message queued");
} else {
    Serial.println("Error: Failed to queue message");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterBlueCherry.h>

// ...

static const char msg[] = "Demo message";

if (bc.publish(0x84, sizeof(msg) - 1, (const uint8_t *)msg)) {
    ESP_LOGI("bluecherry_docs_demo", "Message queued");
} else {
    ESP_LOGE("bluecherry_docs_demo", "Failed to queue message");
}

// ...
```

<!-- tabs:end -->

---

### `sync`

Ask the synchronisation task to run a cycle.

The call is non-blocking: it signals the sync task and returns right away. The task sends the
queued messages and fetches the incoming ones, which are delivered to the
[message handler](#setmsghandler). Use [setStateHandler](#setstatehandler) or
[getState](#getstate) to know when the cycle has finished.

> [!TIP]
> To sync periodically without calling `sync` yourself, use [setAutoSync](#setautosync).
> A device that sleeps between cycles usually calls `sync` itself, so it controls how many
> exchanges happen before going back to sleep.

#### Returns

`bool`
True when the task was signalled, false when BlueCherry is not initialized.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterBlueCherry.h>

// ...

if (!bc.sync()) {
    Serial.println("Error: BlueCherry is not initialized");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterBlueCherry.h>

// ...

if (!bc.sync()) {
    ESP_LOGE("bluecherry_docs_demo", "BlueCherry is not initialized");
}

// ...
```

<!-- tabs:end -->

---

### `setAutoSync`

Synchronise on a timer in addition to on demand.

The interval can be changed or disabled at any time.

#### Params

| Param          | Description                               | Default |
| -------------- | ----------------------------------------- | ------- |
| `interval_sec` | The interval in seconds, or 0 to disable. |         |

#### Returns

`bool`
True on success, false when BlueCherry is not initialized.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterBlueCherry.h>

// ...

if (bc.setAutoSync(60)) {
    Serial.println("Info: Auto sync every 60 seconds");
} else {
    Serial.println("Error: Failed to set auto sync");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterBlueCherry.h>

// ...

if (bc.setAutoSync(60)) {
    ESP_LOGI("bluecherry_docs_demo", "Auto sync every 60 seconds");
} else {
    ESP_LOGE("bluecherry_docs_demo", "Failed to set auto sync");
}

// ...
```

<!-- tabs:end -->

---

### `getState`

Get the current state of the BlueCherry connection.

#### Returns

`BlueCherryState`
The current BlueCherryState.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterBlueCherry.h>

// ...

if (bc.getState() == BLUECHERRY_STATE_IDLE) {
    Serial.println("Info: BlueCherry is synchronized");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterBlueCherry.h>

// ...

if (bc.getState() == BLUECHERRY_STATE_IDLE) {
    ESP_LOGI("bluecherry_docs_demo", "BlueCherry is synchronized");
}

// ...
```

<!-- tabs:end -->

---

### `setStateHandler`

Install a handler notified of every connection state change.

> [!WARNING]
> The handler runs on the sync task and must not block.

#### Params

| Param     | Description                                                                             | Default  |
| --------- | --------------------------------------------------------------------------------------- | -------- |
| `handler` | A [blueCherryStateHandler](#bluecherrystatehandler), or NULL to remove the current one. |          |
| `args`    | Optional user arguments for the handler.                                                | **NULL** |

#### Returns

`bool`
True on success, false on error.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterBlueCherry.h>

void myStateHandler(BlueCherryState state, void *args)
{
    switch (state) {
    case BLUECHERRY_STATE_NOT_PROVISIONED:
        Serial.println("Info: Not provisioned");
        break;
    case BLUECHERRY_STATE_AWAIT_CONNECTION:
        Serial.println("Info: Connecting to BlueCherry");
        break;
    case BLUECHERRY_STATE_IDLE:
        Serial.println("Info: BlueCherry synchronized");
        break;
    default:
        break;
    }
}

// ...

bc.setStateHandler(myStateHandler);

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterBlueCherry.h>

void myStateHandler(BlueCherryState state, void *args)
{
    switch (state) {
    case BLUECHERRY_STATE_NOT_PROVISIONED:
        ESP_LOGI("bluecherry_docs_demo", "Not provisioned");
        break;
    case BLUECHERRY_STATE_AWAIT_CONNECTION:
        ESP_LOGI("bluecherry_docs_demo", "Connecting to BlueCherry");
        break;
    case BLUECHERRY_STATE_IDLE:
        ESP_LOGI("bluecherry_docs_demo", "BlueCherry synchronized");
        break;
    default:
        break;
    }
}

// ...

bc.setStateHandler(myStateHandler);

// ...
```

<!-- tabs:end -->

---

### `setMsgHandler`

Install a handler for incoming messages.

> [!WARNING]
> The handler runs on the sync task and must not block. `data` is only valid during the call,
> so copy it if you need it afterwards.

#### Params

| Param     | Description                                                                           | Default  |
| --------- | ------------------------------------------------------------------------------------- | -------- |
| `handler` | A [blueCherryMsgHandler](#bluecherrymsghandler), or NULL to ignore incoming messages. |          |
| `args`    | Optional user arguments for the handler.                                              | **NULL** |

#### Returns

`bool`
True on success, false on error.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterBlueCherry.h>

void myMessageHandler(uint8_t topic, uint16_t len, const uint8_t *data, void *args)
{
    Serial.printf("Info: Message on topic 0x%02X (%u bytes): %.*s\r\n",
                  topic, len, len, (const char *)data);
}

// ...

bc.setMsgHandler(myMessageHandler);

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterBlueCherry.h>

void myMessageHandler(uint8_t topic, uint16_t len, const uint8_t *data, void *args)
{
    ESP_LOGI("bluecherry_docs_demo", "Message on topic 0x%02X (%u bytes): %.*s",
             topic, len, len, (const char *)data);
}

// ...

bc.setMsgHandler(myMessageHandler);

// ...
```

<!-- tabs:end -->

---

### `setOtaHandler`

Install a handler for OTA events.

The handler can take the decision for an event itself by returning true. When it returns false,
the library applies its default. See [BlueCherryOtaEvent](#bluecherryotaevent) for which events
carry a decision.

> [!IMPORTANT]
> Install the OTA handler **before** calling [init](#init).

> [!TIP]
> Interrupted firmware downloads resume from what is already on flash.

#### Params

| Param     | Description                                                                         | Default  |
| --------- | ----------------------------------------------------------------------------------- | -------- |
| `handler` | A [blueCherryOtaHandler](#bluecherryotahandler), or NULL to remove the current one. |          |
| `args`    | Optional user arguments for the handler.                                            | **NULL** |

#### Returns

`bool`
True on success, false on error.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterBlueCherry.h>

bool myOtaHandler(BlueCherryOtaEvent event, const BlueCherryOtaInfo *info, void *args)
{
    switch (event) {
    case BLUECHERRY_OTA_EVENT_DOWNLOAD_AVAILABLE:
        Serial.printf("Info: Update available (%u bytes)\r\n", info->size);
        bc.otaStartDownload();
        return true;
    case BLUECHERRY_OTA_EVENT_DOWNLOAD_COMPLETE:
        Serial.println("Info: Update downloaded, installing");
        if (bc.otaInstall()) {
            ESP.restart();
        }
        return true;
    case BLUECHERRY_OTA_EVENT_FIRSTBOOT:
        Serial.println("Info: Running new firmware, keeping it");
        bc.otaMarkValid();
        return true;
    default:
        return false;
    }
}

// ...

bc.setOtaHandler(myOtaHandler);
bc.init(BC_TLS_PROFILE, BC_DEVICE_TYPE);

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <esp_system.h>
#include <WalterBlueCherry.h>

bool myOtaHandler(BlueCherryOtaEvent event, const BlueCherryOtaInfo *info, void *args)
{
    switch (event) {
    case BLUECHERRY_OTA_EVENT_DOWNLOAD_AVAILABLE:
        ESP_LOGI("bluecherry_docs_demo", "Update available (%" PRIu32 " bytes)", info->size);
        bc.otaStartDownload();
        return true;
    case BLUECHERRY_OTA_EVENT_DOWNLOAD_COMPLETE:
        ESP_LOGI("bluecherry_docs_demo", "Update downloaded, installing");
        if (bc.otaInstall()) {
            esp_restart();
        }
        return true;
    case BLUECHERRY_OTA_EVENT_FIRSTBOOT:
        ESP_LOGI("bluecherry_docs_demo", "Running new firmware, keeping it");
        bc.otaMarkValid();
        return true;
    default:
        return false;
    }
}

// ...

bc.setOtaHandler(myOtaHandler);
bc.init(BC_TLS_PROFILE, BC_DEVICE_TYPE);

// ...
```

<!-- tabs:end -->

---

### `otaStartDownload`

Accept an offered firmware update.

Call this from the OTA handler on `BLUECHERRY_OTA_EVENT_DOWNLOAD_AVAILABLE`, or later.

#### Returns

`bool`
True when the download was requested, false when no update is on offer, or after otaInstall until the restart.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterBlueCherry.h>

// ...

if (!bc.otaStartDownload()) {
    Serial.println("Error: No update on offer");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterBlueCherry.h>

// ...

if (!bc.otaStartDownload()) {
    ESP_LOGE("bluecherry_docs_demo", "No update on offer");
}

// ...
```

<!-- tabs:end -->

---

### `otaInstall`

Make the downloaded update the firmware Walter boots next.

> [!IMPORTANT]
> This does not restart Walter. Restart it yourself once `otaInstall` returns true.

#### Returns

`bool`
True when the new firmware is set to boot, false when no download is waiting for its install or the boot partition could not be set, which is also reported to the cloud.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterBlueCherry.h>

// ...

if (bc.otaInstall()) {
    ESP.restart();
} else {
    Serial.println("Error: Failed to install the update");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <esp_system.h>
#include <WalterBlueCherry.h>

// ...

if (bc.otaInstall()) {
    esp_restart();
} else {
    ESP_LOGE("bluecherry_docs_demo", "Failed to install the update");
}

// ...
```

<!-- tabs:end -->

---

### `otaAbort`

Decline an offered update, or abandon the download in progress.

The `error_code` is reported to the cloud.

#### Params

| Param        | Description                                                        | Default                            |
| ------------ | ------------------------------------------------------------------ | ---------------------------------- |
| `error_code` | A [BlueCherryOtaError](#bluecherryotaerror) reported to the cloud. | **BLUECHERRY_OTA_ERR_APP_ABORTED** |

#### Returns

`bool`
True when the abort was queued, false when no update is in progress.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterBlueCherry.h>

// ...

if (bc.otaAbort()) {
    Serial.println("Info: Update declined");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterBlueCherry.h>

// ...

if (bc.otaAbort()) {
    ESP_LOGI("bluecherry_docs_demo", "Update declined");
}

// ...
```

<!-- tabs:end -->

---

### `otaMarkValid`

Keep the running firmware, cancelling the rollback.

Call this after `BLUECHERRY_OTA_EVENT_FIRSTBOOT`, once the new firmware is confirmed to work.

> [!NOTE]
> `BLUECHERRY_OTA_EVENT_FIRSTBOOT` is only raised when app rollback is enabled. On Arduino, the
> sketch must also define `extern "C" bool verifyRollbackLater()` returning true to receive it.

#### Returns

`bool`
True on success, false on error.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterBlueCherry.h>

extern "C" bool verifyRollbackLater()
{
    return true;
}

// ...

if (bc.otaMarkValid()) {
    Serial.println("Info: New firmware marked valid");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterBlueCherry.h>

// ...

if (bc.otaMarkValid()) {
    ESP_LOGI("bluecherry_docs_demo", "New firmware marked valid");
}

// ...
```

<!-- tabs:end -->

---

### `otaRollbackRestart`

Reject the running firmware and restart into the previous one.

> [!NOTE]
> This function does not return on success.

#### Returns

`bool`
False, on failure.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterBlueCherry.h>

// ...

bc.otaRollbackRestart();
Serial.println("Error: Rollback failed");

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterBlueCherry.h>

// ...

bc.otaRollbackRestart();
ESP_LOGE("bluecherry_docs_demo", "Rollback failed");

// ...
```

<!-- tabs:end -->

---

### `close`

Close the BlueCherry session and release the modem socket.

#### Returns

`bool`
True on success, false on error.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterBlueCherry.h>

// ...

if (bc.close()) {
    Serial.println("Info: BlueCherry closed");
} else {
    Serial.println("Error: Failed to close BlueCherry");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterBlueCherry.h>

// ...

if (bc.close()) {
    ESP_LOGI("bluecherry_docs_demo", "BlueCherry closed");
} else {
    ESP_LOGE("bluecherry_docs_demo", "Failed to close BlueCherry");
}

// ...
```

<!-- tabs:end -->

---

### `getOtaProgressPercentage`

Get the progress of the firmware update in progress, as a percentage.

#### Returns

`size_t`
The percentage of the image written to flash.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterBlueCherry.h>

// ...

Serial.printf("Info: OTA progress %u%%\r\n", (unsigned)bc.getOtaProgressPercentage());

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterBlueCherry.h>

// ...

ESP_LOGI("bluecherry_docs_demo", "OTA progress %u%%", (unsigned)bc.getOtaProgressPercentage());

// ...
```

<!-- tabs:end -->

---

### `getOtaProgressBytes`

Get the progress of the firmware update in progress, in bytes.

#### Returns

`size_t`
The number of bytes of the image written to flash.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterBlueCherry.h>

// ...

Serial.printf("Info: OTA progress %u / %u bytes\r\n",
              (unsigned)bc.getOtaProgressBytes(), (unsigned)bc.getOtaSize());

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterBlueCherry.h>

// ...

ESP_LOGI("bluecherry_docs_demo", "OTA progress %u / %u bytes",
         (unsigned)bc.getOtaProgressBytes(), (unsigned)bc.getOtaSize());

// ...
```

<!-- tabs:end -->

---

### `getOtaSize`

Get the total size of the firmware update in progress.

#### Returns

`size_t`
The announced image size in bytes, or 0 when no update is running.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterBlueCherry.h>

// ...

if (bc.getOtaSize() == 0) {
    Serial.println("Info: No update running");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterBlueCherry.h>

// ...

if (bc.getOtaSize() == 0) {
    ESP_LOGI("bluecherry_docs_demo", "No update running");
}

// ...
```

<!-- tabs:end -->

---

## Enums

### `BlueCherryState`

The states the BlueCherry connection can be in.

> **BLUECHERRY_STATE_UNINITIALIZED** = 0  
> **BLUECHERRY_STATE_NOT_PROVISIONED**  
> **BLUECHERRY_STATE_AWAIT_CONNECTION**  
> **BLUECHERRY_STATE_IDLE**  
> **BLUECHERRY_STATE_AWAITING_RESPONSE**  
> **BLUECHERRY_STATE_PENDING_MESSAGES**

> [!NOTE]
> These replace the old `WALTER_MODEM_BLUECHERRY_STATUS_*` values. `NOT_INITIALIZED` is now
> `UNINITIALIZED`, `NOT_CONNECTED` is now `AWAIT_CONNECTION`, and `RESPONSE_READY` and
> `TIMED_OUT` have been removed.

### `BlueCherryZtpDeviceIdType`

The device identifier types the ZTP server accepts.

> **BLUECHERRY_ZTP_DEVICE_ID_TYPE_MAC** = 0  
> **BLUECHERRY_ZTP_DEVICE_ID_TYPE_IMEI**  
> **BLUECHERRY_ZTP_DEVICE_ID_TYPE_OOB_CHALLENGE**

### `BlueCherryOtaError`

OTA error codes reported to the cloud.

> **BLUECHERRY_OTA_ERR_NO_PARTITION** = 1  
> **BLUECHERRY_OTA_ERR_TOO_LARGE** = 2  
> **BLUECHERRY_OTA_ERR_ERASE_FAILED** = 3  
> **BLUECHERRY_OTA_ERR_WRITE_FAILED** = 4  
> **BLUECHERRY_OTA_ERR_HASH_MISMATCH** = 5  
> **BLUECHERRY_OTA_ERR_BAD_MAGIC** = 6  
> **BLUECHERRY_OTA_ERR_SET_BOOT_FAILED** = 7  
> **BLUECHERRY_OTA_ERR_APP_ABORTED** = 8  
> **BLUECHERRY_OTA_ERR_CHUNK_OVERRUN** = 9

### `BlueCherryOtaEvent`

OTA events reported to the [OTA handler](#setotahandler).

| Event                                       | Decision the handler can take                                                                                  |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **BLUECHERRY_OTA_EVENT_DOWNLOAD_AVAILABLE** | Start the download ([otaStartDownload](#otastartdownload))                                                     |
| **BLUECHERRY_OTA_EVENT_DOWNLOAD_STARTED**   | None                                                                                                           |
| **BLUECHERRY_OTA_EVENT_DOWNLOAD_PROGRESS**  | None                                                                                                           |
| **BLUECHERRY_OTA_EVENT_DOWNLOAD_COMPLETE**  | Install and restart ([otaInstall](#otainstall))                                                                |
| **BLUECHERRY_OTA_EVENT_FIRSTBOOT**          | Keep the new firmware ([otaMarkValid](#otamarkvalid)) or roll back ([otaRollbackRestart](#otarollbackrestart)) |
| **BLUECHERRY_OTA_EVENT_FAILED**             | None                                                                                                           |

For events without a decision, the handler's return value is ignored.

---

## Structs

### `BlueCherryPublishBuffer`

A user-supplied buffer for queued outgoing messages, passed to [init](#init). It can be placed in
PSRAM or RTC memory. The library borrows it and never frees it.

| Field    | Type       | Description                                                |
| -------- | ---------- | ---------------------------------------------------------- |
| `buffer` | `uint8_t*` | The buffer memory.                                         |
| `size`   | `size_t`   | The buffer size, at least `BLUECHERRY_MIN_PUBLISH_BUFFER`. |

### `BlueCherryOtaInfo`

Details of the update, passed to the [OTA handler](#bluecherryotahandler).

| Field            | Type          | Description                                                 |
| ---------------- | ------------- | ----------------------------------------------------------- |
| `version`        | `int8_t`      | The firmware version offered or installed.                  |
| `size`           | `uint32_t`    | The total image size in bytes.                              |
| `sha256`         | `uint8_t[32]` | The expected SHA-256 hash, or all zeroes if unknown.        |
| `bytes_received` | `uint32_t`    | The bytes written so far (progress event).                  |
| `error_code`     | `uint8_t`     | A [BlueCherryOtaError](#bluecherryotaerror) (failed event). |

---

## Types

### `blueCherryMsgHandler`

```cpp
typedef void (*blueCherryMsgHandler)(uint8_t topic, uint16_t len, const uint8_t *data, void *args);
```

Receives incoming messages on the sync task. It must not block, and `data` is only valid during
the call.

### `blueCherryStateHandler`

```cpp
typedef void (*blueCherryStateHandler)(BlueCherryState state, void *args);
```

Called on every state transition. It must not block.

### `blueCherryOtaHandler`

```cpp
typedef bool (*blueCherryOtaHandler)(BlueCherryOtaEvent event, const BlueCherryOtaInfo *info, void *args);
```

Returns true when the application took the event's decision, or false to let the library apply
its default.
