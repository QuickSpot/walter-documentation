## Introduction

This guide will walk you through insstalling the Walter Modem library
for Micropython

> [!tip]
> If you haven't set up your Micropython dev environment yet, go through the
> [Micropython Toolchain Setup](/developer-toolchains/micropython.md) first.

## Guide

There are multiple ways to install the WalterModem library for Micropython.

<!--- TODO: Make sure there is sufficient explanation about the options --->

<!--- tabs:start --->

### **MIP (Recommended)**

> [!INFO]
> Waiting for PR #7 to be merged before this part of the docs can be written

### **Install Util Script**

<!--- TODO: Add actual link once repo is renamed --->
The `Micropython WalterModem` contains a quick install utility script,
it will copy all library files to the correct place on the board.

The script can be found under `util/install_walter_modem` and is available for
Linux *(.sh)* and Windows *(.ps1)*.

> [!NOTE]
> This utility script requires mpremote to run, if not installed already,
> you can do so by running: `pip install mpremote`

> [!TIP]
> If the script doesn't run, make sure it is executable first, on linux:
> `chmod +x <path_to_script>`

### **Manual Copy (mpremote)**

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

In the cloned repository, right click on the directory `walter_modem` and select `Upload to /lib`

![thonny-upload-to-lib](img/thonny-upload-to-lib.png)

<!--- tabs:end -->

Now, the library is uploaded to Walter.

You can find some example applications for Walter in the `examples` folder.

## Library structure

- ``
- `queue.py` is a third-party `Queue` implementation
  that is missing in `uasyncio`, MicroPython's `asyncio` implementation.
  The code is cherry-picked [from this great repo by Peter Hinch](https://github.com/peterhinch/micropython-async).
- `walter.py` contains the library implementation for interacting with Walter.
- `_walter.py` contains extra constants and helper objects for the library.

The library makes use of asyncio coroutines for communicating with the modem,
queueing commands and running your user code.
You can create your own coroutines,
for example to wait for a GNSS fix in the background
(instead of blocking the main coroutine).
Extra tasks in your main routine can be created as following:

```python
import uasyncio
import walter
import _walter

async def my_extra_task():
    # ...

async def main():
    # ...
    # ......
    uasyncio.create_task(my_extra_task())
    # ......
    # ...

modem = walter.Modem()
modem.begin(main)
```

## Additional resources

- [MicroPython Documentation](https://docs.micropython.org/en/latest/)
- [Esptool.py Documentation](https://docs.espressif.com/projects/esptool/en/latest/esp32s3/index.html)
- [Thonny IDE](https://thonny.org/)
- [scientifichackers/ampy: MicroPython Tool - Utility to interact with a MicroPython board over a serial connection.](https://github.com/scientifichackers/ampy)
- [dhylands/rshell: Remote Shell for MicroPython](https://github.com/dhylands/rshell)