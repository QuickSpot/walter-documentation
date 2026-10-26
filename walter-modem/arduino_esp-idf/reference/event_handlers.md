## Event Handlers

Event handlers are meant to notify the application layer of changes or events that occur
so that the application layer can change states and act on that event without the need for polling.
When calling the functions to set event handlers, only that of the last call will be set.
To remove an event handler, call the set function with a nullptr as the handler.

## Methods Overview

- [setNetworkEventHandler](#setnetworkeventhandler)
- [setSystemEventHandler](#setsystemeventhandler)
- [setTemperatureEventHandler](#settemperatureeventhandler)
- [setVoltageEventHandler](#setvoltageeventhandler)
- [setGNSSEventHandler](#setgnsseventhandler)
- [setMQTTEventHandler](#setmqtteventhandler)
- [setHTTPEventHandler](#sethttpeventhandler)
- [setCoAPEventHandler](#setcoapeventhandler)
- [setSocketEventHandler](#setsocketeventhandler)

## Enums Overview

- [WalterModemEventType](#waltermodemeventtype)
- [WalterModemEventSystemType](#waltermodemeventsystemtype)
- [WMNetworkEventType](#wmnetworkeventtype)
- [WMGNSSEventType](#wmgnsseventtype)
- [WMMQTTEventType](#wmmqtteventtype)
- [WMHTTPEventType](#wmhttpeventtype)
- [WMCoAPEventType](#wmcoapeventtype)
- [WMSocketEventType](#wmsocketeventtype)

## Structs Overview

- [WMNetworkEventData](#wmnetworkeventdata)
- [WalterModemTempData](#waltermodemtempdata)
- [WalterModemVoltageData](#waltermodemvoltagedata)
- [WMGNSSEventData](#wmgnsseventdata)
- [WMMQTTEventData](#wmmqtteventdata)
- [WMHTTPEventData](#wmhttpeventdata)
- [WMCoAPEventData](#wmcoapeventdata)
- [WMSocketEventData](#wmsocketeventdata)

## BlueCherry Handlers

BlueCherry has its own handlers on the `WalterBlueCherry` object. See the
[BlueCherry reference](/walter-modem/arduino_esp-idf/reference/bluecherry.md):

- [setStateHandler](/walter-modem/arduino_esp-idf/reference/bluecherry.md#setstatehandler): connection state changes
- [setMsgHandler](/walter-modem/arduino_esp-idf/reference/bluecherry.md#setmsghandler): incoming messages
- [setOtaHandler](/walter-modem/arduino_esp-idf/reference/bluecherry.md#setotahandler): firmware update events

## Methods

> [!NOTE]
> Handlers run on the library's event task. The `data` pointer is only valid during the call,
> so copy what you need. When a handler takes longer than `WALTER_MODEM_MAX_EVENT_DURATION_MS`,
> the library logs a warning.

### `setNetworkEventHandler`

Set the handler that is called when a network event occurs: a change in network registration
state, or new eDRX parameters.

#### Params

| Param     | Description                                                                       | Default     |
| --------- | --------------------------------------------------------------------------------- | ----------- |
| `handler` | The handler function _(walterModemNetworkEventHandler)_, or nullptr to remove it. | **nullptr** |
| `args`    | Optional arguments passed to the handler.                                         | **nullptr** |

#### walterModemNetworkEventHandler

```cpp
typedef void (*walterModemNetworkEventHandler)(WMNetworkEventType event, const WMNetworkEventData *data, void *args);
```

| Param   | Description                                                            |
| ------- | ---------------------------------------------------------------------- |
| `event` | The type of network event ([WMNetworkEventType](#wmnetworkeventtype)). |
| `data`  | The event data ([WMNetworkEventData](#wmnetworkeventdata)).            |
| `args`  | Optional arguments set by the application layer.                       |

---

### `setSystemEventHandler`

Set the handler that is called when a system event occurs.

#### Params

| Param     | Description                                                                      | Default     |
| --------- | -------------------------------------------------------------------------------- | ----------- |
| `handler` | The handler function _(walterModemSystemEventHandler)_, or nullptr to remove it. | **nullptr** |
| `args`    | Optional arguments passed to the handler.                                        | **nullptr** |

#### walterModemSystemEventHandler

```cpp
typedef void (*walterModemSystemEventHandler)(WalterModemEventSystemType ev, void *args);
```

| Param  | Description                                                                           |
| ------ | ------------------------------------------------------------------------------------- |
| `ev`   | The type of system event ([WalterModemEventSystemType](#waltermodemeventsystemtype)). |
| `args` | Optional arguments set by the application layer.                                      |

---

### `setTemperatureEventHandler`

Set the handler that is called when the modem's temperature monitor reports an event.
Configure the monitor first with `configTemperatureMonitor`.

#### Params

| Param     | Description                                                                           | Default     |
| --------- | ------------------------------------------------------------------------------------- | ----------- |
| `handler` | The handler function _(walterModemTemperatureEventHandler)_, or nullptr to remove it. | **nullptr** |
| `args`    | Optional arguments passed to the handler.                                             | **nullptr** |

#### walterModemTemperatureEventHandler

```cpp
typedef void (*walterModemTemperatureEventHandler)(const WalterModemTempData *data, void *args);
```

| Param  | Description                                                         |
| ------ | ------------------------------------------------------------------- |
| `data` | The temperature data ([WalterModemTempData](#waltermodemtempdata)). |
| `args` | Optional arguments set by the application layer.                    |

---

### `setVoltageEventHandler`

Set the handler that is called when the modem's voltage monitor reports an event.
Configure the monitor first with `configVoltageMonitor`.

#### Params

| Param     | Description                                                                       | Default     |
| --------- | --------------------------------------------------------------------------------- | ----------- |
| `handler` | The handler function _(walterModemVoltageEventHandler)_, or nullptr to remove it. | **nullptr** |
| `args`    | Optional arguments passed to the handler.                                         | **nullptr** |

#### walterModemVoltageEventHandler

```cpp
typedef void (*walterModemVoltageEventHandler)(const WalterModemVoltageData *data, void *args);
```

| Param  | Description                                                           |
| ------ | --------------------------------------------------------------------- |
| `data` | The voltage data ([WalterModemVoltageData](#waltermodemvoltagedata)). |
| `args` | Optional arguments set by the application layer.                      |

---

### `setGNSSEventHandler`

Set the handler that is called when a GNSS fix was obtained or the receiver has given up,
and when the modem reports GNSS assistance data.

#### Params

| Param     | Description                                                                    | Default     |
| --------- | ------------------------------------------------------------------------------ | ----------- |
| `handler` | The handler function _(walterModemGNSSEventHandler)_, or nullptr to remove it. | **nullptr** |
| `args`    | Optional arguments passed to the handler.                                      | **NULL**    |

#### walterModemGNSSEventHandler

```cpp
typedef void (*walterModemGNSSEventHandler)(WMGNSSEventType event, const WMGNSSEventData *data,
                                            void *args);
```

| Param   | Description                                                   |
| ------- | ------------------------------------------------------------- |
| `event` | The type of GNSS event ([WMGNSSEventType](#wmgnsseventtype)). |
| `data`  | The event data ([WMGNSSEventData](#wmgnsseventdata)).         |
| `args`  | Optional arguments set by the application layer.              |

> [!NOTE]
> `WALTER_MODEM_GNSS_EVENT_STATUS` exists in the enum, but the library does not raise it.

---

### `setMQTTEventHandler`

Set the handler that is called when the modem reports an MQTT event.

#### Params

| Param     | Description                                                                    | Default     |
| --------- | ------------------------------------------------------------------------------ | ----------- |
| `handler` | The handler function _(walterModemMQTTEventHandler)_, or nullptr to remove it. | **nullptr** |
| `args`    | Optional arguments passed to the handler.                                      | **NULL**    |

#### walterModemMQTTEventHandler

```cpp
typedef void (*walterModemMQTTEventHandler)(WMMQTTEventType event, const WMMQTTEventData *data,
                                            void *args);
```

| Param   | Description                                                   |
| ------- | ------------------------------------------------------------- |
| `event` | The type of MQTT event ([WMMQTTEventType](#wmmqtteventtype)). |
| `data`  | The event data ([WMMQTTEventData](#wmmqtteventdata)).         |
| `args`  | Optional arguments set by the application layer.              |

---

### `setHTTPEventHandler`

Set the handler that is called when the modem reports an HTTP event.

#### Params

| Param     | Description                                                                    | Default     |
| --------- | ------------------------------------------------------------------------------ | ----------- |
| `handler` | The handler function _(walterModemHttpEventHandler)_, or nullptr to remove it. | **nullptr** |
| `args`    | Optional arguments passed to the handler.                                      | **NULL**    |

#### walterModemHttpEventHandler

```cpp
typedef void (*walterModemHttpEventHandler)(WMHTTPEventType event, const WMHTTPEventData *data,
                                            void *args);
```

| Param   | Description                                                   |
| ------- | ------------------------------------------------------------- |
| `event` | The type of HTTP event ([WMHTTPEventType](#wmhttpeventtype)). |
| `data`  | The event data ([WMHTTPEventData](#wmhttpeventdata)).         |
| `args`  | Optional arguments set by the application layer.              |

---

### `setCoAPEventHandler`

Set the handler that is called when the modem reports a CoAP event.

#### Params

| Param     | Description                                                                    | Default     |
| --------- | ------------------------------------------------------------------------------ | ----------- |
| `handler` | The handler function _(walterModemCoAPEventHandler)_, or nullptr to remove it. | **nullptr** |
| `args`    | Optional arguments passed to the handler.                                      | **NULL**    |

#### walterModemCoAPEventHandler

```cpp
typedef void (*walterModemCoAPEventHandler)(WMCoAPEventType event, const WMCoAPEventData *data,
                                            void *args);
```

| Param   | Description                                                   |
| ------- | ------------------------------------------------------------- |
| `event` | The type of CoAP event ([WMCoAPEventType](#wmcoapeventtype)). |
| `data`  | The event data ([WMCoAPEventData](#wmcoapeventdata)).         |
| `args`  | Optional arguments set by the application layer.              |

---

### `setSocketEventHandler`

Set the handler that is called when the modem reports a socket event.

#### Params

| Param     | Description                                                                      | Default     |
| --------- | -------------------------------------------------------------------------------- | ----------- |
| `handler` | The handler function _(walterModemSocketEventHandler)_, or nullptr to remove it. | **nullptr** |
| `args`    | Optional arguments passed to the handler.                                        | **NULL**    |

#### walterModemSocketEventHandler

```cpp
typedef void (*walterModemSocketEventHandler)(WMSocketEventType ev, const WMSocketEventData *data,
                                              void *args);
```

| Param  | Description                                                         |
| ------ | ------------------------------------------------------------------- |
| `ev`   | The type of socket event ([WMSocketEventType](#wmsocketeventtype)). |
| `data` | The event data ([WMSocketEventData](#wmsocketeventdata)).           |
| `args` | Optional arguments set by the application layer.                    |

---

## Enums

### `WalterModemEventType`

The different types of events supported by the library.

> **WALTER_MODEM_EVENT_TYPE_NETWORK** = `0`  
> Network registration related events.  
> **WALTER_MODEM_EVENT_TYPE_SYSTEM** = `1`  
> System related events.  
> **WALTER_MODEM_EVENT_TYPE_GNSS** = `2`  
> GNSS related events.  
> **WALTER_MODEM_EVENT_TYPE_MQTT** = `3`  
> MQTT related events.  
> **WALTER_MODEM_EVENT_TYPE_HTTP** = `4`  
> HTTP related events.  
> **WALTER_MODEM_EVENT_TYPE_COAP** = `5`  
> CoAP related events.  
> **WALTER_MODEM_EVENT_TYPE_SOCKET** = `6`  
> Socket related events.  
> **WALTER_MODEM_EVENT_TYPE_TEMPERATURE** = `7`  
> Temperature related events.  
> **WALTER_MODEM_EVENT_TYPE_VOLTAGE** = `8`  
> Voltage related events.  
> **WALTER_MODEM_EVENT_TYPE_COUNT** = `9`  
> Number of event types supported by the library.  

### `WalterModemEventSystemType`

The different types of system events.

> **WALTER_MODEM_SYSTEM_EVENT_STARTED** = `0`  
> System startup event.  

### `WMNetworkEventType`

The different network event types.

> **WALTER_MODEM_NETWORK_EVENT_REG_STATE_CHANGE** = `0`  
> The network registration state changed.  
> **WALTER_MODEM_NETWORK_EVENT_EDRX_RECEIVED** = `1`  
> The modem reported new eDRX parameters.  

### `WMGNSSEventType`

The different GNSS event types.

> **WALTER_MODEM_GNSS_EVENT_FIX** = `0`  
> A GNSS fix was obtained or the receiver gave up.  
> **WALTER_MODEM_GNSS_EVENT_STATUS** = `1`  
> Not raised by the library.  
> **WALTER_MODEM_GNSS_EVENT_ASSISTANCE** = `2`  
> The modem reported GNSS assistance data.  

### `WMMQTTEventType`

Groups the different types of MQTT URCs.

> **WALTER_MODEM_MQTT_EVENT_CONNECTED** = `0`  
> MQTT connection established.  
> **WALTER_MODEM_MQTT_EVENT_DISCONNECTED** = `1`  
> MQTT connection lost.  
> **WALTER_MODEM_MQTT_EVENT_SUBSCRIBED** = `2`  
> Subscribe request completed.  
> **WALTER_MODEM_MQTT_EVENT_PUBLISHED** = `3`  
> Publish request completed.  
> **WALTER_MODEM_MQTT_EVENT_MESSAGE** = `4`  
> A message was received on a subscribed topic.  
> **WALTER_MODEM_MQTT_EVENT_MEMORY_FULL** = `5`  
> The modem's MQTT message memory is full.  

### `WMHTTPEventType`

Groups the different types of HTTP URCs.

> **WALTER_MODEM_HTTP_EVENT_CONNECTED** = `0`  
> HTTP connection established.  
> **WALTER_MODEM_HTTP_EVENT_DISCONNECTED** = `1`  
> HTTP connection lost.  
> **WALTER_MODEM_HTTP_EVENT_CONNECTION_CLOSED** = `2`  
> HTTP connection closed.  
> **WALTER_MODEM_HTTP_EVENT_RING** = `3`  
> HTTP ring event notification.  

### `WMCoAPEventType`

The different CoAP event types.

> **WALTER_MODEM_COAP_EVENT_CONNECTED** = `0`  
> CoAP connection established.  
> **WALTER_MODEM_COAP_EVENT_CLOSED** = `1`  
> CoAP connection closed.  
> **WALTER_MODEM_COAP_EVENT_RING** = `2`  
> CoAP ring event notification.  

### `WMSocketEventType`

The different Socket event types.

> **WALTER_MODEM_SOCKET_EVENT_DISCONNECTED** = `0`  
> Socket connection lost.  
> **WALTER_MODEM_SOCKET_EVENT_RING** = `1`  
> Socket ring event notification.

---

## Structs

### `WMNetworkEventData`

The data of a network event, see [setNetworkEventHandler](#setnetworkeventhandler).
`data` is a union. Read `data->cereg` or `data->edrx` depending on the event.

| Event                                         | Field                   | Type                                                                                                                | Description                                          |
| --------------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| `WALTER_MODEM_NETWORK_EVENT_REG_STATE_CHANGE` | `cereg.state`           | [WalterModemNetworkRegState](/walter-modem/arduino_esp-idf/reference/sim_and_network.md#waltermodemnetworkregstate) | The new registration state.                          |
|                                               | `cereg.hasPsmInfo`      | `bool`                                                                                                              | True when the fields below are filled in.            |
|                                               | `cereg.lac`             | `char[16]`                                                                                                          | The tracking area code, as a string.                 |
|                                               | `cereg.ci`              | `char[16]`                                                                                                          | The cell ID, as a string.                            |
|                                               | `cereg.act`             | `uint8_t`                                                                                                           | The access technology.                               |
|                                               | `cereg.activeTime`      | `char[16]`                                                                                                          | The PSM active time (T3324), as a string.            |
|                                               | `cereg.periodicTau`     | `char[16]`                                                                                                          | The PSM periodic TAU (T3412), as a string.           |
| `WALTER_MODEM_NETWORK_EVENT_EDRX_RECEIVED`    | `edrx.actType`          | `uint8_t`                                                                                                           | The access technology type.                          |
|                                               | `edrx.requestedEdrx`    | `char[16]`                                                                                                          | The requested eDRX value, as a string.               |
|                                               | `edrx.nwProvidedEdrx`   | `char[16]`                                                                                                          | The eDRX value provided by the network, as a string. |
|                                               | `edrx.pagingTimeWindow` | `char[16]`                                                                                                          | The paging time window, as a string.                 |

### `WalterModemTempData`

The data of a temperature event, see [setTemperatureEventHandler](#settemperatureeventhandler).
[getTemperature](/walter-modem/arduino_esp-idf/reference/general.md#gettemperature) fills in the same struct.

| Field         | Type                                                                                                        | Description                   |
| ------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------- |
| `mode`        | [WalterModemTempMonitorMode](/walter-modem/arduino_esp-idf/reference/general.md#waltermodemtempmonitormode) | The temperature monitor mode. |
| `status`      | [WalterModemTempStatus](/walter-modem/arduino_esp-idf/reference/general.md#waltermodemtempstatus)           | The temperature status.       |
| `temperature` | `int8_t`                                                                                                    | The temperature in °C.        |

### `WalterModemVoltageData`

The data of a voltage event, see [setVoltageEventHandler](#setvoltageeventhandler).
[getVoltage](/walter-modem/arduino_esp-idf/reference/general.md#getvoltage) fills in the same struct.

| Field       | Type                                                                                                              | Description                                           |
| ----------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| `mode`      | [WalterModemVoltageMonitorMode](/walter-modem/arduino_esp-idf/reference/general.md#waltermodemvoltagemonitormode) | The voltage monitor mode.                             |
| `status`    | [WalterModemVoltageStatus](/walter-modem/arduino_esp-idf/reference/general.md#waltermodemvoltagestatus)           | The voltage status.                                   |
| `voltage`   | `uint16_t`                                                                                                        | The measured voltage.                                 |
| `threshold` | `uint16_t`                                                                                                        | Always 0 in an event. Only filled in by `getVoltage`. |
| `period`    | `uint16_t`                                                                                                        | Always 0 in an event. Only filled in by `getVoltage`. |

### `WMGNSSEventData`

The data of a GNSS event, see [setGNSSEventHandler](#setgnsseventhandler).

| Event                                | Field        | Type                                                                                         | Description                                      |
| ------------------------------------ | ------------ | -------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| `WALTER_MODEM_GNSS_EVENT_FIX`        | `gnssfix`    | [WMGNSSFixEvent](/walter-modem/arduino_esp-idf/reference/gnss.md#wmgnssfixevent)             | The fix: status, position, speed and satellites. |
| `WALTER_MODEM_GNSS_EVENT_ASSISTANCE` | `assistance` | [WMGNSSAssistanceType](/walter-modem/arduino_esp-idf/reference/gnss.md#wmgnssassistancetype) | The type of assistance data the update is about. |

### `WMMQTTEventData`

The data of an MQTT event, see [setMQTTEventHandler](#setmqtteventhandler).

| Event                                  | Fields set                          |
| -------------------------------------- | ----------------------------------- |
| `WALTER_MODEM_MQTT_EVENT_CONNECTED`    | `rc`                                |
| `WALTER_MODEM_MQTT_EVENT_DISCONNECTED` | `rc`                                |
| `WALTER_MODEM_MQTT_EVENT_SUBSCRIBED`   | `topic`, `rc`                       |
| `WALTER_MODEM_MQTT_EVENT_PUBLISHED`    | `rc`, `mid`                         |
| `WALTER_MODEM_MQTT_EVENT_MESSAGE`      | `topic`, `msg_length`, `qos`, `mid` |
| `WALTER_MODEM_MQTT_EVENT_MEMORY_FULL`  | none                                |

| Field        | Type                                                                         | Description                                  |
| ------------ | ---------------------------------------------------------------------------- | -------------------------------------------- |
| `rc`         | [WMMQTTConnRC](/walter-modem/arduino_esp-idf/reference/mqtt.md#wmmqttconnrc) | The result code.                             |
| `topic`      | `char[WALTER_MODEM_MQTT_TOPIC_BUF_SIZE]`                                     | The topic.                                   |
| `msg_length` | `uint16_t`                                                                   | The length of the received message in bytes. |
| `qos`        | `uint8_t`                                                                    | The QoS level of the received message.       |
| `mid`        | `int`                                                                        | The message ID.                              |

### `WMHTTPEventData`

The data of an HTTP event, see [setHTTPEventHandler](#sethttpeventhandler).

| Event                                       | Fields set                                         |
| ------------------------------------------- | -------------------------------------------------- |
| `WALTER_MODEM_HTTP_EVENT_CONNECTED`         | `profile_id`, `rc`                                 |
| `WALTER_MODEM_HTTP_EVENT_DISCONNECTED`      | `profile_id`                                       |
| `WALTER_MODEM_HTTP_EVENT_CONNECTION_CLOSED` | `profile_id`, `rc`                                 |
| `WALTER_MODEM_HTTP_EVENT_RING`              | `profile_id`, `status`, `content_type`, `data_len` |

| Field          | Type       | Description                               |
| -------------- | ---------- | ----------------------------------------- |
| `profile_id`   | `uint8_t`  | The HTTP profile ID.                      |
| `rc`           | `uint8_t`  | The result code.                          |
| `status`       | `uint16_t` | The HTTP status code of the response.     |
| `content_type` | `char[64]` | The content type of the response.         |
| `data_len`     | `uint16_t` | The length of the response body in bytes. |

### `WMCoAPEventData`

The data of a CoAP event, see [setCoAPEventHandler](#setcoapeventhandler).

| Event                               | Fields set                                |
| ----------------------------------- | ----------------------------------------- |
| `WALTER_MODEM_COAP_EVENT_CONNECTED` | `profile_id`                              |
| `WALTER_MODEM_COAP_EVENT_CLOSED`    | `profile_id`, `reason`                    |
| `WALTER_MODEM_COAP_EVENT_RING`      | `profile_id`, `msg_id`, `req_rsp`, `type` |

| Field        | Type       | Description                                               |
| ------------ | ---------- | --------------------------------------------------------- |
| `profile_id` | `uint8_t`  | The CoAP profile ID.                                      |
| `msg_id`     | `uint16_t` | The CoAP message ID.                                      |
| `req_rsp`    | `bool`     | True when the message is a response, false for a request. |
| `type`       | `uint8_t`  | The CoAP send type (CON, NON, ACK or RST).                |
| `rsp_code`   | `uint16_t` | Not filled in by the library.                             |
| `data_len`   | `uint16_t` | Not filled in by the library.                             |
| `reason`     | `char[16]` | Why the connection was closed.                            |

### `WMSocketEventData`

The data of a socket event, see [setSocketEventHandler](#setsocketeventhandler).

| Event                                    | Fields set            |
| ---------------------------------------- | --------------------- |
| `WALTER_MODEM_SOCKET_EVENT_DISCONNECTED` | `conn_id`             |
| `WALTER_MODEM_SOCKET_EVENT_RING`         | `conn_id`, `data_len` |

| Field      | Type                                                                                      | Description                             |
| ---------- | ----------------------------------------------------------------------------------------- | --------------------------------------- |
| `conn_id`  | `uint8_t`                                                                                 | The socket ID.                          |
| `rc`       | [WMURCSocketConnRC](/walter-modem/arduino_esp-idf/reference/sockets.md#wmurcsocketconnrc) | Not filled in by the library.           |
| `data_len` | `uint16_t`                                                                                | The number of bytes waiting to be read. |
| `data`     | `uint8_t[1500]`                                                                           | Not filled in by the library.           |