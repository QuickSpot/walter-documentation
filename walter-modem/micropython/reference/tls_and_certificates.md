## Methods Overview

- [tls_config_profile](#tlsconfigprofile)
- [tls_write_credential](#tls_write_credential)

## Enums Overview

- [WalterModemTlsVersion](#waltermodemtlsversion)
- [WalterModemTlsValidation](#waltermodemtlsvalidation)

---

## Methods

### `tls_config_profile`

Configures TLS profiles in the modem,
including optional client authentication certificates,
validation levels, and TLS version.

> [!NOTE]
> This should be done in an initialiser sketch,
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

`bool` True on success, False otherwise.

---

### `tls_write_credential`

Upload a key or certificate to the modem NVRAM.

> [!NOTE]
> It is recommended to save credentials in index 10-19 to avoid overwriting 
> preinstalled certificates and (if applicable) BlueCherry cloud platform credentials.

### Example

```py
await modem.tls_write_credential(
    is_private_key=False,
    slot_idx=SLOT_IDX,
    credential=CERT
)
```

### Params

| Param            | Description                                              | Default |
| ---------------- | -------------------------------------------------------- | ------- |
| `is_private_key` | True if it's a private key, False if it's a certificate. |         |
| `slot_idx`       | Slot index within the modem NVRAM keystore.              |         |
| `credential`     | NULL-terminated string containing the PEM key/cert data. |         |
| `rsp`            | Reference to a modem response instance.                  |         |

### Returns

`bool` True on success, False otherwise

---

### `tls_provision_keys`

> [!WARNING]
> **DEPRECATED:** This method will be removed in the near future.\

It is still present for backwards compatibility.
Use [`tls_write_credential`](#tls_write_credential) instead.

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
