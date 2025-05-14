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

This function will create a CoAP context if it was not open yet.
This needs to be done before you can set headers or options or send or receive data.

> [!WARNING]
> profile **1** is reserved for BlueCherry and will not be ussable when it is enabled

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
if (!modem.coapCreateContext(MODEM_COAP_PROFILE, "coap.me", 5683)) {
    Serial.println("CoAP: Could not create COAP context.");
    return;
} else {
    Serial.println("CoAP: Successfully created or refreshed COAP context.");
}
```

##### **ESP-IDF**

```cpp
if (!modem.coapCreateContext(MODEM_COAP_PROFILE, "coap.me", 5683)) {
    ESP_LOGE(TAG, "Could not create COAP context.");
    return;
} else {
    ESP_LOGI(TAG, "Successfully created or refreshed COAP context.");
}
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

| Param          | Description                                                      | Default  |
| -------------- | ---------------------------------------------------------------- | -------- |
| `profileId`    | CoAP profile ID (0 is used by BlueCherry).                       |          |
| `serverName`   | The server name to connect to.                                   |          |
| `port`         | The port of the server to connect to.                            |          |
| `tlsProfileId` | If not 0, DTLS is used with the given profile (1–6).             | **0**    |
| `localPort`    | The local port to use (0 = random).                              | **-1**   |
| `rsp`          | Optional modem response structure to save the result in.         | **NULL** |
| `cb`           | Optional callback function, if set this function will not block. | **NULL** |
| `args`         | Optional argument to pass to the callback.                       | **NULL** |


#### **ESP-IDF**

| Param          | Description                                                      | Default  |
| -------------- | ---------------------------------------------------------------- | -------- |
| `profileId`    | CoAP profile ID (0 is used by BlueCherry).                       |          |
| `serverName`   | The server name to connect to.                                   |          |
| `port`         | The port of the server to connect to.                            |          |
| `tlsProfileId` | If not 0, DTLS is used with the given profile (1–6).             | **0**    |
| `localPort`    | The local port to use (0 = random).                              | **-1**   |
| `rsp`          | Optional modem response structure to save the result in.         | **NULL** |
| `cb`           | Optional callback function, if set this function will not block. | **NULL** |
| `args`         | Optional argument to pass to the callback.                       | **NULL** |

<!-- tabs:end -->


### `coapClose`

Close a CoAP context.

This function will close a CoAP context previously opened with coapCreateContext.

> [!TIP]
> To change parameters such as the server name, you must first close the context using this call.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
if (!modem.coapClose(MODEM_COAP_PROFILE)) {
    Serial.println("CoAP: Could not close CoAP profile");
    return;
} else {
    Serial.println("CoAP: Successfully closed CoAP profile");
}
```

##### **ESP-IDF**

```cpp
if (!modem.coapClose(MODEM_COAP_PROFILE)) {
    ESP_LOGE(TAG, "Could not close CoAP profile");
    return;
} else {
    ESP_LOGI(TAG, "Successfully closed CoAP profile");
}
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

| Param       | Description                                                      | Default  |
| ----------- | ---------------------------------------------------------------- | -------- |
| `profileId` | CoAP profile ID (0 is used by BlueCherry).                       |          |
| `rsp`       | Optional modem response structure to save the result in.         | **NULL** |
| `cb`        | Optional callback function, if set this function will not block. | **NULL** |
| `args`      | Optional argument to pass to the callback.                       | **NULL** |


#### **ESP-IDF**

| Param       | Description                                                      | Default  |
| ----------- | ---------------------------------------------------------------- | -------- |
| `profileId` | CoAP profile ID (0 is used by BlueCherry).                       |          |
| `rsp`       | Optional modem response structure to save the result in.         | **NULL** |
| `cb`        | Optional callback function, if set this function will not block. | **NULL** |
| `args`      | Optional argument to pass to the callback.                       | **NULL** |

<!-- tabs:end -->

### `coapGetContextStatus`

Get the connection status of a CoAP context.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
if (!modem.coapGetContextStatus(MODEM_COAP_PROFILE)) {
    Serial.println("CoAP: CoAP profile is not connected to the remote server");
    return;
} else {
    Serial.println("CoAP: CoAP profile is connected to the remote server");
}
```

##### **ESP-IDF**

```cpp
if (!modem.coapGetContextStatus(MODEM_COAP_PROFILE)) {
    ESP_LOGE(TAG, "CoAP profile is not connected to the remote server");
    return;
} else {
    ESP_LOGI(TAG, "CoAP profile is connected to the remote server");
}
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

| Param       | Description                                | Default |
| ----------- | ------------------------------------------ | ------- |
| `profileId` | The profile ID (0, 1 or 2) of the context. | —       |


