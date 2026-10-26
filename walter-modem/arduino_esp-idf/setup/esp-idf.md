## Introduction

This guide will walk you through installing the Walter Modem library for ESP-IDF and how to run your first project.

> [!TIP]
> If you haven't set up the ESP-IDF dev environment yet, go through the
> [ESP-IDF Toolchain Setup](/developer-toolchains/esp-idf.md) first

## Guide

### 1. Create a new project

To create a new project, open the VS Code command palette (Quickmenu) and select:\
`>ESP-IDF: New Project`   
select the desired ESP-IDF version from the dropdown menu.

> [!WARNING]    
> When using the walter modem all implementation files (`.c`, `.cpp`) should have the `.cpp` extension.
> -> not `main.c` but `main.cpp`

1. Then under ESP-IDF Templates select `sample_project_cpp`  as your starter project.
2. Choose the project name.
3. Choose the location for the new project.
4. Set the Espressif **IDF_TARGET** to **esp32s3** and **Board** to **ESP32-S3 chip (via builtin USB-JTAG)**.

### 2. Installing the Walter Modem Component

> [!WARNING]
> Run all `idf.py` commands inside the ESP-IDF Terminal.

Open the ESP-IDF Terminal from the Status bar icon or use the VS Code command palette:
`>ESP-IDF: Open ESP-IDF Terminal` and run the following command:

```console
idf.py add-dependency "dptechnics/walter-modem^1.6.1"
```

> [!NOTE]
> Make sure to check the version number

> [!NOTE]
> If you want to use your own `fork` or use the `DEV` version of waltermodem,
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

### 3. SDK Configuration

Walter has 16MB of flash memory, but new ESP-IDF projects assume 2MB.
Change the following settings:

| Setting              | Default | New value | Needed for                     |
| -------------------- | ------- | --------- | ------------------------------ |
| Flash size           | 2MB     | 16MB      | Every project                  |
| Main task stack size | 3584    | 8192      | The example code in this guide |

You can change them in the SDK Configuration Editor or with an
`sdkconfig.defaults` file.

<!-- tabs:start -->

#### **SDK Configuration Editor**

1. Open the ESP-IDF Explorer and select **SDK Configuration Editor**.
2. Under **Serial flasher config**, set **Flash size** to `16MB`.
3. Under **Component config → ESP System Settings**, set
   **Main task stack size** to `8192`.
4. Click **Save**.

#### **sdkconfig.defaults**

Create a file named `sdkconfig.defaults` in the project root:

```
CONFIG_ESPTOOLPY_FLASHSIZE_16MB=y
CONFIG_ESP_MAIN_TASK_STACK_SIZE=8192
```

> [!NOTE]   
> ESP-IDF only reads `sdkconfig.defaults` when it generates a new `sdkconfig`.
> If your project already has an `sdkconfig` file, delete it before you build.

<!-- tabs:end -->

> [!WARNING]    
> After changing the SDK configuration, run `>ESP-IDF: Full Clean Project`
> before you build, so the new settings end up on Walter.

### 4. Building, Flashing and Monitoring

Choose one of the examples below, make sure to check if you have the required hardware and software. 
To run the example code replace the contents of the `.cpp` file in
the `main` folder with the code below, then build, flash and monitor.
Incase you only have the walter board itself, use the example code provided below. 

