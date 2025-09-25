## Methods Overview

- [blueCherryProvision](#bluecherryprovision)
- [blueCherryIsProvisioned](#bluecherryisprovisioned)
- [blueCherryInit](#bluecherryinit)
- [blueCherryPublish](#bluecherrypublish)
- [blueCherrySync](#bluecherrysync)
- [blueCherryClose](#bluecherryclose)

## Enums Overview

- [WalterModemBlueCherryStatus](#waltermodembluecherrystatus)
- [WalterModemBlueCherryEventType](#waltermodembluecherryeventtype)

## Methods

### `blueCherryProvision`

Upload BlueCherry credentials to the modem.

Upload Walter's certificate and private key
and the BlueCherry cloud server CA certificate to the modem.

> [!NOTE]
> The "key" parameters are NULL terminated strings containing the PEM data
> with each line terminated by CRLF _(\r\n)_.

#### Params

| Param               | Description                                                      | Default  |
| ------------------- | ---------------------------------------------------------------- | -------- |
| `walterCertificate` | Walter X.509 certificate as PEM string                           |          |
| `walterPrivateKey`  | Walter private key as PEM string                                 |          |
| `caCertificate`     | BlueCherry CA certificate                                        |          |
| `rsp`               | Optional modem response structure to save the result in.         | **NULL** |
| `cb`                | Optional callback function, if set this function will not block. | **NULL** |
| `args`              | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on success, False otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <BlueCherryZTP.h>
#include <WalterModem.h>

const char *bc_ca_cert = "-----BEGIN CERTIFICATE-----\r\n\
-----END CERTIFICATE-----\r\n\
-----BEGIN CERTIFICATE-----\r\n\
-----END CERTIFICATE-----\r\n";

// ...

if (modem.blueCherryProvision(BlueCherryZTP::getCert(), BlueCherryZTP::getPrivKey(), bc_ca_cert)) {
    Serial.println("Info: DTLS certificates uploaded");
} else {
    Serial.println("Error: Failed to upload the DTLS certificates");
}

// ..
```

##### **ESP-IDF**

```cpp
#include <BlueCherryZTP.h>
#include <WalterModem.h>
#include <esp_log.h>

const char *bc_ca_cert = "-----BEGIN CERTIFICATE-----\r\n\
-----END CERTIFICATE-----\r\n\
-----BEGIN CERTIFICATE-----\r\n\
-----END CERTIFICATE-----\r\n";

// ...

if (modem.blueCherryProvision(BlueCherryZTP::getCert(), BlueCherryZTP::getPrivKey(), bc_ca_cert)) {
    ESP_LOGI("bluecherry_docs_demo", "DTLS certificates uploaded");
} else {
    ESP_LOGE("bluecherry_docs_demo", "Failed to upload the DTLS certificates");
}

// ...
```

<!-- tabs:end -->

---

### `blueCherryIsProvisioned`

Check if Walter is provisioned for BlueCherry IoT connectivity.

This function checks if the necessary certificates and private key are present in the modem's NVRAM.

> [!NOTE]
> It does not check if the credentials are valid, but only checks if
> the BlueCherry reserved slot indexes are occupied inside the modem's NVRAM.

#### Returns

`bool`  
True when provisioned, false if not.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <BlueCherryZTP.h>
#include <WalterModem.h>

// ...

if (modem.blueCherryIsProvisioned()) {
    Serial.println("Info: Provisioned");
} else {
    Serial.println("Info: Not provisioned");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (modem.blueCherryIsProvisioned()) {
    ESP_LOGI("bluecherry_docs_demo", "Provisioned");
} else {
    ESP_LOGI("bluecherry_docs_demo", "Not provisioned");
}

// ...
```

<!-- tabs:end -->

---

### `blueCherryInit`

Initialize BlueCherry MQTT <-> CoAP bridge.

This function sets the TLS profile ID and initializes
the accumulated outgoing datagram.
It sets the current message ID to 1, the last acknowledged ID to 0,
and sets the state machine to IDLE.

#### Params

| Param          | Description                                                           | Default  |
| -------------- | --------------------------------------------------------------------- | -------- |
| `tlsProfileId` | DTLS is used with the given profile (1-6).                            |          |
| `otaBuffer`    | A user-supplied buffer for OTA updates to flash, aligned to 4K bytes. | **NULL** |
| `rsp`          | Optional modem response structure to save the result in.              | **NULL** |
| `ackTimeout`   | Timeout for ACK of outgoing BlueCherry CoAP messages, in seconds.     | **60**   |

#### Returns

`bool`  
True on success, False otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <BlueCherryZTP.h>
#include <WalterModem.h>

CONFIG_UINT8(BC_TLS_PROFILE, 1)

WalterModemRsp rsp = {};

byte otaBuffer[SPI_FLASH_BLOCK_SIZE] = {0};

// ...

if (modem.blueCherryInit(BC_TLS_PROFILE, otaBuffer, &rsp)) {
    ESP_LOGI(TAG, "BlueCherry initialized");
} else {
    ESP_LOGE(TAG, "Failed to init BlueCherry");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG_UINT8(BC_TLS_PROFILE, 1)

WalterModemRsp rsp = {};

uint8_t otaBuffer[SPI_FLASH_BLOCK_SIZE] = {0};

// ...

if (modem.blueCherryInit(BC_TLS_PROFILE, otaBuffer, &rsp)) {
    ESP_LOGI("bluecherry_docs_demo", "BlueCherry initialized");
} else {
    ESP_LOGE("bluecherry_docs_demo", "Failed to init BlueCherry");
}

// ...
```

<!-- tabs:end -->

---

### `blueCherryPublish`

Enqueue an MQTT publish message.

This function will add the message to the accumulated outgoing datagram,
which will - after blueCherrySync - be sent to the BlueCherry cloud server
and published through MQTT.

#### Params

| Param   | Description                                          | Default |
| ------- | ---------------------------------------------------- | ------- |
| `topic` | The topic of the message, passed as the topic index. |         |
| `len`   | The length of the data.                              |         |
| `data`  | The data to send.                                    |         |

#### Returns

`bool`  
True on success, False otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <BlueCherryZTP.h>
#include <WalterModem.h>

// ...

static const char msg[] = "Demo message";

if (modem.blueCherryPublish(0x84, sizeof(msg)-1, (uint8_t *)msg)) {
    Serial.println("Info: blueCherryPublish succeeded");
} else {
    Serial.println("Error: blueCherryPublish failed");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

static const char msg[] = "Demo message";

if (modem.blueCherryPublish(0x84, sizeof(msg) - 1, (uint8_t *)msg)) {
    ESP_LOGI("bluecherry_docs_demo", "blueCherryPublish succeeded");
} else {
    ESP_LOGE("bluecherry_docs_demo", "blueCherryPublish failed");
}

// ...
```

<!-- tabs:end -->

---

### `blueCherrySync`

Send accumulated MQTT messages and poll for incoming data.

This function will send all accumulated MQTT publish messages to the BlueCherry cloud
server, and ask the server for an acknowledgement and for the new incoming MQTT messages
since the last blueCherrySync call.

> [!NOTE]
> Even if nothing was enqueued for publish, this call must frequently be executed if Walter
> is subscribed to one or more MQTT topics or has enabled BlueCherry OTA updates.
>
> A response might not fit in a single datagram response. As long as syncFinished is false,
> this function needs to be called again repeatedly.

#### Params

<!-- tabs:start -->

| Param | Description                                              | Default  |
| ----- | -------------------------------------------------------- | -------- |
| `rsp` | Optional modem response structure to save the result in. |          |

#### Returns

`bool`  
True on success, False otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <BlueCherryZTP.h>
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (!modem.blueCherrySync(&rsp)) {
    Serial.print("Error: failure during BlueCherry cloud platform synchronisation: ");
    Serial.println(rsp.data.blueCherry.state);
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (!modem.blueCherrySync(&rsp)) {
    ESP_LOGE(
        "bluecherry_docs_demo",
        "Error during BlueCherry cloud platform synchronisation: %d",
        rsp.data.blueCherry.state);
}

// ...
```

<!-- tabs:end -->

---

### `blueCherryClose`

Close the BlueCherry platform CoAP connection.

This function will close the CoAP connection to the Bluecherry cloud platform.

> [!TIP]
> Usually there is no need to call this function, unless using deep sleep mode (which might cause a
> modem bug in the latest modem firmware versions).

#### Params

| Param  | Description                                                      | Default  |
| ------ | ---------------------------------------------------------------- | -------- |
| `rsp`  | Optional modem response structure to save the result in.         | **NULL** |
| `cb`   | Optional callback function, if set this function will not block. | **NULL** |
| `args` | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on success, False otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <BlueCherryZTP.h>
#include <WalterModem.h>

// ...

if (modem.blueCherryClose()) {
    Serial.println("Info: BlueCherry closed");
} else {
    Serial.println("Error: Failed to close BlueCherry");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (modem.blueCherryClose()) {
    ESP_LOGI("bluecherry_docs_demo", "BlueCherry closed");
} else {
    ESP_LOGE("bluecherry_docs_demo", "Failed to close BlueCherry");
}

// ...
```

<!-- tabs:end -->

---

## Enums

### `WalterModemBlueCherryStatus`

The possible statuses of a BlueCherry communication cycle.

> **WALTER_MODEM_BLUECHERRY_STATUS_NOT_CONNECTED**  
> **WALTER_MODEM_BLUECHERRY_STATUS_IDLE**  
> **WALTER_MODEM_BLUECHERRY_STATUS_AWAITING_RESPONSE**  
> **WALTER_MODEM_BLUECHERRY_STATUS_RESPONSE_READY**  
> **WALTER_MODEM_BLUECHERRY_STATUS_PENDING_MESSAGES**  
> **WALTER_MODEM_BLUECHERRY_STATUS_TIMED_OUT**  
> **WALTER_MODEM_BLUECHERRY_STATUS_NOT_PROVISIONED**  

### `WalterModemBlueCherryEventType`

The possible types of BlueCherry events.

> **WALTER_MODEM_BLUECHERRY_EVENT_TYPE_OTA_INITIALIZE** = `1`  
> **WALTER_MODEM_BLUECHERRY_EVENT_TYPE_OTA_CHUNK** = `2`  
> **WALTER_MODEM_BLUECHERRY_EVENT_TYPE_OTA_FINISH** = `3`  
> **WALTER_MODEM_BLUECHERRY_EVENT_TYPE_OTA_ERROR** = `4`  
> **WALTER_MODEM_BLUECHERRY_EVENT_TYPE_MOTA_INITIALIZE** = `5`  
> **WALTER_MODEM_BLUECHERRY_EVENT_TYPE_MOTA_CHUNK** = `6`  
> **WALTER_MODEM_BLUECHERRY_EVENT_TYPE_MOTA_FINISH** = `7`  
> **WALTER_MODEM_BLUECHERRY_EVENT_TYPE_MOTA_ERROR** = `8`  
