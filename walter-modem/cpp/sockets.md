# sockets
### methods overview

- [createSocket](#createsocket)
- [configSocket](#configSocket)
- [connectSocket]()
- [socketSend]()
- [closeSocket]()

## methods
---
### `createSocket`
> Create a new socket in a certain PDP context.
>
> This function will create a new socket. \
> After socket creation one can set additional socket settings and use the socket for communication.

> [!NOTE]
> id's are from 1-6
> 
<!-- tabs:start -->
#### **Arduino**
```cpp
WalterModemRsp rsp = {};
int socketId = 0;
if(modem.createSocket(&rsp)) {
    Serial.printf("socket created successfully\n");
    socketId = rsp.data.socketId;
}
```
#### **ESP-IDF**
```cpp
WalterModemRsp rsp = {};
int socketId = 0;
if(modem.createSocket(&rsp)) {
    ESP_LOGI("socket", "created successfully");
    socketId = rsp.data.socketId;
}
```
#### **Micropython**
<!-- tabs:end -->

#### params:

<!-- tabs:start -->
#### **Arduino / ESP-IDF**
| Param | Description | Default
| --- | --- | ---
| `rsp` | Pointer to a [modem response structure]() to save the result of the command in. When NULL is given the result is ignored. | **None** |
| `cb` | Optional callback argument, when not NULL this function will return immediately. | **nullptr** |
| `args` | Optional argument to pass to the callback. | **nullptr** |
| `pdpCtxId` | The PDP context id or -1 to re-use the last one. | **-1** |
| `mtu`  | The maximum transmission unit used by the socket. | **300** |
| `exchangeTimeout` | The maximum number of seconds this socket can be inactive. | **90** |
| `connTimeout` | The maximum number of seconds this socket is allowed to try to connect | **60** |
| `sendDelayMs` | The number of milliseconds send delay | **5000** |

#### **Micropython**

| Param | Description | Default
| --- | --- | ---
| `pdp_context_id` | The PDP context id or -1 to re-use the last one. | **-1** |
| `mtu`  | The maximum transmission unit used by the socket. | **300** |
| `exchange_timeout` | The maximum number of seconds this socket can be inactive. | **90** |
| `conn_timeout` | The maximum number of seconds this socket is allowed to try to connect | **60** |
| `send_delay_ms` | The number of milliseconds send delay | **5000** |

<!-- tabs:end -->

### Returns:
`bool`
True on success, false otherwise.

---

### `configSocket`
> This step is required for the library to correctly configure the modem to use this socket.

#### params:
<!-- tabs:start -->
#### **Arduino / ESP-IDF**
| Param      | Description                                                                      | Default  |
| ---------- | -------------------------------------------------------------------------------- | -------- |
| `rsp`      | Pointer to a modem response structure to save the result of the command in.      | **NULL** |
| `cb`       | Optional callback argument, when not NULL this function will return immediately. | **NULL** |
| `args`     | Optional argument to pass to the callback.                                       | **NULL** |
| `socketId` | The id of the socket to connect or -1 to re-use the last one.                    | **-1**   |



#### **Micropython**
| Param | Description | Default |
| ----- | ----------- | ------- |

<!-- tabs:end -->

### Returns:
`bool`
True on success, false otherwise.