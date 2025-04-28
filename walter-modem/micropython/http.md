## Methods Overview

- [httpConfigProfile](#httpconfigprofile)
- [httpSend](#httpsend)
- [httpQuery](#httpquery)
- [httpDidRing](#httpdidring)

## Enums Overview

- [WalterModemHttpSendCmd](#waltermodemhttpsendcmd)
- [WalterModemHttpQueryCmd](#waltermodemhttpquerycmd)
- [WalterModemHttpPostParam](#waltermodemhttppostparam)

---

## Methods

### `httpConfigProfile`

Configure a HTTP profile.

This function will configure a HTTP profile
with parameters such as server name and auth info.
The profile info is stored persistently in the modem, so it is possible
to store connection info once, using an Arduino sketch to prepare all settings,
and later rely on this preconfigured profile in the modem without the need to
set the parameters again in the actual Arduino sketch used in production.

> [!WARNING]
> You first need call tlsConfigProfile.

> [!NOTE]
> **File uploads/downloads** not supported.

#### Example

```py
HTTP_PROFILE = 1
TLS_PROFILE = 1

if await modem.http_config_profile(
    profile_id=HTTP_PROFILE,
    server_address="tls13.akamai.io",
    port=443,
    tls_profile_id=TLS_PROFILE
):
    print('Successfully configured the HTTP profile')
else:
    print('Failed to configure HTTP profile')

```
#### Params

| Param            | Description                                      | Default   |
| ---------------- | ------------------------------------------------ | --------- |
| `profile_id`     | HTTP profile id (0, 1 or 2).                     |           |
| `server_address` | The server name to connect to.                   |           |
| `port`           | The port of the server to connect to.            | **80**    |
| `use_basic_auth` | Set true to use basic auth and send username/pw. | **False** |
| `auth_user`      | Username.                                        | **""**    |
| `auth_pass`      | Password.                                        | **""**    |
| `tls_profile_id` | If not 0, TLS is used with the given profile.    | **None**  |
| `rsp`            | Reference to a modem response instance.          | **None**  |

#### Returns

`bool`
True on success, False otherwise.

---

### `httpSend`

Perform a http **POST** or **PUT** request.

No need to first open the connection with the buggy httpConnect command
unless you need TLS + a private key.

#### Example

```py
modem_rsp = ModemRsp()
data_buf = bytearray(8)

if await modem.http_send(
    profile_id=HTTP_PROFILE,
    uri='/',
    data=data_buf,
    send_cmd=WalterModemHttpSendCmd.POST,
    post_param=WalterModemHttpPostParam.OCTET_STREAM,
    rsp=modem_rsp
):
    print('HTTP query performed')
else:
    print('HTTP query failed')
```
#### Params

| Param        | Description                                               | Default                                  |
| ------------ | --------------------------------------------------------- | ---------------------------------------- |
| `profile_id` | The profile id (0, 1 or 2) of the HTTP context.         |                                          |
| `uri`        | The URI.                                                  |                                          |
| `data`       | Data to be sent to the server.                            |                                          |
| `send_cmd`   | POST or PUT [command](#waltermodemhttpsendcmd).           | **WalterModemHttpSendCmd.POST**          |
| `post_param` | [Content type](#waltermodemhttppostparam) *(enum value)*. | **WalterModemHttpPostParam.UNSPECIFIED** |
| `rsp`        | Reference to a modem response instance.                   | **None**                                 |

#### Returns

`bool`
True on success, False otherwise.

---

### `httpQuery`

Perform a http **GET**, **DELETE** or **HEAD** request.

No need to first open the connection with the buggy httpConnect command
unless you need TLS + a private key.

#### Example

```py
modem_rsp = ModemRsp()

if await modem.http_query(
    profile_id=HTTP_PROFILE,
    uri='/',
    query_cmd=WalterModemHttpQueryCmd.GET,
    rsp=modem_rsp
):
    print('HTTP query performed')
else:
    print('HTTP query failed')
```

#### Params

| Param               | Description                                                     | Default                         |
| ------------------- | --------------------------------------------------------------- | ------------------------------- |
| `profile_id`        | The profile id (0, 1 or 2) of the HTTP context.               |                                 |
| `uri`               | The URI.                                                        |                                 |
| `query_cmd`         | GET, DELETE, or HEAD [command](#waltermodemhttpquerycmd).       | **WalterModemHttpQueryCmd.GET** |
| `extra_header_line` | Optional additional lines to be placed in the request's header. | **None**                        |
| `rsp`               | Reference to a modem response instance.                         | **None**                        |

#### Returns

`bool`
True on success, False otherwise.

---

### `httpDidRing`

Fetch http response to earlier http request, if any

#### Example

```py
modem_rsp = ModemRsp()

while not await modem.http_did_ring(profile_id=HTTP_PROFILE, rsp=modem_rsp):
    if modem_rsp.result not in (WalterModemState.OK, WalterModemState.AWAITING_RING):
        print(f"Error: {modem_rsp.result}")
        break
    await asyncio.sleep(1)

if modem_rsp.http_response is not None:
    print(f'HTTP status code: {modem_rsp.http_response.http_status}')
    print(f'HTTP content type: {modem_rsp.http_response.content_type}')
    print(f'HTTP: {modem_rsp.http_response.data}')
```

#### Params

| Param        | Description                             | Default  |
| ------------ | --------------------------------------- | -------- |
| `profile_id` | Profile for which to get the response.  |          |
| `rsp`        | Reference to a modem response instance. | **None** |

#### Returns

`bool`
True on success, False otherwise.

---

## Enums

### `WalterModemHttpSendCmd`

The possible commands for a HTTP send operation.

> **POST** = `0` \
> Perform a POST request \
> **PUT** = `1` \
> Perform PUT request

### `WalterModemHttpQueryCmd`

The possible commands for a HTTP query operation.

> **GET** = `0` \
> Perform a GET request \
> **HEAD** = `1` \
> Perform a HEAD request \
> **DELETE** = `2` \
> Perform a DELETE request

### `WalterModemHttpPostParam`

The possible post params for a HTTP send operation.

> **URL_ENCODED** = `0` \
> Param type is encoded in the url \
> **TEXT_PLAIN** = `1` \
> Param is plain text \
> **OCTET_STREAM** = `2` \
> Param is an octet/byte stream \
> **FORM_DATA** = `3` \
> Param is form data \
> **JSON** = `4` \
> Param is JSON \
> **UNSPECIFIED** = `99` \
> Param is unspecified
