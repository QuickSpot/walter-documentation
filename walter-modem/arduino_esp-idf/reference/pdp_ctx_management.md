## Methods Overview

- [definePDPContext](#definepdpcontext)
- [setPDPAuthParams](#setpdpauthparams)
- [setPDPContextActive](#setpdpcontextactive)
- [setNetworkAttachmentState](#setnetworkattachmentstate)
- [getPDPAddress](#getpdpaddress)

## Enums Overview

- [WalterModemPDPContextState](#waltermodempdpcontextstate)
- [WalterModemPDPType](#waltermodempdptype)
- [WalterModemPDPHeaderCompression](#waltermodempdpheadercompression)
- [WalterModemPDPDataCompression](#waltermodempdpdatacompression)
- [WalterModemPDPIPv4AddrAllocMethod](#waltermodempdpipv4addrallocmethod)
- [WalterModemPDPRequestType](#waltermodempdprequesttype)
- [WalterModemPDPPCSCFDiscoveryMethod](#waltermodempdppcscfdiscoverymethod)
- [WalterModemPDPAuthProtocol](#waltermodempdpauthprotocol)

---

## Methods

### `definePDPContext`

Define a new packet data protocol (PDP) context.

This function will define a new packet data protocol.

#### Params

| Param                     | Description                                                                                                         | Default                                      |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| `ctxId`                   | The context id to store the definition in.                                                                          | **1**                                        |
| `apn`                     | The access point name.                                                                                              | **NULL**                                     |
| `rsp`                     | Optional modem response structure to save the result.                                                               | **NULL**                                     |
| `cb`                      | Optional callback function, if set this function will not block.                                                    | **NULL**                                     |
| `args`                    | Optional argument to pass to the callback.                                                                          | **NULL**                                     |
| `type`                    | The type of PDP context to create. ([WalterModemPDPType](#waltermodempdptype))                                      | **WALTER_MODEM_PDP_TYPE_IP**                 |
| `pdpAddress`              | Optional PDP address.                                                                                               | **NULL**                                     |
| `headerComp`              | The type of header compression to use. ([WalterModemPDPHeaderCompression](#waltermodempdpheadercompression))        | **WALTER_MODEM_PDP_HCOMP_OFF**               |
| `dataComp`                | The type of data compression to use. ([WalterModemPDPDataCompression](#waltermodempdpdatacompression))              | **WALTER_MODEM_PDP_DCOMP_OFF**               |
| `ipv4AllocMethod`         | The IPv4 allocation method. ([WalterModemPDPIPv4AddrAllocMethod](#waltermodempdpipv4addrallocmethod))               | **WALTER_MODEM_PDP_IPV4_ALLOC_NAS**          |
| `requestType`             | The type of PDP requests. ([WalterModemPDPRequestType](#waltermodempdprequesttype))                                 | **WALTER_MODEM_PDP_REQUEST_NEW_OR_HANDOVER** |
| `pcscfMethod`             | The method to use for P-CSCF discovery. ([WalterModemPDPPCSCFDiscoveryMethod](#waltermodempdppcscfdiscoverymethod)) | **WALTER_MODEM_PDP_PCSCF_AUTO**              |
| `forIMCN`                 | Set when this PDP ctx is used for IM CN signalling.                                                                 | **false**                                    |
| `useNSLPI`                | Set when NSLPI is used.                                                                                             | **false**                                    |
| `useSecurePCO`            | Set to use secure protocol config options.                                                                          | **false**                                    |
| `useNASIPv4MTUDiscovery`  | Set to use NAS for IPv4 MTU discovery.                                                                              | **false**                                    |
| `useLocalAddrInd`         | Set when local IPs are supported in the TFT.                                                                        | **false**                                    |
| `useNASNonIPMTUDiscovery` | Set for NAS based no-IP MTU discovery.                                                                              | **false**                                    |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

CONFIG(CELLULAR_APN, const char *, "")

// ...

if (modem.definePDPContext(1, CELLULAR_APN)) {
    Serial.println("Info: PDP CTX created");
} else {
    Serial.println("Error: Failed to create PDP CTX");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

CONFIG(CELLULAR_APN, const char *, "")

// ...

if (modem.definePDPContext(1, CELLULAR_APN)) {
    ESP_LOGI("pdp_ctx_mgnt_docs_demo", "PDP CTX Created");
} else {
    ESP_LOGE("pdp_ctx_mgnt_docs_demo", "Failed to create PDP CTX");
}

// ...
```

<!-- tabs:end -->

---

### `setPDPAuthParams`

Authenticate a PDP context.

When a PDP context's APN requires authentication,
this function will prepare the PDP context for this authentication.

> [!NOTE]
> If the authentication method is set to 'NONE', this function performs no operation.

#### Params

| Param       | Description                                                                                                         | Default                              |
| ----------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| `authProto` | The authentication protocol to use for the PDP context. ([WalterModemPDPAuthProtocol](#waltermodempdpauthprotocol)) | **WALTER_MODEM_PDP_AUTH_PROTO_NONE** |
| `authUser`  | Authentication username.                                                                                            | **NULL**                             |
| `authPass`  | Authentication password.                                                                                            | **NULL**                             |
| `pdpCtxId`  | The PDP context ID to configure, or -1 to reuse the last one.                                                       | **-1**                               |
| `rsp`       | Optional modem response structure to save the result.                                                               | **NULL**                             |
| `cb`        | Optional callback function, if set this function will not block.                                                    | **NULL**                             |
| `args`      | Optional argument to pass to the callback.                                                                          | **NULL**                             |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.setPDPAuthParams(WALTER_MODEM_PDP_AUTH_PROTO_PAP, "user", "pass")) {
    Serial.println("Info: PDP CTX auth params set");
} else {
    Serial.println("Error: Failed to set PDP CTX auth params");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (modem.setPDPAuthParams(WALTER_MODEM_PDP_AUTH_PROTO_PAP, "user", "pass")) {
    ESP_LOGI("pdp_ctx_mgnt_docs_demo", "PDP CTX auth params set");
} else {
    ESP_LOGE("pdp_ctx_mgnt_docs_demo", "Failed to set PDP CTX auth params");
}

// ...
```

<!-- tabs:end -->

---

### `setPDPContextActive`

Activate or deactivate a PDP context.

This function activates or deactivates a given PDP context.

> [!TIP]
> A PDP context must be activated before it can be attached to.

#### Params

| Param      | Description                                                            | Default  |
| ---------- | ---------------------------------------------------------------------- | -------- |
| `active`   | True to activate the PDP context, false to deactivate.                 | **true** |
| `pdpCtxId` | The PDP context ID to activate/deactivate or -1 to reuse the last one. | **-1**   |
| `rsp`      | Optional modem response structure to save the result.                  | **NULL** |
| `cb`       | Optional callback function, if set this function will not block.       | **NULL** |
| `args`     | Optional argument to pass to the callback.                             | **NULL** |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.setPDPContextActive(true)) {
    Serial.println("Info: PDP CTX activated");
} else {
    Serial.println("Error: Failed to active PDP CTX");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (modem.setPDPContextActive(true)) {
    ESP_LOGI("pdp_ctx_mgnt_docs_demo", "PDP CTX actived");
} else {
    ESP_LOGE("pdp_ctx_mgnt_docs_demo", "Failed to activate PDP CTX");
}

// ...
```

<!-- tabs:end -->

---

### `setNetworkAttachmentState`

Attach the defined PDP contexts.

This function will attach to or detach from a packet domain service.

#### Params

| Param    | Description                                                      | Default  |
| -------- | ---------------------------------------------------------------- | -------- |
| `attach` | True to attach, false to detach.                                 | **true** |
| `rsp`    | Optional modem response structure to save the result.            | **NULL** |
| `cb`     | Optional callback function, if set this function will not block. | **NULL** |
| `args`   | Optional argument to pass to the callback.                       | **NULL** |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.setNetworkAttachmentState(true)) {
    Serial.println("Info: Attached");
} else {
    Serial.println("Error: Failed to attach");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (modem.setNetworkAttachmentState(true)) {
    ESP_LOGI("pdp_ctx_mgnt_docs_demo", "Attached");
} else {
    ESP_LOGE("pdp_ctx_mgnt_docs_demo", "Failed to attach");
}

// ...
```

<!-- tabs:end -->

---

### `getPDPAddress`

Get a list of PDP addresses of a PDP context.

This function will retrieve the list of PDP addresses for the requested PDP context ID.

#### Params

| Param      | Description                                                      | Default  |
| ---------- | ---------------------------------------------------------------- | -------- |
| `rsp`      | Optional modem response structure to save the result.            | **NULL** |
| `cb`       | Optional callback function, if set this function will not block. | **NULL** |
| `args`     | Optional argument to pass to the callback.                       | **NULL** |
| `pdpCtxId` | The PDP context ID to query or -1 to reuse the last one.         | **-1**   |

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

if (modem.getPDPAddress(&rsp)) {
    Serial.print("PDP addresses for CTX ID: ");
    Serial.println(rsp.data.pdpAddressList.pdpCtxId);
    
    Serial.print("Primary PDP Address: ");
    if (rsp.data.pdpAddressList.pdpAddress && rsp.data.pdpAddressList.pdpAddress[0] != '\0') {
        Serial.println(rsp.data.pdpAddressList.pdpAddress);
    } else {
        Serial.println("None");
    }

    Serial.print("Secondary PDP Address: ");
    if (rsp.data.pdpAddressList.pdpAddress2 && rsp.data.pdpAddressList.pdpAddress2[0] != '\0') {
        Serial.println(rsp.data.pdpAddressList.pdpAddress2);
    } else {
        Serial.println("None");
    }
} else {
    Serial.println("Error: Failed to get PDP address list");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

WalterModemRsp rsp = {};

// ...

if (modem.getPDPAddress(&rsp)) {
    ESP_LOGI("pdp_ctx_mgnt_docs_demo", , "PDP addresses for CTX ID: %d", rsp.data.pdpAddressList.pdpCtxId);
    
    if (rsp.data.pdpAddressList.pdpAddress && rsp.data.pdpAddressList.pdpAddress[0] != '\0') {
        ESP_LOGI("pdp_ctx_mgnt_docs_demo", , "Primary PDP Address: %s", rsp.data.pdpAddressList.pdpAddress);
    } else {
        ESP_LOGI("pdp_ctx_mgnt_docs_demo", , "Primary PDP Address: None");
    }
    
    if (rsp.data.pdpAddressList.pdpAddress2 && rsp.data.pdpAddressList.pdpAddress2[0] != '\0') {
        ESP_LOGI("pdp_ctx_mgnt_docs_demo", , "Secondary PDP Address: %s", rsp.data.pdpAddressList.pdpAddress2);
    } else {
        ESP_LOGI("pdp_ctx_mgnt_docs_demo", , "Secondary PDP Address: None");
    }
} else {
    ESP_LOGE("pdp_ctx_mgnt_docs_demo", , "Failed to get PDP address list");
}

// ...
```

<!-- tabs:end -->

---

## Enums

### `WalterModemPDPContextState`

The different states a PDP context can be in.

> **WALTER_MODEM_PDP_CONTEXT_STATE_INACTIVE** = `0`  
> PDP context is inactive.  
> **WALTER_MODEM_PDP_CONTEXT_STATE_ACTIVE** = `1`  
> PDP context is active.  
> **WALTER_MODEM_PDP_CONTEXT_STATE_NOT_ATTACHED** = `2`  
> PDP context is not attached.  
> **WALTER_MODEM_PDP_CONTEXT_STATE_ATTACHED** = `3`  
> PDP context is attached.  

### `WalterModemPDPType`

The supported packet data protocol types.

> **WALTER_MODEM_PDP_TYPE_X25** = `0`  
> X.25 packet data protocol.  
> **WALTER_MODEM_PDP_TYPE_IP** = `1`  
> IPv4 packet data protocol.  
> **WALTER_MODEM_PDP_TYPE_IPV6** = `2`  
> IPv6 packet data protocol.  
> **WALTER_MODEM_PDP_TYPE_IPV4V6** = `3`  
> Dual stack IPv4/IPv6 packet data protocol.  
> **WALTER_MODEM_PDP_TYPE_OSPIH** = `4`  
> OSPIH packet data protocol.  
> **WALTER_MODEM_PDP_TYPE_PPP** = `5`  
> Point-to-Point Protocol (PPP).  
> **WALTER_MODEM_PDP_TYPE_NON_IP** = `6`  
> Non-IP packet data protocol.  

### `WalterModemPDPHeaderCompression`

The supported packet data protocol header compression mechanisms.

> **WALTER_MODEM_PDP_HCOMP_OFF** = `0`  
> Header compression off.  
> **WALTER_MODEM_PDP_HCOMP_ON** = `1`  
> Header compression on.  
> **WALTER_MODEM_PDP_HCOMP_RFC1144** = `2`  
> RFC 1144 header compression.  
> **WALTER_MODEM_PDP_HCOMP_RFC2507** = `3`  
> RFC 2507 header compression.  
> **WALTER_MODEM_PDP_HCOMP_RFC3095** = `4`  
> RFC 3095 header compression.  
> **WALTER_MODEM_PDP_HCOMP_UNSPEC** = `99`  
> Unspecified header compression.  

### `WalterModemPDPDataCompression`

The supported packet data protocol data compression mechanisms.

> **WALTER_MODEM_PDP_DCOMP_OFF** = `0`  
> Data compression off.  
> **WALTER_MODEM_PDP_DCOMP_ON** = `1`  
> Data compression on.  
> **WALTER_MODEM_PDP_DCOMP_V42BIS** = `2`  
> V.42bis data compression.  
> **WALTER_MODEM_PDP_DCOMP_V44** = `3`  
> V.44 data compression.  
> **WALTER_MODEM_PDP_DCOMP_UNSPEC** = `99`  
> Unspecified data compression.  

### `WalterModemPDPIPv4AddrAllocMethod`

The supported packet data protocol IPv4 address allocation methods.

> **WALTER_MODEM_PDP_IPV4_ALLOC_NAS** = `0`  
> NAS allocated IPv4 address.  
> **WALTER_MODEM_PDP_IPV4_ALLOC_DHCP** = `1`  
> DHCP allocated IPv4 address.  

### `WalterModemPDPRequestType`

The supported packet data protocol request types.

> **WALTER_MODEM_PDP_REQUEST_NEW_OR_HANDOVER** = `0`  
> New request or handover.  
> **WALTER_MODEM_PDP_REQUEST_EMERGENCY** = `1`  
> Emergency request.  
> **WALTER_MODEM_PDP_REQUEST_NEW** = `2`  
> New request only.  
> **WALTER_MODEM_PDP_REQUEST_HANDOVER** = `3`  
> Handover request only.  
> **WALTER_MODEM_PDP_REQUEST_EMERGENCY_HANDOVER** = `4`  
> Emergency handover request.  

### `WalterModemPDPPCSCFDiscoveryMethod`

The supported types of P-CSCF discovery in a packet data context.

> **WALTER_MODEM_PDP_PCSCF_AUTO** = `0`  
> Automatic P-CSCF discovery.  
> **WALTER_MDOEM_PDP_PCSCF_NAS** = `1`  
> NAS-based P-CSCF discovery.  

### `WalterModemPDPAuthProtocol`

The authentication protocol used within the PDP context.

> **WALTER_MODEM_PDP_AUTH_PROTO_NONE** = `0`  
> No authentication protocol.  
> **WALTER_MODEM_PDP_AUTH_PROTO_PAP** = `1`  
> Password Authentication Protocol (PAP).  
> **WALTER_MODEM_PDP_AUTH_PROTO_CHAP** = `2`  
> Challenge-Handshake Authentication Protocol (CHAP).
