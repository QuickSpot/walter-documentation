## Methods Overview

- [mqttConfig](#mqttconfig)
- [mqttConnect](#mqttconnect)
- [mqttDisconnect](#mqttdisconnect)
- [mqttSubscribe](#mqttsubscribe)
- [mqttPublish](#mqttpublish)
- [mqttReceive](#mqttreceive)
- [getMqttStatus](#getmqttstatus) _(deprecated)_
- [mqttDidRing](#mqttdidring) _(deprecated)_

## Enums Overview

- [WMMQTTConnRC](#wmmqttconnrc)

## Structs Overview

- [WalterModemMqttResponse](#waltermodemmqttresponse)

---

## Methods

### `mqttConfig`

Configure an MQTT client.

This function configures an MQTT client, without connecting.

> [!NOTE]
> `username` and `password` are only sent when both are set.

#### Params

| Param            | Description                                                      | Default                  |
| ---------------- | ---------------------------------------------------------------- | ------------------------ |
| `client_id`      | MQTT client id to be used.                                       | **"walter-mqtt-client"** |
| `username`       | Username for auth.                                               | **NULL**                 |
| `password`       | Password for auth.                                               | **NULL**                 |
| `tls_profile_id` | If not 0, TLS is used with the given profile (1-6).              | **0**                    |
| `rsp`            | Optional modem response structure to save the result in.         | **NULL**                 |
| `cb`             | Optional callback function, if set this function will not block. | **NULL**                 |
| `args`           | Optional argument to pass to the callback.                       | **NULL**                 |

#### Returns

`bool`  
True on "OK" response, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.mqttConfig("walter-mqtt-client")) {
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

if (modem.mqttConfig("walter-mqtt-client")) {
    ESP_LOGI("mqtt_docs_demo", "MQTT configured");
} else {
    ESP_LOGE("mqtt_docs_demo", "Failed to configure MQTT");
}

// ...
```

<!-- tabs:end -->

---

### `mqttConnect`

Initialize MQTT and establish a connection.

This function initializes the MQTT client on the modem and establishes a connection
with the settings from [mqttConfig](#mqttconfig).

> [!NOTE]
> The connection result is reported in the `rc` of the `WALTER_MODEM_MQTT_EVENT_CONNECTED` event,
> `WALTER_MODEM_MQTT_SUCCESS` means connected.

#### Params

| Param        | Description                                                               | Default  |
| ------------ | ------------------------------------------------------------------------- | -------- |
| `hostname`   | MQTT broker hostname.                                                     |          |
| `port`       | Port to connect to.                                                       |          |
| `keep_alive` | Maximum time (in seconds) allowed between communications with the broker. | **60**   |
| `rsp`        | Optional modem response structure to save the result in.                  | **NULL** |
| `cb`         | Optional callback function, if set this function will not block.          | **NULL** |
| `args`       | Optional argument to pass to the callback.                                | **NULL** |

#### Returns

`bool`  
True on "OK" response, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.mqttConnect("test.mosquitto.org", 1883)) {
    Serial.println("Info: MQTT connect requested");
} else {
    Serial.println("Error: Failed to start MQTT connection");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (modem.mqttConnect("test.mosquitto.org", 1883)) {
    ESP_LOGI("mqtt_docs_demo", "MQTT connect requested");
} else {
    ESP_LOGE("mqtt_docs_demo", "Failed to start MQTT connection");
}

// ...
```

<!-- tabs:end -->

---

### `mqttDisconnect`

Disconnect an MQTT connection.

This function disconnects the MQTT client connection to the broker.
The result is reported in the `WALTER_MODEM_MQTT_EVENT_DISCONNECTED` event.

#### Params

| Param  | Description                                                      | Default  |
| ------ | ---------------------------------------------------------------- | -------- |
| `rsp`  | Optional modem response structure to save the result in.         | **NULL** |
| `cb`   | Optional callback function, if set this function will not block. | **NULL** |
| `args` | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on "OK" response, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.mqttDisconnect()) {
    Serial.println("Info: MQTT disconnect requested");
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
    ESP_LOGI("mqtt_docs_demo", "MQTT disconnect requested");
} else {
    ESP_LOGE("mqtt_docs_demo", "Failed to disconnect MQTT connection");
}

// ...
```

<!-- tabs:end -->

---

### `mqttSubscribe`

Subscribe to an MQTT topic.

This function subscribes to a given topic using the connection established
earlier through [mqttConnect](#mqttconnect).
The result is reported in the `rc` of the `WALTER_MODEM_MQTT_EVENT_SUBSCRIBED` event.

> [!NOTE]
> At most `WALTER_MODEM_MQTT_MAX_TOPICS` topics (4 by default, set in Kconfig) can be subscribed to.
> When all are in use, this function returns false and sets `rsp.data.mqttResponse.mqttStatus`
> to `WALTER_MODEM_MQTT_UNAVAILABLE`.
> Subscribing to a topic that is already subscribed returns true without sending a command.

#### Params

| Param   | Description                                                          | Default  |
| ------- | -------------------------------------------------------------------- | -------- |
| `topic` | The topic to subscribe to, at most 127 characters.                   |          |
| `qos`   | QoS: 0 = at most once, 1 = at least once, 2 = exactly once received. | **1**    |
| `rsp`   | Optional modem response structure to save the result in.             | **NULL** |
| `cb`    | Optional callback function, if set this function will not block.     | **NULL** |
| `args`  | Optional argument to pass to the callback.                           | **NULL** |

#### Returns

`bool`  
True on "OK" response, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.mqttSubscribe("walter-mqtt-test-topic")) {
    Serial.println("Info: MQTT subscribe requested");
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
    ESP_LOGI("mqtt_docs_demo", "MQTT subscribe requested");
} else {
    ESP_LOGE("mqtt_docs_demo", "Failed to subscribe to MQTT topic");
}

// ...
```

<!-- tabs:end -->

---

### `mqttPublish`

Publish something through MQTT.

This function publishes the passed data on the given MQTT topic using the
connection established earlier through [mqttConnect](#mqttconnect).
The result is reported in the `rc` and `mid` of the `WALTER_MODEM_MQTT_EVENT_PUBLISHED` event.

#### Params

| Param      | Description                                                          | Default  |
| ---------- | -------------------------------------------------------------------- | -------- |
| `topic`    | The topic to publish on.                                             |          |
| `buf`      | Data to be published.                                                |          |
| `buf_size` | Size of the data block.                                              |          |
| `qos`      | QoS: 0 = at most once, 1 = at least once, 2 = exactly once received. | **1**    |
| `rsp`      | Optional modem response structure to save the result in.             | **NULL** |
| `cb`       | Optional callback function, if set this function will not block.     | **NULL** |
| `args`     | Optional argument to pass to the callback.                           | **NULL** |

#### Returns

`bool`  
True on "OK" response, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

static char outgoingMsg[] = "Example Message";

if (modem.mqttPublish("walter-mqtt-test-topic", (uint8_t *)outgoingMsg, sizeof(outgoingMsg) - 1)) {
    Serial.println("Info: MQTT publish requested");
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

if (modem.mqttPublish("walter-mqtt-test-topic", (uint8_t *)outgoingMsg, sizeof(outgoingMsg) - 1)) {
    ESP_LOGI("mqtt_docs_demo", "MQTT publish requested");
} else {
    ESP_LOGE("mqtt_docs_demo", "Failed to perform MQTT publish");
}

// ...
```

<!-- tabs:end -->

---

### `mqttReceive`

Receive MQTT data from the modem buffer.

This function reads an incoming message for a specific topic.
Call it after a `WALTER_MODEM_MQTT_EVENT_MESSAGE` event, which reports the topic,
length (`msg_length`), QoS and message id (`mid`) of the message.

> [!WARNING]
> The modem's response carries no length, so exactly `buf_size` bytes are read.
> Pass the `msg_length` reported by the `WALTER_MODEM_MQTT_EVENT_MESSAGE` event.
> A larger value makes the command wait until it times out.

> [!NOTE]
> The modem keeps no more than 1 message with QoS 0 per topic,
> every new message with QoS 0 overwrites the previous one.

#### Params

| Param        | Description                                                                                 | Default  |
| ------------ | ------------------------------------------------------------------------------------------- | -------- |
| `topic`      | The topic to receive data from.                                                             |          |
| `message_id` | The `mid` from the message event. 0 receives the QoS 0 message.                             |          |
| `buf`        | User buffer to store the received data. The data is not null-terminated.                    |          |
| `buf_size`   | The `msg_length` from the message event (1-4096). `buf` must hold at least this many bytes. |          |
| `rsp`        | Optional modem response structure to save the result in.                                    | **NULL** |
| `cb`         | Optional callback function, if set this function will not block.                            | **NULL** |
| `args`       | Optional argument to pass to the callback.                                                  | **NULL** |

#### Returns

`bool`  
True on "OK" response, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

static uint8_t inBuf[1024];

void myMQTTEventHandler(WMMQTTEventType event, const WMMQTTEventData *data, void *args)
{
    if (event != WALTER_MODEM_MQTT_EVENT_MESSAGE) {
        return;
    }

    if (data->msg_length > sizeof(inBuf)) {
        Serial.printf("Error: MQTT message of %u bytes does not fit\r\n", data->msg_length);
        return;
    }

    if (modem.mqttReceive(data->topic, data->mid, inBuf, data->msg_length)) {
        Serial.printf("Info: Message on %s (qos %u, %u bytes): %.*s\r\n",
                      data->topic, data->qos, data->msg_length,
                      data->msg_length, (const char *)inBuf);
    } else {
        Serial.println("Error: Failed to receive the MQTT message");
    }
}

// ...

modem.setMQTTEventHandler(myMQTTEventHandler);

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

static uint8_t inBuf[1024];

void myMQTTEventHandler(WMMQTTEventType event, const WMMQTTEventData *data, void *args)
{
    if (event != WALTER_MODEM_MQTT_EVENT_MESSAGE) {
        return;
    }

    if (data->msg_length > sizeof(inBuf)) {
        ESP_LOGE("mqtt_docs_demo", "MQTT message of %u bytes does not fit", data->msg_length);
        return;
    }

    if (modem.mqttReceive(data->topic, data->mid, inBuf, data->msg_length)) {
        ESP_LOGI("mqtt_docs_demo", "Message on %s (qos %u, %u bytes): %.*s",
                 data->topic, data->qos, data->msg_length,
                 data->msg_length, (const char *)inBuf);
    } else {
        ESP_LOGE("mqtt_docs_demo", "Failed to receive the MQTT message");
    }
}

// ...

modem.setMQTTEventHandler(myMQTTEventHandler);

// ...
```

<!-- tabs:end -->

---

### `getMqttStatus`

> [!WARNING]
> **DEPRECATED:** This method will be removed in a future release.
> Use the `rc` of the MQTT events instead, see
> [setMQTTEventHandler](/walter-modem/arduino_esp-idf/reference/event_handlers.md#setmqtteventhandler).

Returns the last received MQTT status.

#### Returns

[`WMMQTTConnRC`](#wmmqttconnrc)  
The status code of the last MQTT connect, disconnect, subscribe or publish result.

---

### `mqttDidRing`

> [!WARNING]
> **DEPRECATED:** This method will be removed in a future release.
> Use [mqttReceive](#mqttreceive) instead.

Receive data from an incoming MQTT message.

This method calls [mqttReceive](#mqttreceive) with message id 0,
so it can only receive QoS 0 messages.
`targetBufSize` must be the `msg_length` reported by the `WALTER_MODEM_MQTT_EVENT_MESSAGE` event.

#### Params

| Param           | Description                                                                              | Default  |
| --------------- | ---------------------------------------------------------------------------------------- | -------- |
| `topic`         | The topic to receive data from.                                                          |          |
| `targetBuf`     | User buffer to store the received data. The data is not null-terminated.                 |          |
| `targetBufSize` | The `msg_length` from the message event. `targetBuf` must hold at least this many bytes. |          |
| `rsp`           | Optional modem response structure to save the result in.                                 | **NULL** |

#### Returns

`bool`  
True on "OK" response, false otherwise.

---

## Enums

### `WMMQTTConnRC`

The MQTT result codes, reported in the `rc` of the MQTT events.

> **WALTER_MODEM_MQTT_SUCCESS** = `0`  
> The operation succeeded.  
> **WALTER_MODEM_MQTT_NOMEM** = `-1`  
> Out of memory.  
> **WALTER_MODEM_MQTT_PROTOCOL** = `-2`  
> MQTT protocol error.  
> **WALTER_MODEM_MQTT_INVAL** = `-3`  
> Invalid parameters.  
> **WALTER_MODEM_MQTT_NO_CONN** = `-4`  
> Not connected to a broker.  
> **WALTER_MODEM_MQTT_CONN_REFUSED** = `-5`  
> The broker refused the connection.  
> **WALTER_MODEM_MQTT_NOT_FOUND** = `-6`  
> Not found.  
> **WALTER_MODEM_MQTT_CONN_LOST** = `-7`  
> The connection to the broker was lost.  
> **WALTER_MODEM_MQTT_TLS** = `-8`  
> TLS error.  
> **WALTER_MODEM_MQTT_PAYLOAD_SIZE** = `-9`  
> The payload is too large.  
> **WALTER_MODEM_MQTT_NOT_SUPPORTED** = `-10`  
> Not supported.  
> **WALTER_MODEM_MQTT_AUTH** = `-11`  
> Authentication failed.  
> **WALTER_MODEM_MQTT_ACL_DENIED** = `-12`  
> Access denied by the broker's access control list.  
> **WALTER_MODEM_MQTT_UNKNOWN** = `-13`  
> Unknown error.  
> **WALTER_MODEM_MQTT_ERRNO** = `-14`  
> System error.  
> **WALTER_MODEM_MQTT_EAI** = `-15`  
> DNS lookup of the broker failed.  
> **WALTER_MODEM_MQTT_PROXY** = `-16`  
> Proxy error.  
> **WALTER_MODEM_MQTT_UNAVAILABLE** = `-17`  
> Unavailable. Also set by [mqttSubscribe](#mqttsubscribe) when all subscription slots are in use.

---

## Structs

### `WalterModemMqttResponse`

The MQTT response data in `rsp.data.mqttResponse`.

> [!WARNING]
> The library does not fill in `messageId`, `qos` and `length`, they are not valid after
> [mqttReceive](#mqttreceive). The details of an incoming message are reported in the
> `WALTER_MODEM_MQTT_EVENT_MESSAGE` event
> ([WMMQTTEventData](/walter-modem/arduino_esp-idf/reference/event_handlers.md#wmmqtteventdata)).
> `mqttStatus` is only set by [mqttSubscribe](#mqttsubscribe) when all subscription slots are in use.

| Field        | Type                          | Description                |
| ------------ | ----------------------------- | -------------------------- |
| `messageId`  | `uint16_t`                    | The message ID.            |
| `qos`        | `uint8_t`                     | The QoS level.             |
| `length`     | `uint16_t`                    | The length of the message. |
| `mqttStatus` | [WMMQTTConnRC](#wmmqttconnrc) | The MQTT status code.      |
