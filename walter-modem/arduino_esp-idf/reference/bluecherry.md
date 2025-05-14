## Methods Overview

- [blueCherryProvision](#bluecherryprovision)
- [blueCherryIsProvisioned](#bluecherryisprovisioned)
- [blueCherryInit](#bluecherryinit)
- [blueCherryPublish](#bluecherrypublish)
- [blueCherrySync](#bluecherrysync)
- [blueCherryDidRing](#bluecherrydidring)
- [blueCherryClose](#bluecherryclose)

## Enums Overview

- [WalterModemBlueCherryStatus](#waltermodembluecherrystatus)
- [WalterModemBlueCherryEventType](#waltermodembluecherryeventtype)

## Methods

### `blueCherryProvision`

Upload BlueCherry credentials to the modem.

Upload Walter's certificate and private key and the BlueCherry cloud server CA certificate to the modem.

> [!NOTE]
> The key parameters are NULL terminated strings containing the PEM data with each line terminated by CRLF (\r\n).

> [!WARNING]
> profile `0`,`5`,`6` are reserved for BlueCherry

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
```

##### **ESP-IDF**

```cpp
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

#### **ESP-IDF**

<!-- tabs:end -->

### `blueCherryIsProvisioned`

Check if Walter is provisioned for BlueCherry IoT connectivity.

This function checks if the necessary certificates and private key are present in the modem's NVRAM.

> [!NOTE]
> It does not check if the credentials are valid, but only checks if the BlueCherry reserved slot indexes are occupied inside the modem's NVRAM.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
```

##### **ESP-IDF**

```cpp
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

#### **ESP-IDF**

<!-- tabs:end -->

### `blueCherryInit`

Initialize BlueCherry `MQTT <-> CoAP` bridge.

This function will set the TLS profile id and initialize the accumulated outgoing datagram, initialize the current message id to 1, the last acknowledged id to 0 and set the state machine to IDLE.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
```

##### **ESP-IDF**

```cpp
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

#### **ESP-IDF**

<!-- tabs:end -->

### `blueCherryPublish`

Enqueue a MQTT publish message.

This function will add the message to the accumulated outgoing datagram, which will - after blueCherrySync - be sent to the BlueCherry cloud server and published through MQTT.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
```

##### **ESP-IDF**

```cpp
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

#### **ESP-IDF**

<!-- tabs:end -->

### `blueCherrySync`

Send accumulated MQTT messages and poll for incoming data.

This function will send all accumulated MQTT publish messages to the BlueCherry cloud server,
and ask the server for an acknowledgement and for the new incoming MQTT messages since the last blueCherrySync call.

> [!WARNING]
> Even if nothing was enqueued for publish, this call must frequently be executed if Walter is subscribed to one or more MQTT topics or has enabled BlueCherry OTA updates.

> [!NOTE]
> A response might not fit in a single datagram response.
> As long as `syncFinished` is false, this function needs to be called again repeatedly.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
```

##### **ESP-IDF**

```cpp
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

#### **ESP-IDF**

<!-- tabs:end -->

### `blueCherryDidRing`

Poll BlueCherry for a received response.

> [!NOTE]
> This call is named `blueCherryDidRing` for consistancy with the HTTP, CoAP and other polling network calls.

> [!NOTE]
> It can only be used after a blueCherrySync call, and will return the response from the server (an ACK for any published messages, and a list of incoming messages for MQTT topics Walter is subscribed to, if any).
>
> Only after the (possibly empty) response has been received, or a timeout has been reported, it will be possible to publish more data or do a new blueCherrySync call.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
```

##### **ESP-IDF**

```cpp
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

#### **ESP-IDF**

<!-- tabs:end -->

### `blueCherryClose`

Close the BlueCherry platform CoAP connection.

> [!TIP]
> This function should not have to be called, except when using `deepSleep`.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
```

##### **ESP-IDF**

```cpp
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

#### **ESP-IDF**

<!-- tabs:end -->

## Enums

### `WalterModemBlueCherryStatus`

The possible statuses of a BlueCherry communication cycle.

### `WalterModemBlueCherryEventType`

The possible types of BlueCherry events.
