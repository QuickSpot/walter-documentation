## Methods Overview

- [createPDPContext](#createpdpcontext)
- [authenticatePDPContext](#authenticatepdpcontext)
- [setPDPContextActive](#setpdpcontextactive)
- [attachPDPContext](#attachpdpcontext)
- [getPDPAddress](#getpdpaddress)

## Enums Overview

- [WalterModemPDPAuthProtocol](#waltermodempdpauthprotocol)
- [WalterModemPDPType](#waltermodempdptype)
- [WalterModemPDPHeaderCompression](#waltermodempdpheadercompression)
- [WalterModemPDPDataCompression](#waltermodempdpdatacompression)
- [WalterModemPDPIPv4AddrAllocMethod](#waltermodempdpipv4addrallocmethod)
- [WalterModemPDPRequestType](#waltermodempdprequesttype)
- [WalterModemPDPPCSCFDiscoveryMethod](#waltermodempdppcscfdiscoverymethod)
- [WalterModemPDPContextState](#waltermodempdpcontextstate)

---

## Methods

### `createPDPContext`

#### Example

```py
CELL_APN = ''
APN_USERNAME = None
APN_PASSWORD = None

modem_rsp = ModemRsp()

if not await modem.create_PDP_context(
    apn=CELL_APN,
    auth_user=APN_USERNAME,
    auth_pass=APN_PASSWORD,
    rsp=modem_rsp
):
    print('Failed to create PDP Context')
print('Successfully created PDP Context')
```

#### Params

| Param                        | Description                                                                    | Default                                       |
| ---------------------------- | ------------------------------------------------------------------------------ | --------------------------------------------- |
| `apn`                        | The access point name.                                                         | **""**                                        |
| `auth_proto`                 | The used [authentication protocol](#waltermodempdpauthprotocol).               | **WalterModemPDPAuthProtocol.NONE**           |
| `auth_user`                  | Optional user to use for authentication.                                       | **None**                                      |
| `auth_pass`                  | Optional password to use for authentication.                                   | **None**                                      |
| `type`                       | The [type of PDP context](#waltermodempdptype) to create.                      | **WalterModemPDPType.IP**                     |
| `pdp_address`                | Optional PDP address.                                                          | **None**                                      |
| `header_comp`                | The [type of header compression](#waltermodempdpheadercompression) to use.     | **WalterModemPDPHeaderCompression.OFF**       |
| `data_comp`                  | The [type of data compression](#waltermodempdpdatacompression) to use.         | **WalterModemPDPDataCompression.OFF**         |
| `ipv4_alloc_method`          | The [IPv4 alloction method](#waltermodempdpipv4addrallocmethod).               | **WalterModemPDPIPv4AddrAllocMethod.DHCP**    |
| `request_type`               | The [type of PDP requests](#waltermodempdprequesttype).                        | **WalterModemPDPRequestType.NEW_OR_HANDOVER** |
| `pcscf_method`               | The [method to use for P-CSCF discovery](#waltermodempdppcscfdiscoverymethod). | **WalterModemPDPPCSCFDiscoveryMethod.AUTO**   |
| `for_IMCN`                   | Set when this PDP ctx is used for IM CN signalling.                            | **False**                                     |
| `use_NSLPI`                  | Set when NSLPI is used.                                                        | **False**                                     |
| `use_secure_PCO`             | Set to use secure protocol config options.                                     | **False**                                     |
| `use_NAS_ipv4_MTU_discovery` | Set to use NAS for IPv4 MTU discovery.                                         | **False**                                     |
| `use_local_addr_ind`         | Set when local IPs are supported in the TFT.                                   | **False**                                     |
| `use_NAS_on_IPMTU_discovery` | Set for NAS based no-IP MTU discovery.                                         | **False**                                     |
| `rsp`                        | Reference to a modem response instance.                                        | **None**                                      |

#### Returns

`bool`
True on success, False otherwise.

---

### `authenticatePDPContext`

Authenticates a PDP context if its APN requires authentication.

> [!NOTE]
> Has no effect if **NONE** is selected as the authentication method.

#### Example

```py
if await modem.authenticate_PDP_context():
    print('PDP context authenticated')
else:
    print('Failed to authenticate PDP context')
```

#### Params

| param        | description                                          | default  |
| ------------ | ---------------------------------------------------- | -------- |
| `context_id` | The PDP context id or **-1 to re-use the last one.** | **-1**   |
| `rsp`        | Reference to a modem response instance.              | **None** |

#### Returns

`bool`
True on success, False otherwise.

---

### `setPDPContextActive`

Activates or deactivates a given PDP context.

#### Example

```py
if not await modem.set_PDP_context_active(active=False):
    print('Failed to deactivate last used pdp context')
```

#### Params

| Param        | Description                                            | Default  |
| ------------ | ------------------------------------------------------ | -------- |
| `active`     | True to activate the PDP context, False to deactivate. | **True** |
| `context_id` | The PDP context id or **-1 to re-use the last one.**   | **-1**   |
| `rsp`        | Reference to a modem response instance.                | **None** |

#### Returns

`bool`
True on success, False otherwise.

---

### `attachPDPContext`

Attaches to or detaches from the currently active PDP context
for packet domain service.

#### Example

```py
if not await modem.attach_PDP_context(attach=True):
    print('Failed to attach PDP context')
```

#### Params

| Param    | Description                             | Default  |
| -------- | --------------------------------------- | -------- |
| `attach` | True to attach, False to detach.        | **True** |
| `rsp`    | Reference to a modem response instance. | **None** |

#### Returns

`bool`
True on success, False otherwise.

---

### `getPDPAddress`

Retrieves the list of PDP addresses for the specified PDP context ID.

#### Example

```py
PDP_CONTEXT_ID = 1

if not await modem.get_PDP_address(context_id=PDP_CONTEXT_ID):
    print('Failed to get PDP addresses')
```

#### Params

| Param        | Description                                          | Default  |
| ------------ | ---------------------------------------------------- | -------- |
| `context_id` | The PDP context id or **-1 to re-use the last one.** | **-1**   |
| `rsp`        | Reference to a modem response instance               | **None** |

#### Returns

`bool`
True on success, False otherwise.

---

## Enums

### `WalterModemPDPAuthProtocol`

PDP context authentication protocols.

> **NONE** = `0` \
> No authentication required. \
> **PAP** = `1` \
> Password Authentication Protocol,
> a simple authentication method that transmits credentials in plaintext. \
> **CHAP** = `2` \
> Uses challenge-response for safer authentication.

### `WalterModemPDPType`

Supported packet data protocol types.

> **X25** = `0` \
> Packet-switched data protocol used in legacy networks. \
> **IP** = `1` \
> Standard IPv4 protocol for internet communication. \
> **IPV6** = `2` \
> Next-generation IP with improved addressing. \
> **IPV4V6** = `3` \
> Supports both IPv4 and IPv6. \
> **OSPIH** = `4` \
> Obsolete packet-switched protocol. \
> **PPP** = `5` \
> Point-to-Point Protocol for direct connections. \
> **NON_IP** = `6` \
> For non-IP data transmission.

### `WalterModemPDPHeaderCompression`

Supported packet data protocol header compression mechanisms.

> **OFF** = `0` \
> No header compression. \
> **ON** = `1` \
> Header compression enabled. \
> **RFC1144** = `2` \
> Van Jacobson TCP/IP header compression. \
> **RFC2507** = `3` \
> IP header compression for low-bandwidth links. \
> **RFC3095** = `4` \
> ROHC (Robust Header Compression) for IP, UDP, and RTP. \
> **UNSPEC** = `99` \
> Unspecified compression method.

### `WalterModemPDPDataCompression`

Supported packet data protocol data compression mechanisms.

> **OFF** = `0` \
> No data compression. \
> **ON** = `1` \
> Data compression enabled. \
> **V42BIS** = `2` \
> ITU-T V.42bis data compression. \
> **V44** = `3` \
> ITU-T V.44 improved data compression. \
> **UNSPEC** = `99` \
> Unspecified compression method.  

### `WalterModemPDPIPv4AddrAllocMethod`

Supported packet data protocol IPv4 address allocation methods.

> **NAS** = `0` \
> Address allocation by the Network Access Server. \
> **DHCP** = `1` \
> Dynamic Host Configuration Protocol for address allocation.  

### `WalterModemPDPRequestType`

Supported packet data protocol request types.

> **NEW_OR_HANDOVER** = `0` \
> Request for a new connection or handover. \
> **EMERGENCY** = `1` \
> Emergency connection request. \
> **NEW** = `2` \
> Request for a new connection. \
> **HANDOVER** = `3` \
> Request to handover an existing connection. \
> **EMERGENCY_HANDOVER** = `4` \
> Emergency handover request.  

### `WalterModemPDPPCSCFDiscoveryMethod`

Supported types of P-CSCF discovery in a packet data context.

> **AUTO** = `0` \
> Automatic P-CSCF discovery. \
> **NAS** = `1` \
> P-CSCF discovery by the Network Access Server.  

### `WalterModemPDPContextState`

PDP context states.

> **FREE** = `0` \
> Free and available. \
> **RESERVED** = `1` \
> Reserved but not yet active. \
> **INACTIVE** = `2` \
> Is not in use. \
> **ACTIVE** = `3` \
> Is active and in use. \
> **ATTACHED** = `4` \
> Is attached.
