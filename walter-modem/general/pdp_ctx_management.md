## Methods Overview

- [createPDPContext](#createpdpcontext)
- [authenticatePDPContext](#authenticatepdpcontext)
- [setPDPContextActive](#setpdpcontextactive)
- [attachPDPContext](#attachpdpcontext)
- [getPDPAddress](#getpdpaddress)

## Enums Overview

---

## Methods

### `createPDPContext`

#### Example

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

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

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

| Param                        | Description                                         | Default                                       |
| ---------------------------- | --------------------------------------------------- | --------------------------------------------- |
| `apn`                        | The access point name.                              | **""**                                        |
| `auth_proto`                 | The used authentication protocol.                   | **WalterModemPDPAuthProtocol.NONE**           |
| `auth_user`                  | Optional user to use for authentication.            | **None**                                      |
| `auth_pass`                  | Optional password to use for authentication.        | **None**                                      |
| `type`                       | The type of PDP context to create.                  | **WalterModemPDPType.IP**                     |
| `pdp_address`                | Optional PDP address.                               | **None**                                      |
| `header_comp`                | The type of header compression to use.              | **WalterModemPDPHeaderCompression.OFF**       |
| `data_comp`                  | The type of data compression to use.                | **WalterModemPDPDataCompression.OFF**         |
| `ipv4_alloc_method`          | The IPv4 alloction method.                          | **WalterModemPDPIPv4AddrAllocMethod.DHCP**    |
| `request_type`               | The type of PDP requests.                           | **WalterModemPDPRequestType.NEW_OR_HANDOVER** |
| `pcscf_method`               | The method to use for P-CSCF discovery.             | **WalterModemPDPPCSCFDiscoveryMethod.AUTO**   |
| `for_IMCN`                   | Set when this PDP ctx is used for IM CN signalling. | **False**                                     |
| `use_NSLPI`                  | Set when NSLPI is used.                             | **False**                                     |
| `use_secure_PCO`             | Set to use secure protocol config options.          | **False**                                     |
| `use_NAS_ipv4_MTU_discovery` | Set to use NAS for IPv4 MTU discovery.              | **False**                                     |
| `use_local_addr_ind`         | Set when local IPs are supported in the TFT.        | **False**                                     |
| `use_NAS_on_IPMTU_discovery` | Set for NAS based no-IP MTU discovery.              | **False**                                     |
| `rsp`                        | Reference to a modem response instance.             | **None**                                      |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

### `authenticatePDPContext`

Authenticates a PDP context if its APN requires authentication.

> [!NOTE]
> Has no effect if **NONE** is selected as the authentication method.

#### Example

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

```py
if await modem.authenticate_PDP_context():
    print('PDP context authenticated')
else:
    print('Failed to authenticate PDP context')
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

| param        | description                                          | default  |
| ------------ | ---------------------------------------------------- | -------- |
| `context_id` | The PDP context id or **-1 to re-use the last one.** | **-1**   |
| `rsp`        | Reference to a modem response instance.              | **None** |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

### `setPDPContextActive`

Activates or deactivates a given PDP context.

#### Example

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

```py
if not await modem.set_PDP_context_active(active=False):
    print('Failed to deactivate last used pdp context')
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

| Param        | Description                                            | Default  |
| ------------ | ------------------------------------------------------ | -------- |
| `active`     | True to activate the PDP context, False to deactivate. | **True** |
| `context_id` | The PDP context id or **-1 to re-use the last one.**   | **-1**   |
| `rsp`        | Reference to a modem response instance.                | **None** |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

### `attachPDPContext`

Attaches to or detaches from the currently active PDP context
for packet domain service.

#### Example

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

```py
if not await modem.attach_PDP_context(attach=True):
    print('Failed to attach PDP context')
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

| Param    | Description                             | Default  |
| -------- | --------------------------------------- | -------- |
| `attach` | True to attach, False to detach.        | **True** |
| `rsp`    | Reference to a modem response instance. | **None** |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---

### `getPDPAddress`

Retrieves the list of PDP addresses for the specified PDP context ID.

#### Example

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

```py
PDP_CONTEXT_ID = 1

if not await modem.get_PDP_address(context_id=PDP_CONTEXT_ID):
    print('Failed to get PDP addresses')
```

<!-- tabs:end -->

#### Params

<!-- tabs:start -->

##### **Arduino**

##### **ESP-IDF**

##### **Micropython**

| Param        | Description                                          | Default  |
| ------------ | ---------------------------------------------------- | -------- |
| `context_id` | The PDP context id or **-1 to re-use the last one.** | **-1**   |
| `rsp`        | Reference to a modem response instance               | **None** |

<!-- tabs:end -->

#### Returns

`bool`
True on success, False otherwise.

---
