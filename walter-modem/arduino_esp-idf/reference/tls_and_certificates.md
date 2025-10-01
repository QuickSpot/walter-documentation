## Methods Overview

- [tlsConfigProfile](#tlsconfigprofile)
- [tlsWriteCredential](#tlswritecredential)

## Enums Overview

- [WalterModemTlsVersion](#waltermodemtlsversion)
- [WalterModemTlsValidation](#waltermodemtlsvalidation)

---

## Methods

### `tlsConfigProfile`

Configure a TLS profile.

This function should be called once in an initializer sketch that prepares the modem
for its intended use on this Walter device.
It configures a set of TLS profiles within the modem, with optional client authentication certificates,
validation level (none, URL, CA, URL and CA), and TLS version.
Later HTTP, MQTT, CoAP, BlueCherry, and Socket sessions can use these preconfigured profile IDs.

#### Params

| Param                 | Description                                                                                           | Default                              |
| --------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------ |
| `profileId`           | Security profile ID (range 1-6).                                                                      |                                      |
| `tlsValid`            | TLS validation level: none, URL, CA, or URL and CA. ([WalterModemTlsVersion](#waltermodemtlsversion)) | **WALTER_MODEM_TLS_VALIDATION_NONE** |
| `tlsVersion`          | TLS version to use. ([WalterModemTlsValidation](#waltermodemtlsvalidation))                           | **WALTER_MODEM_TLS_VERSION_12**      |
| `caCertificateId`     | CA certificate index (0-19), or 0xff to specify none.                                                 | **0xff**                             |
| `clientCertificateId` | Client TLS certificate index (0-19), or 0xff to specify none.                                         | **0xff**                             |
| `clientPrivKeyId`     | Client TLS private key index (0-19), or 0xff to specify none.                                         | **0xff**                             |
| `rsp`                 | Optional modem response structure to save the result.                                                 | **NULL**                             |
| `cb`                  | Optional callback function, if set this function will not block.                                      | **NULL**                             |
| `args`                | Optional argument to pass to the callback.                                                            | **NULL**                             |

#### Returns

`bool`  
True on success, false otherwise.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

// ...

if (modem.tlsConfigProfile(1, WALTER_MODEM_TLS_VALIDATION_CA)) {
    Serial.println("Info: TLS profile configured");
} else {
    Serial.println("Error: Failed to configure TLS profile");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

// ...

if (modem.tlsConfigProfile(1, WALTER_MODEM_TLS_VALIDATION_CA)) {
    ESP_LOGI("tls_and_certs_docs_demo", "TLS profile configured");
} else {
    ESP_LOGE("tls_and_certs_docs_demo", "Failed to configure TLS profile");
}

// ...
```

<!-- tabs:end -->

---

### `tlsWriteCredential`

Upload key or certificate to modem NVRAM.

This function uploads a key or certificate to the modem NVRAM.

> [!NOTE]
> It is recommended to save credentials in index 10-19 to avoid overwriting
> preinstalled certificates and (if applicable) BlueCherry cloud platform credentials.

#### Params

| Param          | Description                                                            | Default |
| -------------- | ---------------------------------------------------------------------- | ------- |
| `isPrivateKey` | True if the credential is a private key, false if it is a certificate. |         |
| `slotIdx`      | Slot index within the modem NVRAM keystore.                            |         |
| `credential`   | NULL-terminated string containing the PEM key or certificate data.     |         |

#### Returns

`bool`  
True if succeeded, false if not.

#### Example

<!-- tabs:start -->

##### **Arduino**

```cpp
#include <WalterModem.h>

const char *cert = "-----BEGIN CERTIFICATE-----\r\n\
-----END CERTIFICATE-----\r\n";

// ...

if (modem.tlsWriteCredential(false, 10, cert)) {
    Serial.println("Info: Cert uploaded");
} else {
    Serial.println("Error: Failed to upload cert");
}

// ...
```

##### **ESP-IDF**

```cpp
#include <esp_log.h>
#include <WalterModem.h>

const char *cert = "-----BEGIN CERTIFICATE-----\r\n\
-----END CERTIFICATE-----\r\n";

// ...

if (modem.tlsWriteCredential(false, 9, cert)) {
    ESP_LOGI("tls_and_certs_docs_demo", "Cert uploaded");
} else {
    ESP_LOGE("tls_and_certs_docs_demo", "Failed to upload cert");
}

// ...
```

<!-- tabs:end -->

---

## Enums

### `WalterModemTlsVersion`

The supported TLS versions.

> **WALTER_MODEM_TLS_VERSION_10** = `0`  
> TLS version 1.0.  
> **WALTER_MODEM_TLS_VERSION_11** = `1`  
> TLS version 1.1.  
> **WALTER_MODEM_TLS_VERSION_12** = `2`  
> TLS version 1.2.  
> **WALTER_MODEM_TLS_VERSION_13** = `3`  
> TLS version 1.3.  
> **WALTER_MODEM_TLS_VERSION_RESET** = `255`  
> Reset to default TLS version.  

### `WalterModemTlsValidation`

The TLS validation policy.

> **WALTER_MODEM_TLS_VALIDATION_NONE** = `0`  
> No TLS validation performed.  
> **WALTER_MODEM_TLS_VALIDATION_CA** = `1`  
> Validate against Certificate Authority (CA).  
> **WALTER_MODEM_TLS_VALIDATION_URL** = `4`  
> Validate using URL.  
> **WALTER_MODEM_TLS_VALIDATION_URL_AND_CA** = `5`  
> Validate using both URL and CA.
