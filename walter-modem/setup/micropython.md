## Introduction

This guide will walk you through insstalling the Walter Modem library
for Micropython

> [!tip]
> If you haven't set up your Micropython dev environment yet, go through the
> [Micropython Toolchain Setup](/developer-toolchains/micropython.md) first.

## Guide

### 1. Clone the Walter MicroPython library

   ```shell
   git clone https://github.com/QuickSpot/walter-micropython.git
   ```

### 2. Open the repository in Thonny

- Open Thonny and ensure that the MicroPython interpreter is set up correctly
  (See the [Micropython Toolchain Setup; step 6](/developer-toolchains/micropython.md#6-uploading-scripts-via-thonny)).
- Go to `File` -> `Open...`.
- Navigate to the local directory where you cloned the repository.

### 3. Upload all files to Walter

Upload the `boot.py`, `queue.py`, `walter.py` and `_walter.py`
file by right clicking on each file and selecting `Upload to /`,
if this option is not availble, click on: `File` -> `Save as...`,
and select `MicroPython device`.
Now, the library is uploaded to Walter and the uploaded `boot.py`
script will run on every restart.

You can find some example applications for Walter in the `examples` folder.

The Walter MicroPython library currently features four files:

- `boot.py` initially contains an example application for Walter,
  but can be modified to contain your own application.
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