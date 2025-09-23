## Methods Overview

- [socketConfig](#socketconfig)
- [socketConfigExtended](#socketconfigextended)
- [socketDial](#socketdial)
- [socketSend](#socketsend)
- [socketAccept](#socketaccept)
- [socketListen](#socketlisten)
- [socketReceive](#socketreceive)
- [socketGetState](#socketgetstate)
- [socketResume](#socketresume)
- [socketClose](#socketclose)

## Enums Overview

- [WalterModemSocketState](#waltermodemsocketstate)
- [WalterModemSocketProto](#waltermodemsocketproto)
- [WalterModemSocketAcceptAnyRemote](#waltermodemsocketacceptanyremote)
- [WalterModemSocketRingMode](#waltermodemsocketringmode)
- [WalterModemSocketRecvMode](#waltermodemsocketrecvmode)
- [WalterModemSocketListenMode](#waltermodemsocketlistenmode)
- [WalterModemsocketSendMode](#waltermodemsocketsendmode)
- [WalterModemSocketListenState](#waltermodemsocketlistenstate)

---

## Methods

### `socketConfig`

Configure a new socket with a certain PDP context.

This function will configure a new socket.
After socket creation one can set additional [socket settings](#socketconfigextended)
and use the socket for communication.

> [!NOTE]
> id's are from **1-6**.

#### Params

| Param             | Description                                                                                                           | Default     |
| ----------------- | --------------------------------------------------------------------------------------------------------------------- | ----------- |
| `rsp`             | Pointer to a modem response structure to save the result of the command in. When NULL is given the result is ignored. |             |
| `cb`              | Optional callback argument, when not NULL this function will return immediately.                                      | **nullptr** |
| `args`            | Optional argument to pass to the callback.                                                                            | **nullptr** |
| `pdpCtxId`        | The PDP context id or -1 to re-use the last one.                                                                      | **-1**      |
| `mtu`             | The maximum transmission unit used by the socket.                                                                     | **300**     |
| `exchangeTimeout` | The maximum number of seconds this socket can be inactive.                                                            | **90**      |
| `connTimeout`     | The maximum number of seconds this socket is allowed to try to connect.                                               | **60**      |
| `sendDelayMs`     | The number of milliseconds send delay.                                                                                | **5000**    |

#### Returns

`bool`
True on success, False otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.socketConfig(&rsp)) {
  Serial.println("Info: New socket created succesfully");
} else {
  Serial.println("Error: Failed to create a new socket");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.socketConfig(&rsp)) {
    ESP_LOGI("socket_docs_demo", "New socket created successfully");
} else {
    ESP_LOGE("socket_docs_demo", "Failed to create a new socket");
}

// ...
```

<!-- tabs:end -->

---

### `socketConfigExtended`

Configure the socket extended parameters.
This function confgiures the socket extended parameters.

#### Params

| Param        | Description                                                       | Default                                      |
| ------------ | ----------------------------------------------------------------- | -------------------------------------------- |
| `rsp`        | Optional modem response structure to save the result in.          | **NULL**                                     |
| `cb`         | Optional callback function, if set this function will not block.  | **NULL**                                     |
| `args`       | Optional argument to pass to the callback.                        | **NULL**                                     |
| `socketId`   | The ID of the socket to connect or **-1 to re-use the last one.** | **-1**                                       |
| `ringMode`   | The format of the ring notification.                              | **WALTER_MODEM_SOCKET_RING_MODE_DATA_VIEW**  |
| `recvMode`   | The data receive mode of the socket.                              | **WALTER_MODEM_SOCKET_RECV_MODE_TEXT**       |
| `keepAlive`  | The keepAlive time (currently unused).                            | **0**                                        |
| `listenMode` | Should the socket auto accept incoming connections.               | **WALTER_MODEM_SOCKET_LISTEN_MODE_DISABLED** |
| `sendMode`   | The format of the send data.                                      | **WALTER_MODEM_SOCKET_SEND_MODE_TEXT**       |

#### Returns

`bool`
True on success, False otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.socketConfigExtended(&rsp)) {
    Serial.println("Info: Socket extended configuration parameters defined successfully");
} else {
    Serial.println("Error: Failed to define socket extended configuration parameters");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.socketConfigExtended(&rsp)) {
    ESP_LOGI("socket_docs_demo", "Socket extended configuration parameters defined successfully");
} else {
    ESP_LOGE("socket_docs_demo", "Failed to define socket extended configuration parameters");
}

// ...
```

<!-- tabs:end -->

---

### `socketConfigSecure`

Enable or disable (D)TLS on a socket.

This function will enable or disable (D)TLS on a socket. This can only be done when the socket is not connected.

#### Params

| Param       | Description                                                                | Default  |
|-------------|----------------------------------------------------------------------------|----------|
| `enableTLS` | True to enable TLS, false to disable it.                                   |          |
| `profileId` | The TLS profile ID to use.                                                 | **1**    |
| `socketId`  | The ID of the socket to configure, or -1 to reuse the last one.            | **-1**   |
| `rsp`       | Optional modem response structure to save the result.                      | **NULL** |
| `cb`        | Optional callback function, if set this function will not block.           | **NULL** |
| `args`      | Optional argument to pass to the callback.                                 | **NULL** |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.socketConfigSecure(false)) {
    Serial.println("Info: Socket TLS disabled successfully");
} else {
    Serial.println("Error: Failed to disable socket TLS");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (modem.socketConfigSecure(false)) {
    ESP_LOGI("socket_docs_demo", "Socket TLS disabled successfully");
} else {
    ESP_LOGE("socket_docs_demo", "Failed to disable socket TLS");
}

// ...
```

<!-- tabs:end -->

---

### `socketDial`

Dial a socket after which data can be exchanged.

This function will dial a socket to a remote host.
When the dial is successful data can be exchanged.

#### Params

| Param             | Description                                                                      | Default                                     |
| ----------------- | -------------------------------------------------------------------------------- | ------------------------------------------- |
| `remoteHost`      | The remote IPv4/IPv6 or hostname to connect to.                                  |                                             |
| `remotePort`      | The remote port to connect on.                                                   |                                             |
| `localPort`       | The local port in case of a UDP socket.                                          | **0**                                       |
| `rsp`             | Pointer to a modem response structure to save the result of the command in.      | **NULL**                                    |
| `cb`              | Optional callback argument, when not NULL this function will return immediately. | **NULL**                                    |
| `args`            | Optional argument to pass to the callback.                                       | **NULL**                                    |
| `protocol`        | The [protocol](#waltermodemsocketproto) to use, UDP by default.                  | **WALTER_MODEM_SOCKET_PROTO_UDP**           |
| `acceptAnyRemote` | How to [accept remote](#waltermodemsocketacceptanyremote) UDP packets.           | **WALTER_MODEM_ACCEPT_ANY_REMOTE_DISABLED** |
| `socketId`        | The id of the socket to connect or **-1 to re-use the last one**.                | **-1**                                      |

#### Returns

`bool`
True on success, False otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG(SERV_ADDR, const char *, "example.com")
CONFIG_INT(SERV_PORT, 80)

// ...

if (modem.socketDial(
        SERV_ADDR, SERV_PORT, 0, NULL, NULL, NULL, WALTER_MODEM_SOCKET_PROTO_TCP)) {
    Serial.print("Info: Connected to demo server ");
    Serial.print(SERV_ADDR);
    Serial.print(":");
    Serial.println(SERV_PORT);
} else {
    Serial.println("Error: Failed to connect demo socket");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

CONFIG(SERV_ADDR, const char *, "example.com")
CONFIG_INT(SERV_PORT, 80)

if (modem.socketDial(
        SERV_ADDR, SERV_PORT, 0, NULL, NULL, NULL, WALTER_MODEM_SOCKET_PROTO_TCP)) {
    ESP_LOGI("socket_docs_demo", "Connected to demo server %s:%d", SERV_ADDR, SERV_PORT);
} else {
    ESP_LOGE("socket_docs_demo", "Failed to connect demo socket");
}

// ...
```

<!-- tabs:end -->

---

### `socketSend`

Send data over a socket.

This function will send data over a socket.

> [!WARNING]
> The data buffer **cannot be freed** until the send response is received
> (sync or async).

> [!NOTE]
> The size of the modem packet is **1500 bytes** when size exceeds **1500 bytes**.

> [!NOTE]
> The maximum amount of bytes to send is **16777216** bytes. (16MB)

#### params

| Param      | Description                                                                      | Default                      |
| ---------- | -------------------------------------------------------------------------------- | ---------------------------- |
| `data`     | The data to send.                                                                |                              |
| `dataSize` | The number of bytes to transmit.                                                 |                              |
| `rsp`      | Pointer to a modem response structure to save the result of the command in.      | **NULL**                     |
| `cb`       | Optional callback argument, when not NULL this function will return immediately. | **NULL**                     |
| `args`     | Optional argument to pass to the callback.                                       | **NULL**                     |
| `rai`      | The release assistance information.                                              | **WALTER_MODEM_RAI_NO_INFO** |
| `socketId` | The id of the socket to close or **-1 to re-use the last one.**                  | **-1**                       |

A second version of socketSend exists to simplify sending strings:

| Param      | Description                                                                      | Default                      |
| ---------- | -------------------------------------------------------------------------------- | ---------------------------- |
| `str`      | A zero-terminated string to send over the socket                                 |                              |
| `rsp`      | Pointer to a modem response structure to save the result of the command in.      | **NULL**                     |
| `cb`       | Optional callback argument, when not NULL this function will return immediately. | **NULL**                     |
| `args`     | Optional argument to pass to the callback.                                       | **NULL**                     |
| `rai`      | The release assistance information.                                              | **WALTER_MODEM_RAI_NO_INFO** |
| `socketId` | The id of the socket to close or **-1 to re-use the last one.**                  | **-1**                       |

#### Returns

`bool`
True on success, False otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

const char *demoMsg = "Demo Message";

if (modem.socketSend((uint8_t *)demoMsg, sizeof(demoMsg) - 1)) {
    Serial.print("Info: Transmitted message: ");
    Serial.println(demoMsg);
} else {
    Serial.println("Error: Failed to transmit data");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

const char *demoMsg = "Demo Message";

if (modem.socketSend((uint8_t *)demoMsg, sizeof(demoMsg) - 1)) {
    ESP_LOGI("socket_docs_demo", "Transmitted message: %s", demoMsg);
} else {
    ESP_LOGE("socket_docs_demo", "Failed to transmit data");
}

// ...
```

<!-- tabs:end -->

---

### `socketAccept`

Accepts an incoming socket connection.

This function will accept an incoming connection after a ring event has been received.

> [!NOTE]
> This function must be preceded by a call to [socketListen](#socketlisten).

#### Params

| Param         | Description                                                      | Default   |
| ------------- | ---------------------------------------------------------------- | --------- |
| `rsp`         | Optional modem response structure to save the result in.         | **NULL**  |
| `cb`          | Optional callback function, if set this function will not block. | **NULL**  |
| `args`        | Optional argument to pass to the callback.                       | **NULL**  |
| `socketId`    | The ID of the socket to close or **-1 to re-use the last one.**  | **-1**    |
| `commandMode` | Whether to use command mode for the operation.                   | **false** |

#### Returns

`bool`
True on success, False otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.socketAccept()) {
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

// ...

if (modem.socketAccept()) {
    ESP_LOGI("socket_docs_demo", "Accepted incoming socket connection");
} else {
    ESP_LOGE("socket_docs_demo", "Failed to accept incoming socket connection");
}

// ...
```

<!-- tabs:end -->

---

### `socketListen`

This function makes the modem listen for incoming socket connections.

> [!WARNING]
> Only one incoming socket connection can be handled at a time.

> [!NOTE]
> listens to TCP sockets by default.

#### Params

| Param              | Description                                                      | Default                                   |
| ------------------ | ---------------------------------------------------------------- | ----------------------------------------- |
| `rsp`              | Optional modem response structure to save the result in.         | **NULL**                                  |
| `cb`               | Optional callback function, if set this function will not block. | **NULL**                                  |
| `args`             | Optional argument to pass to the callback.                       | **NULL**                                  |
| `socketId`         | The ID of the socket to listen or **-1 to re-use the last one.** | **-1**                                    |
| `protocol`         | The protocol of the listening socket.                            | **WALTER_MODEM_SOCKET_PROTO_TCP**         |
| `listenState`      | The state to listen on.                                          | **WALTER_MODEM_SOCKET_LISTEN_STATE_IPV4** |
| `socketListenPort` | The port to listen on.                                           | **0**                                     |

#### Returns

`bool`
True on success, False otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.socketListen()) {
    Serial.println("Info: Started listening for incoming socket connections");
} else {
    Serial.println("Error: Failed to start listening for incoming socket connections");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (modem.socketListen()) {
    ESP_LOGI("socket_docs_demo", "Started listening for incoming socket connections");
} else {
    ESP_LOGE("socket_docs_demo", "Failed to start listening for incoming socket connections");
}

// ...
```

<!-- tabs:end -->

---

### `socketAvailable`

Get the number of bytes available in the socket buffer.

This function returns the amount of bytes ready in the buffer to be read.

#### Params

| Param      | Description                                          | Default |
| ---------- | ---------------------------------------------------- | ------- |
| `socketId` | The socket ID to query, or -1 to reuse the last one. | **-1**  |

#### Returns

`uint16_t`  
The number of bytes available to read in the socket buffer.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

while (modem.socketAvailable() > 0) {
    // 1500 is the max amount of bytes the modem can read at a time.
    uint16_t dataToRead = (modem.socketAvailable() > 1500) ? 1500 : modem.socketAvailable();
    Serial.print("Info: Reading: ");
    Serial.print(dataToRead);
    Serial.println(" bytes");

    // Reading logic here ....
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

while (modem.socketAvailable() > 0) {
    // 1500 is the max amount of bytes the modem can read at a time.
    uint16_t dataToRead = (modem.socketAvailable() > 1500) ? 1500 : modem.socketAvailable();
    ESP_LOGI("socket_docs_demo","Reading: %u bytes", dataToRead);

    // Reading logic here ....
}

// ...
```

<!-- tabs:end -->

---

### `socketReceive`

Receive data from an incoming socket connection, or from the remote server.

> [!TIP]
> make sure you have received a ring notification beforehand.

> [!tip]
> use the size retrieved from the event handler.

#### Params

| Param           | Description                                              | Default  |
| --------------- | -------------------------------------------------------- | -------- |
| `targetBufSize` | The size of the target buffer.                           |          |
| `targetBuf`     | The target buffer to write the data to.                  |          |
| `socketId`      | The socket ID to receive from.                           | **-1**   |
| `rsp`           | Optional modem response structure to save the result in. | **NULL** |

#### Returns

`bool`
True on success, False otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

uint8_t dataBuf[1500] = {0};

// ...

uint16_t toRead = 100; // Number of bytes to receive

Serial.print("Info: Attempting to read ");
Serial.print(toRead);
Serial.println(" bytes");

if (modem.socketReceive(toRead, sizeof(dataBuf), dataBuf)) {
    Serial.print("Info: Received ");
    Serial.print(toRead);
    Serial.print(" bytes: ");
    for (uint16_t i = 0; i < toRead; ++i) {
        Serial.print((char)dataBuf[i]);
    }
    Serial.println("");
} else {
    Serial.println("Info: Failed to receive data");
}

// ...
```

##### **ESP_IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

uint8_t dataBuf[1500] = {0};

// ...

uint16_t toRead = 100; // Number of bytes to receive

ESP_LOGI("socket_docs_demo", "Attempting to read %u bytes", toRead);

if (modem.socketReceive(toRead, sizeof(dataBuf), dataBuf)) {
    ESP_LOGI("socket_docs_demo", "Received %u bytes: %.*s", toRead, toRead, dataBuf);
} else {
    ESP_LOGE("socket_docs_demo", "Failed to receive data");
}

// ...
```

<!-- tabs:end -->

---

### `socketGetState`

This function updates all the socket states and returns the current state for the requested socket.

#### Params

| Param     | Description                                    | Default  |
|-----------|------------------------------------------------|----------|
| `socketId`| The socket ID to retrieve the current state.   | **0**    |

#### Returns

[`WalterModemSocketState`](#waltermodemsocketstate)  
The socket state.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

Serial.println("Info: State of socket 0:");
Serial.println(modem.socketGetState(0));

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

ESP_LOGI("socket_docs_demo", "State of socket 0:");
ESP_LOGI(modem.socketGetState(0));

// ...
```

<!-- tabs:end -->

---

### `socketResume`

This function resumes a suspended socket connection.

#### Params

| Param      | Description                                                      | Default  |
| ---------- | ---------------------------------------------------------------- | -------- |
| `socketId` | The ID of the UDP socket to resume.                              | **-1**   |
| `rsp`      | Optional modem response structure to save the result.            | **NULL** |
| `cb`       | Optional callback function, if set this function will not block. | **NULL** |
| `args`     | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if(modem.socketResume()) { 
    Serial.println("Info: Socket resumed"); 
} else { 
    Serial.println("Error: Failed to resume socket"); 
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if(modem.socketResume()) { 
    ESP_LOGI("socket_docs_demo", "Socket resumed"); 
} else { 
    ESP_LOGI("socket_docs_demo", "Failed to resume socket"); 
}

// ...
```

<!-- tabs:end -->

---

### `socketClose`

Close a socket connection.

> [!WARNING]
> Sockets can only be **closed** when they are **suspended or inactive**.

#### Params

| Param      | Description                                                                      | Default  |
| ---------- | -------------------------------------------------------------------------------- | -------- |
| `rsp`      | Pointer to a modem response structure to save the result of the command in.      | **NULL** |
| `cb`       | Optional callback argument, when not NULL this function will return immediately. | **NULL** |
| `args`     | Optional argument to pass to the callback.                                       | **NULL** |
| `socketId` | The id of the socket to close or **-1 to re-use the last one.**                  | **-1**   |

#### Returns

`bool`
True on success, False otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if(modem.socketClose()) { 
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

// ...

if(modem.socketClose()) { 
    ESP_LOGI("socket_docs_demo", "Socket closed"); 
} else { 
    ESP_LOGI("socket_docs_demo", "Failed to close the socket"); 
}

// ...
```

<!-- tabs:end -->

---

## Enums

### `WalterModemSocketState`

> **WALTER_MODEM_SOCKET_STATE_FREE** = `0`  
> **WALTER_MODEM_SOCKET_STATE_RESERVED** = `1`  
> **WALTER_MODEM_SOCKET_STATE_CONFIGURED** = `2`  
> **WALTER_MODEM_SOCKET_STATE_CLOSED** = `3`  
> **WALTER_MODEM_SOCKET_STATE_OPENED** = `4`  
> **WALTER_MODEM_SOCKET_STATE_PENDING_NO_DATA** = `5`  
> **WALTER_MODEM_SOCKET_STATE_PENDING_WITH_DATA** = `6`  
> **WALTER_MODEM_SOCKET_STATE_LISTENING** = `7`  
> **WALTER_MODEM_SOCKET_STATE_INCOMMING_CONNECTION** = `8`  
> **WALTER_MODEM_SOCKET_STATE_SUSPENDED** = `9`  

### `WalterModemSocketProto`

The protocol that us used by the socket.

> **WALTER_MODEM_SOCKET_PROTO_TCP** = `0`  
> Use the TCP protocol for the socket  
> **WALTER_MODEM_SOCKET_PROTO_UDP** = `1`  
> Use the UDP protocol for the socket

### `WalterModemSocketAcceptAnyRemote`

Possible methodologies on how a socket handles data from other hosts
besides the IP-address and remote port it is configured for.

> **WALTER_MODEM_ACCEPT_ANY_REMOTE_DISABLED** = `0`  
> Do not accepty any remote data  
> **WALTER_MODEM_ACCEPT_ANY_REMOTE_RX_ONLY** = `1`  
> Only acccept read  
> **WALTER_MODEM_ACCEPT_ANY_REMOTE_RX_AND_TX** = `2`  
> Accept read write from remote

### `WalterModemSocketRingMode`

This enumeration determines how the **SQNSRING** message should be **formatted**.

> **WALTER_MODEM_SOCKET_RING_MODE_NORMAL** = `0`  
> Only the socket id is in the URC.  
> **WALTER_MODEM_SOCKET_RING_MODE_DATA_AMOUNT** = `1`  
> The received data amount has been added to the URC  
> **WALTER_MODEM_SOCKET_RING_MODE_DATA_VIEW** = `2`  
> The URC contains the data amount and the payload

### `WalterModemSocketRecvMode`

This enumeration determines in what way the **payload data** should be returned.

> **WALTER_MODEM_SOCKET_RECV_MODE_TEXT** = `0`  
> Receive the payload data as raw byte text.  
> **WALTER_MODEM_SOCKET_RECV_MODE_HEX** = `1`  
> Receive the payload data as a hex string

### `WalterModemSocketListenMode`

This enumeration determines whether an incoming socket connection should be auto accepted.

> **WALTER_MODEM_SOCKET_LISTEN_MODE_DISABLED** = `0`  
> Incoming socket connections will `not` be auto accepted  
> **WALTER_MODEM_SOCKET_LISTEN_MODE_ENABLED** = `1`  
> Incoming socket connections will be auto accepted

### `WalterModemsocketSendMode`

This enumeration determines how the send data should be `expected`.

> **WALTER_MODEM_SOCKET_SEND_MODE_TEXT** = `0`  
> Expect the payload data as a raw byte string  
> **WALTER_MODEM_SOCKET_SEND_MODE_HEX** = `1`  
> Expect the payload data as a hex string

### `WalterModemSocketListenState`

This enumeration represents the listen state of the socket.

> **WALTER_MODEM_SOCKET_LISTEN_STATE_CLOSE** = `0`  
> Close a listening socket.  
> **WALTER_MODEM_SOCKET_LISTEN_STATE_IPV4** = `1`  
> Open a listening IPV4 socket.  
> **WALTER_MODEM_SOCKET_LISTEN_STATE_IPV6** = `2`
