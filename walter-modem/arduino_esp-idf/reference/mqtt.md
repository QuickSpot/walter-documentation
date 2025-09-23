## Methods Overview

- [getMqttStatus](#getmqttstatus)
- [mqttConfig](#mqttconfig)
- [mqttConnect](#mqttconnect)
- [mqttSubscribe](#mqttsubscribe)
- [mqttPublish](#mqttpublish)
- [mqttDidRing](#mqttdidring)

## Enums Overview

- [WalterModemMqttStatus](#waltermodemmqttstatus)

---

## Methods

### `getMqttStatus`

Returns the last received mqttStatus.

#### Returns

[`WalterModemMqttStatus`](#waltermodemmqttstatus)

---

### `mqttConfig`

Configure an MQTT client.

This function configures an mqtt client, without connecting.

#### Params

| Param          | Description                | Default                  |
| -------------- | -------------------------- | ------------------------ |
| `clientId`     | MQTT client id to be used. | **"walter-mqtt-client"** |
| `username`     | Username for auth.         | **NULL**                 |
| `password`     | Password for auth.         | **NULL**                 |
| `tlsProfileId` | TLS profile id to be used. | **0**                    |

#### Returns

`bool`  
True on success, False otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.mqttConfig("walter-mqtt-test-topic","","",0)) {
    Serial.println("Info: MQTT configured");
} else {
    Serial.println("Error: Failed to configure MQTT");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (modem.mqttConfig("walter-mqtt-test-topic","","",0)) {
    ESP_LOGI("mqtt_docs_demo", "MQTT configured");
} else {
    ESP_LOGE("mqtt_docs_demo", "Failed to configure MQTT");
}

// ...
```

<!-- tabs:end -->

---

### `mqttConnect`

Initialize MQTT and establish connection.

This function initializes the mqtt client on the modem and establishes a connection.

#### Params

| Param        | Description                                                                                            | Default  |
| ------------ | ------------------------------------------------------------------------------------------------------ | -------- |
| `serverName` | MQTT broker hostname.                                                                                  |          |
| `port`       | Port to connect to.                                                                                    |          |
| `keepAlive`  | Maximum time (in seconds) allowed between communications with the broker.                              | **60**   |
| `rsp`        | Pointer to a modem response structure to save the result of the command in. When NULL, result ignored. | **NULL** |
| `cb`         | Optional callback argument. When not NULL, this function returns immediately.                          | **NULL** |
| `args`       | Optional argument to pass to the callback.                                                             | **NULL** |

#### Returns

`bool`  
True on success, False otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.mqttConnect("test.mosquitto.org", 1883)) {
    Serial.println("Info: MQTT connection established");
} else {
    Serial.println("Error: Failed to establish MQTT connection");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (modem.mqttConnect("broker.hivemq.com", 1883)) {
    ESP_LOGI("mqtt_docs_demo", "MQTT connection established");
} else {
    ESP_LOGE("mqtt_docs_demo", "Failed to establish MQTT connection");
}

// ...
```

<!-- tabs:end -->

---

### `mqttDisconnect`

Disconnect an MQTT connection.

This function disconnects the mqtt client connection to the broker.

#### Params

| Params | Description                                                                                            | Default  |
| ------ | ------------------------------------------------------------------------------------------------------ | -------- |
| `rsp`  | Pointer to a modem response structure to save the result of the command in. When NULL, result ignored. | **NULL** |
| `cb`   | Optional callback argument. When not NULL, this function returns immediately.                          | **NULL** |
| `args` | Optional argument to pass to the callback.                                                             | **NULL** |

#### Returns

`bool`  
True on success, False otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.mqttDisconnect()) {
    Serial.println("Info: MQTT connection disconnected");
} else {
    Serial.println("Error: Failed to disconnect MQTT connection");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (modem.mqttDisconnect()) {
    ESP_LOGI("mqtt_docs_demo", "MQTT connection disconnected");
} else {
    ESP_LOGE("mqtt_docs_demo", "Failed to disconnect MQTT connection");
}

// ...
```

<!-- tabs:end -->

---

### `mqttSubscribe`

Subscribe to a MQTT topic

This function subscribes to a given topic using the connection established
earlier through [mqttConnect](#mqttconnect).

#### Params

| Param         | Description                                                                                            | Default  |
| ------------- | ------------------------------------------------------------------------------------------------------ | -------- |
| `topicString` | Topic to publish on.                                                                                   |          |
| `qos`         | QoS: 0 = at most once, 1 = at least once, 2 = exactly once received.                                   | **1**    |
| `rsp`         | Pointer to a modem response structure to save the result of the command in. When NULL, result ignored. | **NULL** |
| `cb`          | Optional callback argument. When not NULL, this function returns immediately.                          | **NULL** |
| `args`        | Optional argument to pass to the callback.                                                             | **NULL** |

#### Returns

`bool`  
True on success, False otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.mqttSubscribe("walter-mqtt-test-topic")) {
    Serial.println("Info: Subscribed to MQQT topic successfully");
} else {
    Serial.println("Error: Failed to subscribe to MQTT topic");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (modem.mqttSubscribe("walter-mqtt-test-topic")) {
    ESP_LOGI("mqtt_docs_demo", "Subscribed to MQTT topic successfully");
} else {
    ESP_LOGE("mqtt_docs_demo", "Failed to subscribe to MQTT topic");
}

// ...
```

<!-- tabs:end -->

---

### `mqttPublish`

Publish something through mqtt.

This function publishes the passed data on the given mqtt topic using the
connection established earlier through [mqttConnect](#mqttconnect).

#### Params

| Param         | Description                                                                                            | Default  |
| ------------- | ------------------------------------------------------------------------------------------------------ | -------- |
| `topicString` | Topic to publish on.                                                                                   |          |
| `data`        | Data to be published.                                                                                  |          |
| `dataSize`    | Size of the data block.                                                                                |          |
| `qos`         | QoS: 0 = at most once, 1 = at least once, 2 = exactly once received.                                   | **1**    |
| `rsp`         | Pointer to a modem response structure to save the result of the command in. When NULL, result ignored. | **NULL** |
| `cb`          | Optional callback argument. When not NULL, this function returns immediately.                          | **NULL** |
| `args`        | Optional argument to pass to the callback.                                                             | **NULL** |

#### Returns

`bool`  
True on success, False otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

static char outgoingMsg[] = "Example Message";

if (modem.mqttPublish("waltertopic", (uint8_t *)outgoingMsg, sizeof(outgoingMsg) - 1)) {
    Serial.print("Info: Published: ");
    Serial.print(outgoingMsg);
    Serial.println(" on topic waltertopic");
} else {
    Serial.println("Error: Failed to perform MQTT publish");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

static char outgoingMsg[] = "Example Message";

if (modem.mqttPublish("waltertopic", (uint8_t *)outgoingMsg, sizeof(outgoingMsg) - 1)) {
    ESP_LOGI("mqtt_docs_demo", "Published: %s on topic waltertopic", outgoingMsg);
} else {
    ESP_LOGE("mqtt_docs_demo", "Failed to perform MQTT publish");
}

// ...
```

<!-- tabs:end -->

---

### `mqttDidRing`

Poll if there were incoming MQTT messages.

Poll if the modem has reported any incoming MQTT messages
on the topics we are subscribed on.

> [!WARNING]
> No more than 1 message with QoS 0 is stored in the buffer,
> every new message with QoS 0 overwrites the previous.

#### Params

| Param           | Description                                                                                            | Default  |
| --------------- | ------------------------------------------------------------------------------------------------------ | -------- |
| `topic`         | Topic to poll.                                                                                         |          |
| `targetBuf`     | Target buffer to write incoming MQTT data in;                                                          |          |
| `targetBufSize` | Size of the target buffer.                                                                             |          |
| `rsp`           | Pointer to a modem response structure to save the result of the command in. When NULL, result ignored. | **NULL** |

#### Returns

`bool`  
True on success, False
if no message(s) arrived, error or if no message(s) are expected *(eg no ring received)*.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

uint8_t incomingBuf[256] = {0};

while (modem.mqttDidRing("walter-mqtt-test-topic", incomingBuf, sizeof(incomingBuf), &rsp)) {
    Serial.print("Info: Incoming: qos=");
    Serial.print(rsp.data.mqttResponse.qos);
    Serial.print(" msgid=");
    Serial.print(rsp.data.mqttResponse.messageId);
    Serial.print(" len=");
    Serial.print(rsp.data.mqttResponse.length);
    Serial.println(":");

    incomingBuf[rsp.data.mqttResponse.length] = '\0';    
    Serial.println((char*)incomingBuf);
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

uint8_t incomingBuf[256] = {0};

while (modem.mqttDidRing("walter-mqtt-test-topic", incomingBuf, sizeof(incomingBuf), &rsp)) {
    ESP_LOGI(
        "mqtt_docs_demo",
        "incoming: qos=%d msgid=%d len=%d:",
        rsp.data.mqttResponse.qos,
        rsp.data.mqttResponse.messageId,
        rsp.data.mqttResponse.length);
    incomingBuf[rsp.data.mqttResponse.length] = '\0';
    ESP_LOGI(TAG, "%s", incomingBuf);
}

// ...
```

<!-- tabs:end -->

---

## Enums

### `WalterModemMqttStatus`

Enum containing the MQTT response codes.

> **WALTER_MODEM_MQTT_SUCCESS** = `0`  
> **WALTER_MODEM_MQTT_NOMEM** = `-1`  
> **WALTER_MODEM_MQTT_PROTOCOL** = `-2`  
> **WALTER_MODEM_MQTT_INVAL** = `-3`  
> **WALTER_MODEM_MQTT_NO_CONN** = `-4`  
> **WALTER_MODEM_MQTT_CONN_REFUSED** = `-5`  
> **WALTER_MODEM_MQTT_NOT_FOUND** = `-6`  
> **WALTER_MODEM_MQTT_CONN_LOST** = `-7`  
> **WALTER_MODEM_MQTT_TLS** = `-8`  
> **WALTER_MODEM_MQTT_PAYLOAD_SIZE** = `-9`  
> **WALTER_MODEM_MQTT_NOT_SUPPORTED** = `-10`  
> **WALTER_MODEM_MQTT_AUTH** = `-11`  
> **WALTER_MODEM_MQTT_ACL_DENIED** = `-12`  
> **WALTER_MODEM_MQTT_UNKNOWN** = `-13`  
> **WALTER_MODEM_MQTT_ERRNO** = `-14`  
> **WALTER_MODEM_MQTT_EAI** = `-15`  
> **WALTER_MODEM_MQTT_PROXY** = `-16`  
> **WALTER_MODEM_MQTT_UNAVAILABLE** = `-17`  
