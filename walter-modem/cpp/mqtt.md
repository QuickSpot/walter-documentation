# mqtt
## methods overview
- [mqttConnect](#mqttconnect)
- [mqttSubscribe](#mqttSubscribe)
- [mqttPublish]()
- [mqttDidRing]()

## enums overview

## methods
### `mqttConnect`
> Initialize MQTT and establish connection in one call.
>
> This function initializes the mqtt client on the modem and establishes a connection.

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
#### **Arduino / ESP-IDF**
| Param          | Description                                                                                           | Default                |
| -------------- | ----------------------------------------------------------------------------------------------------- | ---------------------- |
| `serverName`   | MQTT broker hostname                                                                                  | **None**               |
| `port`         | Port to connect to                                                                                    | **None**               |
| `clientId`     | Client ID string to be used                                                                           | `"walter-mqtt-client"` |
| `userName`     | Username                                                                                              | `""`                   |
| `password`     | Password                                                                                              | `""`                   |
| `tlsProfileId` | TLS profile ID to be used (default 0 = plaintext)                                                     | `0`                    |
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
> Subscribe to a mqtt topic
>
> This function subscribes to a given topic using the connection established earlier through [mqttConnect](#mqttconnect).

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
#### **Arduino / ESP-IDF**
| Param         | Description                                                                                           | Default  |
| ------------- | ----------------------------------------------------------------------------------------------------- | -------- |
| `topicString` | Topic to publish on                                                                                   | **None** |
| `qos`         | QoS: 0 = at most once, 1 = at least once, 2 = exactly once received                                   | `1`      |
| `rsp`         | Pointer to a modem response structure to save the result of the command in. When NULL, result ignored | **NULL** |
| `cb`          | Optional callback argument. When not NULL, this function returns immediately                          | **NULL** |
| `args`        | Optional argument to pass to the callback                                                             | **NULL** |

#### **Micropython**

<!-- tabs:end -->

### Returns:
`bool`
True on success, false otherwise.

---

