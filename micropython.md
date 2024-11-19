# Using MicroPython with the Walter board

## Introduction

[MicroPython](https://micropython.org/) is a lightweight implementation of the Python programming language that is optimised to run on microcontrollers and in constrained environments. This tutorial will guide you through setting up MicroPython on Walter, running your first script, and using the [Walter MicroPython library](https://github.com/QuickSpot/walter-micropython).

## Step 1: Install Python and required tools

### Windows

1. **Install Python**: Download and install Python from the [official website](https://www.python.org/downloads/). During installation, ensure you select the option to add Python to your PATH.

2. **Set up a Python virtual environment**:
   
   - Open Terminal and navigate to your project directory.
   
   - Create a virtual environment:
     
     ```shell
     python -m venv micropython-env
     ```
   
   - Activate the virtual environment:
     
     ```shell
     micropython-env\Scripts\activate
     ```
   
   - Your terminal prompt should change to indicate that the virtual environment is active.

3. **Install esptool**: [esptool](https://docs.espressif.com/projects/esptool/en/latest/esp32s3/index.html) is a Python-based tool that helps you flash the MicroPython firmware onto the ESP32-S3 SoC of your Walter board. Within the virtual environment, install esptool using pip:
   
   ```shell
   pip install esptool
   ```

### Debian-based OS

1. **Install Python**: Most Debian-based systems come with Python pre-installed. Verify by running:
   
   ```shell
   python3 --version
   ```
   
   If not installed, install it with:
   
   ```shell
   sudo apt-get update
   sudo apt-get install python3 python3-pip
   ```

2. **Set up a Python virtual environment**:
   
   - Install the `venv` module if it's not already installed:
     
     ```shell
     sudo apt-get install python3-venv
     ```
   
   - Create a virtual environment inside your project directory:
     
     ```shell
     python3 -m venv micropython-env
     ```
   
   - Activate the virtual environment:
     
     ```shell
     source micropython-env/bin/activate
     ```
   
   - Your terminal prompt should change to indicate that the virtual environment is active.

3. **Install esptool**: [esptool](https://docs.espressif.com/projects/esptool/en/latest/esp32s3/index.html) is a Python-based tool that helps you flash the MicroPython firmware onto the ESP32-S3 SoC of your Walter board. Within the virtual environment, install esptool using pip:
   
   ```shell
   pip install esptool
   ```

## Step 2: Download MicroPython firmware

1. **Download the MicroPython firmware**: Visit the [MicroPython ESP32-S3 download page](https://micropython.org/download/ESP32_GENERIC_S3/) and download the latest stable **.bin** firmware release for the ESP32-S3.

2. **Identify the correct COM port**:
   
   - **Windows**: Connect your Walter to your computer via USB. Identify the COM port by opening Device Manager and checking under "Ports (COM & LPT)". The port will be labeled something like `COM3` or `COM4`.
   
   - **Debian-based OS**: Connect your ESP32-S3 to your computer via USB and identify the port by running:
     
     ```shell
     ls /dev/ttyACM*
     ```
     
     The port will look something like `/dev/ttyACM0`.
   
   - Remember the port for the following steps.

## Step 3: Flash MicroPython onto the ESP32-S3

> When using a Debian-based OS for the following steps, replace `esptool` with `esptool.py`.

1. **Erase the flash**:
   
   - Run the following command, replacing `<your_port>` with your identifed port from the previous step:
     
     ```shell
     esptool --chip esp32s3 --port <your_port> erase_flash
     ```

2. **Flash the firmware**:
   
   - Use esptool to flash the MicroPython firmware onto the ESP32-S3. Replace `<your_port>` and `<firmware_path>` with your port and the path to the downloaded firmware:
     
     ```shell
     esptool --chip esp32s3 --port <your_port> write_flash -z 0 <firmware_path>
     ```

## Step 4: Access the MicroPython REPL

The REPL (Read-Eval-Print Loop) is an interactive prompt that allows you to run Python commands directly on the ESP32-S3.

### Windows

1. **Install PuTTY**: Download and install PuTTY from the [official website](https://www.putty.org/).

2. **Open PuTTY**:
   
   - Set the connection type to `Serial`.
   
   - Enter your COM port (e.g., `COM3`) and set the speed to `115200`.
   
   - Click "Open" to start the session.

3. **Access the REPL**: Press the `Enter` key. You should see the MicroPython prompt (`>>>`). Try typing the following in the prompt:
   
   ```python
   >>> print('Hello Walter!')
   Hello Walter!
   ```

### Debian-based OS

1. **Install picocom**: If you don't have picocom installed, install it using:
   
   ```shell
   sudo apt-get install picocom
   ```

2. **Open a serial terminal**: Open picocom with the following command:
   
   ```shell
   picocom -b 115200 <your_port>
   ```

3. **Access the REPL**: Press the `Enter` key. You should see the MicroPython prompt (`>>>`). Try typing the following in the prompt:
   
   ```python
   >>> print('Hello Walter!')
   Hello Walter!
   ```

## Step 5: Writing and running your first MicroPython script

You can write and test simple scripts directly in the REPL, such as the following Hello World example:

1. **Hello World**: This simple script will print `Hello World` followed by a random int between 0 and 10 every second. Enter the following code in the REPL:
   
   ```python
   from time import sleep
   from random import randint
   
   while True:
       print("Hello World - %d" % randint(0, 10))
       sleep(1)
   ```

2. **Stopping the Script**: To stop the script, press `Ctrl+C`. In order to restart the script, reboot Walter by pressing `Ctrl+D`.

## Step 6: Uploading scripts via Thonny

Uploading files to a Walter running MicroPython lets you deploy full scripts that are saved to the device’s filesystem, making them persistent and ready to run even after a reboot. Several tools are available, such as [Thonny](https://thonny.org/), [ampy](https://github.com/scientifichackers/ampy) and [rshell](https://github.com/dhylands/rshell). Thonny is an integrated development environment (IDE) designed for Python. It also supports MicroPython, making it a popular choice for uploading scripts to a MicroPython device.

1. **Install Thonny**:
   
   - **Windows**: Download and install Thonny from the [official website](https://thonny.org/).
   
   - **Debian-based OS**: Install Thonny using the following command:
     
     ```shell
     sudo apt-get install thonny
     ```

2. **Connect Thonny to ESP32-S3**:
   
   - Open Thonny and go to `Tools` > `Options` > `Interpreter`.
   
   - Set the interpreter to `MicroPython (ESP32)`.
   
   - Set the port to `< Try to detect port automatically >`.

3. **Write and upload scripts**:
   
   - Write your MicroPython script in the editor.
   
   - Click the `Run current script` button to run the script on Walter.

## Step 7: Using the Walter MicroPython library

1. **Clone the Walter MicroPython library**:
   
   ```shell
   git clone https://github.com/QuickSpot/walter-micropython.git
   ```

2. **Open the repository in Thonny**:
   
   - Open Thonny and ensure that the MicroPython interpreter is set up correctly (as done in Step 6).
   
   - Go to `File` -> `Open...`.
   
   - Navigate to the local directory where you cloned the repository.

3. **Upload all files to Walter**:
   
   - Upload the `boot.py`, `queue.py`, `walter.py` and `_walter.py` file by right clicking on each file and selecting `Upload to /`.  Now, the library is uploaded to Walter and the uploaded `boot.py` script will run on every restart.

You can find some example applications for Walter in the `examples` folder.

The Walter MicroPython library currently features four files:

- `boot.py` initially contains an example application for Walter, but can be modified to contain your own application.
- `queue.py` is a third-party `Queue` implementation that is missing in `uasyncio`, MicroPython's `asyncio` implementation. The code is cherry-picked [from this great repo by Peter Hinch](https://github.com/peterhinch/micropython-async).
- `walter.py` contains the library implementation for interacting with Walter.
- `_walter.py` contains extra constants and helper objects for the library.

The library makes use of asyncio coroutines for communicating with the modem, queueing commands and running your user code. You can create your own coroutines, for example to wait for a GNSS fix in the background (instead of blocking the main coroutine).  Extra tasks in your main routine can be created as following:

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
