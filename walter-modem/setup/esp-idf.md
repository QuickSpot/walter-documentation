## Introduction

This guide will walk you through installing the Walter Modem library for ESP-IDF.

> [!tip]
> If you haven't set up the ESP-IDF dev environment yet, go through the
> [ESP-IDF Toolchain Setup](/developer-toolchains/esp-idf.md) first

## Guide

### 1. Installing the Walter Modem Component

> [!WARNING]
> Run all `idf.py` commands inside the ESP-IDF Terminal.

Open the ESP-IDF Terminal from the VS Code command palette:
`>ESP-IDF: Open ESP-IDF Terminal` and run the following command:

```console
idf.py add-dependency "dptechnics/walter-modem^1.1.3"
```

> [!note]
> Make sure to check the version number

### 2. Setting the Device Target

After installing the Walter Modem extension,
the **Device Target** needs to be set to **esp32s3**
*(This needs to be done for each project)*

Set this using the VSCode quickmenu command:
`>ESP-IDF: Set Espressif Device Target`

## Additional Resources

- **Library Source Code:**
  [GitHub Repository](https://github.com/QuickSpot/walter-esp-idf)
