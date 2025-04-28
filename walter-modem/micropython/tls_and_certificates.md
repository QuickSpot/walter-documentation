## Methods Overview

- [tlsProvisionKeys](#tlsprovisionkeys)
- [tlsConfigProfile](#tlsconfigprofile)

## Enums Overview

- [WalterModemTlsVersion](#waltermodemtlsversion)
- [WalterModemTlsValidation](#waltermodemtlsvalidation)

---

## Methods

### `tlsProvisionKeys`

Uploads a key or certificate to the modem NVRAM.

> [!NOTE]
> This method has been refactored to `tlsWriteCredential` on Arduino & ESP-IDF.\
> `tlsProvisionKeys` is only available on micropython.

#### Example

```py
# fill in your own ca cert or import the text file instead,
# add client cert and client key if needed.
ca_cert = """-----BEGIN CERTIFICATE-----
(...)
-----END CERTIFICATE-----"""

# only using ca cert here, however, you can set cert & priv_key too if needed
if not await modem.tls_provision_keys(
    walter_certificate=None,
    walter_private_key=None,
    ca_certificate=ca_cert
):
    print("Could not upload certificate.")
    return False

print ('Certificates uploaded')
```

#### Params

| Param                | Description                                 | Default  |
| -------------------- | ------------------------------------------- | -------- |
| `walter_certificate` | The client certificate *(multiline string)* |          |
| `walter_private_key` | The private key *(multiline string)*        |          |
| `ca_certificate`     | The CA certificate *(multiline string)*     |          |
| `rsp`                | Reference to a modem response instance.     | **None** |

#### Returns

`bool`
True on success, False otherwise.

---

### `tlsConfigProfile`

Configures TLS profiles in the modem,
including optional client authentication certificates,
validation levels, and TLS version.

> [!NOTE]
> This should be done in an initializer sketch,
> allowing later HTTP, MQTT, CoAP, or socket sessions to use the
> preconfigured profile IDs

#### Example

```py
if not await modem.tls_config_profile(
    profile_id=1,
    tls_validation=WalterModemTlsValidation.NONE,
    tls_version=WalterModemTlsVersion.TLS_VERSION_13
):
    print('Failed to configure TLS profile')
```

#### Params

| Param                   | Description                                            | Default  |
| ----------------------- | ------------------------------------------------------ | -------- |
| `profile_id`            | Security profile id (1-6)                              |          |
| `tls_version`           | TLS version                                            |          |
| `tls_validation`        | TLS validation level: nothing, URL, CA+period or all   |          |
| `ca_certificate_id`     | CA certificate for certificate validation index (0-19) | **None** |
| `client_certificate_id` | Client TLS certificate index (0-19)                    | **None** |
| `client_private_key`    | Client TLS private key index (0-19)                    | **None** |
| `rsp`                   | Reference to a modem response instance.                | **None** |

#### Returns

`bool`
True on success, False otherwise.

---

## Enums

### `WalterModemTlsVersion`

The TLS version to use.

> **TLS_VERSION_10** = `0` \
> TLS 1.0, outdated and insecure. \
> **TLS_VERSION_11** = `1` \
> TLS 1.1, deprecated version. \
> **TLS_VERSION_12** = `2` \
> TLS 1.2, widely used and secure. \
> **TLS_VERSION_13** = `3` \
> TLS 1.3, latest and most secure version. \
> **TLS_VERSION_RESET** = `255` \
> Resets to default TLS version.

### `WalterModemTlsValidation`

The TLS validation policy.

> **NONE** = `0` \
> No TLS validation. \
> **CA** = `1` \
> Validates using a Certificate Authority. \
> **URL** = `4` \
> Validates the server URL. \
> **URL_AND_CA** = `5` \
> Validates both the URL and CA certificate.
