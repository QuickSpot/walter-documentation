## Event Handlers

Event handlers are meant to notify the application layer of changes or events that occur
so that the application layer can change states and act on that event without the need for polling.
When calling the functions to set event handlers, only that of the last call will be set.
To remove an event hander, call the set function with a nullptr as the handler.

> [!WARNING]
> The application code that acts on the event should be short lived and non-blocking, eg. changing a state flag.
> Therefore it is advised not to call modem library methods within an event handler.

## Methods Overview

- [setRegistrationEventHandler](#setregistrationeventhandler)
- [setSystemEventHandler](#setsystemeventhandler)
- [setATEventHandler](#setateventhandler)
- [gnssSetEventHandler](#gnssseteventhandler)
- [mqttSetEventHandler](#mqttseteventhandler)
- [httpSetEventHandler](#httpseteventhandler)
- [coapSetEventHandler](#coapseteventhandler)
- [socketSetEventHandler](#socketseteventhandler)

## Enums Overview

- [WalterModemEventType](#waltermodemeventtype)
- [WalterModemSystemEvent](#waltermodemsystemevent)
- [WalterModemMQTTEvent](#waltermodemmqttevent)
- [WalterModemHttpEvent](#waltermodemhttpevent)
- [WalterModemCoapEvent](#waltermodemcoapevent)
- [WalterModemSocketEvent](#waltermodemsocketevent)

## Methods

### `setRegistrationEventHandler`

This function sets the handler that is called when a network registration event occurs.

#### Params

| Param     | Description                     | Default |
| --------- | ------------------------------- | ------- |
| `handler` | The handler function or nullptr |         |
| `args`    | Optional handler arguments      |         |

---

### `setSystemEventHandler`

This function sets the handler that is called when a system event occurs.

#### Params

| Param     | Description                     | Default |
| --------- | ------------------------------- | ------- |
| `handler` | The handler function or nullptr |         |
| `args`    | Optional handler arguments      |         |

---

### `setATEventHandler`

This function sets the handler that is called when an AT response event occurs.

#### Params

| Param     | Description                     | Default |
| --------- | ------------------------------- | ------- |
| `handler` | The handler function or nullptr |         |
| `args`    | Optional handler arguments      |         |

---

### `gnssSetEventHandler`

This function sets the handler that is called when a GNSS fix was obtained or when the
receiver has given up.

#### Params

| Param     | Description                                                     | Default |
| --------- | --------------------------------------------------------------- | ------- |
| `handler` | The handler function or nullptr _(walterModemGNSSEventHandler)_ |         |
| `args`    | Optional handler arguments                                      |         |

#### walterModemGNSSEventHandler

```cpp
typedef void (*walterModemGNSSEventHandler)(const WalterModemGNSSFix *fix, void *args);
```

| Param  | Description                                      |
| ------ | ------------------------------------------------ |
| `fix`  | The GNSS fix event data.                         |
| `args` | Optional arguments set by the application layer. |

---

### `mqttSetEventHandler`

This function sets the handler that is called when an MQTT event is launched by the modem.

#### Params

| Param     | Description                                                     | Default |
| --------- | --------------------------------------------------------------- | ------- |
| `handler` | The handler function or nullptr _(walterModemMQTTEventHandler)_ |         |
| `args`    | Optional handler arguments                                      |         |

#### walterModemMQTTEventHandler

```cpp
typedef void (*walterModemMQTTEventHandler)(WalterModemMQTTEvent ev, WalterModemMqttStatus status, void *args);
```

| Param  | Description                                      |
| ------ | ------------------------------------------------ |
| `ev`   | The type of MQTTEvent.                           |
| `args` | Optional arguments set by the application layer. |

---

### `httpSetEventHandler`

This function sets the handler that is called when an HTTP event is launched by the modem.

#### Params

| Param     | Description                                                     | Default |
| --------- | --------------------------------------------------------------- | ------- |
| `handler` | The handler function or nullptr _(walterModemHttpEventHandler)_ |         |
| `args`    | Optional handler arguments                                      |         |

#### walterModemHttpEventHandler

```cpp
typedef void (*walterModemHttpEventHandler)(WalterModemHttpEvent ev, int profileId, void *args);
```

| Param       | Description                                      |
| ----------- | ------------------------------------------------ |
| `ev`        | The type of HTTPEvent.                           |
| `profileId` | The id of the Http Profile                       |
| `args`      | Optional arguments set by the application layer. |

---

### `coapSetEventHandler`

This function sets the handler that is called when an CoAP event is launched by the modem.

#### Params

| Param     | Description                                                     | Default |
| --------- | --------------------------------------------------------------- | ------- |
| `handler` | The handler function or nullptr _(walterModemHttpEventHandler)_ |         |
| `args`    | Optional handler arguments                                      |         |

#### walterModemCoAPEventHandler

```cpp
typedef void (*walterModemCoAPEventHandler)(WalterModemCoapEvent ev, int profileId, void *args);
```

| Param       | Description                                      |
| ----------- | ------------------------------------------------ |
| `ev`        | The type of HTTPEvent.                           |
| `profileId` | The id of the CoAP Profile                       |
| `args`      | Optional arguments set by the application layer. |

---

### `socketSetEventHandler`

This function sets the handler that is called when an Socket event is launched by the modem.

#### Params

| Param     | Description                                                     | Default  |
| --------- | --------------------------------------------------------------- | -------- |
| `handler` | The handler function or nullptr _(walterModemHttpEventHandler)_ |          |
| `args`    | Optional handler arguments                                      | **NULL** |

#### walterModemSocketEventHandler

```cpp
typedef void (*walterModemSocketEventHandler)(
    WalterModemSocketEvent ev,
    int socketId,
    uint16_t dataReceived,
    uint8_t *dataBuffer,
    void *args);
```

| Param          | Description                                      |
| -------------- | ------------------------------------------------ |
| `ev`           | The type of HTTPEvent.                           |
| `socketId`     | The id of the socket                             |
| `dataReceived` | The amount of data that has been received        |
| `dataBuffer`   | The data buffer to hold the data in              |
| `args`         | Optional arguments set by the application layer. |

> [!NOTE]
> The dataReceived and dataBuffer params will be used based on the WalterModemSocketRingMode.

---

## Enums

### `WalterModemEventType`

The different types of events supported by the library.

> **WALTER_MODEM_EVENT_TYPE_REGISTRATION** = `0`  
> Network registration related events.  
> **WALTER_MODEM_EVENT_TYPE_SYSTEM** = `1`  
> System related events.  
> **WALTER_MODEM_EVENT_TYPE_AT** = `2`  
> Incoming AT string events.  
> **WALTER_MODEM_EVENT_TYPE_GNSS** = `3`  
> GNSS related events.  
> **WALTER_MODEM_EVENT_TYPE_MQTT** = `4`  
> MQTT related events.  
> **WALTER_MODEM_EVENT_TYPE_HTTP** = `5`  
> HTTP related events.  
> **WALTER_MODEM_EVENT_TYPE_COAP** = `6`  
> CoAP related events.  
> **WALTER_MODEM_EVENT_TYPE_SOCKET** = `7`  
> Socket related events.  
> **WALTER_MODEM_EVENT_TYPE_COUNT** = `8`  
> Number of event types supported by the library.  

### `WalterModemSystemEvent`

The different types of system events.

> **WALTER_MODEM_SYSTEM_EVENT_STARTED** = `0`  
> System startup event.  

### `WalterModemMQTTEvent`

The different MQTT event types.

> **WALTER_MODEM_MQTT_EVENT_CONNECTED** = `0`  
> MQTT connection established.  
> **WALTER_MODEM_MQTT_EVENT_DISCONNECTED** = `1`  
> MQTT connection lost.  
> **WALTER_MODEM_MQTT_EVENT_RING** = `2`  
> MQTT ring event notification.  

### `WalterModemHttpEvent`

The different HTTP event types.

> **WALTER_MODEM_HTTP_EVENT_CONNECTED** = `0`  
> HTTP connection established.  
> **WALTER_MODEM_HTTP_EVENT_DISCONNECTED** = `1`  
> HTTP connection lost.  
> **WALTER_MODEM_HTTP_EVENT_CONNECTION_CLOSED** = `2`  
> HTTP connection closed.  
> **WALTER_MODEM_HTTP_EVENT_RING** = `3`  
> HTTP ring event notification.  

### `WalterModemCoapEvent`

The different CoAP event types.

> **WALTER_MODEM_COAP_EVENT_CONNECTED** = `0`  
> CoAP connection established.  
> **WALTER_MODEM_COAP_EVENT_DISCONNECTED** = `1`  
> CoAP connection lost.  
> **WALTER_MODEM_COAP_EVENT_RING** = `2`  
> CoAP ring event notification.  

### `WalterModemSocketEvent`

The different Socket event types.

> **WALTER_MODEM_SOCKET_EVENT_CONNECTED** = `0`  
> Socket connection established.  
> **WALTER_MODEM_SOCKET_EVENT_DISCONNECTED** = `1`  
> Socket connection lost.  
> **WALTER_MODEM_SOCKET_EVENT_RING** = `2`  
> Socket ring event notification.