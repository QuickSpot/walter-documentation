## Introduction

This guide will walk you through installing the WalterModem library
for Micropython

> [!TIP]
> If you haven't set up your Micropython dev environment yet, go through the
> [Micropython Toolchain Setup](/developer-toolchains/micropython.md) first.

## Guide

There are multiple ways to install the WalterModem library for Micropython.

<!--- tabs:start --->

### **MIP (Recommended)**

[MIP](https://docs.micropython.org/en/latest/reference/packages.html)
is similar in concept to Python's `pip` tool.
It allows you to install packages from
[micropython-lib](https://docs.micropython.org/en/latest/reference/glossary.html#term-micropython-lib)
and from third-party sites *(including Github & Gitlab)*.

You can use `mpremote`, the officially-supported tool for interacting
with a MicroPython device, to install the Modem Library MIP packagae to your device.

Simply run:

```shell
mpremote mip install github:QuickSpot/walter-micropython
```

If needed, you can specify the device as such:

```shell
mpremote connect <device> mip install github:QuickSpot/walter-micropython
```

> [!TIP]
> \<device\> may look like: /dev/ttyACM0 (on Linux) or eg. "COM3" (on Windows)

### **Util Script**

The [Micropython WalterModem](https://github.com/QuickSpot/walter-micropython.git)
repository contains a quick install utility script,
it will copy all library files to the correct place on the board.

The script can be found under `util/install_walter_modem/` and is available for
Linux *(.sh)* and Windows *(.ps1)*.

The purpose of this utility is for convenience during development
of the modem library itself or should there be any issues with
[MIP](https://docs.micropython.org/en/latest/reference/packages.html).

> [!NOTE]
> This utility script requires mpremote to run, if not installed already,
> you can do so by running: `pip install mpremote`

> [!TIP]
> If the script doesn't run, make sure it is executable first, on linux:
> `chmod +x <path_to_script>`

### **Manual Copy (mpremote)**

You can use mpremote to manually copy the WalterModem libary to your device.

1. Clone the [Micropython WalterModem](https://github.com/QuickSpot/walter-micropython.git)
2. Change Directory into the repository
3. Make the lib directory on the MicroPython device:

   ```shell
   mpremote mkdir lib
   ```

4. Copy the modem library to the lib folder
   on the MicroPython device, to install it.

   ```shell
   mpremote cp -r walter_modem :lib/
   ```

   If needed you can specify the device as such:

   ```shell
   mpremote connect <device> cp -r walter_modem :lib/
   ```

   > [!TIP]
   > \<device\> may look like: /dev/ttyACM0 (on Linux) or eg. "COM3" (on Windows)

### **Manual Copy (Thonny)**

#### 1. Clone the Walter MicroPython library

   ```shell
   git clone https://github.com/QuickSpot/walter-micropython.git
   ```

#### 2. Open the repository in Thonny

- Open Thonny and ensure that the MicroPython interpreter is set up correctly 
  (See the [Micropython Toolchain Setup; step 6](/developer-toolchains/micropython.md#6-uploading-scripts-via-thonny)).
- Go to `File` -> `Open...`.
- Navigate to the local directory where you cloned the repository.

#### 3. Upload all files to Walter

On the Micropython device, create a new directory called `lib`.

![thonney-new-dir](img/thonny-new-dir.png)

Double click on the newly created `lib` directory to open it.

![thonny-lib-open](img/thonny-lib-open.png)

In the cloned repository, right click on the directory `walter_modem`
and select `Upload to /lib`

![thonny-upload-to-lib](img/thonny-upload-to-lib.png)

<!--- tabs:end -->

Now, the library is uploaded to Walter.

You can find some example applications for Walter in the `examples` folder.

## Library structure

- `core.py`: The core functionality of the library.
- `modem.py`: The actual modem class you end up importing. It ties everything
  together, inheriting the mixins.
- `mixins`: A folder containing the protocol/purpose specifc methods to interact
  with the library, such as common, sleep, http, mqtt, sockets, ...
- `enums.py`: Where all the enums used in the library are defined.
- `structs.py`: Where all the "structs" used in the library are defined.
- `util.py`: Internal library utility functions.
- `queue.py`: A third-party `Queue` implementation
  that is missing in `uasyncio`, MicroPython's `asyncio` implementation.
  The code is cherry-picked [from this great repo by Peter Hinch](https://github.com/peterhinch/micropython-async).

The library makes use of asyncio coroutines for communicating with the modem,
queueing commands and ensuring nothing is blocking.

```python
import asyncio

from walter_modem import Modem

from walter_modem.enums import (
  # ...
)

from walter_modem.structs import (
  # ...
)

modem = Modem()

async def main():
    # ...
    # ......
    await modem.begin()
    # ......
    # ...

asyncio.run(main())
```
