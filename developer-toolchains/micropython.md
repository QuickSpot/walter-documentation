## Introduction

[MicroPython](https://micropython.org/) is a lightweight implementation
of the Python programming language that is optimised to run on microcontrollers
and in constrained environments.

This guide walks you through setting up MicroPython on Walter and
running your first script.

---

## Guide

### 1. Install Python and required tools

#### Python

<!-- tabs:start -->

##### **Windows**

Download and install Python from the
[official website](https://www.python.org/downloads/).
During installation, ensure you select the option to add Python to your PATH.

##### **Linux: Debian-based**

Most Debian-based systems come with Python pre-installed. Verify by running:

```shell
python3 --version
```

If not installed, install it with:

```shell
sudo apt-get update
sudo apt-get install python3 python3-pip
```

##### **Linux: Fedora**

Fedora normally comes with Python pre-installed, to verify this, run:

```shell
python3 --version
```

If Python is not installed on your system, you can install it like so:

```shell
sudo dnf install python3 python3-pip
```

<!-- tabs:end -->

#### Python virtual environment

<!-- tabs:start -->

##### **Windows**

Open a terminal window in your project directory.

- *Open "Terminal" and navigate to the project directory
  `cd path/to/your/project/dir`*
- *Alternatively, navigate to your project directory in File Explorer,
  then right-click in the empty space and select "Open in Terminal."*

Create a virtual environment:

```shell
python -m venv micropython-env
```

Activate the virtual environment:

```shell
micropython-env\Scripts\activate
```

> [!NOTE]
> In PowerShell, the activation command would be:
>
> ```ps
> .\micropython-env\Scripts\Activate.ps1
> ```

##### **Linux: Debian-based**

Install the `venv` module if it's not already installed:

```shell
sudo apt-get install python3-venv
```

Create a virtual environment inside your project directory:

```shell
python3 -m venv micropython-env
```

Activate the virtual environment:

```shell
source micropython-env/bin/activate
```

##### **Linux: Fedora**

In Fedora, Python 3 includes the built-in venv module.

Create a virtual environment inside your project directory:

```shell
python3 -m venv micropython-env
```

Activate the virtual environment:

```shell
source micropython-env/bin/activate
```

<!-- tabs:end -->

*Your terminal prompt should change to indicate that the virtual environment is active.*

#### ESPTool

[esptool](https://docs.espressif.com/projects/esptool/en/latest/esp32s3/index.html)
is a Python-based tool that helps you flash the MicroPython firmware
onto the ESP32-S3 SoC of your Walter board. Within the virtual environment,
install esptool using pip:

```shell
pip install esptool
```

#### Mpremote

The MicroPython remote control CLI tool, [mpremote](https://docs.micropython.org/en/latest/reference/mpremote.html),
provides a set of utilities for remotely interacting with a MicroPython device,
managing its file system, and automating tasks over a serial connection.

It can be installed using `pip` by running:

```console
pip install --user mpremote
```

or via [pipx](https://pypa.github.io/pipx/)

```console
pipx install mpremote
```

The simplest way to use it, is by simply typing `mpremote`.
This will auto detect the first available USB serial device and access the REPL.
It is highly recommended to read the
[mpremote documentation](https://docs.micropython.org/en/latest/reference/mpremote.html)
so you can make full use of it during your micropython development.

> [!TIP]
> If `mpremote` is not in your system's PATH,
> you can run it by using `python -m mpremote` instead.\
> However, it is recommended to add it to your system's PATH
> (if it did not automatically) should you intend on frequently using this tool.

### 2. Download MicroPython firmware

Visit the [MicroPython ESP32-S3 download page](https://micropython.org/download/ESP32_GENERIC_S3/)
and download the latest stable **.bin** firmware release for the ESP32-S3.

### 3. Identify the correct COM port

<!-- tabs:start -->

#### **Windows**

Connect your Walter to your computer via USB. Identify the COM port by opening
Device Manager and checking under "Ports (COM & LPT)".
The port will be labeled something like `COM3` or `COM4`.

#### **Linux: Debian-based**

Connect your ESP32-S3 to your computer via USB and identify the port by running:

```shell
ls /dev/ttyACM*
```

#### **Linux: Fedora**

Connect your ESP32-S3 to your computer via USB and identify the port by running:

```shell
ls /dev/ttyACM*
```
<!-- tabs:end -->

The port will look something like `/dev/ttyACM0`,
remember the port for the following steps.

Alternatively, you can use `mpremote connect list` to get a list of all COM ports
and anything connected on them.

### 4. Flash MicroPython onto the ESP32-S3

<!-- tabs:start -->

#### **Windows**

1. **Erase the flash** Run the following command,
   replacing `<your_port>` with your identified port from the previous step:

   ```shell
   esptool --chip esp32s3 --port <your_port> erase_flash
   ```

2. **Flash the firmware** Use esptool to flash the MicroPython firmware
3. onto the ESP32-S3. Replace `<your_port>` and `<firmware_path>`
   with your port and the path to the downloaded firmware:
  
   ```shell
   esptool --chip esp32s3 --port <your_port> write_flash -z 0 <firmware_path>
   ```

#### **Linux: Debian-based**

1. **Erase the flash** Run the following command,
   replacing `<your_port>` with your identified port from the previous step:

   ```shell
   esptool.py --chip esp32s3 --port <your_port> erase_flash
   ```

2. **Flash the firmware** Use esptool to flash the MicroPython firmware
   onto the ESP32-S3. Replace `<your_port>` and `<firmware_path>`
   with your port and the path to the downloaded firmware:

   ```shell
   esptool.py --chip esp32s3 --port <your_port> write_flash -z 0 <firmware_path>
   ```

#### **Linux: Fedora**

1. **Erase the flash** Run the following command,
   replacing `<your_port>` with your identified port from the previous step:

   ```shell
   esptool.py --chip esp32s3 --port <your_port> erase_flash
   ```

2. **Flash the firmware** Use esptool to flash the MicroPython firmware
   onto the ESP32-S3. Replace `<your_port>` and `<firmware_path>`
   with your port and the path to the downloaded firmware:

   ```shell
   esptool.py --chip esp32s3 --port <your_port> write_flash -z 0 <firmware_path>
   ```

<!-- tabs:end -->

### 5. Access the MicroPython REPL

The REPL (Read-Eval-Print Loop) is an interactive prompt
that allows you to run Python commands directly on the ESP32-S3.

If only 1 device is connected, simply run:

```console
mpremote
```

This will auto detect the first available USB serial device and access the REPL.
Alternatively, specify the device using:

```console
mpremote connect <device> repl
```

If you wish not to use mpremote, see below alternative ways to access the REPL.

<!-- tabs:start -->

#### **Windows**

1. **Install PuTTY**: Download and install PuTTY from the [official website](https://www.putty.org/).

2. **Open PuTTY**:
   - Set the connection type to `Serial`.
   - Enter your COM port (e.g., `COM3`) and set the speed to `115200`.
   - Click "Open" to start the session.

3. **Access the REPL**: Press the `Enter` key.
   You should see the MicroPython prompt (`>>>`).
   Try typing the following in the prompt:

   ```python
   >>> print('Hello Walter!')
   Hello Walter!
   ```

#### **Linux: Debian-based**

1. **Install picocom**: If you don't have picocom installed, install it using:

   ```shell
   sudo apt-get install picocom
   ```

2. **Open a serial terminal**: Open picocom with the following command:

   ```shell
   picocom -b 115200 <your_port>
   ```

3. **Access the REPL**: Press the `Enter` key.
   You should see the MicroPython prompt (`>>>`).
   Try typing the following in the prompt:

   ```python
   >>> print('Hello Walter!')
   Hello Walter!
   ```

#### **Linux: Fedora**

1. **Install picocom**: If you don't have picocom installed, install it using:

   ```shell
   sudo dnf install picocom
   ```

2. **Open a serial terminal**: Open picocom with the following command:

   ```shell
   picocom -b 115200 <your_port>
   ```

3. **Access the REPL**: Press the `Enter` key.
   You should see the MicroPython prompt (`>>>`).
   Try typing the following in the prompt:

   ```python
   >>> print('Hello Walter!')
   Hello Walter!
   ```
<!-- tabs:end -->

### 6. Writing and running your first MicroPython script

You can write and test simple scripts directly in the REPL,
such as the following Hello World example:

1. **Hello World**: This simple script will print `Hello World`
   followed by a random int between 0 and 10 every second.
   Enter the following code in the REPL:

   ```python
   from time import sleep
   from random import randint
   
   while True:
       print("Hello World - %d" % randint(0, 10))
       sleep(1)
   ```

2. **Stopping the Script**: To stop the script, press `Ctrl+C`.

### 7. Uploading scripts

Uploading files to a Walter running MicroPython lets you deploy full scripts
that are saved to the device's filesystem,
making them persistent and ready to run even after a reboot.
Several tools are available, such as [Thonny](https://thonny.org/),
[rshell](https://github.com/dhylands/rshell) and
[mpremote](https://docs.micropython.org/en/latest/reference/mpremote.html).

We recommend to use `mpremote`, as it is offered by micropython
and is IDE independent.Read the
[official mpremote documentation](https://docs.micropython.org/en/latest/reference/mpremote.html)
to get a detailed overview and idea of what the tool has to offer.

### 8. Thonny

For those who prefer a GUI to upload and communicate with the Micropython device,
we recommend thonny.

Thonny is an integrated development environment (IDE) designed for Python.
It also supports MicroPython, making it a popular choice
for uploading scripts to a MicroPython device.

#### Install Thonny

<!-- tabs:start -->

##### **Windows**

Download and install Thonny from the [official website](https://thonny.org/).

##### **Linux: Debian-based**

Install Thonny using the following command:

```shell
sudo apt-get install thonny
```

##### **Linux: Fedora**

Install Thonny using the following command:

```shell
sudo dnf install thonny
```
<!-- tabs:end -->

#### Connect Thonny to ESP32-S3

- Open Thonny and go to `Tools` > `Options` > `Interpreter`.
- Set the interpreter to `MicroPython (ESP32)`.
- Set the port to `< Try to detect port automatically >`.

#### Write and upload scripts

- Write your MicroPython script in the editor.
- Click the `Run current script` button to run the script on Walter.

## Additional resources

- [Official MicroPython Documentation](https://docs.micropython.org/en/latest/)
- [mpremote Documentation](https://docs.micropython.org/en/latest/reference/mpremote.html)
- [Esptool.py Documentation](https://docs.espressif.com/projects/esptool/en/latest/esp32s3/index.html)
- [Thonny IDE](https://thonny.org/)