| Example                                                                                              | What it does                                                         |
| ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| [mqtt](https://github.com/QuickSpot/walter-esp-idf/tree/main/examples/mqtt)                           | Publish and subscribe to messages on an MQTT topic                   |
| [mqtts](https://github.com/QuickSpot/walter-esp-idf/tree/main/examples/mqtts)                         | MQTT secured with TLS certificates                                   |
| [http](https://github.com/QuickSpot/walter-esp-idf/tree/main/examples/http)                           | Send HTTP GET and POST requests                                      |
| [https](https://github.com/QuickSpot/walter-esp-idf/tree/main/examples/https)                         | Send HTTPS GET and POST requests                                     |
| [coap](https://github.com/QuickSpot/walter-esp-idf/tree/main/examples/coap)                           | Exchange data with a CoAP server                                     |
| [tcp](https://github.com/QuickSpot/walter-esp-idf/tree/main/examples/tcp)                             | Two-way TCP connection with a remote server                          |
| [udp](https://github.com/QuickSpot/walter-esp-idf/tree/main/examples/udp)                             | Two-way UDP connection with a remote server                          |
| [positioning](https://github.com/QuickSpot/walter-esp-idf/tree/main/examples/positioning)             | Low-power GNSS tracker that sends its position to a server           |
| [bluecherry](https://github.com/QuickSpot/walter-esp-idf/tree/main/examples/bluecherry)               | Connect to the BlueCherry cloud platform, with MQTT and OTA updates  |
| [modem_firmware_flash](https://github.com/QuickSpot/walter-esp-idf/tree/main/examples/modem_firmware_flash) | Update or recover the modem firmware  |


Run the following commands from the VS Code command palette.

> [!TIP]    
> Most of these commands also have an icon in the VS Code status bar.

#### Connect to Walter

Do this once for each project:

| Step                                         | Command                                              |
| -------------------------------------------- | ---------------------------------------------------- |
| Check that the device target is `esp32s3`    | `>ESP-IDF: Set Espressif Device Target`              |
| Select the port Walter is connected to       | `>ESP-IDF: Select Port to Use (COM, tty, usbserial)` |
| Set the flash method to **UART**             | `>ESP-IDF: Select Flash Method`                      |

#### Build, flash and monitor

<!-- tabs:start -->

#### **All in one**

`>ESP-IDF: Build App, Flash App and Start Monitor`

#### **Step by step**

| Step                         | Command                         |
| ---------------------------- | ------------------------------- |
| Build the project            | `>ESP-IDF: Build Your Project`  |
| Flash the project to Walter  | `>ESP-IDF: Flash Your Project`  |
| Show the logs                | `>ESP-IDF: Monitor Device`      |

<!-- tabs:end -->

#### Example code

The monitor shows information about the application,
the ESP32-S3 and the modem, followed by the temperature the modem measured.

> [!NOTE]       
> This example only talks to the modem itself, so it works without a SIM card or network connection.


```cpp
#include <cstdio>
#include <WalterModem.h>
#include "esp_log.h"
#include "esp_system.h"
#include "esp_chip_info.h"
#include "esp_idf_version.h"
#include "esp_app_desc.h"
#include "esp_flash.h"
#include "esp_mac.h"
#include "esp_heap_caps.h"

WalterModem modem;
static const char *TAG = "main";

/* Print general information about the ESP32, the ESP-IDF build and this application. */
static void print_system_info(void)
{
    const esp_app_desc_t *app = esp_app_get_description();
    ESP_LOGI(TAG, "Application: %s %s (built %s %s)", app->project_name, app->version, app->date,app->time);
    ESP_LOGI(TAG, "ESP-IDF version: %s", esp_get_idf_version());

    esp_chip_info_t chip;
    esp_chip_info(&chip);
    ESP_LOGI(TAG, "Chip: %s rev v%d.%d, %d CPU core(s), %s%s%s", CONFIG_IDF_TARGET,
             chip.revision / 100, chip.revision % 100, chip.cores,
             (chip.features & CHIP_FEATURE_WIFI_BGN) ? "WiFi " : "",
             (chip.features & CHIP_FEATURE_BLE) ? "BLE " : "",
             (chip.features & CHIP_FEATURE_EMB_PSRAM) ? "embedded PSRAM" : "");

    uint32_t flash_size = 0;
    if (esp_flash_get_size(NULL, &flash_size) == ESP_OK)
    {
        ESP_LOGI(TAG, "Flash: %lu MB %s", (unsigned long) (flash_size / (1024 * 1024)),
                 (chip.features & CHIP_FEATURE_EMB_FLASH) ? "embedded" : "external");
    }

    uint8_t mac[6];
    if (esp_read_mac(mac, ESP_MAC_WIFI_STA) == ESP_OK)
    {
        ESP_LOGI(TAG, "MAC: %02x:%02x:%02x:%02x:%02x:%02x", mac[0], mac[1], mac[2], mac[3], mac[4], mac[5]);
    }

    ESP_LOGI(TAG, "Heap: %lu bytes free (minimum ever %lu), PSRAM: %u bytes",
             (unsigned long) esp_get_free_heap_size(), (unsigned long) esp_get_minimum_free_heap_size(),
             (unsigned) heap_caps_get_total_size(MALLOC_CAP_SPIRAM));
}

/* Print the modem's identity numbers. Works without a SIM or network. */
static void print_modem_info(void)
{
    WalterModemRsp rsp = {};
    if (modem.getIdentity(&rsp) && rsp.type == WALTER_MODEM_RSP_DATA_TYPE_IDENTITY)
    {
        ESP_LOGI(TAG, "Modem IMEI: %s, IMEISV: %s, SVN: %s", rsp.data.identity.imei,
                 rsp.data.identity.imeisv, rsp.data.identity.svn);
    }
    else
    {
        ESP_LOGE(TAG, "Could not read the modem identity");
    }
}

extern "C" void app_main(void)
{
    WalterModemRsp rsp = {};
    printf("Testing ESP-IDF and the Walter Modem\n");
    print_system_info();

    printf("Initializing modem...\n");
    if (!modem.begin(UART_NUM_1))
    {
        printf("Failed to initialize modem.\n");
        return;
    }
    printf("Modem initialized successfully.\n");
    print_modem_info();

    /* Temp monitor is modem-local, so they need no network either. */
    /* Enable temperature monitoring */
    if (modem.configTemperatureMonitor(WALTER_MODEM_TEMP_MONITOR_MODE_ON))
    {
        ESP_LOGI(TAG, "Successfully enabled temperature monitoring");
    }
    else
    {
        ESP_LOGE(TAG, "Could not enable temperature monitoring");
    }

    /* Get temperature reading */
    int8_t temperature = 0;
    if (modem.getTemperature(&rsp))
    {
        if (rsp.type == WALTER_MODEM_RSP_DATA_TYPE_TEMPERATURE)
        {
            temperature = rsp.data.temperature.temperature;
            ESP_LOGI(TAG, "Current temperature: %d°C (status: %d)", temperature,
                     rsp.data.temperature.status);
        }
    }
    else
    {
        ESP_LOGE(TAG, "Could not get temperature reading");
    }

    /* Disable temperature monitoring */
    if (modem.configTemperatureMonitor(WALTER_MODEM_TEMP_MONITOR_MODE_OFF))
    {
        ESP_LOGI(TAG, "Successfully disabled temperature monitoring");
    }
    else
    {
        ESP_LOGE(TAG, "Could not disable temperature monitoring");
    }
}
```

## Additional Resources

- **Library Source Code:**
  [GitHub Repository](https://github.com/QuickSpot/walter-esp-idf)
