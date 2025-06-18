## Methods Overview

- [socketConfig](#socketconfig)
- [socketConfigExtended](#socketconfigextended)
- [socketDial](#socketdial)
- [socketSend](#socketsend)
- [socketAccept](#socketaccept)
- [socketListen](#socketlisten)
- [socketDidRing](#socketdidring)
- [socketReceive](#socketreceive)
- [socketClose](#socketclose)

## Enums Overview

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

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
WalterModemRsp rsp = {};
int socketId = 0;
if(modem.socketConfig(&rsp)) {
    Serial.printf("socket configured successfully\n");
    socketId = rsp.data.socketId;
}
```

##### **ESP-IDF**

```cpp
WalterModemRsp rsp = {};
int socketId = 0;
if(modem.socketConfig(&rsp)) {
    ESP_LOGI("socket", "configured successfully");
    socketId = rsp.data.socketId;
}
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

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

##### **ESP-IDF**

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

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

### `socketConfigExtended`

Configure the socket extended parameters.
This function confgiures the socket extended parameters.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
if(modem.socketConfigExtended(NULL,NULL,NULL,1,WALTER_MODEM_SOCKET_RING_MODE_DATA_VIEW)) {
    Serial.printf("socket: Successfully  extended the socket configuration\n");
} else {
    Serial.printf("socket: Could not configure the socket\n");
}
```

##### **ESP-IDF**

```cpp
if(modem.socketConfigExtended(NULL,NULL,NULL,1,WALTER_MODEM_SOCKET_RING_MODE_DATA_VIEW)) { 
    ESP_LOGI("socket", "Successfully extended the socket configuration"); 
} else { 
    ESP_LOGI("socket", "Could not configure the socket"); 
}
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

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

##### **ESP-IDF**

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


<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

### `socketDial`

Dial a socket after which data can be exchanged.

This function will dial a socket to a remote host.
When the dial is successful data can be exchanged.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
/**
 * @brief The address of the Walter demo server.
 */
CONFIG(SERV_ADDR, const char *, "walterdemo.quickspot.io")

/**
 * @brief The UDP port of the Walter demo server.
 */
CONFIG_INT(SERV_PORT, 1999)

if(modem.socketDial(SERV_ADDR, SERV_PORT)) {
    Serial.printf("socket: Connected to demo server %s:%d\n", SERV_ADDR, SERV_PORT);
} else {
    Serial.printf("socket: Could not connect demo socket\n");
}

```

##### **ESP-IDF**

```cpp
/**
 * @brief The address of the Walter demo server.
 */
CONFIG(SERV_ADDR, const char *, "walterdemo.quickspot.io")

/**
 * @brief The UDP port of the Walter demo server.
 */
CONFIG_INT(SERV_PORT, 1999)


if(modem.socketDial(SERV_ADDR, SERV_PORT)) {
    ESP_LOGI("socket", "Connected to demo server %s:%d", SERV_ADDR, SERV_PORT);
} else {
    ESP_LOGI("socket", "Could not connect demo socket");
}
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

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

##### **ESP-IDF**

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

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

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
#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
/**
 * @brief The buffer to transmit to the UDP server. The first 6 bytes will be
 * the MAC address of the Walter this code is running on.
 */
uint8_t dataBuf[8] = { 0 };
esp_read_mac(dataBuf, ESP_MAC_WIFI_STA);

dataBuf[6] = counter >> 8;
dataBuf[7] = counter & 0xFF;

if(modem.socketSend(dataBuf, 8)) {
    Serial.printf("socket: Transmitted data %d\n", counter);
    counter += 1;
} else {
    Serial.printf("socket: Could not transmit data\n");
    delay(1000);
    ESP.restart();
}

```

##### **ESP-IDF**

```cpp
/**
 * @brief The buffer to transmit to the UDP server. The first 6 bytes will be
 * the MAC address of the Walter this code is running on.
 */
uint8_t dataBuf[8] = { 0 };
esp_read_mac(dataBuf, ESP_MAC_WIFI_STA);

dataBuf[6] = counter >> 8;
dataBuf[7] = counter & 0xFF;

if(modem.socketSend(dataBuf, 8)) {
      ESP_LOGI("socket", "Transmitted data %d", counter);
      counter += 1;
} else {
      ESP_LOGI("socket", "Could not transmit data");
      vTaskDelay(pdMS_TO_TICKS(1000));
      esp_restart();
}
```

<!-- tabs:end -->

#### params

<!-- tabs:start -->

##### **Arduino**

| Param      | Description                                                                      | Default                      |
| ---------- | -------------------------------------------------------------------------------- | ---------------------------- |
| `data`     | The data to send.                                                                |                              |
| `dataSize` | The number of bytes to transmit.                                                 |                              |
| `rsp`      | Pointer to a modem response structure to save the result of the command in.      | **NULL**                     |
| `cb`       | Optional callback argument, when not NULL this function will return immediately. | **NULL**                     |
| `args`     | Optional argument to pass to the callback.                                       | **NULL**                     |
| `rai`      | The release assistance information.                                              | **WALTER_MODEM_RAI_NO_INFO** |
| `socketId` | The id of the socket to close or **-1 to re-use the last one.**                  | **-1**                       |

##### **ESP-IDF**

| Param      | Description                                                                      | Default                      |
| ---------- | -------------------------------------------------------------------------------- | ---------------------------- |
| `data`     | The data to send.                                                                |                              |
| `dataSize` | The number of bytes to transmit.                                                 |                              |
| `rsp`      | Pointer to a modem response structure to save the result of the command in.      | **NULL**                     |
| `cb`       | Optional callback argument, when not NULL this function will return immediately. | **NULL**                     |
| `args`     | Optional argument to pass to the callback.                                       | **NULL**                     |
| `rai`      | The release assistance information.                                              | **WALTER_MODEM_RAI_NO_INFO** |
| `socketId` | The id of the socket to close or **-1 to re-use the last one.**                  | **-1**                       |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

### `socketAccept`

Accepts an incoming socket connection.

This function will accept an incoming connection after a ring event has been received.

> [!NOTE]
> This function must be preceded by a call to [socketListen](#socketlisten).

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
if(modem.socketAccept()) {
    Serial.printl("socket: Successfully accepted incoming socket connection");
} else {
    Serial.printl("socket: Could not accepted incoming socket connection");
}
```

##### **ESP-IDF**

```cpp
if(modem.socketAccept()) {
    ESP_LOGI("socket", "Successfully accepted incoming socket connection");
} else {
    ESP_LOGI("socket", "Could not accepted incoming socket connection");
}
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

| Param         | Description                                                      | Default   |
| ------------- | ---------------------------------------------------------------- | --------- |
| `rsp`         | Optional modem response structure to save the result in.         | **NULL**  |
| `cb`          | Optional callback function, if set this function will not block. | **NULL**  |
| `args`        | Optional argument to pass to the callback.                       | **NULL**  |
| `socketId`    | The ID of the socket to close or **-1 to re-use the last one.**  | **-1**    |
| `commandMode` | Whether to use command mode for the operation.                   | **false** |


##### **ESP-IDF**

| Param         | Description                                                      | Default   |
| ------------- | ---------------------------------------------------------------- | --------- |
| `rsp`         | Optional modem response structure to save the result in.         | **NULL**  |
| `cb`          | Optional callback function, if set this function will not block. | **NULL**  |
| `args`        | Optional argument to pass to the callback.                       | **NULL**  |
| `socketId`    | The ID of the socket to close or **-1 to re-use the last one.**  | **-1**    |
| `commandMode` | Whether to use command mode for the operation.                   | **false** |

<!-- tabs:end -->


#### Returns

`bool`
True on success, False otherwise.

---

### `socketListen`

This function makes the modem listen for incoming socket connections.

> [!WARNING]
> Only one incoming socket connection can be handled at a time.

> [!NOTE]
> listens to TCP sockets by default.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
if(modem.socketListen()) {
    Serial.printl("socket: Successfully started listening for incoming socket connections");
} else {
    Serial.printl("socket: Failed to start listening for incoming socket Connections");
}
```

##### **ESP-IDF**

```cpp
if(modem.socketListen()) {
    ESP_LOGI("socket", "Successfully started listening for incoming socket connections");
} else {
    ESP_LOGI("socket", "Failed to start listening for incoming socket Connections");
}
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

| Param              | Description                                                      | Default                                   |
| ------------------ | ---------------------------------------------------------------- | ----------------------------------------- |
| `rsp`              | Optional modem response structure to save the result in.         | **NULL**                                  |
| `cb`               | Optional callback function, if set this function will not block. | **NULL**                                  |
| `args`             | Optional argument to pass to the callback.                       | **NULL**                                  |
| `socketId`         | The ID of the socket to listen or **-1 to re-use the last one.** | **-1**                                    |
| `protocol`         | The protocol of the listening socket.                            | **WALTER_MODEM_SOCKET_PROTO_TCP**         |
| `listenState`      | The state to listen on.                                          | **WALTER_MODEM_SOCKET_LISTEN_STATE_IPV4** |
| `socketListenPort` | The port to listen on.                                           | **0**                                     |

##### **ESP-IDF**

| Param              | Description                                                      | Default                                   |
| ------------------ | ---------------------------------------------------------------- | ----------------------------------------- |
| `rsp`              | Optional modem response structure to save the result in.         | **NULL**                                  |
| `cb`               | Optional callback function, if set this function will not block. | **NULL**                                  |
| `args`             | Optional argument to pass to the callback.                       | **NULL**                                  |
| `socketId`         | The ID of the socket to listen or **-1 to re-use the last one.** | **-1**                                    |
| `protocol`         | The protocol of the listening socket.                            | **WALTER_MODEM_SOCKET_PROTO_TCP**         |
| `listenState`      | The state to listen on.                                          | **WALTER_MODEM_SOCKET_LISTEN_STATE_IPV4** |
| `socketListenPort` | The port to listen on.                                           | **0**                                     |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

### `socketDidRing`

check if the Socket received a Ring URC.

> [!WARNING]
> rings will be halted until the data has been received.

> [!WARNING]
> The target buffer will only be filled when ringMode is set to WALTER_MODEM_SOCKET_RING_MODE_DATA_VIEW in [socketConfigExtended](#socketconfigextended).

> [!TIP]
> use the socket event handler to now when data has been received.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
if(modem.socketDidRing(1)){
    Serial.println("socket: received ring notification");
    //receive data.
}
```

##### **ESP-IDF**

```cpp
if(modem.socketDidRing(1)){
    ESP_LOGI("socket", "received ring notification");
    //receive data.
}
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

| Param           | Description                                                                  | Default     |
| --------------- | ---------------------------------------------------------------------------- | ----------- |
| `socketId`      | The ID of the socket to wait for the ring, or **-1 to re-use the last one.** | **-1**      |
| `targetBufSize` | The size of the target buffer.                                               | **0**       |
| `targetBuf`     | The buffer to store the received data in.                                    | **nullptr** |

##### **ESP-IDF**

| Param           | Description                                                                  | Default     |
| --------------- | ---------------------------------------------------------------------------- | ----------- |
| `socketId`      | The ID of the socket to wait for the ring, or **-1 to re-use the last one.** | **-1**      |
| `targetBufSize` | The size of the target buffer.                                               | **0**       |
| `targetBuf`     | The buffer to store the received data in.                                    | **nullptr** |

<!-- tabs:end -->

#### Returns

`bool`
True on ring received, False otherwise.

---

### `socketReceive`

Receive data from an incoming socket connection, or from the remote server.

> [!TIP]
> make sure you have received a ring notification beforehand.

> [!tip]
> use the size retrieved from the event handler.
> 
#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
uint8_t ringBuffer[1500];

if(modem.socketReceive(1500,ringBuffer)) {
    Serial.printl("socket: Successfully received the data");
} else {
    Serial.printl("socket: Could not receive the data");
}
```

##### **ESP_IDF**

```cpp
uint8_t ringBuffer[1500];

if(modem.socketReceive(1500,ringBuffer)) {
    ESP_LOGI("socket", "Successfully received the data");
} else {
    ESP_LOGI("socket", "Could not receive the data");
}
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

| Param           | Description                                              | Default  |
| --------------- | -------------------------------------------------------- | -------- |
| `targetBufSize` | The size of the target buffer.                           |          |
| `targetBuf`     | The target buffer to write the data to.                  |          |
| `socketId`      | The socket ID to receive from.                           | **-1**   |
| `rsp`           | Optional modem response structure to save the result in. | **NULL** |

##### **ESP-IDF**

| Param           | Description                                              | Default  |
| --------------- | -------------------------------------------------------- | -------- |
| `targetBufSize` | The size of the target buffer.                           |          |
| `targetBuf`     | The target buffer to write the data to.                  |          |
| `socketId`      | The socket ID to receive from.                           | **-1**   |
| `rsp`           | Optional modem response structure to save the result in. | **NULL** |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

<!-- tabs:start -->

### `socketClose`

Close a socket connection.

> [!WARNING]
> Sockets can only be **closed** when they are **suspended or inactive**.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
if(modem.socketClose()) {
    Serial.printl("socket: Successfully closed the socket");
} else {
    Serial.printl("socket: Could not close the socket");
}
```

##### **ESP-IDF**

```cpp
if(modem.socketClose()) { 
    ESP_LOGI("socket", "Successfully closed the socket"); 
} else { 
    ESP_LOGI("socket", "Could not close the socket"); 
}
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

| Param      | Description                                                                      | Default  |
| ---------- | -------------------------------------------------------------------------------- | -------- |
| `rsp`      | Pointer to a modem response structure to save the result of the command in.      | **NULL** |
| `cb`       | Optional callback argument, when not NULL this function will return immediately. | **NULL** |
| `args`     | Optional argument to pass to the callback.                                       | **NULL** |
| `socketId` | The id of the socket to close or **-1 to re-use the last one.**                  | **-1**   |

##### **ESP-IDF**

| Param      | Description                                                                      | Default  |
| ---------- | -------------------------------------------------------------------------------- | -------- |
| `rsp`      | Pointer to a modem response structure to save the result of the command in.      | **NULL** |
| `cb`       | Optional callback argument, when not NULL this function will return immediately. | **NULL** |
| `args`     | Optional argument to pass to the callback.                                       | **NULL** |
| `socketId` | The id of the socket to close or **-1 to re-use the last one.**                  | **-1**   |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

## Enums

### `WalterModemSocketProto`

The protocol that us used by the socket.

<!-- tabs:start -->

#### **Arduino**

> **WALTER_MODEM_SOCKET_PROTO_TCP** = `0` \
> Use the TCP protocol for the socket \
> **WALTER_MODEM_SOCKET_PROTO_UDP** = `1` \
> Use the UDP protocol for the socket

#### **ESP-IDF**

> **WALTER_MODEM_SOCKET_PROTO_TCP** = `0` \
> Use the TCP protocol for the socket \
> **WALTER_MODEM_SOCKET_PROTO_UDP** = `1` \
> Use the UDP protocol for the socket

<!-- tabs:end -->

### `WalterModemSocketAcceptAnyRemote`

Possible methodologies on how a socket handles data from other hosts
besides the IP-address and remote port it is configured for.

<!-- tabs:start -->

#### **Arduino**

> **WALTER_MODEM_ACCEPT_ANY_REMOTE_DISABLED** = `0`\
> Do not accepty any remote data \
> **WALTER_MODEM_ACCEPT_ANY_REMOTE_RX_ONLY** = `1`\
> Only acccept read \
> **WALTER_MODEM_ACCEPT_ANY_REMOTE_RX_AND_TX** = `2` \
> Accept read write from remote

#### **ESP-IDF**

> **WALTER_MODEM_ACCEPT_ANY_REMOTE_DISABLED** = `0`\
> Do not accepty any remote data \
> **WALTER_MODEM_ACCEPT_ANY_REMOTE_RX_ONLY** = `1`\
> Only acccept read \
> **WALTER_MODEM_ACCEPT_ANY_REMOTE_RX_AND_TX** = `2` \
> Accept read write from remote

<!-- tabs:end -->

### `WalterModemSocketRingMode`

This enumeration determines how the **SQNSRING** message should be **formatted**.

<!-- tabs:start -->

#### **Arduino**

> **WALTER_MODEM_SOCKET_RING_MODE_NORMAL** = `0` \
> Only the socket id is in the URC. \
> **WALTER_MODEM_SOCKET_RING_MODE_DATA_AMOUNT** = `1` \
> The received data amount has been added to the URC \
> **WALTER_MODEM_SOCKET_RING_MODE_DATA_VIEW** = `2` \
> The URC contains the data amount and the payload

#### **ESP-IDF**

> **WALTER_MODEM_SOCKET_RING_MODE_NORMAL** = `0` \
> Only the socket id is in the URC. \
> **WALTER_MODEM_SOCKET_RING_MODE_DATA_AMOUNT** = `1` \
> The received data amount has been added to the URC \
> **WALTER_MODEM_SOCKET_RING_MODE_DATA_VIEW** = `2` \
> The URC contains the data amount and the payload

<!-- tabs:end -->

### `WalterModemSocketRecvMode`

This enumeration determines in what way the **payload data** should be returned.

<!-- tabs:start -->

#### **Arduino**

> **WALTER_MODEM_SOCKET_RECV_MODE_TEXT** = `0` \
> Receive the payload data as raw byte text. \
> **WALTER_MODEM_SOCKET_RECV_MODE_HEX** = `1` \
> Receive the payload data as a hex string

#### **ESP-IDF**

> **WALTER_MODEM_SOCKET_RECV_MODE_TEXT** = `0` \
> Receive the payload data as raw byte text. \
> **WALTER_MODEM_SOCKET_RECV_MODE_HEX** = `1` \
> Receive the payload data as a hex string

<!-- tabs:end -->

### `WalterModemSocketListenMode`

This enumeration determines whether an incoming socket connection should be auto accepted.

<!-- tabs:start -->

#### **Arduino**

> **WALTER_MODEM_SOCKET_LISTEN_MODE_DISABLED** = `0` \
> Incoming socket connections will `not` be auto accepted \
> **WALTER_MODEM_SOCKET_LISTEN_MODE_ENABLED** = `1` \
> Incoming socket connections will be auto accepted

#### **ESP-IDF**

> **WALTER_MODEM_SOCKET_LISTEN_MODE_DISABLED** = `0` \
> Incoming socket connections will `not` be auto accepted \
> **WALTER_MODEM_SOCKET_LISTEN_MODE_ENABLED** = `1` \
> Incoming socket connections will be auto accepted

<!-- tabs:end -->

### `WalterModemsocketSendMode`

This enumeration determines how the send data should be `expected`.

<!-- tabs:start -->

#### **Arduino**

> **WALTER_MODEM_SOCKET_SEND_MODE_TEXT** = `0` \
> Expect the payload data as a raw byte string \
> **WALTER_MODEM_SOCKET_SEND_MODE_HEX** = `1` \
> Expect the payload data as a hex string

#### **ESP-IDF**

> **WALTER_MODEM_SOCKET_SEND_MODE_TEXT** = `0` \
> Expect the payload data as a raw byte string. \
> **WALTER_MODEM_SOCKET_SEND_MODE_HEX** = `1` \
> Expect the payload data as a hex string.

<!-- tabs:end -->

### `WalterModemSocketListenState`

This enumeration represents the listen state of the socket.

<!-- tabs:start -->

#### **Arduino**

> **WALTER_MODEM_SOCKET_LISTEN_STATE_CLOSE** = `0` \
> Close a listening socket. \
> **WALTER_MODEM_SOCKET_LISTEN_STATE_IPV4** = `1` \
> Open a listening IPV4 socket. \
> **WALTER_MODEM_SOCKET_LISTEN_STATE_IPV6** = `2`

#### **ESP-IDF**

> **WALTER_MODEM_SOCKET_LISTEN_STATE_CLOSE** = `0` \
> Close a listening socket. \
> **WALTER_MODEM_SOCKET_LISTEN_STATE_IPV4** = `1` \
> Open a listening IPV4 socket. \
> **WALTER_MODEM_SOCKET_LISTEN_STATE_IPV6** = `2`

<!-- tabs:end -->