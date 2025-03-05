## Introduction

This walks you through setting up the ESP-IDF development environment in VS Code.

It covers installing the ESP-IDF extension, creating a new projec
and configuring the device target.

---

## Guide

### 1. Installing the ESP-IDF Extension

> [!NOTE]
> VS Code is recommended for an easier ESP-IDF experience.

1. Install the
   [ESP-IDF extension](https://marketplace.visualstudio.com/items?itemName=espressifesp-idf-extension)
   from the VS Code Marketplace.
2. After installation, the extension will prompt you to set it up.
3. Select the latest ESP-IDF version and click **Install**.
4. The extension will automatically install all necessary tools.

![ESP-IDF Setup](../../img/esp-idf-setup.png)

![ESP-IDF Install](../../img/esp-idf-install.png)

### 2. Creating a New Project

To create a new project, open the VS Code command palette (Quickmenu) and select:\
`>ESP-IDF: Create project from Extension Template`

Then select `template-app` as your starter project.

### 3. Setting the Device Target

Each new project must have the device target set to **ESP32S3**:\
`>ESP-IDF: Set Espressif Device Target`

Your ESP-IDF environment in VS Code is now set up and ready for development.
