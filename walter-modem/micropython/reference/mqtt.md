# MQTT

## Methods Overview

- [mqtt_config](#mqtt_config)
- [mqtt_connect](#mqtt_connect)
- [mqtt_disconnect](#mqtt_disconnect)
- [mqtt_subscribe](#mqtt_subscribe)
- [mqtt_publish](#mqtt_publish)
- [mqtt_did_ring](#mqtt_did_ring)

---

## Methods

### `mqtt_config`

Configure the MQTT client without connecting.

#### Example

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
#### Params

| Param                    | Description                                         | Default    |
| ------------------------ | --------------------------------------------------- | ---------- |
| `client_id`              | MQTT client ID to use.                              | device MAC |
| `user_name`              | Optional username for authentication.               | **""**     |
| `password`               | Optional password for authentication.               | **""**     |
| `tls_profile_id`         | Optional TLS profile ID to use.                     | **None**   |
| `library_message_buffer` | Size of the library's internal MQTT message buffer. | **16**     |
| `rsp`                    | Reference to a modem response instance.             | **None**   |

> [!WARNING]
> The **library_message_bugger** stores metadata for received messages
> but does not hold their payloads. \
> The modem itself supports up to 100 messages, however,
> significantly increasing this buffer may consume excessive memory
> and is not recommended

#### Returns

`bool`
True on success, False otherwise.

---

### `mqtt_connect`

Initialise MQTT and establish a connection.

#### Example

```py
if await modem.mqtt_connect(
    server_name='test.mosquitto.org',
    port=1883
):
    print('MQTT connection successfull')
else:
    print('MQTT connection failed')
```

#### Params

| Param         | Description                             | Default  |
| ------------- | --------------------------------------- | -------- |
| `server_name` | MQTT broker hostname.                   |          |
| `port`        | Port to connect to.                     |          |
| `keep_alive`  | Maximum keepalive time *(in seconds)*.  | 60       |
| `rsp`         | Reference to a modem response instance. | **None** |

#### Returns

`bool`
True on success, False otherwise.

---

### `mqtt_disconnect`

Disconnect from an MQTT broker.

#### Example

```py
await modem.mqtt_disconnect()
```

#### Params

| Param | Description                             | Default  |
| ----- | --------------------------------------- | -------- |
| `rsp` | Reference to a modem response instance. | **None** |

#### Returns

`bool`
True on success, False otherwise.

---

### `mqtt_subscribe`

Subscribe to a MQTT topic.

This function subscribes to a given topic using the connection established
earlier through [`mqtt_connect`](#mqtt_connect).

#### Example

```py
if await modem.mqtt_subscribe(

):
    print('subscribed to topic waltertopic')
else:
    print('subscribe failed')
```

#### Params

| Param   | Description                                                              | Default  |
| ------- | ------------------------------------------------------------------------ | -------- |
| `topic` | Topic to subscribe to.                                                   |          |
| `qos`   | Quality of Service (0: at least once, 1: at least once, 2: exactly once) | **1**    |
| `rsp`   | Reference to a modem response instance.                                  | **None** |

#### Returns

`bool`
True on success, False otherwise.

---

### `mqtt_publish`

Publish something through MQTT.

This function publishes the passed data on the given mqtt topic using the
connection established earlier through [`mqtt_connect`](#mqttconnect).

#### Example

```py
if await modem.mqtt_publish(
    topic=topic,
    data='Hello from Walter'
):
    print('Message Published')
else:
    print('Failed to publish message')
```

#### Params

| Param   | Description                                                          | Default  |
| ------- | -------------------------------------------------------------------- | -------- |
| `topic` | Topic to publish on.                                                 |          |
| `data`  | The data to publish                                                  |          |
| `qos`   | QoS: 0 = at most once, 1 = at least once, 2 = exactly once received. | **1**    |
| `rsp`   | Reference to a modem response instance.                              | **None** |

#### Returns

`bool`
True on success, False otherwise.

---

### `mqtt_did_ring`

Poll if the modem has reported any incoming MQTT messages received on subscribed
topics.

> [!WARNING]
> No more than 1 message with QoS 0 are stored in the buffer,
> every new message with QoS 0 overwrites the previous\
> (this only applies to messages with QoS 0)

#### Example

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

#### Params

| Param      | Description                                                 | Default  |
| ---------- | ----------------------------------------------------------- | -------- |
| `msg_list` | Refence to a list where the received messages will be put.  |          |
| `topic`    | The exact topic to filter on, leave as None for all topics. | **None** |
| `rsp`      | Reference to a modem response instance.                     | **None** |

#### Returns

`bool`
True on success, False
if no message(s) arrived, error or if no message(s) are expected *(eg no ring received)*.
