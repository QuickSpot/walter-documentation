# MQTT

## Methods Overview

- [mqttConnect](#mqttconnect)
- [mqttSubscribe](#mqttsubscribe)
- [mqttPublish](#mqttpublish)
- [mqttDidRing](#mqttdidring)

---

## Methods

### `mqttConnect`

Initialize MQTT and establish connection in one call.

This function initializes the mqtt client on the modem
and establishes a connection.

<!-- tabs:start -->

#### **Arduino**

```cpp
if(modem.mqttConnect("test.mosquitto.org", 8883, macString, "user", "pass", 1)) {
    Serial.println("mqtt: connection succeeded");
} else {
    Serial.println("mqtt: connection failed");
}
```

#### **ESP-IDF**

```cpp
if(modem.mqttConnect("test.mosquitto.org", 8883, macString, "user", "pass", 1)) {
    ESP_LOGI("mqtt", "connection succeeded");
} else {
    ESP_LOGI("mqtt", "connection failed");
}
```

#### **Micropython**

<!-- tabs:end -->

### params:

<!-- tabs:start -->

#### **Arduino**

| Param          | Description                                                                                           | Default                  |
| -------------- | ----------------------------------------------------------------------------------------------------- | ------------------------ |
| `serverName`   | MQTT broker hostname                                                                                  | **None**                 |
| `port`         | Port to connect to                                                                                    | **None**                 |
| `clientId`     | Client ID string to be used                                                                           | **"walter-mqtt-client"** |
| `userName`     | Username                                                                                              | **""**                   |
| `password`     | Password                                                                                              | **""**                   |
| `tlsProfileId` | TLS profile ID to be used (default 0 = plaintext)                                                     | **0**                    |
| `rsp`          | Pointer to a modem response structure to save the result of the command in. When NULL, result ignored | **NULL**                 |
| `cb`           | Optional callback argument. When not NULL, this function returns immediately                          | **NULL**                 |
| `args`         | Optional argument to pass to the callback                                                             | **NULL**                 |

#### **ESP-IDF**

| Param          | Description                                                                                           | Default                |
| -------------- | ----------------------------------------------------------------------------------------------------- | ---------------------- |
| `serverName`   | MQTT broker hostname                                                                                  | **None**               |
| `port`         | Port to connect to                                                                                    | **None**               |
| `clientId`     | Client ID string to be used                                                                           | **"walter-mqtt-client"**|
| `userName`     | Username                                                                                              | **""**                 |
| `password`     | Password                                                                                              | **""**                 |
| `tlsProfileId` | TLS profile ID to be used (default 0 = plaintext)                                                     | **0**                  |
| `rsp`          | Pointer to a modem response structure to save the result of the command in. When NULL, result ignored | **NULL**               |
| `cb`           | Optional callback argument. When not NULL, this function returns immediately                          | **NULL**               |
| `args`         | Optional argument to pass to the callback                                                             | **NULL**               |

#### **Micropython**

<!-- tabs:end -->

### Returns:

`bool`
True on success, false otherwise.

---

### `mqttSubscribe`

Subscribe to a mqtt topic

This function subscribes to a given topic using the connection established
earlier through [mqttConnect](#mqttconnect).

<!-- tabs:start -->

#### **Arduino**

```cpp
if(modem.mqttSubscribe("waltertopic")) {
    Serial.println("mqtt: subscribed to topic 'waltertopic'");
} else {
    Serial.println("mqtt: subscribe failed");
}
```

#### **ESP-IDF**

```cpp
if(modem.mqttSubscribe("waltertopic")) {
    ESP_LOGI("mqtt", "subscribed to topic 'waltertopic'");
} else {
    ESP_LOGI("mqtt", "subscribe failed");
}
```

#### **Micropython**

<!-- tabs:end -->

### params:

<!-- tabs:start -->

#### **Arduino**

| Param         | Description                                                                                           | Default  |
| ------------- | ----------------------------------------------------------------------------------------------------- | -------- |
| `topicString` | Topic to publish on                                                                                   | **None** |
| `qos`         | QoS: 0 = at most once, 1 = at least once, 2 = exactly once received                                   | **1**    |
| `rsp`         | Pointer to a modem response structure to save the result of the command in. When NULL, result ignored | **NULL** |
| `cb`          | Optional callback argument. When not NULL, this function returns immediately                          | **NULL** |
| `args`        | Optional argument to pass to the callback                                                             | **NULL** |

#### **ESP-IDF**

| Param         | Description                                                                                           | Default  |
| ------------- | ----------------------------------------------------------------------------------------------------- | -------- |
| `topicString` | Topic to publish on                                                                                   | **None** |
| `qos`         | QoS: 0 = at most once, 1 = at least once, 2 = exactly once received                                   | **1**      |
| `rsp`         | Pointer to a modem response structure to save the result of the command in. When NULL, result ignored | **NULL** |
| `cb`          | Optional callback argument. When not NULL, this function returns immediately                          | **NULL** |
| `args`        | Optional argument to pass to the callback                                                             | **NULL** |

#### **Micropython**

<!-- tabs:end -->

### Returns:

`bool`
True on success, false otherwise.

---

### `mqttPublish`

Publish something through mqtt.

This function publishes the passed data on the given mqtt topic using the
connection established earlier through [mqttConnect](#mqttconnect).

<!-- tabs:start -->

#### **Arduino**

```cpp
static char outgoingMsg[64];

if(modem.mqttPublish("waltertopic", (uint8_t *) outgoingMsg, strlen(outgoingMsg))) {
  Serial.printf("mqtt: published '%s' on topic 'waltertopic' \r\n", outgoingMsg);
} else {
  Serial.println("mqtt: publish failed");
}
```

#### **ESP-IDF**

```cpp
static char outgoingMsg[64];

if(modem.mqttPublish("waltertopic", (uint8_t *) outgoingMsg, strlen(outgoingMsg))) {
  ESP_LOGI("mqtt_test", "published '%s' on topic 'waltertopic'", outgoingMsg);
} else {
  ESP_LOGI("mqtt_test", "MQTT publish failed");
}
```

#### **Micropython**

<!-- tabs:end -->

### params:

<!-- tabs:start -->

#### **Arduino**

| Param         | Description                                                                                           | Default  |
| ------------- | ----------------------------------------------------------------------------------------------------- | -------- |
| `topicString` | Topic to publish on                                                                                   | **None** |
| `data`        | Data to be published                                                                                  | **None** |
| `dataSize`    | Size of the data block                                                                                | **None** |
| `qos`         | QoS: 0 = at most once, 1 = at least once, 2 = exactly once received                                   | **1**    |
| `rsp`         | Pointer to a modem response structure to save the result of the command in. When NULL, result ignored | **NULL** |
| `cb`          | Optional callback argument. When not NULL, this function returns immediately                          | **NULL** |
| `args`        | Optional argument to pass to the callback                                                             | **NULL** |

#### **ESP-IDF**

| Param         | Description                                                                                           | Default  |
| ------------- | ----------------------------------------------------------------------------------------------------- | -------- |
| `topicString` | Topic to publish on                                                                                   | **None** |
| `data`        | Data to be published                                                                                  | **None** |
| `dataSize`    | Size of the data block                                                                                | **None** |
| `qos`         | QoS: 0 = at most once, 1 = at least once, 2 = exactly once received                                   | **1**    |
| `rsp`         | Pointer to a modem response structure to save the result of the command in. When NULL, result ignored | **NULL** |
| `cb`          | Optional callback argument. When not NULL, this function returns immediately                          | **NULL** |
| `args`        | Optional argument to pass to the callback                                                             | **NULL** |

#### **Micropython**

<!-- tabs:end -->

### Returns:

`bool`
True on success, false otherwise.

---

### `mqttDidRing`

Poll if there were incoming mqtt messages

Poll if the modem has reported any incoming mqtt messages on the topics we are subscribed on.

<!-- tabs:start -->

#### **Arduino**

```cpp
while (modem.mqttDidRing("waltertopic", incomingBuf, sizeof(incomingBuf), &rsp)) {
    Serial.printf("mqtt: incoming: qos=%d msgid=%d len=%d:\r\n",
        rsp.data.mqttResponse.qos,
        rsp.data.mqttResponse.messageId,
        rsp.data.mqttResponse.length);
    for (int i = 0; i < rsp.data.mqttResponse.length; i++) {
        Serial.printf("mqtt: '%c' 0x%02x\r\n", incomingBuf[i], incomingBuf[i]);
    }
}
```

#### **ESP-IDF**

```cpp
while(modem.mqttDidRing("waltertopic", incomingBuf, sizeof(incomingBuf), &rsp)) {
    ESP_LOGI("mqtt", "incoming: qos=%d msgid=%d len=%d:",
        rsp.data.mqttResponse.qos,
        rsp.data.mqttResponse.messageId,
        rsp.data.mqttResponse.length);
    for(int i = 0; i < rsp.data.mqttResponse.length; i++) {
        ESP_LOGI("mqtt", "'%c' 0x%02x", incomingBuf[i], incomingBuf[i]);
    }
}
```

#### **Micropython**

<!-- tabs:end -->

### params:

<!-- tabs:start -->

#### **Arduino**

| Param           | Description                                                                                           | Default  |
| --------------- | ----------------------------------------------------------------------------------------------------- | -------- |
| `topic`         | Topic to poll                                                                                         | **None** |
| `targetBuf`     | Target buffer to write incoming MQTT data in                                                          | **None** |
| `targetBufSize` | Size of the target buffer                                                                             | **None** |
| `rsp`           | Pointer to a modem response structure to save the result of the command in. When NULL, result ignored | **NULL** |

#### **ESP-IDF**

| Param           | Description                                                                                           | Default  |
| --------------- | ----------------------------------------------------------------------------------------------------- | -------- |
| `topic`         | Topic to poll                                                                                         | **None** |
| `targetBuf`     | Target buffer to write incoming MQTT data in                                                          | **None** |
| `targetBufSize` | Size of the target buffer                                                                             | **None** |
| `rsp`           | Pointer to a modem response structure to save the result of the command in. When NULL, result ignored | **NULL** |

#### **Micropython**
<!-- tabs:end -->

### Returns:

`bool`
True on success, false if no message arrived or error or no message expected (eg no ring received).
