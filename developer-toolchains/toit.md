## Prerequisites

We assume that you have set up your development environment as described in
[the IDE tutorial](https://docs.toit.io/tutorials/setup/ide)

We also assume that you have flashed your device with Jaguar and that you are
familiar with running Toit programs on it. If not, have a look at the
[Hello world](https://docs.toit.io/tutorials/setup/firstprogram) tutorial.

Note that the Walter device is an ESP32-S3 board, which requires the 
`--chip=esp32s3` flag when flashing.

In later sections we will refer to containers and services, but these are not
strictly necessary.

We will use HTTP to fetch data from the internet.

## Packages

Cellular functionality is not part of the core libraries and must be imported as
a package. See the [packages](https://docs.toit.io/tutorials/setup/packages)
tutorial for details.

As of writing, all drivers for cellular modems are in the
[cellular](https://pkg.toit.io/package/github.com%2Ftoitware%2Fcellular@v2) package.

To install it, run the following command:

```toit
jag pkg install github.com/toitware/cellular@v2
```

We will use the
[http](https://pkg.toit.io/package/github.com%2Ftoitlang%2Fpkg-http@v2) and the 
[certificate-roots](https://pkg.toit.io/package/github.com%2Ftoitware%2Ftoit-cert-roots@v1)
packages to fetch data from the internet.

```toit
jag pkg install github.com/toitlang/pkg-http@v2
jag pkg install github.com/toitware/toit-cert-roots@v1
```

## Code

Start a new Toit program `walter.toit` and watch it with Jaguar. If necessary,
uncomment the `CONFIG-APN` line and set the correct APN for your provider.

```toit
import cellular.modules.sequans.monarch
import http
import encoding.json
import net
import net.cellular
import certificate-roots
​
RX ::= 14
TX ::= 48
RTS ::= 21
CTS ::= 47
RESET ::= 45
POWER ::= 46
BAUD ::= 115200
​
main:
  // Start the monarch driver/provider.
  task --background::
    monarch.main
​
  // Establish the connection to the network.
  network := cellular.open --name="gm02sp" {
    cellular.CONFIG-UART-RX: RX,
    cellular.CONFIG-UART-TX: TX,
    cellular.CONFIG-UART-CTS: CTS,
    cellular.CONFIG-UART-RTS: RTS,
    cellular.CONFIG-RESET: [RESET, cellular.CONFIG-ACTIVE-LOW],
    cellular.CONFIG-POWER: POWER,
    cellular.CONFIG-UART-BAUD-RATE: BAUD,
    // If your provider requires an APN, you can set it here.
    // cellular.CONFIG-APN: "<your-apn>",
  }
​
  try:
    do-network-things network
  finally:
    network.close
```

Even though the modem isn't a "Monarch", but a "GM02SP", we can use the monarch
driver. Both are manufactured by Sequans, and use similar AT commands.
Eventually, there might be a more specialized driver for the GM02SP.

The `monarch.main` function installs the driver as a provider so that other code
can use it through a service. We happen to use it from the same process, but
that's not a requirement. In fact, we will see later how the provider can be
started in a different container, so that different programs can have access to
the internet at the same time.

Once the provider is running in the background, we simply use the 
`cellular.open` function to establish a connection to the network. It will
return a `net.Client` object that we can pass to code that needs to use the
network.

For example, the `do-network-things` function could look as follows:

```toit
do-network-things network/net.Client:
  certificate-roots.install-common-trusted-roots
  client := http.Client.tls network
  request := client.get --uri="https://official-joke-api.appspot.com/random_joke"
  decoded := json.decode-stream request.body
  print decoded["setup"]
  print decoded["punchline"]
```

## Container

In our first iteration the cellular provider was started in the same container
as the rest of the code. This is not ideal, as the cellular connection is then
not available to other containers.

We can fix this, by installing the cellular provider in its own container.

Create a new file `cellular.toit` with the following content. If necessary,
uncomment the `CONFIG-APN` line and set the correct APN for your provider.

```toit
import net.cellular
import cellular.modules.sequans.monarch
​
RX ::= 14
TX ::= 48
RTS ::= 21
CTS ::= 47
RESET ::= 45
POWER ::= 46
BAUD ::= 115200
​
class WalterCellularProvider extends monarch.MonarchService:
  connect client/int config/Map? -> List:
    if not config or config.is-empty:
      config = {
        cellular.CONFIG-UART-RX: RX,
        cellular.CONFIG-UART-TX: TX,
        cellular.CONFIG-UART-CTS: CTS,
        cellular.CONFIG-UART-RTS: RTS,
        cellular.CONFIG-RESET: [RESET, cellular.CONFIG-ACTIVE-LOW],
        cellular.CONFIG-POWER: POWER,
        cellular.CONFIG-UART-BAUD-RATE: BAUD,
        // If your provider requires an APN, you can set it here.
        // cellular.CONFIG-APN: "<your-apn>",
      }
    return super client config
​
main:
  provider := WalterCellularProvider
  provider.install
```

The `WalterCellularProvider` extends the `MonarchService` (which was installed
as part of the `monarch.main` call in the previous section), and overrides the
connect method to use the constants for the Walter board.

Note that the name `MonarchService` is a bit misleading, as it is actually a
provider (extending the `CellularServiceProvider` class).

The `main` function then installs the provider, so that containers can use it.

We can now install this container on the device:

```toit
jag container install cellular cellular.toit
```

Other containers can now use the cellular provider.

For example, create, and watch the following `cellular-user.toit` program:

```toit
import net
import net.cellular
​
do-network-things network/net.Client:
  ...
​
main:
  network := cellular.open --name="walter" {:}
​
  try:
    do-network-things network
  finally:
    network.close
```

The `do-network-things` function could be the same as in the previous section
(in which case you will have to add a few more imports).

Note that multiple containers can call `cellular.open` at the same time and
access the internet concurrently.
