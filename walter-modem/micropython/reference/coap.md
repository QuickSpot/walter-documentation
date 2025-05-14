## Methods Overview

- [coap_context_create](#coap_context_create)
- [coap_context_close](#coap_context_close)
- [coap_set_options](#coap_set_options)
- [coap_set_header](#coap_set_header)
- [coap_send](#coap_send)
- [coap_receive_data](#coap_receive_data)
- [coap_receive_options](#coap_receive_options)

## Enums Overview

- [WalterModemCoapCloseCause](#waltermodemcoapclosecause)
- [WalterModemCoapReqResp](#waltermodemcoapreqresp)
- [WalterModemCoapType](#waltermodemcoaptype)
- [WalterModemCoapMethod](#waltermodemcoapmethod)
- [WalterModemCoapResponseCode](#waltermodemcoapresponsecode)
- [WalterModemCoapOptionAction](#waltermodemcoapoptionaction)
- [WalterModemCoapOption](#waltermodemcoapoption)
- [WalterModemCoapContentType](#waltermodemcoapcontenttype)

---

## Methods

### `coap_context_create`

Create a CoAP context, required to perform CoAP related operations.

If the server_address & server_port are omitted and only local_port is provided,
the context is created in isten mode, waiting for an incoming connection.

#### Example

```py
await modem.coap_context_create(
    ctx_id=0,
    server_address='coap.me',
    server_port=5683
)

# Or listen mode :
# (server_address & server_port are omitted, only local_port is set)
await modem.coap_context_create(
    ctx_id=1,
    local_port=5683
)
```

#### Params

| Param               | Description                                                                                                                                          | Default   |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| `ctx_id`            | Context profile identifier (0, 1, 2)                                                                                                                 |           |
| `server_address`    | IP address/hostname  of the CoAP server                                                                                                              | **None**  |
| `server_port`       | The UDP remote port of the CoAP server                                                                                                               | **None**  |
| `local_port`        | The UDP local port, if omitted, a randomly available port is assigned (recommended)                                                                  | **None**  |
| `timeout`           | The time, in seconds, to wait for a response from the CoAP server before aborting (1-120) *(independent of the ACK_TIMEOUT used for retransmission)* | **20**    |
| `dtls`              | Whether or not to use DTLS encryption                                                                                                                | **False** |
| `secure_profile_id` | The SSL/TLS security profile configuration (ID) to use.                                                                                              | **None**  |
| `rsp`               | Reference to a modem response instance                                                                                                               | **None**  |

#### Returns

`bool`
True on success, False on failure

---

### `coap_context_close`

Close a CoAP context.

#### Example

```py
await modem.coap_context_close(ctx_id=1)
```

#### Params

| Param    | Description                            | Default  |
| -------- | -------------------------------------- | -------- |
| `ctx_id` | Context profile identifier (0, 1, 2)   |          |
| `rsp`    | Reference to a modem response instance | **None** |

#### Returns

`bool`
True on success, False on failure

### `coap_set_options`

Configure CoAP options for the next message to be sent.
Options are to be configured one at a time.

> [!NOTE]
> Options: IF_MATCH, ETAG, LOCATION_PATH, URI_PATH, URI_QUERY, LOCATION_QUERY
> are repeatable.\
> For these, up to 6 values can be provided *(the order is respected)*.

#### Examples

```py
await modem.coap_set_options(
    ctx_id=0,
    action=WalterModemCoapOptionAction.SET,
    option=WalterModemCoapOption.URI_PATH,
    value=('.well-known','core')
)
```

```py
modem_rsp = ModemRsp()

if not await modem.coap_set_options(
    ctx_id=0,
    action=WalterModemCoapOptionAction.READ,
    option=WalterModemCoapOption.URI_PATH,
    rsp=modem_rsp
):
    print('Failed to read CoAP option URI_PATH')

print(f'Context ID: {modem_rsp.coap_options.ctx_id}')
print(f'Option: {modem_rsp.coap_options.option}')
print(f'Value: {modem_rsp.coap_options.value}')
```

#### Params

| Param    | Description                                                                           | Default  |
| -------- | ------------------------------------------------------------------------------------- | -------- |
| `ctx_id` | Context profile identifier (0, 1, 2)                                                  |          |
| `action` | Action to perform ([WalterModemCoapOptionAction](#waltermodemcoapoptionaction))       |          |
| `option` | The option to perform the action on ([WalterModemCoapOption](#waltermodemcoapoption)) |          |
| `value`  | Value(s) to pass along                                                                | **None** |
| `rsp`    | Reference to a modem response instance                                                | **None** |

#### Returns

`bool`
True on success, False on failure

---

### `coap_set_header`

Configure the CoAP header fo the next message to be sent.

If **only msg_id is set**, the CoAP client sets a **random token** value.  
If **only token is set**, the CoAP client sets a **random msg_id** value.

#### Example

```py
if not await modem.coap_set_header(
    ctx_id=0,
    token='74EBFDE0'
):
    print('Failed to set coap header.')
```

#### Params

| Param  | Description                                                                                             | Default  |
| ------ | ------------------------------------------------------------------------------------------------------- | -------- |
| ctx_id | Context profile identifier (0, 1, 2)                                                                    |          |
| msg_id | Message ID of the CoAP header (0-65535)                                                                 | **None** |
| token  | hexidecimal format, token to be used in the CoAP header, specify "NO_TOKEN" for a header without token. | **None** |
| rsp    | Reference to a modem response instance                                                                  | **None** |

#### Returns

`bool`
True on success, False on failure

---

### `coap_send`

Send data over CoAP.  
If no data is sent, length must be set to zero.

> [!NOTE]
> This method supports passing along a path or content type, when doing so the
> method automatically sets these as options before sending the messagee.  
> These are not mandatory and can be ignored or set using coap_set_options manually.

#### Examples

```py
if not await modem.coap_send(
    ctx_id=0,
    m_type=WalterModemCoapType.CON,
    method=WalterModemCoapMethod.GET,
    length=0,
    data='/.well-known/core'
    # Parser ignores leading or trailing "/"
    # ".well-known/core", ".well-known/core/", ... would also be valid.
):
    print('Failed to send')
```

```py
data = 'Hello from Walter'

if not await modem.coap_send(
    ctx=0,
    m_type=WalterModemCoapType.CON,
    method=WalterModemCoapMethod.POST,
    length=len(data),
    data=data,
    path='test',
    content_type=WalterModemCoapContentType.APPLICATION_JSON
):
    print('Failed to send')
```

#### Params

| Param          | Description                                                                                      | Default  |
| -------------- | ------------------------------------------------------------------------------------------------ | -------- |
| `ctx_id`       | Context profile identifier (0, 1, 2)                                                             |          |
| `m_type`       | CoAP message type ([WalterModemCoapType](#waltermodemcoaptype))                                  |          |
| `method`       | Method ([WalterModemCoapMethod](#waltermodemcoapmethod))                                         |          |
| `data`         | Binary data to send (bytes, bytearray) or string (will be UTF-8 encoded)                         | **None** |
| `length`       | Length of the payload (optional, auto-calculated if not provided)                                | **None** |
| `path`         | Optional: the URI_PATH to send on *(this will set the path in the CoAP options before sending)*  | **None** |
| `content_type` | Optional: the content_type *(this will set the content type in the CoAP options before sending)* | **None** |
| `rsp`          | Reference to a modem response instance                                                           | **None** |

#### Returns

`bool`
True on success, False on failure

---

### `coap_receive_data`

Read the contents of a CoAP message after it's ring has been received.

#### Example

```py
# Create CoAP context & send a message expecting a response in return (eg. GET)

while len(modem.coap_context_states[COAP_CTX_ID].rings) = 0:
    await asyncio.sleep(1)
ring = modem.coap_context_states[COAP_CTX_ID].rings.pop()

modem_rsp = ModemRsp()
if not await modem.coap_receive_data(
    ctx_id=ring.ctx_id,
    msg_id=ring.msg_id,
    length=ring.length,
    rsp=modem_rsp
):
    print('Failed to receive ring')

print('Payload:')
print(modem_rsp.coap_rcv_response.payload)
```

#### Params

| Param       | Description                                                        | Default  |
| ----------- | ------------------------------------------------------------------ | -------- |
| `ctx_id`    | Context profile identifier (0, 1, 2)                               |          |
| `msg_id`    | CoAP message ID                                                    |          |
| `length`    | The length of the payload to receive *(length is set in the ring)* |          |
| `max_bytes` | How many bytes of the message payload to read at once              | **1024** |
| `rsp`       | Reference to a modem response instance                             | **None** |

#### Returns

`bool`
True on success, False on failure

---

### `coap_receive_options`

Read the options of a CoAP message after it's ring has been received.

#### Example

```py
# Create CoAP context & send a message expecting a response in return (eg. GET)

while len(modem.coap_context_states[COAP_CTX_ID].rings) = 0:
    await asyncio.sleep(1)
ring = modem.coap_context_states[COAP_CTX_ID].rings.pop()

modem_rsp = ModemRsp()
if not await modem.coap_receive_data(
    ctx_id=ring.ctx_id,
    msg_id=ring.msg_id,
    rsp=modem_rsp
):
    print('Failed to receive ring')

for coap_option in modem_rsp.coap_options:
    print(f'Context ID: {coap_option.ctx_id}')
    print(f'Option: {WalterModemCoapOption.get_value_name(coap_option.option)}')
    print(f'Value: {coap_option.value}')
```

#### Params

| Param         | Description                                                  | Default  |
| ------------- | ------------------------------------------------------------ | -------- |
| `ctx_id`      | Context profile identifier (0, 1, 2)                         |          |
| `msg_id`      | CoAP message ID                                              |          |
| `max_options` | The maximum options that can be shown in the response (0-32) | **32**   |
| `rsp`         | Reference to a modem response instance                       | **None** |

#### Returns

`bool`
True on success, False on failure

---

## Enums

### `WalterModemCoapCloseCause`

Reason why connection has been closed.

> **USER** = ``b'USER'``  
> Connection closed by the user.  
> **SERVER** = ``b'SERVER'``  
> Connection closed by the server.  
> **NAT_TIMEOUT** = ``b'NAT_TIMEOUT'``  
> Connection closed due to NAT timeout.  
> **NETWORK** = ``b'NETWORK'``  
> Connection closed by a network error.  

---

### `WalterModemCoapReqResp`

Indicator whether a ring is a request from or response from a CoAP seever.

> **REQUEST** = `0`  
> A CoAP request message.  
> **RESPONSE** = `1`  
> A CoAP response message.  

---

### `WalterModemCoapType`

CoAP message type.

> **CON** = `0`  
> Confirmable message.  
> **NON** = `1`  
> Non-confirmable message.  
> **ACK** = `2`  
> Acknowledgement message.  
> **RST** = `3`  
> Reset message.  

---

### `WalterModemCoapMethod`

CoAP request method.

> **GET** = `1`  
> Retrieve a resource.  
> **POST** = `2`  
> Create or append to a resource.  
> **PUT** = `3`  
> Create or replace a resource.  
> **DELETE** = `4`  
> Remove a resource.  

---

### `WalterModemCoapResponseCode`

CoAP response code.

> **CREATED** = `201`  
> Resource created.  
> **DELETED** = `202`  
> Resource deleted.  
> **VALID** = `203`  
> Content is valid.  
> **CHANGED** = `204`  
> Resource changed.  
> **CONTENT** = `205`  
> Content returned.  
> **BAD_REQUEST** = `400`  
> Bad request syntax or options.  
> **UNAUTHORIZED** = `401`  
> Unauthorized.  
> **BAD_OPTION** = `402`  
> Bad option in request.  
> **FORBIDDEN** = `403`  
> Forbidden.  
> **NOT_FOUND** = `404`  
> Resource not found.  
> **METHOD_NOT_ALLOWED** = `405`  
> Method not allowed.  
> **NOT_ACCEPTABLE** = `406`  
> Content not acceptable.  
> **PRECONDITION_FAILED** = `412`  
> Precondition failed.  
> **REQUEST_ENTITY_TOO_LARGE** = `413`  
> Payload too large.  
> **UNSUPPORTED_MEDIA_TYPE** = `415`  
> Unsupported media type.  
> **INERNAL_SERVER_ERROR** = `500`  
> Internal server error.  
> **NOT_IMPLIMENTED** = `501`  
> Not implemented.  
> **BAD_GATEWAY** = `502`  
> Bad gateway.  
> **SERVICE_UNAVAILABLE** = `503`  
> Service unavailable.  
> **GATEWAY_TIMEOUT** = `501`  
> Gateway timeout.  
> **PROXYING_NOT_SUPPORTED** = `505`  
> Proxying not supported.  

---

### `WalterModemCoapOptionAction`

Action on CoAP options.

> **SET** = `0`  
> Set or add an option.  
> **DELETE** = `1`  
> Remove an option.  
> **READ** = `2`  
> Read an option's value.  
> **EXTEND** = `3`  
> Extend an existing option.  

---

### `WalterModemCoapOption`

CoAP option numbers and their semantics.

> **IF_MATCH** = `1`  
> Contains one or more Entity-Tag values;
> makes a request conditional on the current representation's
> ETag matching one in the list.  
> Useful for optimistic concurrency control.  
> **URI_HOST** = `3`  
> Specifies the host name (or literal IP address) of the target server
> if different from the message's destination address.  
> **ETAG** = `4`  
> Carries an Entity-Tag for the representation in a response,
> enabling cache validation and conditional requests.  
> **IF_NONE_MATCH** = `5`  
> Makes a request conditional on none of the current representation's
> ETags matching the provided value—often used to avoid re-sending unchanged data.  
> **OBSERVE** = `6`  
> Registers (in requests) or updates (in notifications) an observation relationship;
> the value is a sequence number for notification ordering.  
> **URI_PORT** = `7`  
> Overrides the default transport port for the target URI, if non-standard.  
> **LOCATION_PATH** = `8`  
> Indicates the path segments of the resource's location in a response to POST/PUT,
> appended to the Server's base URI.  
> **URI_PATH** = `11`  
> Specifies one segment of the request URI's path;
> multiple instances concatenate with '/' to form the full path.  
> **CONTENT_TYPE** = `12`  
> Indicates the media type (content format) of the message payload.  
> **MAX_AGE** = `14`  
> Advises caches how long (in seconds) the representation remains
> fresh without revalidation.  
> **URI_QUERY** = `15`  
> Specifies one key=value query parameter;
> multiple instances form the full query string.  
> **ACCEPT** = `17`  
> Lists acceptable media types (content formats) for the response,
> by numeric identifier.  
> **TOKEN** = `19`  
> Correlates responses to requests; the value is opaque data chosen by the client.  
> **LOCATION_QUERY** = `20`  
> Indicates the query part of the Location-URI in a response,
> following the Location-Path.  
> **BLOCK2** = `23`  
> Used in block-wise responses to negotiate and retrieve large payloads in chunks;
> indicates block number, “more” flag and size.  
> **BLOCK1** = `27`  
> Used in block-wise requests to send large payloads in chunks;
> similar structure to BLOCK2.  
> **SIZE2** = `28`  
> Advertises the total size (in bytes) of a resource being retrieved (response).  
> **PROXY_URI** = `35`  
> Carries a complete URI to be used by a proxy on the client's behalf.  
> **SIZE1** = `60`  
> Indicates the total size (in bytes) of the payload being sent (request).  

---

### `WalterModemCoapContentType`

CoAP content-format identifiers.

> **TEXT_PLAIN** = `'0'`  
> Unformatted, UTF-8 text  
> **TEXT_XML** = `'1'`  
> XML markup.  
> **TEXT_CSV** = `'2'`  
> Comma-separated tabular data.  
> **TEXT_HTML** = `'3'`  
> HTML document or fragment.  
> **IMAGE_GIF** = `'21'`  
> GIF-format image.  
> **IMAGE_JPEG** = `'22'`  
> JPEG-format photo.  
> **IMAGE_PNG** = `'23'`  
> PNG-format graphic.  
> **IMAGE_TIFF** = `'24'`  
> TIFF-format image.  
> **AUDIO_RAW** = `'25'`  
> Unencoded PCM audio samples.  
> **VIDEO_RAW** = `'26'`  
> Uncompressed video frames.  
> **APPLICATION_LINK_FORMAT** = `'40'`  
> CoRE link-format entries.  
> **APPLICATION_XML** = `'41'`  
> Generic XML payload.  
> **APPLICATION_OCTET_STREAM** = `'42'`  
> Opaque binary stream.  
> **APPLICATION_RDF_XML** = `'43'`  
> RDF graph encoded in XML.  
> **APPLICATION_SOAP_XML** = `'44'`  
> SOAP envelope in XML.  
> **APPLICATION_ATOM_XML** = `'45'`  
> Atom feed or entry.  
> **APPLICATION_XMPP_XML** = `'46'`  
> XMPP stanza in XML.  
> **APPLICATION_EXI** = `'47'`  
> EXI (binary XML) encoding.  
> **APPLICATION_FASTINFOSET** = `'48'`  
> Fast Infoset binary XML.  
> **APPLICATION_SOAP_FASTINFOSET** = `'49'`  
> SOAP in Fast Infoset form.  
> **APPLICATION_JSON** = `'50'`  
> JSON text.  
> **APPLICATION_X_OBIX_BINARY** = `'51'`  
> oBIX binary payload.  
> **APPLICATION_CBOR** = `'60'`  
> CBOR (binary JSON alternative).  
