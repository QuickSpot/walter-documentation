## Methods Overview

- [createSocket](#createsocket)
- [configSocket](#configsocket)
- [connectSocket](#connectsocket)
- [socketSend](#socketsend)
- [closeSocket](#closesocket)

## Enums Overview

- [WalterModemSocketProto](#waltermodemsocketproto)
- [WalterModemSocketAcceptAnyRemote](#waltermodemsocketacceptanyremote)

---

## Methods

### `createSocket`

Create a new socket in a certain PDP context.

This function will create a new socket.
After socket creation one can set additional socket settings
and use the socket for communication.

> [!NOTE]
> id's are from **1-6**.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
WalterModemRsp rsp = {};
int socketId = 0;
if(modem.createSocket(&rsp)) {
    Serial.printf("socket created successfully\n");
    socketId = rsp.data.socketId;
}
```

##### **ESP-IDF**

```cpp
WalterModemRsp rsp = {};
int socketId = 0;
if(modem.createSocket(&rsp)) {
    ESP_LOGI("socket", "created successfully");
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

### `configSocket`

This step is required for the library
to correctly configure the modem to use this socket.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
if(modem.configSocket()) {
    Serial.printf("socket: Successfully configured the socket\n");
} else {
    Serial.printf("socket: Could not configure the socket\n");
}
```

##### **ESP-IDF**

```cpp
if(modem.configSocket()) { 
    ESP_LOGI("socket", "Successfully configured the socket"); 
} else { 
    ESP_LOGI("socket", "Could not configure the socket"); 
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
| `socketId` | The id of the socket to connect or **-1 to re-use the last one.**                | **-1**   |

##### **ESP-IDF**

| Param      | Description                                                                      | Default  |
| ---------- | -------------------------------------------------------------------------------- | -------- |
| `rsp`      | Pointer to a modem response structure to save the result of the command in.      | **NULL** |
| `cb`       | Optional callback argument, when not NULL this function will return immediately. | **NULL** |
| `args`     | Optional argument to pass to the callback.                                       | **NULL** |
| `socketId` | The id of the socket to connect or **-1 to re-use the last one.**                | **-1**   |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

### `connectSocket`

Connect a socket after which data can be exchanged.

This function will connect a socket to a remote host.
When the connection was successful data can be exchanged.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
/**
 * @brief The address of the server to upload the data to. 
 */
#define SERV_ADDR "64.225.64.140"

/**
 * @brief The port on which the server is listening.
 */
#define SERV_PORT 1999

if(modem.connectSocket(SERV_ADDR, SERV_PORT, SERV_PORT)) {
    Serial.printf("socket: Connected to server %s:%d\n", SERV_ADDR, SERV_PORT);
} else {
    Serial.printf("socket: Could not connect socket\n");
}

```

##### **ESP-IDF**

```cpp
/**
 * @brief The address of the server to upload the data to. 
 */
#define SERV_ADDR "64.225.64.140"

/**
 * @brief The port on which the server is listening.
 */
#define SERV_PORT 1999

if(modem.connectSocket(SERV_ADDR, SERV_PORT, SERV_PORT)) {
    ESP_LOGI("socket", "Connected to server %s:%d", SERV_ADDR, SERV_PORT);
} else {
    ESP_LOGI("socket", "Could not connect socket");
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
> The maximum size of the data buffer is **1500 bytes**.

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

### `closeSocket()`

Close a socket connection.

> [!WARNING]
> Sockets can only be **closed** when they are **suspended or inactive**.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
if(modem.closeSocket()) {
    Serial.printf("socket: Successfully closed the socket\n");
} else {
    Serial.printf("socket: Could not close the socket\n");
}
```

##### **ESP-IDF**

```cpp
if(modem.closeSocket()) { 
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
