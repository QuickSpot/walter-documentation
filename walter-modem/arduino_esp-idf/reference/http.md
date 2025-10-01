## Methods Overview

- [httpConfigProfile](#httpconfigprofile)
- [httpConnect](#httpconnect)
- [httpClose](#httpclose)
- [httpGetContextStatus](#httpgetcontextstatus)
- [httpQuery](#httpquery)
- [httpSend](#httpsend)
- [httpDidRing](#httpdidring)

## Enums Overview

- [WalterModemHttpContextState](#waltermodemhttpcontextstate)
- [WalterModemHttpQueryCmd](#waltermodemhttpquerycmd)
- [WalterModemHttpSendCmd](#waltermodemhttpsendcmd)
- [WalterModemHttpPostParam](#waltermodemhttppostparam)

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
> You first need call tlsConfigProfile

#### Params

| Param               | Description                                                                                                           | Default   |
| ------------------- | --------------------------------------------------------------------------------------------------------------------- | --------- |
| `profileId`         | HTTP profile id (0, 1 or 2).                                                                                          |           |
| `serverName`        | The server name to connect to.                                                                                        |           |
| `port`              | The port of the server to connect to.                                                                                 | **80**    |
| `tlsProfileId`      | If not 0, TLS is used with the given profile (1-6).                                                                   | **0**     |
| `useBasicAuth`      | Set true to use basic auth and send username/pw.                                                                      | **false** |
| `authUser`          | Username.                                                                                                             | **""**    |
| `authPass`          | Password.                                                                                                             | **""**    |
| `maxTimeout`        | Maximum data transfer time-out in seconds.                                                                            | **120**   |
| `cnxTimeout`        | Maximum time in seconds to wait for the HTTP server response.                                                         | **60**    |
| `inactivityTimeout` | If this parameter is not zero, it defines the longest permitted reduced throughput period.                            | **15**    |
| `rsp`               | Pointer to a modem response structure to save the result of the command in. When NULL is given the result is ignored. | **NULL**  |
| `cb`                | Optional callback argument, when not NULL this function will return immediately.                                      | **NULL**  |
| `args`              | Optional argument to pass to the callback.                                                                            | **NULL**  |

#### Returns

`bool`  
True on success, False otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_HTTP_PROFILE, 1)
CONFIG(SERVER_NAME, const char* , "example.com")
CONFIG_UINT16(SERVER_PORT, 80)

// ...

if(modem.httpConfigProfile(MODEM_HTTP_PROFILE, SERVER_NAME, SERVER_PORT)) {
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

Establish a HTTP connection.

Make an HTTP connection using a predefined profile configured using [httpConfigProfile](#httpconfigprofile).

> [!WARNING]
> This modem command will also return **OK** whilst establishing the connection in the
> background, so you need to use httpGetContextStatus to poll when the connection
> is ready to be used.

#### Params

| Param       | Description                 | Default  |
| ----------- | --------------------------- | -------- |
| `profileId` | HTTP profile id (0, 1 or 2) |          |
| `rsp`       | Response object.            | **NULL** |
| `cb`        | Callback.                   | **NULL** |
| `args`      | Callback arguments.         | **NULL** |

#### Returns

`bool`  
True on success, false otherwise

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_HTTP_PROFILE, 1)

// ...

modem.httpConnect(MODEM_HTTP_PROFILE)

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG_UINT8(MODEM_HTTP_PROFILE, 1)

// ...

modem.httpConnect(MODEM_HTTP_PROFILE)

// ...
```

<!-- tabs:end -->

---

### `httpClose`

Close an HTTP connection

Close the HTTP connection for the given HTTP context.

> [!WARNING]
> Avoid connect and disconnect if possible.

#### Params

| Param       | Description                 | Default  |
| ----------- | --------------------------- | -------- |
| `profileId` | HTTP profile id (0, 1 or 2) |          |
| `rsp`       | Response object.            | **NULL** |
| `cb`        | Callback.                   | **NULL** |
| `args`      | Callback arguments.         | **NULL** |

#### Returns

`bool`  
True on success, false otherwise

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_HTTP_PROFILE, 1)

// ...

modem.httpClose(MODEM_HTTP_PROFILE)

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG_UINT8(MODEM_HTTP_PROFILE, 1)

// ...

modem.httpClose(MODEM_HTTP_PROFILE)

// ...
```

<!-- tabs:end -->

---

### `httpGetContextStatus`

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

while (!httpGetContextStatus(MODEM_HTTP_PROFILE)) {
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

while (!httpGetContextStatus(MODEM_HTTP_PROFILE)) {
    vTaskDelay(pdMS_TO_TICKS(100));
}

// ...
```

<!-- tabs:end -->

---

### `httpQuery`

Perform an HTTP **GET**, **DELETE** or **HEAD** request.

> [!NOTE]
> No need to first open the connection with the buggy [httpConnect](#httpconnect) command
> unless you need TLS + a private key.

#### Params

| Param                | Description                                               | Default                             |
| -------------------- | --------------------------------------------------------- | ----------------------------------- |
| `profileId`          | The profile id (0, 1, or 2) of the HTTP context.          |                                     |
| `uri`                | The URI.                                                  |                                     |
| `httpQueryCmd`       | GET, DELETE, or HEAD [command](#waltermodemhttpquerycmd). | **WALTER_MODEM_HTTP_QUERY_CMD_GET** |
| `contentTypeBuf`     | Optional user buffer to store content type header in.     | **NULL**                            |
| `contentTypeBufSize` | Size of the user buffer, including terminating null byte. | **0**                               |
| `rsp`                | Response object.                                          | **NULL**                            |
| `cb`                 | Callback.                                                 | **NULL**                            |
| `args`               | Callback arguments.                                       | **NULL**                            |

#### Returns

`bool`  
True on success, False otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_HTTP_PROFILE, 1)

// ...

static char ctbuf[32];

if (modem.httpQuery(
        MODEM_HTTP_PROFILE,
        "/",
        WALTER_MODEM_HTTP_QUERY_CMD_GET,
        ctbuf,
        sizeof(ctbuf))) {
    Serial.print("Info: HTTP query successful, response: ");
    Serial.println(ctbuf);
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

static char ctbuf[32];

if (modem.httpQuery(
        MODEM_HTTP_PROFILE,
        "/",
        WALTER_MODEM_HTTP_QUERY_CMD_GET,
        ctbuf,
        sizeof(ctbuf))) {
    ESP_LOGI("http_docs_demo", "HTTP query successful, response: %s", ctbuf);
} else {
    ESP_LOGE("http_docs_demo", "Failed to perform HTTP query");
}

// ...
```

<!-- tabs:end -->

---

### `httpSend`

Perform a http **POST** or **PUT** request.

> [!NOTE]
> No need to first open the connection with the buggy [httpConnect](#httpconnect) command
> unless you need TLS + a private key.

#### Params

| Param                | Description                                               | Default                                      |
| -------------------- | --------------------------------------------------------- | -------------------------------------------- |
| `profileId`          | The profile id (0, 1 or 2) of the HTTP context.           |                                              |
| `uri`                | The URI.                                                  |                                              |
| `data`               | Data to be sent to the server.                            |                                              |
| `dataSize`           | Length of the data buffer to be sent to the server.       |                                              |
| `httpSendCmd`        | POST or PUT [command](#waltermodemhttpsendcmd).           | **WALTER_MODEM_HTTP_SEND_CMD_POST**          |
| `httpPostParam`      | [Content type](#waltermodemhttppostparam) *(enum value)*. | **WALTER_MODEM_HTTP_POST_PARAM_UNSPECIFIED** |
| `contentTypeBuf`     | Optional user buffer to store content type header in.     | **NULL**                                     |
| `contentTypeBufSize` | Size of the user buffer, including terminating null byte. | **0**                                        |
| `rsp`                | Response object.                                          | **NULL**                                     |
| `cb`                 | Callback.                                                 | **NULL**                                     |
| `args`               | Callback arguments.                                       | **NULL**                                     |

#### Returns

`bool`  
True on success, False otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_HTTP_PROFILE, 1)

// ...

static const char demoData[] = "Demo Data";
static char ctbuf[32];

if (modem.httpSend(
        MODEM_HTTP_PROFILE,
        "/",
        (const uint8_t *)demoData,
        sizeof(demoData) - 1,
        WALTER_MODEM_HTTP_SEND_CMD_POST,
        WALTER_MODEM_HTTP_POST_PARAM_OCTET_STREAM,
        ctbuf,
        sizeof(ctbuf))) {
    Serial.print("Info: HTTP POST sent successfully, response: ");
    Serial.println(ctbuf);
} else {
    Serial.println("Error: Failed to send HTTP query");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG_UINT8(MODEM_HTTP_PROFILE, 1)

// ...

static const char demoData[] = "Demo Data";
static char ctbuf[32];

if (modem.httpSend(
        MODEM_HTTP_PROFILE,
        "/",
        (const uint8_t *)demoData,
        sizeof(demoData) - 1,
        WALTER_MODEM_HTTP_SEND_CMD_POST,
        WALTER_MODEM_HTTP_POST_PARAM_OCTET_STREAM,
        ctbuf,
        sizeof(ctbuf))) {
    ESP_LOGI("http_docs_demo", "HTTP POST sent successfully, response: %s", ctbuf);
} else {
    ESP_LOGE("http_docs_demo", "Failed to send HTTP query");
}

// ...
```

<!-- tabs:end -->

---

### `httpDidRing`

Retrieve the response on an earlier HTTP request.

This function checks if the modem already received a response from the HTTP server.

#### Params

| Param           | Description                                                                 | Default  |
| --------------- | --------------------------------------------------------------------------- | -------- |
| `profileId`     | Profile for which to get the response.                                      |          |
| `targetBuf`     | User buffer to store response in.                                           |          |
| `targetBufSize` | Size of the user buffer, including space for a terminating null byte.       |          |
| `rsp`           | Pointer to a modem response structure to save the result of the command in. | **NULL** |

#### Returns

`bool`  
True on success, false if no data arrived or error or no data expected.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG_UINT8(MODEM_HTTP_PROFILE, 1)

WalterModemRsp rsp = {};

// ...

uint8_t incomingBuf[256] = { 0 };

while (modem.httpDidRing(MODEM_HTTP_PROFILE, incomingBuf, sizeof(incomingBuf), &rsp)) {
    Serial.print("status code: ");
    Serial.println(rsp.data.httpResponse.httpStatus);
    Serial.print("content type: ");
    Serial.println(ctbuf);

    Serial.print("[");
    Serial.print(incomingBuf);
    Serial.println("]\r\n");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG_UINT8(MODEM_HTTP_PROFILE, 1)

WalterModemRsp rsp = {};

// ...

uint8_t incomingBuf[256] = { 0 };

while (modem.httpDidRing(MODEM_HTTP_PROFILE, incomingBuf, sizeof(incomingBuf), &rsp)) {
    ESP_LOGI("http_docs_demo", "status code: %d", rsp.data.httpResponse.httpStatus);
    ESP_LOGI("http_docs_demo", "content type: %s", ctbuf);
    ESP_LOGI("http_docs_demo", "[%s]\r\n", incomingBuf);
}

// ...
```

<!-- tabs:end -->

---

## Enums

### `WalterModemHttpContextState`

The state of an http context.

> **WALTER_MODEM_HTTP_CONTEXT_STATE_IDLE**  
> **WALTER_MODEM_HTTP_CONTEXT_STATE_EXPECT_RING**  
> **WALTER_MODEM_HTTP_CONTEXT_STATE_GOT_RING**  

### `WalterModemHttpQueryCmd`

The possible commands for a HTTP query operation.

> **WALTER_MODEM_HTTP_QUERY_CMD_GET**  
> Perform a GET request  
> **WALTER_MODEM_HTTP_QUERY_CMD_HEAD**  
> Perform a HEAD request  
> **WALTER_MODEM_HTTP_QUERY_CMD_DELETE**  
> Perform a DELETE request  

### `WalterModemHttpSendCmd`

The possible commands for a HTTP send operation.

> **WALTER_MODEM_HTTP_SEND_CMD_POST**  
> Perform a POST request  
> **WALTER_MODEM_HTTP_SEND_CMD_PUT**  
> Perform PUT request  

### `WalterModemHttpPostParam`

The possible post params for a HTTP send operation.

> **WALTER_MODEM_HTTP_POST_PARAM_URL_ENCODED** = `0`  
> Param type is encoded in the url  
> **WALTER_MODEM_HTTP_POST_PARAM_TEXT_PLAIN** = `1`  
> Param is plain text  
> **WALTER_MODEM_HTTP_POST_PARAM_OCTET_STREAM** = `2`  
> Param is an octet/byte stream  
> **WALTER_MODEM_HTTP_POST_PARAM_FORM_DATA** = `3`  
> Param is form data  
> **WALTER_MODEM_HTTP_POST_PARAM_JSON** = `4`  
> Param is JSON  
> **WALTER_MODEM_HTTP_POST_PARAM_UNSPECIFIED** = `99`  
> Param is unspecified  
