# MQTT

## Methods Overview

- [mqttConnect](#mqttconnect)
- [mqttSubscribe](#mqttsubscribe)
- [mqttPublish](#mqttpublish)
- [mqttDidRing](#mqttdidring)

---

## Methods

### `mqttConnect`

Initialize MQTT and establish a connection.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
if(modem.mqttConnect("test.mosquitto.org", 8883, macString, "user", "pass", 1)) {
    Serial.println("mqtt: connection succeeded");
} else {
    Serial.println("mqtt: connection failed");
}
```

##### **ESP-IDF**

```cpp
if(modem.mqttConnect("test.mosquitto.org", 8883, macString, "user", "pass", 1)) {
    ESP_LOGI("mqtt", "connection succeeded");
} else {
    ESP_LOGI("mqtt", "connection failed");
}
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

| Param          | Description                                                                                            | Default                  |
| -------------- | ------------------------------------------------------------------------------------------------------ | ------------------------ |
| `serverName`   | MQTT broker hostname.                                                                                  |                          |
| `port`         | Port to connect to.                                                                                    |                          |
| `clientId`     | Client ID string to be used.                                                                           | **"walter-mqtt-client"** |
| `userName`     | Username.                                                                                              | **""**                   |
| `password`     | Password.                                                                                              | **""**                   |
| `tlsProfileId` | TLS profile ID to be used *(default 0 = plaintext)*.                                                   | **0**                    |
| `rsp`          | Pointer to a modem response structure to save the result of the command in. When NULL, result ignored. | **NULL**                 |
| `cb`           | Optional callback argument. When not NULL, this function returns immediately.                          | **NULL**                 |
| `args`         | Optional argument to pass to the callback.                                                             | **NULL**                 |

##### **ESP-IDF**

| Param          | Description                                                                                            | Default                  |
| -------------- | ------------------------------------------------------------------------------------------------------ | ------------------------ |
| `serverName`   | MQTT broker hostname.                                                                                  |                          |
| `port`         | Port to connect to.                                                                                    |                          |
| `clientId`     | Client ID string to be used.                                                                           | **"walter-mqtt-client"** |
| `userName`     | Username.                                                                                              | **""**                   |
| `password`     | Password.                                                                                              | **""**                   |
| `tlsProfileId` | TLS profile ID to be used *(default 0 = plaintext)*.                                                   | **0**                    |
| `rsp`          | Pointer to a modem response structure to save the result of the command in. When NULL, result ignored. | **NULL**                 |
| `cb`           | Optional callback argument. When not NULL, this function returns immediately.                          | **NULL**                 |
| `args`         | Optional argument to pass to the callback.                                                             | **NULL**                 |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

### `mqttSubscribe`

Subscribe to a MQTT topic

This function subscribes to a given topic using the connection established
earlier through [mqttConnect](#mqttconnect).

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
if(modem.mqttSubscribe("waltertopic")) {
    Serial.println("mqtt: subscribed to topic waltertopic");
} else {
    Serial.println("mqtt: subscribe failed");
}
```

##### **ESP-IDF**

```cpp
if(modem.mqttSubscribe("waltertopic")) {
    ESP_LOGI("mqtt", "subscribed to topic waltertopic");
} else {
    ESP_LOGI("mqtt", "subscribe failed");
}
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

| Param         | Description                                                                                            | Default  |
| ------------- | ------------------------------------------------------------------------------------------------------ | -------- |
| `topicString` | Topic to publish on.                                                                                   |          |
| `qos`         | QoS: 0 = at most once, 1 = at least once, 2 = exactly once received.                                   | **1**    |
| `rsp`         | Pointer to a modem response structure to save the result of the command in. When NULL, result ignored. | **NULL** |
| `cb`          | Optional callback argument. When not NULL, this function returns immediately.                          | **NULL** |
| `args`        | Optional argument to pass to the callback.                                                             | **NULL** |

##### **ESP-IDF**

| Param         | Description                                                                                            | Default  |
| ------------- | ------------------------------------------------------------------------------------------------------ | -------- |
| `topicString` | Topic to publish on.                                                                                   |          |
| `qos`         | QoS: 0 = at most once, 1 = at least once, 2 = exactly once received.                                   | **1**    |
| `rsp`         | Pointer to a modem response structure to save the result of the command in. When NULL, result ignored. | **NULL** |
| `cb`          | Optional callback argument. When not NULL, this function returns immediately.                          | **NULL** |
| `args`        | Optional argument to pass to the callback.                                                             | **NULL** |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

### `mqttPublish`

Publish something through mqtt.

This function publishes the passed data on the given mqtt topic using the
connection established earlier through [mqttConnect](#mqttconnect).

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
static char outgoingMsg[64];

if(modem.mqttPublish("waltertopic", (uint8_t *) outgoingMsg, strlen(outgoingMsg))) {
  Serial.printf("mqtt: published: %s, on topic waltertopic \r\n", outgoingMsg);
} else {
  Serial.println("mqtt: publish failed");
}
```

##### **ESP-IDF**

```cpp
static char outgoingMsg[64];

if(modem.mqttPublish("waltertopic", (uint8_t *) outgoingMsg, strlen(outgoingMsg))) {
  ESP_LOGI("mqtt_test", "published: %s on topic waltertopic", outgoingMsg);
} else {
  ESP_LOGI("mqtt_test", "MQTT publish failed");
}
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

| Param         | Description                                                                                            | Default  |
| ------------- | ------------------------------------------------------------------------------------------------------ | -------- |
| `topicString` | Topic to publish on.                                                                                   |          |
| `data`        | Data to be published.                                                                                  |          |
| `dataSize`    | Size of the data block.                                                                                |          |
| `qos`         | QoS: 0 = at most once, 1 = at least once, 2 = exactly once received.                                   | **1**    |
| `rsp`         | Pointer to a modem response structure to save the result of the command in. When NULL, result ignored. | **NULL** |
| `cb`          | Optional callback argument. When not NULL, this function returns immediately.                          | **NULL** |
| `args`        | Optional argument to pass to the callback.                                                             | **NULL** |

##### **ESP-IDF**

| Param         | Description                                                                                            | Default  |
| ------------- | ------------------------------------------------------------------------------------------------------ | -------- |
| `topicString` | Topic to publish on.                                                                                   |          |
| `data`        | Data to be published.                                                                                  |          |
| `dataSize`    | Size of the data block.                                                                                |          |
| `qos`         | QoS: 0 = at most once, 1 = at least once, 2 = exactly once received.                                   | **1**    |
| `rsp`         | Pointer to a modem response structure to save the result of the command in. When NULL, result ignored. | **NULL** |
| `cb`          | Optional callback argument. When not NULL, this function returns immediately.                          | **NULL** |
| `args`        | Optional argument to pass to the callback.                                                             | **NULL** |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

### `mqttDidRing`

Poll if there were incoming MQTT messages

Poll if the modem has reported any incoming MQTT messages
on the topics we are subscribed on.

> [!NOTE]
> No more than 1 message with QoS 0 is stored in the buffer,
> every new message with QoS 0 overwrites the previous.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
while (modem.mqttDidRing("waltertopic", incomingBuf, sizeof(incomingBuf), &rsp)) {
    Serial.printf("mqtt: incoming: qos=%d msgid=%d len=%d:\r\n",
        rsp.data.mqttResponse.qos,
        rsp.data.mqttResponse.messageId,
        rsp.data.mqttResponse.length);
    for (int i = 0; i < rsp.data.mqttResponse.length; i++) {
        Serial.printf("mqtt: %c, 0x%02x\r\n", incomingBuf[i], incomingBuf[i]);
    }
}
```

##### **ESP-IDF**

```cpp
while(modem.mqttDidRing("waltertopic", incomingBuf, sizeof(incomingBuf), &rsp)) {
    ESP_LOGI("mqtt", "incoming: qos=%d msgid=%d len=%d:",
        rsp.data.mqttResponse.qos,
        rsp.data.mqttResponse.messageId,
        rsp.data.mqttResponse.length);
    for(int i = 0; i < rsp.data.mqttResponse.length; i++) {
        ESP_LOGI("mqtt:", "%c, 0x%02x", incomingBuf[i], incomingBuf[i]);
    }
}
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

| Param           | Description                                                                                            | Default  |
| --------------- | ------------------------------------------------------------------------------------------------------ | -------- |
| `topic`         | Topic to poll.                                                                                         |          |
| `targetBuf`     | Target buffer to write incoming MQTT data in;                                                          |          |
| `targetBufSize` | Size of the target buffer.                                                                             |          |
| `rsp`           | Pointer to a modem response structure to save the result of the command in. When NULL, result ignored. | **NULL** |

##### **ESP-IDF**

| Param           | Description                                                                                            | Default  |
| --------------- | ------------------------------------------------------------------------------------------------------ | -------- |
| `topic`         | Topic to poll.                                                                                         |          |
| `targetBuf`     | Target buffer to write incoming MQTT data in;                                                          |          |
| `targetBufSize` | Size of the target buffer.                                                                             |          |
| `rsp`           | Pointer to a modem response structure to save the result of the command in. When NULL, result ignored. | **NULL** |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False
if no message(s) arrived, error or if no message(s) are expected *(eg no ring received)*.