#### **ESP-IDF**

| Param       | Description                                | Default |
| ----------- | ------------------------------------------ | ------- |
| `profileId` | The profile ID (0, 1 or 2) of the context. | —       |


<!-- tabs:end -->

### `coapSetHeader`

Set a CoAP header.

> [!NOTE]
> This is not necessary, if you do not set the header.
> The message id and the token will be set to random values.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
if (!modem.coapSetHeader(MODEM_COAP_PROFILE, counter)) {
    Serial.println("CoAP: Could not set the CoAP header");
} else {
    Serial.print("CoAP: Set COAP header with message id ");
    Serial.println(counter);
}
```

##### **ESP-IDF**

```cpp
if (!modem.coapSetHeader(MODEM_COAP_PROFILE, counter)) {
    ESP_LOGE(TAG, "Could not set the CoAP header");
    return;
} else {
    ESP_LOGI(TAG, "Set COAP header with message id %d", counter);
}
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

| Param       | Description                                                                       | Default        |
| ----------- | --------------------------------------------------------------------------------- | -------------- |
| `profileId` | CoAP profile id (1 or 2 - 0 is used by BlueCherry)                                |                |
| `messageId` | The message id of the next message to send.                                       | **1**          |
| `token`     | The token of the next message to send as a string of 16 hex digits (max 8 bytes). | **"NO_TOKEN"** |
| `rsp`       | Optional modem response structure to save the result in.                          | **NULL**       |
| `cb`        | Optional callback function, if set this function will not block.                  | **NULL**       |
| `args`      | Optional argument to pass to the callback.                                        | **NULL**       |

#### **ESP-IDF**

| Param       | Description                                                                       | Default        |
| ----------- | --------------------------------------------------------------------------------- | -------------- |
| `profileId` | CoAP profile id (1 or 2 - 0 is used by BlueCherry)                                |                |
| `messageId` | The message id of the next message to send.                                       | **1**          |
| `token`     | The token of the next message to send as a string of 16 hex digits (max 8 bytes). | **"NO_TOKEN"** |
| `rsp`       | Optional modem response structure to save the result in.                          | **NULL**       |
| `cb`        | Optional callback function, if set this function will not block.                  | **NULL**       |
| `args`      | Optional argument to pass to the callback.                                        | **NULL**       |

<!-- tabs:end -->

### `coapSetOptions`

Set the options for the next CoAP message.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
if (!modem.coapSetOptions(MODEM_COAP_PROFILE,WALTER_MODEM_COAP_OPT_DELETE, WALTER_MODEM_COAP_OPT_CODE_URI_PATH)) {
    Serial.println("CoAP: Could not set the CoAP options");
    return
} else {
    Serial.println("CoAP: Set COAP options succesfully");
}
```

##### **ESP-IDF**

```cpp
if (!modem.coapSetOptions(MODEM_COAP_PROFILE,WALTER_MODEM_COAP_OPT_DELETE, WALTER_MODEM_COAP_OPT_CODE_URI_PATH)) {
    ESP_LOGE(TAG, "Could not set the CoAP options");
    return
} else {
    ESP_LOGI(TAG, "Set COAP options succesfully");
}
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

| Param       | Description                                                                                        | Default  |
| ----------- | -------------------------------------------------------------------------------------------------- | -------- |
| `profileId` | CoAP profile id (1 or 2)                                                                           |          |
| `action`    | The action code of the option.                                                                     |          |
| `code`      | The code of the options.                                                                           |          |
| `values`    | Optional values array, as a comma-delimited string of up to 6 strings or recognized option values. | **NULL** |
| `rsp`       | Optional modem response structure to save the result in.                                           | **NULL** |
| `cb`        | Optional callback function, if set this function will not block.                                   | **NULL** |
| `args`      | Optional argument to pass to the callback.                                                         | **NULL** |

#### **ESP-IDF**

| Param       | Description                                                                                        | Default  |
| ----------- | -------------------------------------------------------------------------------------------------- | -------- |
| `profileId` | CoAP profile id (1 or 2)                                                                           |          |
| `action`    | The action code of the option.                                                                     |          |
| `code`      | The code of the options.                                                                           |          |
| `values`    | Optional values array, as a comma-delimited string of up to 6 strings or recognized option values. | **NULL** |
| `rsp`       | Optional modem response structure to save the result in.                                           | **NULL** |
| `cb`        | Optional callback function, if set this function will not block.                                   | **NULL** |
| `args`      | Optional argument to pass to the callback.                                                         | **NULL** |

<!-- tabs:end -->

### `coapSendData`

Send a datagram

