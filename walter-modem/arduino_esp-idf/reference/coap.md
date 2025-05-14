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

### `coapClose`

Close a CoAP context.

This function will close a CoAP context previously opened with coapCreateContext.

> [!TIP]
> To change parameters such as the server name, you must first close the context using this call.

### `coapGetContextStatus`

Get the connection status of a CoAP context.

### `coapSetHeader`

Set a CoAP header.

> [!NOTE]
> This is not necessary, if you do not set the header.
> The message id and the token will be set to random values.

### `coapSetOptions`

Set the options for the next CoAP message.

### `coapSendData`

Send a datagram

> [!NOTE]
> Preffered options/header need to be set beforehand using [coapSetOptions](#coapsetoptions) or [coapSetHeader](#coapsetheader)

### `coapDidRing`

Fetch incoming CoAP messages, if any.

## Enums

### `WalterModemCoapOptCode`

The possible option codes for the CoAP message.

### `WalterModemCoapOptValue`

The possible option values for the CoAP message.

### `WalterModemCoapOptAction`

The possible option actions for the CoAP message.

### `WalterModemCoapSendType`

The possible CoAP send types.

### `WalterModemCoapSendMethodRsp`

The possible CoAP send methods.
