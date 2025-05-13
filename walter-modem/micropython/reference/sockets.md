## Methods Overview

- [create_socket](#create_socket)
- [connect_socket](#connect_socket)
- [socket_send](#socket_send)
- [close_socket](#close_socket)

## Enums Overview

- [WalterModemSocketProto](#waltermodemsocketproto)
- [WalterModemSocketAcceptAnyRemote](#waltermodemsocketacceptanyremote)

---

## Methods

### `create_socket`

Creates a new socket in a specified PDP context

> [!NOTE]
> Id's range from **1-6**.

#### Example

```py
modem_rsp = ModemRsp()
socket_id: int

if await modem.create_socket(rsp=modem_rsp):
    print('socket created successfully')
    socket_id = modem_rsp.socket_id
```

#### Params

| Param              | Description                                                             | Default  |
| ------------------ | ----------------------------------------------------------------------- | -------- |
| `pdp_context_id`   | The PDP context id.                                                     | **1**    |
| `mtu`              | The maximum transmission unit used by the socket.                       | **300**  |
| `exchange_timeout` | The maximum number of seconds this socket can be inactive.              | **90**   |
| `conn_timeout`     | The maximum number of seconds this socket is allowed to try to connect. | **60**   |
| `send_delay_ms`    | The number of milliseconds send delay.                                  | **5000** |
| `rsp`              | Reference to a modem response instance.                                 | **None** |

#### Returns

`bool`
True on success, False otherwise.

---

### `connect_socket`

Connects a socket to a remote host,
allowing data exchange once the connection is successful.

#### Example

```py
SERV_ADDR = '64.255.64.140'
"""The address of the server to upload the data to"""

SERV_PORT = 1999
"""The port on which the server is listening"""

if await modem.connect_socket(
    remote_host=SERV_ADDR,
    remote_port=SERV_PORT,
    local_port=SERV_PORT
):
    print(f'Connected to server {SERV_ADDR}:{SERV_PORT}')
else:
    print('Could not connect socket')
```

#### Params

| Param               | Description                                                            | Default                                 |
| ------------------- | ---------------------------------------------------------------------- | --------------------------------------- |
| `remote_host`       | The remote IPv4/IPv6 or hostname to connect to.                        |                                         |
| `remote_port`       | The remote port to connect on.                                         |                                         |
| `local_port`        | The local port in case of an UDP socket.                               |                                         |
| `socket_id`         | The id of the socket to connect.                                       | **1**                                   |
| `protocol`          | The [protocol](#waltermodemsocketproto) to use, UDP by default.        | **ModemSocketProto.UDP**                |
| `accept_any_remote` | How to [accept remote](#waltermodemsocketacceptanyremote) UDP packets. | **ModemSocketAcceptAnyRemote.DISABLED** |
| `rsp`               | Reference to a modem response instance.                                | **None**                                |

#### Returns

`bool`
True on success, False otherwise.

---

### `socket_send`

Send data over a socket.

#### Example

```py
async def loop():
    global counter
    global socket_id
    data_buffer: bytearray = bytearray(network.WLAN().config('mac'))
    data_buffer.append(counter >> 8)
    data_buffer.append(counter & 0xff)

    print('Attempting to transmit data')
    if not await modem.socket_send(data=data_buffer, socket_id=socket_id):
        print('Failed to transmit data')
        return False
    
    print(f'Transmitted counter value: {counter}')
    counter += 1

    await asyncio.sleep(10)
```

#### params

| Param       | Description                         | Default              |
| ----------- | ----------------------------------- | -------------------- |
| `data`      | The data to send.                   |                      |
| `socket_id` | The id of the socket to send over.  | **1**                |
| `rai`       | The release assistance information. | **ModemRai.NO_INFO** |
| `rsp`       | Reference to a modem instance.      | **None**             |

#### Returns

`bool`
True on success, False otherwise.

---

### `close_socket`

Close a socket connection.

> [!WARNING]
> Sockets can only be **closed** when they are **suspended or inactive**.

#### Example

```py
if await modem.close_socket():
    print('Successfully closed the socket')
else:
    print('Could not close the socket')
```

#### Params

| Param       | Description                    | Default  |
| ----------- | ------------------------------ | -------- |
| `socket_id` | The id of the socket to close. | **1**    |
| `rsp`       | Reference to a modem instance. | **None** |

#### Returns

`bool`
True on success, False otherwise.

---

## Enums

### `WalterModemSocketProto`

The protocol that us used by the socket.

> **TCP** = `0` \
> Use the TCP protocol for the socket \
> **UDP** = `1` \
> Use the UDP protocol for the socket

### `WalterModemSocketAcceptAnyRemote`

Possible methodologies on how a socket handles data from other hosts
besides the IP-address and remote port it is configured for.

> **DISABLED** = `0`\
> Do not accepty any remote data \
> **REMOTE_RX_ONLY** = `1`\
> Only acccept read \
> **REMOTE_RX_AND_TX** = `2` \
> Accept read write from remote