> [!NOTE]
> Preffered options/header need to be set beforehand using [coapSetOptions](#coapsetoptions) or [coapSetHeader](#coapsetheader)

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
if (!modem.coapSendData(
        MODEM_COAP_PROFILE,
        WALTER_MODEM_COAP_SEND_TYPE_CON,
        WALTER_MODEM_COAP_SEND_METHOD_GET,
        8,
        dataBuf)) {
    Serial.println("CoAP: Could not send COAP datagram");
    return;
} else {
    Serial.println("CoAP: Sent COAP datagram");
}
```

##### **ESP-IDF**

```cpp
if (!modem.coapSendData(
        MODEM_COAP_PROFILE,
        WALTER_MODEM_COAP_SEND_TYPE_CON,
        WALTER_MODEM_COAP_SEND_METHOD_GET,
        8,
        dataBuf)) {
    ESP_LOGE(TAG, "Could not send COAP datagram");
    return;
} else {
    ESP_LOGI(TAG, "Sent COAP datagram");
}
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

| Param       | Description                                                              | Default  |
| ----------- | ------------------------------------------------------------------------ | -------- |
| `profileId` | CoAP profile id (1 or 2; 0 should not be used and is used by BlueCherry) |          |
| `type`      | The type of message (NON, CON, ACK, RST).                                |          |
| `methodRsp` | The method or response code.                                             |          |
| `length`    | The length of the payload.                                               |          |
| `payload`   | The payload to send, max 1024 bytes.                                     |          |
| `rsp`       | Optional modem response structure to save the result in.                 | **NULL** |
| `cb`        | Optional callback function, if set this function will not block.         | **NULL** |
| `args`      | Optional argument to pass to the callback.                               | **NULL** |

#### **ESP-IDF**

| Param       | Description                                                              | Default  |
| ----------- | ------------------------------------------------------------------------ | -------- |
| `profileId` | CoAP profile id (1 or 2; 0 should not be used and is used by BlueCherry) |          |
| `type`      | The type of message (NON, CON, ACK, RST).                                |          |
| `methodRsp` | The method or response code.                                             |          |
| `length`    | The length of the payload.                                               |          |
| `payload`   | The payload to send, max 1024 bytes.                                     |          |
| `rsp`       | Optional modem response structure to save the result in.                 | **NULL** |
| `cb`        | Optional callback function, if set this function will not block.         | **NULL** |
| `args`      | Optional argument to pass to the callback.                               | **NULL** |

<!-- tabs:end -->

### `coapDidRing`

Fetch incoming CoAP messages, if any.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
while (modem.coapDidRing(MODEM_COAP_PROFILE, incomingBuf, sizeof(incomingBuf), &rsp)) {
    Serial.println("CoAP: incoming ring!");
}
```

##### **ESP-IDF**

```cpp
while (modem.coapDidRing(MODEM_COAP_PROFILE, incomingBuf, sizeof(incomingBuf), &rsp)) {
    ESP_LOGI(TAG, "incoming ring!");
}
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

| Param           | Description                                                        | Default  |
| --------------- | ------------------------------------------------------------------ | -------- |
| `profileId`     | Profile for which to get incoming data (1 or 2)                    |          |
| `targetBuf`     | User buffer to store response in.                                  |          |
| `targetBufSize` | Size of the user buffer, including space for a terminating 0-byte. |          |
| `rsp`           | Optional modem response structure to save the result in.           | **NULL** |

#### **ESP-IDF**

| Param           | Description                                                        | Default  |
| --------------- | ------------------------------------------------------------------ | -------- |
| `profileId`     | Profile for which to get incoming data (1 or 2)                    |          |
| `targetBuf`     | User buffer to store response in.                                  |          |
| `targetBufSize` | Size of the user buffer, including space for a terminating 0-byte. |          |
| `rsp`           | Optional modem response structure to save the result in.           | **NULL** |

<!-- tabs:end -->

## Enums

### `WalterModemCoapOptCode`

The possible option codes for the CoAP message.

<!-- tabs:start -->

#### **Arduino**

#### **ESP-IDF**

<!-- tabs:end -->

### `WalterModemCoapOptValue`

The possible option values for the CoAP message.

<!-- tabs:start -->

#### **Arduino**

#### **ESP-IDF**

<!-- tabs:end -->

### `WalterModemCoapOptAction`

The possible option actions for the CoAP message.

<!-- tabs:start -->

#### **Arduino**

#### **ESP-IDF**

<!-- tabs:end -->

### `WalterModemCoapSendType`

The possible CoAP send types.

<!-- tabs:start -->

#### **Arduino**

#### **ESP-IDF**

<!-- tabs:end -->

### `WalterModemCoapSendMethodRsp`

The possible CoAP send methods.

<!-- tabs:start -->

#### **Arduino**

#### **ESP-IDF**

<!-- tabs:end -->