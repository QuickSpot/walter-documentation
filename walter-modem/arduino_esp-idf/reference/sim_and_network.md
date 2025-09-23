## Methods Overview

- [getSIMState](#getsimstate)
- [getSIMCardID](#getsimcardid)
- [getSIMCardIMSI](#getsimcardimsi)
- [unlockSIM](#unlocksim)
- [setNetworkSelectionMode](#setnetworkselectionmode)
- [getNetworkRegState](#getnetworkregstate)
- [getOpState](#getopstate)
- [setOpState](#setopstate)
- [getRAT](#getrat)
- [setRAT](#setrat)
- [getRadioBands](#getradiobands)
- [setRadioBands](#setradiobands)
- [getRSSI](#getrssi)
- [getSignalQuality](#getsignalquality)
- [getCellInformation](#getcellinformation)

## Enums Overview

- [WalterModemNetworkSelMode](#waltermodemnetworkselmode)
- [WalterModemOperatorFormat](#waltermodemoperatorformat)
- [WalterModemBand](#waltermodemband)
- [WalterModemCEREGReportsType](#waltermodemceregreportstype)
- [WalterModemOpState](#waltermodemopstate)
- [WalterModemSIMState](#waltermodemsimstate)
- [WalterModemRat](#waltermodemrat)
- [WalterModemNetworkRegState](#waltermodemnetworkregstate)
- [WalterModemSQNMONIReportsType](#waltermodemsqnmonireportstype)
- [WalterModemRAI](#waltermodemrai)

---

## Methods

### `getSIMState`

Get the SIM state.

This function will get the state of the SIM card.

#### Params

| Param  | Description                                                      | Default  |
| ------ | ---------------------------------------------------------------- | -------- |
| `rsp`  | Optional modem response structure to save the result.            | **NULL** |
| `cb`   | Optional callback function, if set this function will not block. | **NULL** |
| `args` | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.getSIMState(&rsp)) {
    Serial.println(rsp.data.simState);
} else {
    Serial.println("Error: Failed to get SIM state");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.getSIMState(&rsp)) {
    ESP_LOGI("sim_and_network_docs_demo", rsp.data.simState);
} else {
    ESP_LOGE("sim_and_network_docs_demo", "Failed to get SIM state");
}

// ...
```

<!-- tabs:end -->

---

### `getSIMCardID`

Get the SIM ICCID and/or eUICCID.

This function will receive the ICCID (Integrated Circuit Card ID) and
eUICCID (embedded Universal Integrated Circuit Card ID) of the installed SIM card.

> [!NOTE]
> For this function to be able to actually read these numbers from the SIM,
> the modem must be in the WALTER_MODEM_OPSTATE_FULL or WALTER_MODEM_OPSTATE_NO_RF operational state.

#### Params

| Param  | Description                                                      | Default  |
| ------ | ---------------------------------------------------------------- | -------- |
| `rsp`  | Optional modem response structure to save the result.            | **NULL** |
| `cb`   | Optional callback function, if set this function will not block. | **NULL** |
| `args` | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.getSIMCardID(&rsp)) {
    Serial.println(rsp.data.simCardID);
} else {
    Serial.println("Error: Failed to get SIM card ID");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.getSIMCardID(&rsp)) {
    ESP_LOGI("sim_and_network_docs_demo", rsp.data.simCardID);
} else {
    ESP_LOGE("sim_and_network_docs_demo", "Failed to get SIM card ID");
}

// ...
```

<!-- tabs:end -->

---

### `getSIMCardIMSI`

Get the IMSI on the SIM card.

This function will receive the IMSI (International Mobile Subscriber Identity) number
which is currently active on the SIM card.

> [!NOTE]
> For this function to be able to actually read the IMSI from the SIM,
> the modem must be in the WALTER_MODEM_OPSTATE_FULL or WALTER_MODEM_OPSTATE_NO_RF operational state.

#### Params

| Param  | Description                                                      | Default  |
| ------ | ---------------------------------------------------------------- | -------- |
| `rsp`  | Optional modem response structure to save the result.            | **NULL** |
| `cb`   | Optional callback function, if set this function will not block. | **NULL** |
| `args` | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.getSIMCardIMSI(&rsp)) {
    Serial.println(rsp.data.imsi);
} else {
    Serial.println("Error: Failed to get SIM card IMSI");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.getSIMCardIMSI(&rsp)) {
    ESP_LOGI("sim_and_network_docs_demo", rsp.data.imsi);
} else {
    ESP_LOGE("sim_and_network_docs_demo", "Failed to get SIM card IMSI");
}

// ...
```

<!-- tabs:end -->

---

### `unlockSIM`

Set the SIM card's PIN code.

This function will set the PIN code of the SIM card.

> [!NOTE]
> For this function to work
> the modem must be in the WALTER_MODEM_OPSTATE_FULL or WALTER_MODEM_OPSTATE_NO_RF operational state.

#### Params

| Param  | Description                                                      | Default  |
| ------ | ---------------------------------------------------------------- | -------- |
| `rsp`  | Optional modem response structure to save the result.            | **NULL** |
| `cb`   | Optional callback function, if set this function will not block. | **NULL** |
| `args` | Optional argument to pass to the callback.                       | **NULL** |
| `pin`  | The PIN code of the SIM card, or NULL for no PIN.                |          |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.unlockSIM()) {
    Serial.println("SIM unlocked");
} else {
    Serial.println("Error: Failed to get SIM card IMSI");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (modem.unlockSIM()) {
    ESP_LOGI("sim_and_network_docs_demo", "SIM unlocked");
} else {
    ESP_LOGE("sim_and_network_docs_demo", "Failed to get SIM card IMSI");
}

// ...
```

<!-- tabs:end -->

---

### `setNetworkSelectionMode`

Set the network selection mode.

This function sets up the network selection mode that Walter should use.

> [!NOTE]
> For this function to work
> the modem must be in the WALTER_MODEM_OPSTATE_FULL operational state.

#### Params

| Param          | Description                                                         | Default                                            |
| -------------- | ------------------------------------------------------------------- | -------------------------------------------------- |
| `mode`         | The network selection mode to use.                                  | **WALTER_MODEM_NETWORK_SEL_MODE_AUTOMATIC**        |
| `operatorName` | The network operator name, used only if manual selection is chosen. | **NULL**                                           |
| `format`       | The format in which the network operator name is passed.            | **WALTER_MODEM_OPERATOR_FORMAT_LONG_ALPHANUMERIC** |
| `rsp`          | Optional modem response structure to save the result.               | **NULL**                                           |
| `cb`           | Optional callback function, if set this function will not block.    | **NULL**                                           |
| `args`         | Optional argument to pass to the callback.                          | **NULL**                                           |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.setNetworkSelectionMode(WALTER_MODEM_NETWORK_SEL_MODE_AUTOMATIC)) {
    Serial.println("Info: Network selection mode set to automatic");
} else {
    Serial.println("Error: Failed to set network selection mode to automatic");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (modem.setNetworkSelectionMode(WALTER_MODEM_NETWORK_SEL_MODE_AUTOMATIC)) {
    ESP_LOGI("sim_and_network_docs_demo", "SIM unlocked");
} else {
    ESP_LOGE("sim_and_network_docs_demo", "Failed to get SIM card IMSI");
}

// ...
```

<!-- tabs:end -->

---

### `getNetworkRegState`

Get the network registration state.

This function returns the current network registration state.

> [!NOTE]
> The state is buffered by the library and thus instantly available.

#### Returns

`WalterModemNetworkRegState`  
The current modem registration state.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

Serial.println(modem.getNetworkRegState());

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

ESP_LOGI("sim_and_network_docs_demo", modem.getNetworkRegState());

// ...
```

<!-- tabs:end -->

---

### `getOpState`

Get the operational state of the modem.

This function will request the operational state the modem is currently in.

#### Params

| Param  | Description                                                      | Default  |
| ------ | ---------------------------------------------------------------- | -------- |
| `rsp`  | Optional modem response structure to save the result.            | **NULL** |
| `cb`   | Optional callback function, if set this function will not block. | **NULL** |
| `args` | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.getOpState(&rsp)) {
    Serial.println(rsp.data.opState);
} else {
    Serial.println("Error: Failed to get operational state");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.getOpState(&rsp)) {
    ESP_LOGI("sim_and_network_docs_demo", rsp.data.opState);
} else {
    ESP_LOGE("sim_and_network_docs_demo", "Failed to get operational state");
}

// ...
```

<!-- tabs:end -->

---

### `setOpState`

Set the operational state of the modem.

This function will set the operational state of the modem.

#### Params

| Param     | Description                                                      | Default  |
| --------- | ---------------------------------------------------------------- | -------- |
| `opState` | The new operational state of the modem.                          |          |
| `rsp`     | Optional modem response structure to save the result.            | **NULL** |
| `cb`      | Optional callback function, if set this function will not block. | **NULL** |
| `args`    | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.setOpState(WALTER_MODEM_OPSTATE_FULL)) {
    Serial.println("Info: Operational state set to FULL");
} else {
    Serial.println("Error: Failed to set operational state to FULL");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (modem.setOpState(WALTER_MODEM_OPSTATE_FULL)) {
    ESP_LOGI("sim_and_network_docs_demo", "Operational state set to FULL");
} else {
    ESP_LOGE("sim_and_network_docs_demo", "Failed to set operational state to FULL");
}

// ...
```

<!-- tabs:end -->

---

### `getRAT`

Get the selected RAT (Radio Access Technology).

This function will request the Radio Access Technology which the modem should apply.

#### Params

| Param  | Description                                                      | Default  |
| ------ | ---------------------------------------------------------------- | -------- |
| `rsp`  | Optional modem response structure to save the result.            | **NULL** |
| `cb`   | Optional callback function, if set this function will not block. | **NULL** |
| `args` | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.getRAT(&rsp)) {
    Serial.println(rsp.data.rat);
} else {
    Serial.println("Error: Failed to get RAT");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.getRAT(&rsp)) {
    ESP_LOGI("sim_and_network_docs_demo", rsp.data.rat);
} else {
    ESP_LOGE("sim_and_network_docs_demo", "Failed to get RAT");
}

// ...
```

<!-- tabs:end -->

---

### `setRAT`

Set the RAT (Radio Access Technology).

This function will set the Radio Access Technology which the modem should apply.

#### Params

| Param  | Description                                                      | Default  |
| ------ | ---------------------------------------------------------------- | -------- |
| `rat`  | The new RAT to set.                                              |          |
| `rsp`  | Optional modem response structure to save the result.            | **NULL** |
| `cb`   | Optional callback function, if set this function will not block. | **NULL** |
| `args` | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.setRAT(WALTER_MODEM_RAT_LTEM)) {
    Serial.println("Info: RAT set to LTEM");
} else {
    Serial.println("Error: Failed to set RAT to LTEM");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (modem.setRAT(WALTER_MODEM_RAT_LTEM)) {
    ESP_LOGI("sim_and_network_docs_demo", "RAT set to LTEM");
} else {
    ESP_LOGE("sim_and_network_docs_demo", "Failed to set RAT to LTEM");
}

// ...
```

<!-- tabs:end -->

---

### `getRadioBands`

Get the radio bands that the modem is configured to use.

This function will retrieve the bands which are used to connect to the mobile network.

#### Params

| Param  | Description                                                      | Default  |
| ------ | ---------------------------------------------------------------- | -------- |
| `rsp`  | Optional modem response structure to save the result.            | **NULL** |
| `cb`   | Optional callback function, if set this function will not block. | **NULL** |
| `args` | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on success, false on error.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.getRadioBands(&rsp)) {
    Serial.println(rsp.data.bandSelCfgSet);
} else {
    Serial.println("Error: Failed to get radio bands");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.getRadioBands(&rsp)) {
    ESP_LOGI("sim_and_network_docs_demo", rsp.data.bandSelCfgSet);
} else {
    ESP_LOGE("sim_and_network_docs_demo", "Failed to get radio bands");
}

// ...
```

<!-- tabs:end -->

---

### `setRadioBands`

Set the radio bands the modem will use.

This function configures the radio bands the modem will use.

#### Params

| Param   | Description                                                      | Default  |
| ------- | ---------------------------------------------------------------- | -------- |
| `rat`   | Radio access technology.                                         |          |
| `bands` | Bitset of WalterModemBand bits to specify the bands.             |          |
| `rsp`   | Optional modem response structure to save the result.            | **NULL** |
| `cb`    | Optional callback function, if set this function will not block. | **NULL** |
| `args`  | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on success, false on error.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.setRadioBands(WalterModemRAT::WALTER_MODEM_RAT_LTEM, WALTER_MODEM_BAND_B20)) {
    Serial.println("Info: Radio bands set to B20");
} else {
    Serial.println("Error: Failed to set radio bands");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (modem.setRadioBands(WalterModemRAT::WALTER_MODEM_RAT_LTEM, WALTER_MODEM_BAND_B20)) {
    ESP_LOGI("sim_and_network_docs_demo", "Radio bands set to B20");
} else {
    ESP_LOGE("sim_and_network_docs_demo", "Failed to set radio bands");
}

// ...
```

<!-- tabs:end -->

---

### `getRSSI`

Get the current signal quality.

This function returns the current signal quality expressed as RSSI in dBm.
The typical RSSI range is from -113 dBm (weakest signal) to -51 dBm (strongest signal).

#### Params

| Param  | Description                                                      | Default  |
| ------ | ---------------------------------------------------------------- | -------- |
| `rsp`  | Optional modem response structure to save the result.            | **NULL** |
| `cb`   | Optional callback function, if set this function will not block. | **NULL** |
| `args` | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.getRSSI(&rsp)) {
    Serial.println(rsp.data.rssi);
} else {
    Serial.println("Error: Failed to get rssi");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.getRSSI(&rsp)) {
    ESP_LOGI("sim_and_network_docs_demo", rsp.data.rssi);
} else {
    ESP_LOGE("sim_and_network_docs_demo", "Failed to get rssi");
}

// ...
```

<!-- tabs:end -->

---

### `getSignalQuality`

Get extended RSRQ and RSRP signal quality.

This function returns the RSRQ (Reference Signal Received Quality)
and RSRP (Reference Signal Received Power) indicators of signal quality.

These metrics provide a detailed view of LTE signal quality beyond basic RSSI,
useful for assessing network performance and making handover decisions.

#### Params

| Param  | Description                                                      | Default  |
| ------ | ---------------------------------------------------------------- | -------- |
| `rsp`  | Optional modem response structure to save the result.            | **NULL** |
| `cb`   | Optional callback function, if set this function will not block. | **NULL** |
| `args` | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.getSignalQuality(&rsp)) {
    Serial.println("Signal Quality:");
    Serial.print("-> rsrq: ");
    Serial.println(rsp.data.signalQuality.rsrq);
    Serial.print("-> rsrp: ");
    Serial.println(rsp.data.signalQuality.rsrp);
} else {
    Serial.println("Error: Failed to get signal quality");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.getSignalQuality(&rsp)) {
    ESP_LOGI("sim_and_network_docs_demo", "Signal Quality:");
    ESP_LOGI("sim_and_network_docs_demo", "-> rsrq: %d", rsp.data.signalQuality.rsrq);
    ESP_LOGI("sim_and_network_docs_demo", "-> rsrp: %d", rsp.data.signalQuality.rsrp);
} else {
    ESP_LOGE("sim_and_network_docs_demo", "Failed to get signal quality");
}

// ...
```

<!-- tabs:end -->

---

### `getCellInformation`

Get information on the serving and neighbouring cells.

This function returns information such as operator,
cell ID, RSSI, and RSRP for the serving and neighbouring cells.

#### Params

| Param  | Description                                                                                      | Default                                       |
| ------ | ------------------------------------------------------------------------------------------------ | --------------------------------------------- |
| `type` | The type of cell information to retrieve. Defaults to the cell currently serving the connection. | **WALTER_MODEM_SQNMONI_REPORTS_SERVING_CELL** |
| `rsp`  | Optional modem response structure to save the result.                                            | **NULL**                                      |
| `cb`   | Optional callback function, if set this function will not block.                                 | **NULL**                                      |
| `args` | Optional argument to pass to the callback.                                                       | **NULL**                                      |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.getCellInformation(&rsp)) {
    Serial.println("Cell Information:");
    Serial.print("-> netName: ");
    Serial.println(rsp.data.cellInformation.netName);
    Serial.print("-> cc: ");
    Serial.println(rsp.data.cellInformation.cc);
    Serial.print("-> nc: ");
    Serial.println(rsp.data.cellInformation.nc);
    Serial.print("-> rsrp: ");
    Serial.println(rsp.data.cellInformation.rsrp, 2);
    Serial.print("-> cinr: ");
    Serial.println(rsp.data.cellInformation.cinr, 2);
    Serial.print("-> rsrq: ");
    Serial.println(rsp.data.cellInformation.rsrq, 2);
    Serial.print("-> tac: ");
    Serial.println(rsp.data.cellInformation.tac);
    Serial.print("-> pci: ");
    Serial.println(rsp.data.cellInformation.pci);
    Serial.print("-> earfcn: ");
    Serial.println(rsp.data.cellInformation.earfcn);
    Serial.print("-> rssi: ");
    Serial.println(rsp.data.cellInformation.rssi, 2);
    Serial.print("-> paging: ");
    Serial.println(rsp.data.cellInformation.paging);
    Serial.print("-> cid: ");
    Serial.println(rsp.data.cellInformation.cid);
    Serial.print("-> band: ");
    Serial.println(rsp.data.cellInformation.band);
    Serial.print("-> bw: ");
    Serial.println(rsp.data.cellInformation.bw);
    Serial.print("-> ceLevel: ");
    Serial.println(rsp.data.cellInformation.ceLevel);
} else {
    Serial.println("Error: Failed to get signal quality");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.getCellInformation(&rsp)) {
    WalterModemCellInformation &cellInfo = rsp.data.cellInformation;

    ESP_LOGI("sim_and_network_docs_demo", "Cell Information:");
    ESP_LOGI("sim_and_network_docs_demo", "-> netName: %s", cellInfo.netName);
    ESP_LOGI("sim_and_network_docs_demo", "-> cc: %u", cellInfo.cc);
    ESP_LOGI("sim_and_network_docs_demo", "-> nc: %u", cellInfo.nc);
    ESP_LOGI("sim_and_network_docs_demo", "-> rsrp: %.2f", cellInfo.rsrp);
    ESP_LOGI("sim_and_network_docs_demo", "-> cinr: %.2f", cellInfo.cinr);
    ESP_LOGI("sim_and_network_docs_demo", "-> rsrq: %.2f", cellInfo.rsrq);
    ESP_LOGI("sim_and_network_docs_demo", "-> tac: %u", cellInfo.tac);
    ESP_LOGI("sim_and_network_docs_demo", "-> pci: %u", cellInfo.pci);
    ESP_LOGI("sim_and_network_docs_demo", "-> earfcn: %u", cellInfo.earfcn);
    ESP_LOGI("sim_and_network_docs_demo", "-> rssi: %.2f", cellInfo.rssi);
    ESP_LOGI("sim_and_network_docs_demo", "-> paging: %u", cellInfo.paging);
    ESP_LOGI("sim_and_network_docs_demo", "-> cid: %u", cellInfo.cid);
    ESP_LOGI("sim_and_network_docs_demo", "-> band: %u", cellInfo.band);
    ESP_LOGI("sim_and_network_docs_demo", "-> bw: %u", cellInfo.bw);
    ESP_LOGI("sim_and_network_docs_demo", "-> ceLevel: %u", cellInfo.ceLevel);
} else {
    ESP_LOGE("sim_and_network_docs_demo", "Failed to get signal quality");
}

// ...
```

<!-- tabs:end -->

---

## Enums

### `WalterModemNetworkSelMode`

The supported network selection modes.

> **WALTER_MODEM_NETWORK_SEL_MODE_AUTOMATIC** = `0`  
> Automatic network selection.  
> **WALTER_MODEM_NETWORK_SEL_MODE_MANUAL** = `1`  
> Manual network selection.  
> **WALTER_MODEM_NETWORK_SEL_MODE_UNREGISTER** = `2`  
> Unregister from network.  
> **WALTER_MODEM_NETWORK_SEL_MODE_MANUAL_AUTO_FALLBACK** = `4`  
> Manual selection with automatic fallback.  

### `WalterModemOperatorFormat`

The supported network operator formats.

> **WALTER_MODEM_OPERATOR_FORMAT_LONG_ALPHANUMERIC** = `0`  
> Long alphanumeric operator format.  
> **WALTER_MODEM_OPERATOR_FORMAT_SHORT_ALPHANUMERIC** = `1`  
> Short alphanumeric operator format.  
> **WALTER_MODEM_OPERATOR_FORMAT_NUMERIC** = `2`  
> Numeric operator format.  

### `WalterModemBand`

The different supported modem bands, usable as a bitmask in band selection configuration.

> **WALTER_MODEM_BAND_B1** = `0x00001`  
> Band 1.  
> **WALTER_MODEM_BAND_B2** = `0x00002`  
> Band 2.  
> **WALTER_MODEM_BAND_B3** = `0x00004`  
> Band 3.  
> **WALTER_MODEM_BAND_B4** = `0x00008`  
> Band 4.  
> **WALTER_MODEM_BAND_B5** = `0x00010`  
> Band 5.  
> **WALTER_MODEM_BAND_B8** = `0x00020`  
> Band 8.  
> **WALTER_MODEM_BAND_B12** = `0x00040`  
> Band 12.  
> **WALTER_MODEM_BAND_B13** = `0x00080`  
> Band 13.  
> **WALTER_MODEM_BAND_B14** = `0x00100`  
> Band 14.  
> **WALTER_MODEM_BAND_B17** = `0x00200`  
> Band 17.  
> **WALTER_MODEM_BAND_B18** = `0x00400`  
> Band 18.  
> **WALTER_MODEM_BAND_B19** = `0x00800`  
> Band 19.  
> **WALTER_MODEM_BAND_B20** = `0x01000`  
> Band 20.  
> **WALTER_MODEM_BAND_B25** = `0x02000`  
> Band 25.  
> **WALTER_MODEM_BAND_B26** = `0x04000`  
> Band 26.  
> **WALTER_MODEM_BAND_B28** = `0x08000`  
> Band 28.  
> **WALTER_MODEM_BAND_B66** = `0x10000`  
> Band 66.  
> **WALTER_MODEM_BAND_B71** = `0x20000`  
> Band 71.  
> **WALTER_MODEM_BAND_B85** = `0x40000`  
> Band 85.

### `WalterModemCEREGReportsType`

The CEREG unsolicited reporting methods.

> **WALTER_MODEM_CEREG_REPORTS_OFF** = `0`  
> Reporting disabled.  
> **WALTER_MODEM_CEREG_REPORTS_ENABLED** = `1`  
> Basic reporting enabled.  
> **WALTER_MODEM_CEREG_REPORTS_ENABLED_WITH_LOCATION** = `2`  
> Reporting includes location information.  
> **WALTER_MODEM_CEREG_REPORTS_ENABLED_WITH_LOCATION_EMM_CAUSE** = `3`  
> Reporting includes location and EMM cause.  
> **WALTER_MODEM_CEREG_REPORTS_ENABLED_UE_PSM_WITH_LOCATION** = `4`  
> Reporting includes UE PSM parameters and location.  
> **WALTER_MODEM_CEREG_REPORTS_ENABLED_UE_PSM_WITH_LOCATION_EMM_CAUSE** = `5`  
> Reporting includes UE PSM parameters, location, and EMM cause.

### `WalterModemOpState`

Modem operational modes.

> **WALTER_MODEM_OPSTATE_MINIMUM** = `0`  
> Minimal operational mode.  
> **WALTER_MODEM_OPSTATE_FULL** = `1`  
> Full operational mode.  
> **WALTER_MODEM_OPSTATE_NO_RF** = `4`  
> No RF (Radio Frequency) operation.  
> **WALTER_MODEM_OPSTATE_MANUFACTURING** = `5`  
> Manufacturing mode for testing and diagnostics.

### `WalterModemSIMState`

The possible states of the SIM card.

> **WALTER_MODEM_SIM_STATE_READY** = `0`  
> SIM card is ready for use.  
> **WALTER_MODEM_SIM_STATE_PIN_REQUIRED** = `1`  
> SIM PIN code is required.  
> **WALTER_MODEM_SIM_STATE_PUK_REQUIRED** = `2`  
> SIM PUK code is required.  
> **WALTER_MODEM_SIM_STATE_PHONE_TO_SIM_PIN_REQUIRED** = `3`  
> Phone-to-SIM PIN code is required.  
> **WALTER_MODEM_SIM_STATE_PHONE_TO_FIRST_SIM_PIN_REQUIRED** = `4`  
> Initial phone-to-first-SIM PIN is required.  
> **WALTER_MODEM_SIM_STATE_PHONE_TO_FIRST_SIM_PUK_REQUIRED** = `5`  
> Initial phone-to-first-SIM PUK is required.  
> **WALTER_MODEM_SIM_STATE_PIN2_REQUIRED** = `6`  
> PIN2 code is required.  
> **WALTER_MODEM_SIM_STATE_PUK2_REQUIRED** = `7`  
> PUK2 code is required.  
> **WALTER_MODEM_SIM_STATE_NETWORK_PIN_REQUIRED** = `8`  
> Network unlock PIN is required.  
> **WALTER_MODEM_SIM_STATE_NETWORK_PUK_REQUIRED** = `9`  
> Network unlock PUK is required.  
> **WALTER_MODEM_SIM_STATE_NETWORK_SUBSET_PIN_REQUIRED** = `10`  
> Network subset unlock PIN is required.  
> **WALTER_MODEM_SIM_STATE_NETWORK_SUBSET_PUK_REQUIRED** = `11`  
> Network subset unlock PUK is required.  
> **WALTER_MODEM_SIM_STATE_SERVICE_PROVIDER_PIN_REQUIRED** = `12`  
> Service provider unlock PIN is required.  
> **WALTER_MODEM_SIM_STATE_SERVICE_PROVIDER_PUK_REQUIRED** = `13`  
> Service provider unlock PUK is required.  
> **WALTER_MODEM_SIM_STATE_CORPORATE_SIM_REQUIRED** = `14`  
> Corporate SIM unlock PIN is required.  
> **WALTER_MODEM_SIM_STATE_CORPORATE_PUK_REQUIRED** = `15`  
> Corporate SIM unlock PUK is required.  

### `WalterModemRat`

Types of 3GPP access technologies supported by Walter.

> **WALTER_MODEM_RAT_LTEM** = `0`  
> LTE-M (Long-Term Evolution for Machines).  
> **WALTER_MODEM_RAT_NBIOT** = `1`  
> NB-IoT (Narrowband Internet of Things).  
> **WALTER_MODEM_RAT_AUTO** = `2`  
> Automatic selection between RATs.  
> **WALTER_MODEM_RAT_UNKNOWN** = `99`  
> RAT could not be determined.

### `WalterModemNetworkRegState`

The different network registration states that the modem can be in.

> **WALTER_MODEM_NETWORK_REG_NOT_SEARCHING** = `0`  
> Not searching for a network.  
> **WALTER_MODEM_NETWORK_REG_REGISTERED_HOME** = `1`  
> Registered on home network.  
> **WALTER_MODEM_NETWORK_REG_SEARCHING** = `2`  
> Actively searching for a network.  
> **WALTER_MODEM_NETWORK_REG_DENIED** = `3`  
> Registration denied by network.  
> **WALTER_MODEM_NETWORK_REG_UNKNOWN** = `4`  
> Registration state is unknown.  
> **WALTER_MODEM_NETWORK_REG_REGISTERED_ROAMING** = `5`  
> Registered on a roaming network.  
> **WALTER_MODEM_NETWORK_REG_REGISTERED_SMS_ONLY_HOME** = `6`  
> Registered for SMS only on home network.  
> **WALTER_MODEM_NETWORK_REG_REGISTERED_SMS_ONLY_ROAMING** = `7`  
> Registered for SMS only while roaming.  
> **WALTER_MODEM_NETWORK_REG_ATTACHED_EMERGENCY_ONLY** = `8`  
> Only emergency services are available.  
> **WALTER_MODEM_NETWORK_REG_REGISTERED_CSFB_NOT_PREFERRED_HOME** = `9`  
> Registered on home network, CSFB not preferred.  
> **WALTER_MODEM_NETWORK_REG_REGISTERED_CSFB_NOT_PREFERRED_ROAMING** = `10`  
> Registered on roaming network, CSFB not preferred.  
> **WALTER_MODEM_NETWORK_REG_REGISTERED_TEMP_CONN_LOSS** = `80`  
> Temporarily lost connection while registered.

### `WalterModemSQNMONIReportsType`

The SQNMONI cell information reporting scopes.

> **WALTER_MODEM_SQNMONI_REPORTS_SERVING_CELL** = `0`  
> Report serving cell only.  
> **WALTER_MODEM_SQNMONI_REPORTS_INTRA_FREQUENCY_CELLS** = `1`  
> Report intra-frequency neighboring cells.  
> **WALTER_MODEM_SQNMONI_REPORTS_INTER_FREQUENCY_CELLS** = `2`  
> Report inter-frequency neighboring cells.  
> **WALTER_MODEM_SQNMONI_REPORTS_ALL_CELLS** = `7`  
> Report all available cells.  
> **WALTER_MODEM_SQNMONI_REPORTS_SERVING_CELL_WITH_CINR** = `9`  
> Report serving cell including CINR value.

### `WalterModemRAI`

Indicates Release Assistance Information (RAI) for NB-IoT connections, signaling if further transmissions are expected.

> **WALTER_MODEM_RAI_NO_INFO** = `0`  
> No release assistance information provided.  
> **WALTER_MODEM_RAI_NO_FURTHER_RXTX_EXPECTED** = `1`  
> No further transmission or reception expected.  
> **WALTER_MODEM_RAI_ONLY_SINGLE_RXTX_EXPECTED** = `2`  
> Only a single transmission or reception is expected.
