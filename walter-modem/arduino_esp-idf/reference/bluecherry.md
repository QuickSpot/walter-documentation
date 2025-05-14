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
if (!modem.blueCherryProvision(BlueCherryZTP::getCert(), BlueCherryZTP::getPrivKey(), bc_ca_cert)) {
    Serial.println("BlueCherry: Failed to upload the DTLS certificates");
    return
} else {
    Serial.println("BlueCherry: Succesfully uploaded the DTLS certificates");
}
```

##### **ESP-IDF**

```cpp
if (!modem.blueCherryProvision(BlueCherryZTP::getCert(), BlueCherryZTP::getPrivKey(), bc_ca_cert)) {
    ESP_LOGE(TAG, "Failed to upload the DTLS certificates");
    return
} else {
    ESP_LOGE(TAG, "Succesfully uploaded the DTLS certificates");
}
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
if (!modem.blueCherryIsProvisioned()) {
    Serial.println("BlueCherry: not provisioned!");
    return
} else {
    Serial.println("BlueCherry: provisioned!");
}
```

##### **ESP-IDF**

```cpp
if (!modem.blueCherryIsProvisioned()) {
    ESP_LOGE(TAG, "not provisioned!");
    return
} else {
    ESP_LOGE(TAG, "provisioned!");
}
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
if (!modem.blueCherryInit(BC_TLS_PROFILE, otaBuffer, &rsp)) {
    Serial.println("BlueCherry: not provisioned!");
    return
} else {
    Serial.println("BlueCherry: provisioned!");
}
```

##### **ESP-IDF**

```cpp
if (!modem.blueCherryInit(BC_TLS_PROFILE, otaBuffer, &rsp)) {
    ESP_LOGE(TAG, "not provisioned!");
    return
} else {
    ESP_LOGE(TAG, "provisioned!");
}
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
WalterModemRsp rsp = {};
if (modem.getCellInformation(WALTER_MODEM_SQNMONI_REPORTS_SERVING_CELL, &rsp)) {
    char msg[18];
    snprintf(msg, sizeof(msg), "{\"RSRP\": %7.2f}", rsp.data.cellInformation.rsrp);
    modem.blueCherryPublish(0x84, sizeof(msg) - 1, (uint8_t *)msg);
}
```

##### **ESP-IDF**

```cpp
WalterModemRsp rsp = {};
if (modem.getCellInformation(WALTER_MODEM_SQNMONI_REPORTS_SERVING_CELL, &rsp)) {
    char msg[18];
    snprintf(msg, sizeof(msg), "{\"RSRP\": %7.2f}", rsp.data.cellInformation.rsrp);
    modem.blueCherryPublish(0x84, sizeof(msg) - 1, (uint8_t *)msg);
}
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
WalterModemRsp rsp = {};

do {
    if (!modem.blueCherrySync(&rsp)) {
        Serial.printf(
            "Error during BlueCherry cloud platform synchronisation: %d\n",
            rsp.data.blueCherry.state);
        modem.softReset();
        lteConnect();
        return;
    }
} while (!rsp.data.blueCherry.syncFinished);

```

##### **ESP-IDF**

```cpp
WalterModemRsp rsp = {};

do {
    if (!modem.blueCherrySync(&rsp)) {
        ESP_LOGE(
            TAG,
            "Error during BlueCherry cloud platform synchronisation: %d",
            rsp.data.blueCherry.state);
        modem.softReset();
        lteConnect();
        return;
    }
} while(!rsp.data.blueCherry.syncFinished)
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
if (!modem.blueCherryClose()) {
    Serial.println("BlueCherry: Could not Close bluecherry");
    return
} else {
    Serial.println("BlueCherry: Closed bluecherry");
}
```

##### **ESP-IDF**

```cpp
if (!modem.blueCherryClose()) {
    ESP_LOGE(TAG, "Could not Close bluecherry");
    return
} else {
    ESP_LOGE(TAG, "Closed bluecherry");
}
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
