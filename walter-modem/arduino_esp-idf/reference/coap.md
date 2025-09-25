## Methods Overview

- [coapCreateContext](#coapcreatecontext)
- [coapClose](#coapclose)
- [coapGetContextStatus](#coapgetcontextstatus)
- [coapSetHeader](#coapsetheader)
- [coapSetOptions](#coapsetoptions)
- [coapSendData](#coapsenddata)
- [coapDidRing](#coapdidring)

## Enums Overview

- [WalterModemCoapOptCode](#waltermodemcoapoptcode)
- [WalterModemCoapOptValue](#waltermodemcoapoptvalue)
- [WalterModemCoapOptAction](#waltermodemcoapoptaction)
- [WalterModemCoapSendType](#waltermodemcoapsendtype)
- [WalterModemCoapSendMethodRsp](#waltermodemcoapsendmethodrsp)

---

## Methods

### `coapCreateContext`

Create a CoAP context.

This function will create a CoAP context if it was not open yet. This needs to be done
before you can set headers or options or send or receive data.

#### Params

| Param          | Description                                                       | Default  |
| -------------- | ----------------------------------------------------------------- | -------- |
| `profileId`    | CoAP profile ID.                                                  |          |
| `serverName`   | The server name to connect to.                                    |          |
| `port`         | The port of the server to connect to.                             |          |
| `tlsProfileId` | If not 0, DTLS is used with the given profile (1-6).              | **0**    |
| `localPort`    | The local port to use (0 = random).                               | **-1**   |
| `rsp`          | Optional modem response structure to save the result in.          | **NULL** |
| `cb`           | Optional callback function, if set, this function will not block. | **NULL** |
| `args`         | Optional argument to pass to the callback.                        | **NULL** |

#### Returns

`bool`  
True on success, False otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_COAP_PROFILE, 1)

// ...

if (modem.coapCreateContext(MODEM_COAP_PROFILE, "coap.me", 5683)) {
    Serial.println("Info: COAP context created successfully");
} else {
    Serial.println("Error: Failed to create COAP context");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG_UINT8(MODEM_COAP_PROFILE, 1)

// ...

if (modem.coapCreateContext(MODEM_COAP_PROFILE, "coap.me", 5683)) {
    ESP_LOGI("coap_docs_demo", "COAP context created successfully");
} else {
    ESP_LOGE("coap_docs_demo", "Failed to create COAP context");
}

// ...
```

<!-- tabs:end -->

---

### `coapClose`

Close a CoAP context.

This function will close a CoAP context previously opened with [coapCreateContext](#coapcreatecontext). To
change parameters such as the server name, you must first close the context using this
call.

> [!NOTE]
> Eventually the context will be automatically closed after the timeout.

#### Params

| Param       | Description                                                       | Default  |
| ----------- | ----------------------------------------------------------------- | -------- |
| `profileId` | CoAP profile ID.                                                  |          |
| `rsp`       | Optional modem response structure to save the result in.          | **NULL** |
| `cb`        | Optional callback function, if set, this function will not block. | **NULL** |
| `args`      | Optional argument to pass to the callback.                        | **NULL** |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_COAP_PROFILE, 1)

// ...

if (modem.coapClose(MODEM_COAP_PROFILE)) {
    Serial.println("Info: CoAP profile closed");
} else {
    Serial.println("Error: Failed to close CoAP profile");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG_UINT8(MODEM_COAP_PROFILE, 1)

// ...

if (modem.coapClose(MODEM_COAP_PROFILE)) {
    ESP_LOGI("coap_docs_demo", "CoAP profile closed");
} else {
    ESP_LOGE("coap_docs_demo", "Failed to close CoAP profile");
}

// ...
```

<!-- tabs:end -->

---

### `coapGetContextStatus`

Get the connection status of a CoAP context.

#### Params

| Param       | Description                                | Default |
| ----------- | ------------------------------------------ | ------- |
| `profileId` | The profile ID (0-2) of the context. |         |

#### Returns

`bool`  
True if context with the profile id is connected, false if not.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_COAP_PROFILE, 1)

// ...

if (modem.coapGetContextStatus(MODEM_COAP_PROFILE)) {
    Serial.println("Info: CoAP profile is connected to the remote server");
} else {
    Serial.println("Error: CoAP profile is not connected to the remote server");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG_UINT8(MODEM_COAP_PROFILE, 1)

// ...

if (modem.coapGetContextStatus(MODEM_COAP_PROFILE)) {
    ESP_LOGI("coap_docs_demo", "CoAP profile is connected to the remote server");
} else {
    ESP_LOGI("coap_docs_demo", "CoAP profile is not connected to the remote server");
}

// ...
```

<!-- tabs:end -->

---

<!-- tabs:end -->

### `coapSetHeader`

Set a CoAP header.

This function will set the header of the next message to send.

> [!NOTE]
> This is not necessary,
> if you do not set the header the message id and the token will be set to random values.

#### Params

| Param       | Description                                                                                                                                                                                    | Default        |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| `profileId` | CoAP profile id (0-2)                                                                                                                                                                          |                |
| `messageId` | The message id of the next message to send.                                                                                                                                                    | **1**          |
| `token`     | The token of the next message to send as a string of 16 hex digits for a max token length of 8 bytes, with default value "NO_TOKEN" which is the magic value to send a datagram without token. | **"NO_TOKEN"** |
| `rsp`       | Optional modem response structure to save the result in.                                                                                                                                       | **NULL**       |
| `cb`        | Optional callback function, if set, this function will not block.                                                                                                                              | **NULL**       |
| `args`      | Optional argument to pass to the callback.                                                                                                                                                     | **NULL**       |

#### Returns

`bool`  
True on success, False otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_COAP_PROFILE, 1)

// ...

if (modem.coapSetHeader(MODEM_COAP_PROFILE, 1)) {
    Serial.println("Info: CoAP header set");
} else {
    Serial.println("Error: Failed to set the CoAP header");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG_UINT8(MODEM_COAP_PROFILE, 1)

// ...

if (modem.coapSetHeader(MODEM_COAP_PROFILE, 1)) {
    ESP_LOGI("coap_docs_demo", "CoAP header set");
} else {
    ESP_LOGE("coap_docs_demo", "Failed to set the CoAP header");
}

// ...
```

<!-- tabs:end -->

---

### `coapSetOptions`

Set the options for the next CoAP message.

#### Params

| Param       | Description                                                                                                                                                              | Default  |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| `profileId` | CoAP profile id (0-2)                                                                                                                                                    |          |
| `action`    | The action code of the option.                                                                                                                                           |          |
| `code`      | The code of the options.                                                                                                                                                 |          |
| `values`    | The optional values array, expected as a comma delimited string of up to 6 strings or recognized option values (see [WalterModemCoapOptValue](#waltermodemcoapoptvalue)) | **NULL** |
| `rsp`       | Optional modem response structure to save the result in.                                                                                                                 | **NULL** |
| `cb`        | Optional callback function, if set, this function will not block.                                                                                                        | **NULL** |
| `args`      | Optional argument to pass to the callback.                                                                                                                               | **NULL** |

#### Returns

`bool`  
True on success, False otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_COAP_PROFILE, 1)

// ...

if (modem.coapSetOptions(
        MODEM_COAP_PROFILE,
        WALTER_MODEM_COAP_OPT_DELETE,
        WALTER_MODEM_COAP_OPT_CODE_URI_PATH)) {
    Serial.println("Info: CoAP options set");
} else {
    Serial.println("Error: Failed to set the CoAP options");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG_UINT8(MODEM_COAP_PROFILE, 1)

// ...

if (modem.coapSetOptions(
        MODEM_COAP_PROFILE,
        WALTER_MODEM_COAP_OPT_DELETE,
        WALTER_MODEM_COAP_OPT_CODE_URI_PATH)) {
    ESP_LOGE("coap_docs_demo", "CoAP options set");
} else {
    ESP_LOGI("coap_docs_demo", "Failed to set the CoAP options");
}

// ...
```

<!-- tabs:end -->

---

### `coapSendData`

Send a datagram over CoAP.

> [!NOTE]
> Preferred options/header need to be set beforehand using [coapSetOptions](#coapsetoptions) or [coapSetHeader](#coapsetheader)

#### Params

| Param       | Description                                                       | Default  |
| ----------- | ----------------------------------------------------------------- | -------- |
| `profileId` | CoAP profile id (0-2)                                             |          |
| `type`      | The type of message (NON, CON, ACK, RST).                         |          |
| `methodRsp` | The method or response code.                                      |          |
| `length`    | The length of the payload.                                        |          |
| `payload`   | The payload to send, max 1024 bytes.                              |          |
| `rsp`       | Optional modem response structure to save the result in.          | **NULL** |
| `cb`        | Optional callback function, if set, this function will not block. | **NULL** |
| `args`      | Optional argument to pass to the callback.                        | **NULL** |

#### Returns

`bool`  
True on success, False otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_COAP_PROFILE, 1)

// ...

static const char demoData[] = "Demo Data";

if (modem.coapSendData(
        MODEM_COAP_PROFILE,
        WALTER_MODEM_COAP_SEND_TYPE_CON,
        WALTER_MODEM_COAP_SEND_METHOD_GET,
        sizeof(demoData) - 1,
        (const uint8_t *)demoData)) {
    Serial.println("Info: CoAP datagram sent");
} else {
    Serial.println("Error: Failed to send CoAP datagram");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG_UINT8(MODEM_COAP_PROFILE, 1)

// ...

static const char demoData[] = "Demo Data";

if (modem.coapSendData(
        MODEM_COAP_PROFILE,
        WALTER_MODEM_COAP_SEND_TYPE_CON,
        WALTER_MODEM_COAP_SEND_METHOD_GET,
        sizeof(demoData) - 1,
        (const uint8_t *)demoData)) {
    ESP_LOGI("coap_docs_demo", "CoAP datagram sent");
} else {
    ESP_LOGE("coap_docs_demo", "Failed to send CoAP datagram");
}

// ...
```

<!-- tabs:end -->

---

### `coapDidRing`

Fetch incoming CoAP messages, if any.

#### Params

| Param           | Description                                                        | Default  |
| --------------- | ------------------------------------------------------------------ | -------- |
| `profileId`     | Profile for which to get incoming data (0-2)                       |          |
| `targetBuf`     | User buffer to store response in.                                  |          |
| `targetBufSize` | Size of the user buffer, including space for a terminating 0-byte. |          |
| `rsp`           | Optional modem response structure to save the result in.           | **NULL** |

#### Returns

`bool`  
**true** on success  
**false** if no data arrived, if there was an error or if no data is expected
(eg. no ring received).

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_COAP_PROFILE, 1)

WalterModemRsp rsp = {};

// ...

uint8_t incomingBuf[256] = {0};

while (modem.coapDidRing(MODEM_COAP_PROFILE, incomingBuf, sizeof(incomingBuf), &rsp)) {
    Serial.println("Info: Incoming ring");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG_UINT8(MODEM_COAP_PROFILE, 1)

WalterModemRsp rsp = {};

// ...

uint8_t incomingBuf[256] = {0};

while (modem.coapDidRing(MODEM_COAP_PROFILE, incomingBuf, sizeof(incomingBuf), &rsp)) {
    ESP_LOGI("coap_docs_demo", "Incoming ring");
}

// ...
```

<!-- tabs:end -->

---

## Enums

### `WalterModemCoapOptCode`

The possible option codes for the CoAP message.

> **WALTER_MODEM_COAP_OPT_CODE_IF_MATCH** = `1`  
> The **IfMatch** option in CoAP specifies that the request is conditional upon the resource's ETag matching one of the provided values.  
> **WALTER_MODEM_COAP_OPT_CODE_URI_HOST** = `3`  
> The **URIHost** option in CoAP specifies the host part of the URI of the target resource.  
> **WALTER_MODEM_COAP_OPT_CODE_ETAG** = `4`  
> The **ETag** option in CoAP is used to provide an entity tag for the current resource for the client to compare future versions of the resource.  
> **WALTER_MODEM_COAP_OPT_CODE_IF_NONE_MATCH** = `5`  
> The **IfNoneMatch** option in CoAP specifies that the resource's ETag must not match any of the provided values for the resource change to be accepted.  
> **WALTER_MODEM_COAP_OPT_CODE_OBSERVE** = `6`  
> The **Observe** option in CoAP is used to subscribe for a resource's state changes.  
> **WALTER_MODEM_COAP_OPT_CODE_URI_PORT** = `7`  
> The **URIPort** option in CoAP specifies the port part of the URI of the target resource.  
> **WALTER_MODEM_COAP_OPT_CODE_LOCATION_PATH** = `8`  
> The **LocationPath** option in CoAP specifies the path of the target resource's location.  
> **WALTER_MODEM_COAP_OPT_CODE_URI_PATH** = `11`  
> The **URIPath** option in CoAP specifies the path part of the URI of the target resource.  
> **WALTER_MODEM_COAP_OPT_CODE_CONTENT_TYPE** = `12`  
> The **ContentType** option in CoAP specifies the media type of the resource's payload.  
> **WALTER_MODEM_COAP_OPT_CODE_MAX_AGE** = `14`  
> The **MaxAge** option in CoAP specifies the maximum age limit for the resource's cache.  
> **WALTER_MODEM_COAP_OPT_CODE_URI_QUERY** = `15`  
> The **URIQuery** option in CoAP specifies the query parameters of the URI of the target resource.  
> **WALTER_MODEM_COAP_OPT_CODE_ACCEPT** = `17`  
> The **Accept** option in CoAP specifies the media type of the resource that the server is expected to send back in the response.  
> **WALTER_MODEM_COAP_OPT_CODE_TOKEN** = `19`  
> The **Token** option in CoAP is used to set the token for the next message.  
> **WALTER_MODEM_COAP_OPT_CODE_LOCATION_QUERY** = `20`  
> The **LocationQuery** option in CoAP specifies the query parameters for the target resource's location.  
> **WALTER_MODEM_COAP_OPT_CODE_BLOCK2** = `23`  
> The **Block2** option in CoAP specifies the second block of multiple data during blockwise transfers.  
> **WALTER_MODEM_COAP_OPT_CODE_SIZE2** = `28`  
> The **Size2** option in CoAP specifies the size of the second block of multiple data during blockwise transfers.  
> **WALTER_MODEM_COAP_OPT_CODE_PROXY_URI** = `35`  
> The **ProxyURI** option in CoAP specifies the URI of a proxy through which the CoAP requestor will be communicating.  
> **WALTER_MODEM_COAP_OPT_CODE_SIZE1** = `60`  
> The **Size1** option in CoAP specifies the size of the first block in blockwise data transfers.  

### `WalterModemCoapOptValue`

The possible option values for the CoAP message.

> **WALTER_MODEM_COAP_OPT_VALUE_TEXT_PLAIN** = `0`  
> The **TextPlain** option in CoAP specifies that the content type is plain text.  
> **WALTER_MODEM_COAP_OPT_VALUE_TEXT_XML** = `1`  
> The **TextXML** option in CoAP specifies that the content type is XML.  
> **WALTER_MODEM_COAP_OPT_VALUE_TEXT_CSV** = `2`  
> The **TextCSV** option in CoAP specifies that the content type is CSV (Comma Separated Values).  
> **WALTER_MODEM_COAP_OPT_VALUE_TEXT_HTML** = `3`  
> The **TextHTML** option in CoAP specifies that the content type is HTML.  
> **WALTER_MODEM_COAP_OPT_VALUE_IMAGE_GIF** = `21`  
> The **ImageGIF** option in CoAP specifies that the content type is a GIF image.  
> **WALTER_MODEM_COAP_OPT_VALUE_IMAGE_JPEG** = `22`  
> The **ImageJPEG** option in CoAP specifies that the content type is a JPEG image.  
> **WALTER_MODEM_COAP_OPT_VALUE_IMAGE_PNG** = `23`  
> The **ImagePNG** option in CoAP specifies that the content type is a PNG image.  
> **WALTER_MODEM_COAP_OPT_VALUE_IMAGE_TIFF** = `24`  
> The **ImageTIFF** option in CoAP specifies that the content type is a TIFF image.  
> **WALTER_MODEM_COAP_OPT_VALUE_AUDIO_RAW** = `25`  
> The **AudioRAW** option in CoAP specifies that the content type is raw audio data.  
> **WALTER_MODEM_COAP_OPT_VALUE_VIDEO_RAW** = `26`  
> The **VideoRAW** option in CoAP specifies that the content type is raw video data.  
> **WALTER_MODEM_COAP_OPT_VALUE_APPLICATION_LINK_FORMAT** = `40`  
> The **ApplicationLinkFormat** option in CoAP specifies the content type as a link format for applications.  
> **WALTER_MODEM_COAP_OPT_VALUE_APPLICATION_XML** = `41`  
> The **ApplicationXML** option in CoAP specifies that the content type is XML for application data.  
> **WALTER_MODEM_COAP_OPT_VALUE_APPLICATION_OCTET_STREAM** = `42`  
> The **ApplicationOctetStream** option in CoAP specifies that the content type is binary data (octet stream).  
> **WALTER_MODEM_COAP_OPT_VALUE_APPLICATION_RDF_XML** = `43`  
> The **ApplicationRDFXML** option in CoAP specifies that the content type is RDF in XML format.  
> **WALTER_MODEM_COAP_OPT_VALUE_APPLICATION_SOAP_XML** = `44`  
> The **ApplicationSOAPXML** option in CoAP specifies that the content type is SOAP XML.  
> **WALTER_MODEM_COAP_OPT_VALUE_APPLICATION_ATOM_XML** = `45`  
> The **ApplicationAtomXML** option in CoAP specifies that the content type is Atom XML.  
> **WALTER_MODEM_COAP_OPT_VALUE_APPLICATION_XMPP_XML** = `46`  
> The **ApplicationXMPPXML** option in CoAP specifies that the content type is XMPP XML.  
> **WALTER_MODEM_COAP_OPT_VALUE_APPLICATION_EXI** = `47`  
> The **ApplicationEXI** option in CoAP specifies that the content type is EXI (Efficient XML Interchange).  
> **WALTER_MODEM_COAP_OPT_VALUE_APPLICATION_FASTINFOSET** = `48`  
> The **ApplicationFastInfoSet** option in CoAP specifies that the content type is Fast Infoset.  
> **WALTER_MODEM_COAP_OPT_VALUE_APPLICATION_SOAP_FASTINFOSET** = `49`  
> The **ApplicationSOAPFastInfoSet** option in CoAP specifies that the content type is SOAP Fast Infoset.  
> **WALTER_MODEM_COAP_OPT_VALUE_APPLICATION_JSON** = `50`  
> The **ApplicationJSON** option in CoAP specifies that the content type is JSON (JavaScript Object Notation).  
> **WALTER_MODEM_COAP_OPT_VALUE_APPLICATION_X_OBIX_BINARY** = `51`  
> The **ApplicationXObixBinary** option in CoAP specifies that the content type is OBIX binary.  
> **WALTER_MODEM_COAP_OPT_VALUE_APPLICATION_CBOR** = `60`  
> The **ApplicationCBOR** option in CoAP specifies that the content type is CBOR (Concise Binary Object Representation).  

### `WalterModemCoapOptAction`

The possible option actions for the CoAP message.

> **WALTER_MODEM_COAP_OPT_SET** = `0`  
> The **Set** option in CoAP is used to overwrite an option.  
> **WALTER_MODEM_COAP_OPT_DELETE** = `1`  
> The **Delete** option in CoAP is used to delete one or all options.  
> **WALTER_MODEM_COAP_OPT_READ** = `2`  
> The **Read** option in CoAP is used to read a single option.  
> **WALTER_MODEM_COAP_OPT_EXTEND** = `3`  
> The **Extend** option in CoAP allows adding more values to repeatable options.  

### `WalterModemCoapSendType`

The possible CoAP send types.

> **WALTER_MODEM_COAP_SEND_TYPE_CON** = `0`  
> The **CON** option in CoAP refers to a confirmable message type, requiring acknowledgment.  
> **WALTER_MODEM_COAP_SEND_TYPE_NON** = `1`  
> The **NON** option in CoAP refers to a non-confirmable message type, which does not require acknowledgment.  
> **WALTER_MODEM_COAP_SEND_TYPE_ACK** = `2`  
> The **ACK** option in CoAP refers to an acknowledgment message type, used to acknowledge a confirmable message.  
> **WALTER_MODEM_COAP_SEND_TYPE_RST** = `3`  
> The **RST** option in CoAP refers to a reset message type, used to indicate an error in processing a confirmable message.  

### `WalterModemCoapSendMethodRsp`

The possible CoAP send methods.

> **WALTER_MODEM_COAP_SEND_METHOD_NONE** = `0`  
> The **NONE** option in CoAP represents a no-operation method, used when no specific method is required.  
> **WALTER_MODEM_COAP_SEND_METHOD_GET** = `1`  
> The **GET** method in CoAP is used to retrieve the state of the target resource.  
> **WALTER_MODEM_COAP_SEND_METHOD_POST** = `2`  
> The **POST** method in CoAP is used to submit data to the target resource for processing.  
> **WALTER_MODEM_COAP_SEND_METHOD_PUT** = `3`  
> The **PUT** method in CoAP is used to update or create the resource at the target URI.  
> **WALTER_MODEM_COAP_SEND_METHOD_DELETE** = `4`  
> The **DELETE** method in CoAP is used to remove the resource at the target URI.  
> **WALTER_MODEM_COAP_SEND_RSP_CODE_CREATED** = `201`  
> The **CREATED** response code in CoAP indicates that the resource has been successfully created.  
> **WALTER_MODEM_COAP_SEND_RSP_CODE_DELETED** = `202`  
> The **DELETED** response code in CoAP indicates that the resource has been successfully deleted.  
> **WALTER_MODEM_COAP_SEND_RSP_CODE_VALID** = `203`  
> The **VALID** response code in CoAP indicates that the request was successful and the resource is valid.  
> **WALTER_MODEM_COAP_SEND_RSP_CODE_CHANGED** = `204`  
> The **CHANGED** response code in CoAP indicates that the resource has been successfully modified.  
> **WALTER_MODEM_COAP_SEND_RSP_CODE_CONTENT** = `205`  
> The **CONTENT** response code in CoAP indicates that the resource has been successfully returned, with content.  
> **WALTER_MODEM_COAP_SEND_RSP_CODE_CONTINUE** = `231`  
> The **CONTINUE** response code in CoAP indicates that the request is being processed, but more time is required.  
> **WALTER_MODEM_COAP_SEND_RSP_CODE_BAD_REQUEST** = `400`  
> The **BAD REQUEST** response code in CoAP indicates that the request is malformed or contains invalid parameters.  
> **WALTER_MODEM_COAP_SEND_RSP_CODE_UNAUTHORIZED** = `401`  
> The **UNAUTHORIZED** response code in CoAP indicates that the client is not authorized to access the resource.  
> **WALTER_MODEM_COAP_SEND_RSP_CODE_BAD_OPTION** = `402`  
> The **BAD OPTION** response code in CoAP indicates that the request contains invalid or unsupported options.  
> **WALTER_MODEM_COAP_SEND_RSP_CODE_FORBIDDEN** = `403`  
> The **FORBIDDEN** response code in CoAP indicates that the server refuses to authorize the request.  
> **WALTER_MODEM_COAP_SEND_RSP_CODE_NOT_FOUND** = `404`  
> The **NOT FOUND** response code in CoAP indicates that the resource could not be found on the server.  
> **WALTER_MODEM_COAP_SEND_RSP_CODE_METHOD_NOT_ALLOWED** = `405`  
> The **METHOD NOT ALLOWED** response code in CoAP indicates that the requested method is not allowed on the target resource.  
> **WALTER_MODEM_COAP_SEND_RSP_CODE_NOT_ACCEPTABLE** = `406`  
> The **NOT ACCEPTABLE** response code in CoAP indicates that the resource is not available in a format acceptable to the client.  
> **WALTER_MODEM_COAP_SEND_RSP_CODE_PRECONDITION_FAILED** = `412`  
> The **PRECONDITION FAILED** response code in CoAP indicates that a precondition specified by the request was not met.  
> **WALTER_MODEM_COAP_SEND_RSP_CODE_REQUEST_ENTITY_TOO_LARGE** = `413`  
> The **REQUEST ENTITY TOO LARGE** response code in CoAP indicates that the request's payload is too large to be processed.  
> **WALTER_MODEM_COAP_SEND_RSP_CODE_UNSUPPORTED_MEDIA_TYPE** = `415`  
> The **UNSUPPORTED MEDIA TYPE** response code in CoAP indicates that the request's payload format is not supported by the server.  
> **WALTER_MODEM_COAP_SEND_RSP_CODE_INTERNAL_SERVER_ERROR** = `500`  
> The **INTERNAL SERVER ERROR** response code in CoAP indicates that the server encountered an unexpected error.  
> **WALTER_MODEM_COAP_SEND_RSP_CODE_NOT_IMPLEMENTED** = `501`  
> The **NOT IMPLEMENTED** response code in CoAP indicates that the server does not support the functionality required to process the request.  
> **WALTER_MODEM_COAP_SEND_RSP_CODE_BAD_GATEWAY** = `502`  
> The **BAD GATEWAY** response code in CoAP indicates that the server, while acting as a gateway, received an invalid response from an upstream server.  
> **WALTER_MODEM_COAP_SEND_RSP_CODE_SERVICE_UNAVAILABLE** = `503`  
> The **SERVICE UNAVAILABLE** response code in CoAP indicates that the server is temporarily unavailable, often due to overload or maintenance.  
> **WALTER_MODEM_COAP_SEND_RSP_CODE_GATEWAY_TIMEOUT** = `504`  
> The **GATEWAY TIMEOUT** response code in CoAP indicates that the server, while acting as a gateway, did not receive a timely response from an upstream server.  
> **WALTER_MODEM_COAP_SEND_RSP_CODE_PROXYING_NOT_SUPPORTED** = `505`  
> The **PROXYING NOT SUPPORTED** response code in CoAP indicates that the proxy server does not support the requested operation.  
