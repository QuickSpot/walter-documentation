# MQTT

## Methods Overview

- [mqttConnect](#mqttconnect)
- [mqttSubscribe](#mqttsubscribe)
- [mqttPublish](#mqttpublish)
- [mqttDidRing](#mqttdidring)

---

## Methods

### `mqttConfig`

Configure the MQTT client without connecting.

#### Example

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

```py
MQTT_USERNAME = ''
MQTT_PASSWORD = ''
TLS_PROFILE_ID = 1

if await modem.mqtt_config(
    user_name=MQTT_USERNAME,
    password=MQTT_PASSWORD,
    tls_profile_id=TLS_PROFILE_ID
):
    print('Successfully configured MQTT')
else:
    print('Could not configure MQTT')
```
<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

| Param                    | Description                                         | Default    |
| ------------------------ | --------------------------------------------------- | ---------- |
| `client_id`              | MQTT client ID to use.                              | device MAC |
| `user_name`              | Optional username for authentication.               | **""**     |
| `password`               | Optional password for authentication.               | **""**     |
| `tls_profile_id`         | Optional TLS profile ID to use.                     | **None**   |
| `library_message_buffer` | Size of the library's internal MQTT message buffer. | **16**     |
| `rsp`                    | Reference to a modem response instance.             | **None**   |

> [!warning]
> The **library_message_bugger** stores metadata for received messages
> but does not hold their payloads. \
> The modem itself supports up to 100 messages, however,
> significantly increasing this buffer may consume excessive memory
> and is not recommended

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

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

##### **Micropython**

```py
if await modem.mqtt_connect(
    server_name='test.mosquitto.org',
    port=1883
):
    print('MQTT connection successfull')
else:
    print('MQTT connection failed')
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

##### **Micropython**

| Param         | Description                            | Default |
| ------------- | -------------------------------------- | ------- |
| `server_name` | MQTT broker hostname.                  |         |
| `port`        | Port to connect to.                    |         |
| `keep_alive`  | Maximum keepalive time *(in seconds)*. | 60      |

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

##### **Micropython**

```py
if await modem.mqtt_subscribe(

):
    print('subscribed to topic waltertopic')
else:
    print('subscribe failed')
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

##### **Micropython**

| Param   | Description                                                          | Default  |
| ------- | -------------------------------------------------------------------- | -------- |
| `topic` | Topic to subscribe to.                                               |          |
| `qos`   | QoS: 0 = at most once, 1 = at least once, 2 = exactly once received. | **1**    |
| `rsp`   | Reference to a modem response instance.                              | **None** |

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

##### **Micropython**

```py
if await modem.mqtt_publish(
    topic=topic,
    data='Hello from Walter'
):
    print('Message Published')
else:
    print('Failed to publish message')
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

##### **Micropython**

| Param   | Description                                                          | Default  |
| ------- | -------------------------------------------------------------------- | -------- |
| `topic` | Topic to publish on.                                                 |          |
| `qos`   | QoS: 0 = at most once, 1 = at least once, 2 = exactly once received. | **1**    |
| `rsp`   | Reference to a modem response instance.                              | **None** |

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

##### **Micropython**

```py
modem_rsp = ModemRsp()
mqtt_messages = []

if await modem.mqtt_did_ring(msg_list=mqtt_messages, rsp=modem_rsp):
    print(f'New MQTT message (topic: {modem_rsp.mqtt_response.topic}, qos: {modem_rsp.mqtt_response.qos})')
    print(mqtt_messages.pop())
else:
    if modem_rsp.result != WalterModemState.NO_DATA:
        print('Fault with mqtt_did_ring: '
              f'{WalterModemState.get_value_name(modem_rsp.result)}')
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

##### **Micropython**

| Param      | Description                                                 | Default  |
| ---------- | ----------------------------------------------------------- | -------- |
| `msg_list` | Refence to a list where the received messages will be put.  |          |
| `topic`    | The exact topic to filter on, leave as None for all topics. | **None** |
| `rsp`      | Reference to a modem response instance.                     | **None** |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False
if no message(s) arrived, error or if no message(s) are expected *(eg no ring received)*.
