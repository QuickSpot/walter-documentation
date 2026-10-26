## Methods Overview

- [socketConfig](#socketconfig)
- [socketConfigExtended](#socketconfigextended)
- [socketConfigSecure](#socketconfigsecure)
- [socketDial](#socketdial)
- [socketSend](#socketsend)
- [socketReceive](#socketreceive)
- [socketListen](#socketlisten)
- [socketAccept](#socketaccept)
- [socketGetState](#socketgetstate)
- [socketResume](#socketresume)
- [socketClose](#socketclose)
- [socketAvailable](#socketavailable) _(deprecated)_

## Enums Overview

- [WalterModemSocketState](#waltermodemsocketstate)
- [WalterModemSocketProto](#waltermodemsocketproto)
- [WalterModemSocketAcceptAnyRemote](#waltermodemsocketacceptanyremote)
- [WalterModemSocketRingMode](#waltermodemsocketringmode)
- [WalterModemSocketRecvMode](#waltermodemsocketrecvmode)
- [WalterModemSocketListenMode](#waltermodemsocketlistenmode)
- [WalterModemsocketSendMode](#waltermodemsocketsendmode)
- [WalterModemSocketListenState](#waltermodemsocketlistenstate)
- [WMURCSocketConnRC](#wmurcsocketconnrc)

## Structs Overview

- [WalterModemSocketResponse](#waltermodemsocketresponse)

---

## Methods

> [!WARNING]
> Each method also has an older signature without `socket_id` as the first parameter, which uses
> the last used socket. Those signatures are deprecated, they are listed at the end of each method.

### `socketConfig`

Configure a new socket in a certain PDP context.

This function will configure a new socket.
After socket configuration one can set additional [socket settings](#socketconfigextended)
and use the socket for communication.

#### Params

| Param              | Description                                                      | Default  |
| ------------------ | ---------------------------------------------------------------- | -------- |
| `socket_id`        | The id of the socket (1-6).                                      |          |
| `pdp_ctx_id`       | The PDP context id.                                              | **1**    |
| `mtu`              | The maximum transmission unit used by the socket.                | **300**  |
| `exchange_timeout` | The maximum number of seconds this socket can be inactive.       | **0**    |
| `conn_timeout`     | The maximum number of seconds this socket can try to connect.    | **20**   |
| `send_delay_ms`    | The number of milliseconds send delay.                           | **5000** |
| `rsp`              | Optional modem response structure to save the result in.         | **NULL** |
| `cb`               | Optional callback function, if set this function will not block. | **NULL** |
| `args`             | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on "OK" response, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_SOCKET_ID, 1)

// ...

if (modem.socketConfig(MODEM_SOCKET_ID)) {
    Serial.println("Info: Socket configured");
} else {
    Serial.println("Error: Failed to configure the socket");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG_UINT8(MODEM_SOCKET_ID, 1)

// ...

if (modem.socketConfig(MODEM_SOCKET_ID)) {
    ESP_LOGI("socket_docs_demo", "Socket configured");
} else {
    ESP_LOGE("socket_docs_demo", "Failed to configure the socket");
}

// ...
```

<!-- tabs:end -->

#### Deprecated signature

> [!WARNING]
> **DEPRECATED:** This signature will be removed in a future release.
> Use `socketConfig(socket_id, ...)` above instead.

With `socket_id` -1 this signature reserves a free socket. The id of the socket is stored in `rsp.data.profileId`.

| Param             | Description                                                      | Default  |
| ----------------- | ---------------------------------------------------------------- | -------- |
| `rsp`             | Optional modem response structure to save the result in.         | **NULL** |
| `cb`              | Optional callback function, if set this function will not block. | **NULL** |
| `args`            | Optional argument to pass to the callback.                       | **NULL** |
| `pdp_ctx_id`      | The PDP context id.                                              | **1**    |
| `mtu`             | The maximum transmission unit used by the socket.                | **300**  |
| `exchangeTimeout` | The maximum number of seconds this socket can be inactive.       | **90**   |
| `connTimeout`     | The maximum number of seconds this socket can try to connect.    | **60**   |
| `sendDelayMs`     | The number of milliseconds send delay.                           | **5000** |
| `socket_id`       | The id of the socket (1-6), or -1 to reserve a free one.         | **-1**   |

---

### `socketConfigExtended`

Configure the socket extended parameters.

This function configures the socket extended parameters.

#### Params

| Param         | Description                                                                                       | Default                                       |
| ------------- | ------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| `socket_id`   | The id of the socket (1-6).                                                                       |                                               |
| `ring_mode`   | The format of the ring notification _([WalterModemSocketRingMode](#waltermodemsocketringmode))_.  | **WALTER_MODEM_SOCKET_RING_MODE_DATA_AMOUNT** |
| `recv_mode`   | The data receive mode _([WalterModemSocketRecvMode](#waltermodemsocketrecvmode))_.                | **WALTER_MODEM_SOCKET_RECV_MODE_TEXT**        |
| `keep_alive`  | The keep alive time (currently unused).                                                           | **0**                                         |
| `listen_mode` | Auto accept incoming connections _([WalterModemSocketListenMode](#waltermodemsocketlistenmode))_. | **WALTER_MODEM_SOCKET_LISTEN_MODE_DISABLED**  |
| `send_mode`   | The format of the send data _([WalterModemsocketSendMode](#waltermodemsocketsendmode))_.          | **WALTER_MODEM_SOCKET_SEND_MODE_TEXT**        |
| `rsp`         | Optional modem response structure to save the result in.                                          | **NULL**                                      |
| `cb`          | Optional callback function, if set this function will not block.                                  | **NULL**                                      |
| `args`        | Optional argument to pass to the callback.                                                        | **NULL**                                      |

#### Returns

`bool`  
True on "OK" response, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_SOCKET_ID, 1)

// ...

if (modem.socketConfigExtended(MODEM_SOCKET_ID)) {
    Serial.println("Info: Socket extended parameters configured");
} else {
    Serial.println("Error: Failed to configure the socket extended parameters");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG_UINT8(MODEM_SOCKET_ID, 1)

// ...

if (modem.socketConfigExtended(MODEM_SOCKET_ID)) {
    ESP_LOGI("socket_docs_demo", "Socket extended parameters configured");
} else {
    ESP_LOGE("socket_docs_demo", "Failed to configure the socket extended parameters");
}

// ...
```

<!-- tabs:end -->

#### Deprecated signature

> [!WARNING]
> **DEPRECATED:** This signature will be removed in a future release.
> Use `socketConfigExtended(socket_id, ...)` above instead.

| Param        | Description                                                      | Default                                       |
| ------------ | ---------------------------------------------------------------- | --------------------------------------------- |
| `rsp`        | Optional modem response structure to save the result in.         | **NULL**                                      |
| `cb`         | Optional callback function, if set this function will not block. | **NULL**                                      |
| `args`       | Optional argument to pass to the callback.                       | **NULL**                                      |
| `socket_id`  | The id of the socket (1-6), or -1 to use the last one.           | **-1**                                        |
| `ringMode`   | The format of the ring notification.                             | **WALTER_MODEM_SOCKET_RING_MODE_DATA_AMOUNT** |
| `recvMode`   | The data receive mode of the socket.                             | **WALTER_MODEM_SOCKET_RECV_MODE_TEXT**        |
| `keepAlive`  | The keep alive time (currently unused).                          | **0**                                         |
| `listenMode` | Auto accept incoming connections.                                | **WALTER_MODEM_SOCKET_LISTEN_MODE_DISABLED**  |
| `sendMode`   | The format of the send data.                                     | **WALTER_MODEM_SOCKET_SEND_MODE_TEXT**        |

---

### `socketConfigSecure`

Enable or disable (D)TLS on a socket.

This function will enable or disable (D)TLS on a socket. This can only be done when the socket is not connected.

#### Params

| Param            | Description                                                      | Default  |
| ---------------- | ---------------------------------------------------------------- | -------- |
| `socket_id`      | The id of the socket (1-6).                                      |          |
| `enable_tls`     | True to enable TLS, false to disable it.                         |          |
| `tls_profile_id` | The TLS profile to use (1-6).                                    | **1**    |
| `rsp`            | Optional modem response structure to save the result in.         | **NULL** |
| `cb`             | Optional callback function, if set this function will not block. | **NULL** |
| `args`           | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on "OK" response, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_SOCKET_ID, 1)

// ...

if (modem.socketConfigSecure(MODEM_SOCKET_ID, false)) {
    Serial.println("Info: Socket TLS disabled");
} else {
    Serial.println("Error: Failed to disable socket TLS");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG_UINT8(MODEM_SOCKET_ID, 1)

// ...

if (modem.socketConfigSecure(MODEM_SOCKET_ID, false)) {
    ESP_LOGI("socket_docs_demo", "Socket TLS disabled");
} else {
    ESP_LOGE("socket_docs_demo", "Failed to disable socket TLS");
}

// ...
```

<!-- tabs:end -->

#### Deprecated signature

> [!WARNING]
> **DEPRECATED:** This signature will be removed in a future release.
> Use `socketConfigSecure(socket_id, enable_tls, ...)` above instead.

| Param            | Description                                                      | Default  |
| ---------------- | ---------------------------------------------------------------- | -------- |
| `enableTLS`      | True to enable TLS, false to disable it.                         |          |
| `tls_profile_id` | The TLS profile to use (1-6).                                    | **1**    |
| `profileId`      | The id of the socket (1-6), or -1 to use the last one.           | **-1**   |
| `rsp`            | Optional modem response structure to save the result in.         | **NULL** |
| `cb`             | Optional callback function, if set this function will not block. | **NULL** |
| `args`           | Optional argument to pass to the callback.                       | **NULL** |

---

### `socketDial`

Dial a socket after which data can be exchanged.

This function will dial a socket to a remote host.
When the dial is successful data can be exchanged.

#### Params

| Param               | Description                                                                                                                                                        | Default                                     |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------- |
| `socket_id`         | The id of the socket (1-6).                                                                                                                                        |                                             |
| `protocol`          | The protocol to use _([WalterModemSocketProto](#waltermodemsocketproto))_.                                                                                         |                                             |
| `remote_port`       | The remote port to dial on.                                                                                                                                        |                                             |
| `remote_host`       | The remote IPv4/IPv6 or hostname to dial to.                                                                                                                       |                                             |
| `local_port`        | The local port in case of a UDP socket.                                                                                                                            | **0**                                       |
| `accept_any_remote` | Whether UDP datagrams from/to another address than the remote host and port are allowed _([WalterModemSocketAcceptAnyRemote](#waltermodemsocketacceptanyremote))_. | **WALTER_MODEM_ACCEPT_ANY_REMOTE_DISABLED** |
| `rsp`               | Optional modem response structure to save the result in.                                                                                                           | **NULL**                                    |
| `cb`                | Optional callback function, if set this function will not block.                                                                                                   | **NULL**                                    |
| `args`              | Optional argument to pass to the callback.                                                                                                                         | **NULL**                                    |

#### Returns

`bool`  
True on "OK" response, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_SOCKET_ID, 1)
CONFIG(SERV_ADDR, const char *, "example.com")
CONFIG_UINT16(SERV_PORT, 80)

// ...

if (modem.socketDial(MODEM_SOCKET_ID, WALTER_MODEM_SOCKET_PROTO_TCP, SERV_PORT, SERV_ADDR)) {
    Serial.printf("Info: Connected to %s:%u\r\n", SERV_ADDR, SERV_PORT);
} else {
    Serial.println("Error: Failed to dial the socket");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG_UINT8(MODEM_SOCKET_ID, 1)
CONFIG(SERV_ADDR, const char *, "example.com")
CONFIG_UINT16(SERV_PORT, 80)

// ...

if (modem.socketDial(MODEM_SOCKET_ID, WALTER_MODEM_SOCKET_PROTO_TCP, SERV_PORT, SERV_ADDR)) {
    ESP_LOGI("socket_docs_demo", "Connected to %s:%u", SERV_ADDR, SERV_PORT);
} else {
    ESP_LOGE("socket_docs_demo", "Failed to dial the socket");
}

// ...
```

<!-- tabs:end -->

#### Deprecated signature

> [!WARNING]
> **DEPRECATED:** This signature will be removed in a future release.
> Use `socketDial(socket_id, protocol, remote_port, remote_host, ...)` above instead.

| Param             | Description                                                      | Default                                     |
| ----------------- | ---------------------------------------------------------------- | ------------------------------------------- |
| `remoteHost`      | The remote IPv4/IPv6 or hostname to dial to.                     |                                             |
| `remotePort`      | The remote port to dial on.                                      |                                             |
| `localPort`       | The local port in case of a UDP socket.                          | **0**                                       |
| `rsp`             | Optional modem response structure to save the result in.         | **NULL**                                    |
| `cb`              | Optional callback function, if set this function will not block. | **NULL**                                    |
| `args`            | Optional argument to pass to the callback.                       | **NULL**                                    |
| `protocol`        | The protocol to use.                                             | **WALTER_MODEM_SOCKET_PROTO_UDP**           |
| `acceptAnyRemote` | How to accept remote UDP packets.                                | **WALTER_MODEM_ACCEPT_ANY_REMOTE_DISABLED** |
| `profileId`       | The id of the socket (1-6), or -1 to use the last one.           | **-1**                                      |

---

### `socketSend`

Send data over a socket.

This function will send data over a socket.

> [!WARNING]
> The data buffer **cannot be freed** until the send response is received
> (sync or async).

#### Params

| Param       | Description                                                                                                                         | Default                      |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| `socket_id` | The id of the socket (1-6).                                                                                                         |                              |
| `buf`       | The data to send.                                                                                                                   |                              |
| `buf_size`  | The number of bytes to transmit (1-1500).                                                                                           |                              |
| `rai`       | The release assistance information _([WalterModemRAI](/walter-modem/arduino_esp-idf/reference/sim_and_network.md#waltermodemrai))_. | **WALTER_MODEM_RAI_NO_INFO** |
| `rsp`       | Optional modem response structure to save the result in.                                                                            | **NULL**                     |
| `cb`        | Optional callback function, if set this function will not block.                                                                    | **NULL**                     |
| `args`      | Optional argument to pass to the callback.                                                                                          | **NULL**                     |

#### Returns

`bool`  
True on "OK" response, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_SOCKET_ID, 1)

// ...

static char demoMsg[] = "Demo Message";

if (modem.socketSend(MODEM_SOCKET_ID, (uint8_t *)demoMsg, sizeof(demoMsg) - 1)) {
    Serial.println("Info: Message sent");
} else {
    Serial.println("Error: Failed to send the message");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG_UINT8(MODEM_SOCKET_ID, 1)

// ...

static char demoMsg[] = "Demo Message";

if (modem.socketSend(MODEM_SOCKET_ID, (uint8_t *)demoMsg, sizeof(demoMsg) - 1)) {
    ESP_LOGI("socket_docs_demo", "Message sent");
} else {
    ESP_LOGE("socket_docs_demo", "Failed to send the message");
}

// ...
```

<!-- tabs:end -->

#### Deprecated signatures

> [!WARNING]
> **DEPRECATED:** These signatures will be removed in a future release.
> Use `socketSend(socket_id, buf, buf_size, ...)` above instead.

Data version:

| Param       | Description                                                      | Default                      |
| ----------- | ---------------------------------------------------------------- | ---------------------------- |
| `data`      | The data to send.                                                |                              |
| `dataSize`  | The number of bytes to transmit.                                 |                              |
| `rsp`       | Optional modem response structure to save the result in.         | **NULL**                     |
| `cb`        | Optional callback function, if set this function will not block. | **NULL**                     |
| `args`      | Optional argument to pass to the callback.                       | **NULL**                     |
| `rai`       | The release assistance information.                              | **WALTER_MODEM_RAI_NO_INFO** |
| `socket_id` | The id of the socket (1-6), or -1 to use the last one.           | **-1**                       |

String version:

| Param       | Description                                                      | Default                      |
| ----------- | ---------------------------------------------------------------- | ---------------------------- |
| `str`       | A zero-terminated string to send over the socket.                |                              |
| `rsp`       | Optional modem response structure to save the result in.         | **NULL**                     |
| `cb`        | Optional callback function, if set this function will not block. | **NULL**                     |
| `args`      | Optional argument to pass to the callback.                       | **NULL**                     |
| `rai`       | The release assistance information.                              | **WALTER_MODEM_RAI_NO_INFO** |
| `socket_id` | The id of the socket (1-6), or -1 to use the last one.           | **-1**                       |

---

### `socketReceive`

Receive socket data from the modem buffer.

Call this function after a `WALTER_MODEM_SOCKET_EVENT_RING` event and pass the `data_len`
reported by that event. The socket id and the number of received bytes are stored in
`rsp.data.socketResponse` _([WalterModemSocketResponse](#waltermodemsocketresponse))_.

#### Params

| Param       | Description                                                                      | Default  |
| ----------- | -------------------------------------------------------------------------------- | -------- |
| `socket_id` | The id of the socket to receive from (1-6).                                      |          |
| `buf`       | User buffer to store the received data. The data is not null-terminated.         |          |
| `buf_size`  | The number of bytes to receive (1-1500), use the `data_len` from the ring event. |          |
| `rsp`       | Optional modem response structure to save the result in.                         | **NULL** |
| `cb`        | Optional callback function, if set this function will not block.                 | **NULL** |
| `args`      | Optional argument to pass to the callback.                                       | **NULL** |

#### Returns

`bool`  
True on "OK" response, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

static uint8_t inBuf[1500];

void mySocketEventHandler(WMSocketEventType event, const WMSocketEventData *data, void *args)
{
    if (event != WALTER_MODEM_SOCKET_EVENT_RING || data->data_len == 0) {
        return;
    }

    if (modem.socketReceive(data->conn_id, inBuf, data->data_len)) {
        Serial.printf("Info: Received %u bytes on socket %u: %.*s\r\n",
                      data->data_len, data->conn_id, data->data_len, (const char *)inBuf);
    } else {
        Serial.println("Error: Failed to receive socket data");
    }
}

// ...

modem.setSocketEventHandler(mySocketEventHandler);

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

static uint8_t inBuf[1500];

void mySocketEventHandler(WMSocketEventType event, const WMSocketEventData *data, void *args)
{
    if (event != WALTER_MODEM_SOCKET_EVENT_RING || data->data_len == 0) {
        return;
    }

    if (modem.socketReceive(data->conn_id, inBuf, data->data_len)) {
        ESP_LOGI("socket_docs_demo", "Received %u bytes on socket %u: %.*s",
                 data->data_len, data->conn_id, data->data_len, (const char *)inBuf);
    } else {
        ESP_LOGE("socket_docs_demo", "Failed to receive socket data");
    }
}

// ...

modem.setSocketEventHandler(mySocketEventHandler);

// ...
```

<!-- tabs:end -->

#### Deprecated signature

> [!WARNING]
> **DEPRECATED:** This signature will be removed in a future release.
> Use `socketReceive(socket_id, buf, buf_size, ...)` above instead.

| Param           | Description                                                                      | Default  |
| --------------- | -------------------------------------------------------------------------------- | -------- |
| `receiveCount`  | Not used, `targetBufSize` bytes are received.                                    |          |
| `targetBufSize` | The number of bytes to receive (1-1500), use the `data_len` from the ring event. |          |
| `targetBuf`     | User buffer to store the received data.                                          |          |
| `profileId`     | The id of the socket (1-6), or -1 to use the last one.                           | **-1**   |
| `rsp`           | Optional modem response structure to save the result in.                         | **NULL** |

---

### `socketListen`

Listen for incoming socket connections.

> [!WARNING]
> Only one incoming socket connection can be handled at a time.

#### Params

| Param          | Description                                                                                 | Default                                   |
| -------------- | ------------------------------------------------------------------------------------------- | ----------------------------------------- |
| `socket_id`    | The id of the socket to listen on (1-6).                                                    |                                           |
| `protocol`     | The protocol of the listening socket _([WalterModemSocketProto](#waltermodemsocketproto))_. |                                           |
| `listen_state` | The state to listen on _([WalterModemSocketListenState](#waltermodemsocketlistenstate))_.   | **WALTER_MODEM_SOCKET_LISTEN_STATE_IPV4** |
| `listen_port`  | The port to listen on.                                                                      | **0**                                     |
| `rsp`          | Optional modem response structure to save the result in.                                    | **NULL**                                  |
| `cb`           | Optional callback function, if set this function will not block.                            | **NULL**                                  |
| `args`         | Optional argument to pass to the callback.                                                  | **NULL**                                  |

#### Returns

`bool`  
True on "OK" response, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_SOCKET_ID, 1)

// ...

if (modem.socketListen(MODEM_SOCKET_ID, WALTER_MODEM_SOCKET_PROTO_TCP,
                       WALTER_MODEM_SOCKET_LISTEN_STATE_IPV4, 5000)) {
    Serial.println("Info: Listening for incoming socket connections");
} else {
    Serial.println("Error: Failed to listen for incoming socket connections");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG_UINT8(MODEM_SOCKET_ID, 1)

// ...

if (modem.socketListen(MODEM_SOCKET_ID, WALTER_MODEM_SOCKET_PROTO_TCP,
                       WALTER_MODEM_SOCKET_LISTEN_STATE_IPV4, 5000)) {
    ESP_LOGI("socket_docs_demo", "Listening for incoming socket connections");
} else {
    ESP_LOGE("socket_docs_demo", "Failed to listen for incoming socket connections");
}

// ...
```

<!-- tabs:end -->

#### Deprecated signature

> [!WARNING]
> **DEPRECATED:** This signature will be removed in a future release.
> Use `socketListen(socket_id, protocol, ...)` above instead.

| Param              | Description                                                      | Default                                   |
| ------------------ | ---------------------------------------------------------------- | ----------------------------------------- |
| `rsp`              | Optional modem response structure to save the result in.         | **NULL**                                  |
| `cb`               | Optional callback function, if set this function will not block. | **NULL**                                  |
| `args`             | Optional argument to pass to the callback.                       | **NULL**                                  |
| `profileId`        | The id of the socket (1-6), or -1 to use the last one.           | **-1**                                    |
| `protocol`         | The protocol of the listening socket.                            | **WALTER_MODEM_SOCKET_PROTO_TCP**         |
| `listenState`      | The state to listen on.                                          | **WALTER_MODEM_SOCKET_LISTEN_STATE_IPV4** |
| `socketListenPort` | The port to listen on.                                           | **0**                                     |

---

### `socketAccept`

Accept an incoming socket connection.

This function will accept an incoming connection after a connection event has been received.

> [!NOTE]
> This function must be preceded by a call to [socketListen](#socketlisten),
> and an incoming connection must have been reported.

#### Params

| Param             | Description                                                      | Default   |
| ----------------- | ---------------------------------------------------------------- | --------- |
| `socket_id`       | The id of the socket to accept (1-6).                            |           |
| `connection_mode` | The connection mode.                                             | **false** |
| `rsp`             | Optional modem response structure to save the result in.         | **NULL**  |
| `cb`              | Optional callback function, if set this function will not block. | **NULL**  |
| `args`            | Optional argument to pass to the callback.                       | **NULL**  |

#### Returns

`bool`  
True on "OK" response, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_SOCKET_ID, 1)

// ...

if (modem.socketAccept(MODEM_SOCKET_ID)) {
    Serial.println("Info: Accepted incoming socket connection");
} else {
    Serial.println("Error: Failed to accept incoming socket connection");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG_UINT8(MODEM_SOCKET_ID, 1)

// ...

if (modem.socketAccept(MODEM_SOCKET_ID)) {
    ESP_LOGI("socket_docs_demo", "Accepted incoming socket connection");
} else {
    ESP_LOGE("socket_docs_demo", "Failed to accept incoming socket connection");
}

// ...
```

<!-- tabs:end -->

#### Deprecated signature

> [!WARNING]
> **DEPRECATED:** This signature will be removed in a future release.
> Use `socketAccept(socket_id, ...)` above instead.

| Param         | Description                                                      | Default   |
| ------------- | ---------------------------------------------------------------- | --------- |
| `rsp`         | Optional modem response structure to save the result in.         | **NULL**  |
| `cb`          | Optional callback function, if set this function will not block. | **NULL**  |
| `args`        | Optional argument to pass to the callback.                       | **NULL**  |
| `profileId`   | The id of the socket (1-6), or -1 to use the last one.           | **-1**    |
| `commandMode` | The connection mode.                                             | **false** |

---

### `socketGetState`

Get the state of a socket.

This function updates all the socket states and returns the current state for the requested socket.

#### Params

| Param       | Description                                             | Default |
| ----------- | ------------------------------------------------------- | ------- |
| `socket_id` | The id of the socket (1-6). With 0, `FREE` is returned. | **0**   |

#### Returns

[`WalterModemSocketState`](#waltermodemsocketstate)  
The socket state.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_SOCKET_ID, 1)

// ...

Serial.printf("Info: State of socket %u: %d\r\n", MODEM_SOCKET_ID,
              modem.socketGetState(MODEM_SOCKET_ID));

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG_UINT8(MODEM_SOCKET_ID, 1)

// ...

ESP_LOGI("socket_docs_demo", "State of socket %u: %d", MODEM_SOCKET_ID,
         modem.socketGetState(MODEM_SOCKET_ID));

// ...
```

<!-- tabs:end -->

---

### `socketResume`

Resume a suspended socket connection.

#### Params

| Param       | Description                                                      | Default  |
| ----------- | ---------------------------------------------------------------- | -------- |
| `socket_id` | The id of the socket to resume (1-6).                            |          |
| `rsp`       | Optional modem response structure to save the result in.         | **NULL** |
| `cb`        | Optional callback function, if set this function will not block. | **NULL** |
| `args`      | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on "OK" response, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_SOCKET_ID, 1)

// ...

if (modem.socketResume(MODEM_SOCKET_ID)) {
    Serial.println("Info: Socket resumed");
} else {
    Serial.println("Error: Failed to resume the socket");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG_UINT8(MODEM_SOCKET_ID, 1)

// ...

if (modem.socketResume(MODEM_SOCKET_ID)) {
    ESP_LOGI("socket_docs_demo", "Socket resumed");
} else {
    ESP_LOGE("socket_docs_demo", "Failed to resume the socket");
}

// ...
```

<!-- tabs:end -->

---

### `socketClose`

Close a socket.

> [!WARNING]
> Sockets can only be **closed** when they are **suspended**, active socket connections cannot be closed.

#### Params

| Param       | Description                                                      | Default  |
| ----------- | ---------------------------------------------------------------- | -------- |
| `socket_id` | The id of the socket to close (1-6).                             |          |
| `rsp`       | Optional modem response structure to save the result in.         | **NULL** |
| `cb`        | Optional callback function, if set this function will not block. | **NULL** |
| `args`      | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on "OK" response, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_SOCKET_ID, 1)

// ...

if (modem.socketClose(MODEM_SOCKET_ID)) {
    Serial.println("Info: Socket closed");
} else {
    Serial.println("Error: Failed to close the socket");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG_UINT8(MODEM_SOCKET_ID, 1)

// ...

if (modem.socketClose(MODEM_SOCKET_ID)) {
    ESP_LOGI("socket_docs_demo", "Socket closed");
} else {
    ESP_LOGE("socket_docs_demo", "Failed to close the socket");
}

// ...
```

<!-- tabs:end -->

#### Deprecated signature

> [!WARNING]
> **DEPRECATED:** This signature will be removed in a future release.
> Use `socketClose(socket_id, ...)` above instead.

| Param       | Description                                                      | Default  |
| ----------- | ---------------------------------------------------------------- | -------- |
| `rsp`       | Optional modem response structure to save the result in.         | **NULL** |
| `cb`        | Optional callback function, if set this function will not block. | **NULL** |
| `args`      | Optional argument to pass to the callback.                       | **NULL** |
| `socket_id` | The id of the socket (1-6), or -1 to use the last one.           | **-1**   |

---

### `socketAvailable`

> [!WARNING]
> **DEPRECATED:** This method will be removed in a future release and always returns 0.
> Use the `data_len` of the `WALTER_MODEM_SOCKET_EVENT_RING` event instead, see
> [socketReceive](#socketreceive).

Get the number of bytes available in the socket buffer.

#### Params

| Param       | Description                                            | Default |
| ----------- | ------------------------------------------------------ | ------- |
| `profileId` | The id of the socket (1-6), or -1 to use the last one. | **-1**  |

#### Returns

`uint16_t`  
Always 0.

---

## Enums

### `WalterModemSocketState`

The state of a socket.

> **WALTER_MODEM_SOCKET_STATE_FREE** = `0`  
> The socket is free.  
> **WALTER_MODEM_SOCKET_STATE_RESERVED** = `1`  
> The socket is reserved but not configured yet.  
> **WALTER_MODEM_SOCKET_STATE_READY** = `2`  
> The socket is configured and ready to be dialed.  
> **WALTER_MODEM_SOCKET_STATE_CLOSED** = `3`  
> The socket is closed.  
> **WALTER_MODEM_SOCKET_STATE_OPENED** = `4`  
> The socket connection is active.  
> **WALTER_MODEM_SOCKET_STATE_PENDING_NO_DATA** = `5`  
> The socket is suspended without pending data.  
> **WALTER_MODEM_SOCKET_STATE_PENDING_WITH_DATA** = `6`  
> The socket is suspended with pending data.  
> **WALTER_MODEM_SOCKET_STATE_LISTENING** = `7`  
> The socket is listening for incoming connections.  
> **WALTER_MODEM_SOCKET_STATE_INCOMMING_CONNECTION** = `8`  
> An incoming connection is waiting to be accepted.  
> **WALTER_MODEM_SOCKET_STATE_SUSPENDED** = `9`  
> The socket is suspended.

### `WalterModemSocketProto`

The protocol that is used by the socket.

> **WALTER_MODEM_SOCKET_PROTO_TCP** = `0`  
> Use the TCP protocol for the socket.  
> **WALTER_MODEM_SOCKET_PROTO_UDP** = `1`  
> Use the UDP protocol for the socket.

### `WalterModemSocketAcceptAnyRemote`

Possible methodologies on how a socket handles data from other hosts
besides the IP-address and remote port it is configured for.

> **WALTER_MODEM_ACCEPT_ANY_REMOTE_DISABLED** = `0`  
> Do not accept any remote data.  
> **WALTER_MODEM_ACCEPT_ANY_REMOTE_RX_ONLY** = `1`  
> Only accept received data.  
> **WALTER_MODEM_ACCEPT_ANY_REMOTE_RX_AND_TX** = `2`  
> Accept received data and allow sending to the remote.

### `WalterModemSocketRingMode`

This enumeration determines how the **SQNSRING** message should be **formatted**.

> **WALTER_MODEM_SOCKET_RING_MODE_NORMAL** = `0`  
> Only the socket id is in the URC.  
> **WALTER_MODEM_SOCKET_RING_MODE_DATA_AMOUNT** = `1`  
> The received data amount has been added to the URC.

### `WalterModemSocketRecvMode`

This enumeration determines in what way the **payload data** should be returned.

> **WALTER_MODEM_SOCKET_RECV_MODE_TEXT** = `0`  
> Receive the payload data as raw byte text.  
> **WALTER_MODEM_SOCKET_RECV_MODE_HEX** = `1`  
> Receive the payload data as a hex string.

### `WalterModemSocketListenMode`

This enumeration determines whether an incoming socket connection should be auto accepted.

> **WALTER_MODEM_SOCKET_LISTEN_MODE_DISABLED** = `0`  
> Incoming socket connections will **not** be auto accepted.  
> **WALTER_MODEM_SOCKET_LISTEN_MODE_ENABLED** = `1`  
> Incoming socket connections will be auto accepted.

### `WalterModemsocketSendMode`

This enumeration determines how the send data should be expected.

> **WALTER_MODEM_SOCKET_SEND_MODE_TEXT** = `0`  
> Expect the payload data as a raw byte string.  
> **WALTER_MODEM_SOCKET_SEND_MODE_HEX** = `1`  
> Expect the payload data as a hex string.

### `WalterModemSocketListenState`

This enumeration represents the listen state of the socket.

> **WALTER_MODEM_SOCKET_LISTEN_STATE_CLOSE** = `0`  
> Close a listening socket.  
> **WALTER_MODEM_SOCKET_LISTEN_STATE_IPV4** = `1`  
> Open a listening IPv4 socket.  
> **WALTER_MODEM_SOCKET_LISTEN_STATE_IPV6** = `2`  
> Open a listening IPv6 socket.

### `WMURCSocketConnRC`

The socket connection result codes, the type of `rc` in
[WMSocketEventData](/walter-modem/arduino_esp-idf/reference/event_handlers.md#wmsocketeventdata).

> **WALTER_MODEM_SOCKET_CONNECTION_RESULT_OK** = `0`  
> The connection succeeded.  
> **WALTER_MODEM_SOCKET_CONNECTION_RESULT_NO_CARRIER** = `-1`  
> No carrier.  
> **WALTER_MODEM_SOCKET_CONNECTION_RESULT_UNKNOWN** = `-2`  
> Unknown error.  
> **WALTER_MODEM_SOCKET_CONNECTION_RESULT_CONNECTION_REFUSED** = `-3`  
> The remote host refused the connection.  
> **WALTER_MODEM_SOCKET_CONNECTION_RESULT_AUTHENTICATION_REJECTED** = `-4`  
> Authentication was rejected.  
> **WALTER_MODEM_SOCKET_CONNECTION_RESULT_TLS_ERROR** = `-5`  
> TLS error.

---

## Structs

### `WalterModemSocketResponse`

The socket response data in `rsp.data.socketResponse`, see [socketReceive](#socketreceive).

| Field           | Type       | Description                   |
| --------------- | ---------- | ----------------------------- |
| `socketId`      | `int`      | The socket identifier.        |
| `bytesReceived` | `uint16_t` | The number of bytes received. |
