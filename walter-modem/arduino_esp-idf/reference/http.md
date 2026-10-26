## Methods Overview

- [httpConfigProfile](#httpconfigprofile)
- [httpConnect](#httpconnect)
- [httpClose](#httpclose)
- [httpQuery](#httpquery)
- [httpSend](#httpsend)
- [httpReceive](#httpreceive)
- [httpGetContextStatus](#httpgetcontextstatus) _(deprecated)_
- [httpDidRing](#httpdidring) _(deprecated)_

## Enums Overview

- [WalterModemHttpQueryCmd](#waltermodemhttpquerycmd)
- [WalterModemHttpSendCmd](#waltermodemhttpsendcmd)
- [WalterModemHttpPostParam](#waltermodemhttppostparam)

## Structs Overview

- [WalterModemHttpResponse](#waltermodemhttpresponse)

---

## Methods

### `httpConfigProfile`

Configure an HTTP profile.

This function will configure an HTTP profile
with parameters such as server name and auth info.

The profile information is stored persistently in the modem, it thus is possible
to store connection information once to prepare all settings,
and later rely on this preconfigured profile in the modem without the need to
set the parameters again in the actual code used in production.

> [!TIP]
> To use TLS, first configure a TLS profile with
> [tlsConfigProfile](/walter-modem/arduino_esp-idf/reference/tls_and_certificates.md#tlsconfigprofile)
> and pass its id as `tls_profile_id`.

> [!NOTE]
> When TLS is used and `port` is left at 80, the library uses port 443 instead.

#### Params

| Param                | Description                                                                                          | Default   |
| -------------------- | ---------------------------------------------------------------------------------------------------- | --------- |
| `profile_id`         | HTTP profile id (0, 1 or 2).                                                                         |           |
| `hostname`           | The server name to connect to.                                                                       |           |
| `port`               | The port of the server to connect to.                                                                | **80**    |
| `tls_profile_id`     | If not 0, TLS is used with the given profile (1-6).                                                  | **0**     |
| `use_basic_auth`     | Set true to use basic auth and send username/pw.                                                     | **false** |
| `auth_user`          | Username.                                                                                            | **""**    |
| `auth_pass`          | Password.                                                                                            | **""**    |
| `max_timeout`        | Maximum data transfer time-out in seconds.                                                           | **120**   |
| `cnx_timeout`        | Maximum time in seconds to wait for the HTTP server response. Must not be larger than `max_timeout`. | **60**    |
| `inactivity_timeout` | If this parameter is not zero, it defines the longest permitted reduced throughput period.           | **15**    |
| `rsp`                | Optional modem response structure to save the result in.                                             | **NULL**  |
| `cb`                 | Optional callback function, if set this function will not block.                                     | **NULL**  |
| `args`               | Optional argument to pass to the callback.                                                           | **NULL**  |

#### Returns

`bool`  
True on "OK" response, false otherwise. Also false when `cnx_timeout` is larger than `max_timeout`.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_HTTP_PROFILE, 1)
CONFIG(SERVER_NAME, const char* , "example.com")
CONFIG_UINT16(SERVER_PORT, 80)

// ...

if (modem.httpConfigProfile(MODEM_HTTP_PROFILE, SERVER_NAME, SERVER_PORT)) {
    Serial.println("Info: HTTP profile configured");
} else {
    Serial.println("Error: Failed to configure HTTP profile");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG_UINT8(MODEM_HTTP_PROFILE, 1)
CONFIG(SERVER_NAME, const char* , "example.com")
CONFIG_UINT16(SERVER_PORT, 80)

// ...

if (modem.httpConfigProfile(MODEM_HTTP_PROFILE, SERVER_NAME, SERVER_PORT)) {
    ESP_LOGI("http_docs_demo", "HTTP profile configured");
} else {
    ESP_LOGE("http_docs_demo", "Failed to configure the HTTP profile");
}

// ...
```

<!-- tabs:end -->

---

### `httpConnect`

Establish an HTTP connection.

Make an HTTP connection using a predefined profile configured using [httpConfigProfile](#httpconfigprofile).

> [!NOTE]
> This is only needed when you use TLS with a client private key.
> Otherwise [httpQuery](#httpquery) and [httpSend](#httpsend) connect by themselves.

> [!WARNING]
> This function waits for the modem to report the connect result, but it also returns true
> when the connection could not be established. Check the `rc` of the
> `WALTER_MODEM_HTTP_EVENT_CONNECTED` event, 0 means connected, see
> [setHTTPEventHandler](/walter-modem/arduino_esp-idf/reference/event_handlers.md#sethttpeventhandler).
> When the profile is already connected, it returns true right away.

#### Params

| Param        | Description                                                      | Default  |
| ------------ | ---------------------------------------------------------------- | -------- |
| `profile_id` | HTTP profile id (0, 1 or 2).                                     |          |
| `rsp`        | Optional modem response structure to save the result in.         | **NULL** |
| `cb`         | Optional callback function, if set this function will not block. | **NULL** |
| `args`       | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True when the modem reported the connect result or the profile was already connected, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_HTTP_PROFILE, 1)

// ...

if (modem.httpConnect(MODEM_HTTP_PROFILE)) {
    Serial.println("Info: HTTP connect requested");
} else {
    Serial.println("Error: Failed to connect HTTP profile");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG_UINT8(MODEM_HTTP_PROFILE, 1)

// ...

if (modem.httpConnect(MODEM_HTTP_PROFILE)) {
    ESP_LOGI("http_docs_demo", "HTTP connect requested");
} else {
    ESP_LOGE("http_docs_demo", "Failed to connect HTTP profile");
}

// ...
```

<!-- tabs:end -->

---

### `httpClose`

Close an HTTP connection.

Close the HTTP connection for the given HTTP context.
The library raises a `WALTER_MODEM_HTTP_EVENT_DISCONNECTED` event when the connection is closed.

> [!WARNING]
> Avoid connect and disconnect if possible.

#### Params

| Param        | Description                                                      | Default  |
| ------------ | ---------------------------------------------------------------- | -------- |
| `profile_id` | HTTP profile id (0, 1 or 2).                                     |          |
| `rsp`        | Optional modem response structure to save the result in.         | **NULL** |
| `cb`         | Optional callback function, if set this function will not block. | **NULL** |
| `args`       | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on "OK" response, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_HTTP_PROFILE, 1)

// ...

if (modem.httpClose(MODEM_HTTP_PROFILE)) {
    Serial.println("Info: HTTP connection closed");
} else {
    Serial.println("Error: Failed to close HTTP connection");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG_UINT8(MODEM_HTTP_PROFILE, 1)

// ...

if (modem.httpClose(MODEM_HTTP_PROFILE)) {
    ESP_LOGI("http_docs_demo", "HTTP connection closed");
} else {
    ESP_LOGE("http_docs_demo", "Failed to close HTTP connection");
}

// ...
```

<!-- tabs:end -->

---

### `httpQuery`

Perform an HTTP **GET**, **DELETE** or **HEAD** request.

This function returns as soon as the modem has accepted the request.
The response is announced with a `WALTER_MODEM_HTTP_EVENT_RING` event, read it with [httpReceive](#httpreceive).

> [!NOTE]
> No need to first open the connection with [httpConnect](#httpconnect)
> unless you need TLS + a private key.

#### Params

| Param                   | Description                                                                                        | Default                             |
| ----------------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------- |
| `profile_id`            | The profile id (0, 1 or 2) of the HTTP context.                                                    |                                     |
| `uri`                   | The URI.                                                                                           |                                     |
| `http_query_cmd`        | GET, DELETE or HEAD _([WalterModemHttpQueryCmd](#waltermodemhttpquerycmd))_.                       | **WALTER_MODEM_HTTP_QUERY_CMD_GET** |
| `content_type_buf`      | Not used by the library. The content type is reported in the `WALTER_MODEM_HTTP_EVENT_RING` event. | **NULL**                            |
| `content_type_buf_size` | Not used by the library.                                                                           | **0**                               |
| `extra_header_line`     | Optional extra HTTP header line to send.                                                           | **NULL**                            |
| `rsp`                   | Optional modem response structure to save the result in.                                           | **NULL**                            |
| `cb`                    | Optional callback function, if set this function will not block.                                   | **NULL**                            |
| `args`                  | Optional argument to pass to the callback.                                                         | **NULL**                            |

#### Returns

`bool`  
True on "OK" response, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_HTTP_PROFILE, 1)

// ...

if (modem.httpQuery(MODEM_HTTP_PROFILE, "/", WALTER_MODEM_HTTP_QUERY_CMD_GET)) {
    Serial.println("Info: HTTP GET sent, waiting for the response");
} else {
    Serial.println("Error: Failed to perform HTTP query");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG_UINT8(MODEM_HTTP_PROFILE, 1)

// ...

if (modem.httpQuery(MODEM_HTTP_PROFILE, "/", WALTER_MODEM_HTTP_QUERY_CMD_GET)) {
    ESP_LOGI("http_docs_demo", "HTTP GET sent, waiting for the response");
} else {
    ESP_LOGE("http_docs_demo", "Failed to perform HTTP query");
}

// ...
```

<!-- tabs:end -->

---

### `httpSend`

Perform an HTTP **POST** or **PUT** request.

This function returns as soon as the modem has accepted the request.
The response is announced with a `WALTER_MODEM_HTTP_EVENT_RING` event, read it with [httpReceive](#httpreceive).

> [!NOTE]
> No need to first open the connection with [httpConnect](#httpconnect)
> unless you need TLS + a private key.

> [!WARNING]
> `extra_header_line` is only sent when `http_post_param` is not `WALTER_MODEM_HTTP_POST_PARAM_UNSPECIFIED`.

#### Params

| Param                   | Description                                                                                        | Default                                      |
| ----------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| `profile_id`            | The profile id (0, 1 or 2) of the HTTP context.                                                    |                                              |
| `uri`                   | The URI.                                                                                           |                                              |
| `buf`                   | Data to be sent to the server.                                                                     |                                              |
| `buf_size`              | Length of the data buffer to be sent to the server.                                                |                                              |
| `http_send_cmd`         | POST or PUT _([WalterModemHttpSendCmd](#waltermodemhttpsendcmd))_.                                 | **WALTER_MODEM_HTTP_SEND_CMD_POST**          |
| `http_post_param`       | The content type _([WalterModemHttpPostParam](#waltermodemhttppostparam))_.                        | **WALTER_MODEM_HTTP_POST_PARAM_UNSPECIFIED** |
| `content_type_buf`      | Not used by the library. The content type is reported in the `WALTER_MODEM_HTTP_EVENT_RING` event. | **NULL**                                     |
| `content_type_buf_size` | Not used by the library.                                                                           | **0**                                        |
| `extra_header_line`     | Optional extra HTTP header line to send.                                                           | **NULL**                                     |
| `rsp`                   | Optional modem response structure to save the result in.                                           | **NULL**                                     |
| `cb`                    | Optional callback function, if set this function will not block.                                   | **NULL**                                     |
| `args`                  | Optional argument to pass to the callback.                                                         | **NULL**                                     |

#### Returns

`bool`  
True on "OK" response, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_HTTP_PROFILE, 1)

// ...

static char demoData[] = "{\"hello\": \"walter\"}";

if (modem.httpSend(
        MODEM_HTTP_PROFILE,
        "/",
        (uint8_t *)demoData,
        sizeof(demoData) - 1,
        WALTER_MODEM_HTTP_SEND_CMD_POST,
        WALTER_MODEM_HTTP_POST_PARAM_JSON)) {
    Serial.println("Info: HTTP POST sent, waiting for the response");
} else {
    Serial.println("Error: Failed to send HTTP POST");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG_UINT8(MODEM_HTTP_PROFILE, 1)

// ...

static char demoData[] = "{\"hello\": \"walter\"}";

if (modem.httpSend(
        MODEM_HTTP_PROFILE,
        "/",
        (uint8_t *)demoData,
        sizeof(demoData) - 1,
        WALTER_MODEM_HTTP_SEND_CMD_POST,
        WALTER_MODEM_HTTP_POST_PARAM_JSON)) {
    ESP_LOGI("http_docs_demo", "HTTP POST sent, waiting for the response");
} else {
    ESP_LOGE("http_docs_demo", "Failed to send HTTP POST");
}

// ...
```

<!-- tabs:end -->

---

### `httpReceive`

Receive HTTP data from the modem buffer.

This function reads the body of an HTTP response for a specific profile.
Call it after a `WALTER_MODEM_HTTP_EVENT_RING` event, which reports the status code,
content type and body length (`data_len`) of the response.

> [!WARNING]
> The modem's response carries no length, so exactly `buf_size` bytes are read.
> Pass the `data_len` reported by the `WALTER_MODEM_HTTP_EVENT_RING` event.
> A larger value makes the command wait until it times out,
> a smaller one fails the command with `WALTER_MODEM_STATE_NO_MEMORY`.

#### Params

| Param        | Description                                                                             | Default  |
| ------------ | --------------------------------------------------------------------------------------- | -------- |
| `profile_id` | The profile id (0, 1 or 2) of the HTTP context.                                         |          |
| `buf`        | User buffer to store the received data. The data is not null-terminated.                |          |
| `buf_size`   | The `data_len` from the ring event (0-65535). `buf` must hold at least this many bytes. |          |
| `rsp`        | Optional modem response structure to save the result in.                                | **NULL** |
| `cb`         | Optional callback function, if set this function will not block.                        | **NULL** |
| `args`       | Optional argument to pass to the callback.                                              | **NULL** |

#### Returns

`bool`  
True on "OK" response, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

static uint8_t inBuf[1024];

void myHTTPEventHandler(WMHTTPEventType event, const WMHTTPEventData *data, void *args)
{
    if (event != WALTER_MODEM_HTTP_EVENT_RING) {
        return;
    }

    if (data->data_len > sizeof(inBuf)) {
        Serial.printf("Error: HTTP response of %u bytes does not fit\r\n", data->data_len);
        return;
    }

    if (modem.httpReceive(data->profile_id, inBuf, data->data_len)) {
        Serial.printf("Info: HTTP %u (%s), %u bytes: %.*s\r\n",
                      data->status, data->content_type, data->data_len,
                      data->data_len, (const char *)inBuf);
    } else {
        Serial.println("Error: Failed to receive the HTTP response");
    }
}

// ...

modem.setHTTPEventHandler(myHTTPEventHandler);

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

static uint8_t inBuf[1024];

void myHTTPEventHandler(WMHTTPEventType event, const WMHTTPEventData *data, void *args)
{
    if (event != WALTER_MODEM_HTTP_EVENT_RING) {
        return;
    }

    if (data->data_len > sizeof(inBuf)) {
        ESP_LOGE("http_docs_demo", "HTTP response of %u bytes does not fit", data->data_len);
        return;
    }

    if (modem.httpReceive(data->profile_id, inBuf, data->data_len)) {
        ESP_LOGI("http_docs_demo", "HTTP %u (%s), %u bytes: %.*s",
                 data->status, data->content_type, data->data_len,
                 data->data_len, (const char *)inBuf);
    } else {
        ESP_LOGE("http_docs_demo", "Failed to receive the HTTP response");
    }
}

// ...

modem.setHTTPEventHandler(myHTTPEventHandler);

// ...
```

<!-- tabs:end -->

---

### `httpGetContextStatus`

> [!WARNING]
> **DEPRECATED:** This method will be removed in a future release.
> Use the `WALTER_MODEM_HTTP_EVENT_CONNECTED`, `WALTER_MODEM_HTTP_EVENT_DISCONNECTED` and
> `WALTER_MODEM_HTTP_EVENT_CONNECTION_CLOSED` events instead, see
> [setHTTPEventHandler](/walter-modem/arduino_esp-idf/reference/event_handlers.md#sethttpeventhandler).

Get the status of an HTTP context.

This function checks if a given HTTP context is connected and ready for use.

#### Params

| Param       | Description                                     | Default |
| ----------- | ----------------------------------------------- | ------- |
| `profileId` | The profile id (0, 1 or 2) of the HTTP context. |         |

#### Returns

`bool`  
True if the given HTTP context is connected, false if not.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_HTTP_PROFILE, 1)

// ...

while (!modem.httpGetContextStatus(MODEM_HTTP_PROFILE)) {
    vTaskDelay(pdMS_TO_TICKS(100));
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG_UINT8(MODEM_HTTP_PROFILE, 1)

// ...

while (!modem.httpGetContextStatus(MODEM_HTTP_PROFILE)) {
    vTaskDelay(pdMS_TO_TICKS(100));
}

// ...
```

<!-- tabs:end -->

---

### `httpDidRing`

> [!WARNING]
> **DEPRECATED:** This method will be removed in a future release.
> Use [httpReceive](#httpreceive) instead, it is what this method calls internally.

Receive data from an incoming HTTP connection.

`targetBufSize` must be the `data_len` reported by the `WALTER_MODEM_HTTP_EVENT_RING` event,
see [httpReceive](#httpreceive).

#### Params

| Param           | Description                                                                         | Default  |
| --------------- | ----------------------------------------------------------------------------------- | -------- |
| `profileId`     | The profile id (0, 1 or 2) of the HTTP context.                                     |          |
| `targetBuf`     | User buffer to store the received data. The data is not null-terminated.            |          |
| `targetBufSize` | The `data_len` from the ring event. `targetBuf` must hold at least this many bytes. |          |
| `rsp`           | Optional modem response structure to save the result in.                            | **NULL** |

#### Returns

`bool`  
True on "OK" response, false otherwise.

---

## Enums

### `WalterModemHttpQueryCmd`

The possible commands for an HTTP query operation.

> **WALTER_MODEM_HTTP_QUERY_CMD_GET** = `0`  
> Perform a GET request.  
> **WALTER_MODEM_HTTP_QUERY_CMD_HEAD** = `1`  
> Perform a HEAD request.  
> **WALTER_MODEM_HTTP_QUERY_CMD_DELETE** = `2`  
> Perform a DELETE request.

### `WalterModemHttpSendCmd`

The possible commands for an HTTP send operation.

> **WALTER_MODEM_HTTP_SEND_CMD_POST** = `0`  
> Perform a POST request.  
> **WALTER_MODEM_HTTP_SEND_CMD_PUT** = `1`  
> Perform a PUT request.

### `WalterModemHttpPostParam`

The possible content types for an HTTP send operation.

> **WALTER_MODEM_HTTP_POST_PARAM_URL_ENCODED** = `0`  
> URL encoded form data.  
> **WALTER_MODEM_HTTP_POST_PARAM_TEXT_PLAIN** = `1`  
> Plain text.  
> **WALTER_MODEM_HTTP_POST_PARAM_OCTET_STREAM** = `2`  
> An octet/byte stream.  
> **WALTER_MODEM_HTTP_POST_PARAM_FORM_DATA** = `3`  
> Multipart form data.  
> **WALTER_MODEM_HTTP_POST_PARAM_JSON** = `4`  
> JSON.  
> **WALTER_MODEM_HTTP_POST_PARAM_UNSPECIFIED** = `99`  
> No content type is sent.

---

## Structs

### `WalterModemHttpResponse`

The HTTP response data in `rsp.data.httpResponse`.

> [!WARNING]
> The library does not fill in this struct, its fields are not valid after [httpReceive](#httpreceive).
> The status code, content type and body length of a response are reported in the
> `WALTER_MODEM_HTTP_EVENT_RING` event
> ([WMHTTPEventData](/walter-modem/arduino_esp-idf/reference/event_handlers.md#wmhttpeventdata)).

| Field           | Type       | Description              |
| --------------- | ---------- | ------------------------ |
| `httpStatus`    | `uint16_t` | The HTTP status code.    |
| `contentLength` | `uint16_t` | The HTTP content length. |
