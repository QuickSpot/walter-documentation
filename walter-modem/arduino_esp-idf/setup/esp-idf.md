## Introduction

This guide will walk you through installing the Walter Modem library for ESP-IDF.

> [!TIP]
> If you haven't set up the ESP-IDF dev environment yet, go through the
> [ESP-IDF Toolchain Setup](/developer-toolchains/esp-idf.md) first

## Guide

### 1. Create a new project

To create a new project, open the VS Code command palette (Quickmenu) and select:\
`>ESP-IDF: Create project from Extension Template`

> [!WARNING]
> When using the walter modem all implementation files (`.c`, `.cpp`) should have the `.cpp` extension.
> -> not `main.c` but `main.cpp`

Then select `template-app` as your starter project.

### 2. Installing the Walter Modem Component

> [!WARNING]
> Run all `idf.py` commands inside the ESP-IDF Terminal.

Open the ESP-IDF Terminal from the VS Code command palette:
`>ESP-IDF: Open ESP-IDF Terminal` and run the following command:

```console
idf.py add-dependency "dptechnics/walter-modem^1.1.3"
```

> [!note]
> Make sure to check the version number

### 3. Setting the Device Target

After installing the Walter Modem extension,
the **Device Target** needs to be set to **esp32s3**
*(This needs to be done for each project)*

Set this using the VSCode quickmenu command:
`>ESP-IDF: Set Espressif Device Target`

> [!NOTE]
> If you want to use youre own `fork` or use the `DEV` version of waltermodem,
> you can use the following snippet inside `idf_component.yml`.
>
> You can also specify the branch inside the version tag.
>
> ```yml
> dependencies:
>  dptechnics/walter-modem:
>    version: "*"
>    git: "https://github.com/QuickSpot/walter-esp-idf.git"
> ```

## Additional Resources

- **Library Source Code:**
  [GitHub Repository](https://github.com/QuickSpot/walter-esp-idf)
