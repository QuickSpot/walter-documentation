## Introduction

This guide will walk you through installing the Walter Modem library,
selecting the right board settings,
and running example sketches to get your modem up and running.

> [!TIP]
> If you haven't set up the Arduino IDE yet,
> go through [Arduino Setup Guide](/developer-toolchains/arduino.md) first.

## Guide

### 1. Installing the Walter Modem Library

The Walter modem library can be easily installed
via the built-in Arduino Library Manager:

1. Open the Arduino IDE.
2. Navigate to **Tools > Manage Libraries…**
3. In the search field, type `WalterModem`.
4. Select the Walter modem library from the list and click **Install**.

![Arduino Library Manager](img/arduino_library_manager.png)

### 2. Opening and Running an Example

Once the library is installed, you can explore the provided examples:

1. Open the **Library Manager** in the Arduino IDE.
2. Search for **WalterModem** and select it.
3. Click on the **three dots** in the upper right corner.
4. Hover over **Examples**, then choose one from the list.
5. The selected example will open in a new sketch window.

![Arduino Examples](img/arduino_examples.png)

### 3. Board Selection and Configuration

Before uploading your sketch,
ensure that your board is properly selected and configured:

1. Click the board selection button in the top left corner of the Arduino IDE.
2. In the search bar, type `DPTechnics Walter` and select the board.

   ![Board Selection](img/board_selection.png)

   ![Board Selection Screen](img/board_selection_screen.png)

3. Ensure the partition scheme under **Flash Size** is set to:
   (128Mb APP/12.5MB FATFS), this is required to allow mmodem firmware updates.

### 4. Running the Sketch

With the board configured and the example open:

1. Click the **Upload** button in the Arduino IDE.
2. Wait for the sketch to compile and upload to the board.
3. Open the Serial Monitor to view output
   and confirm that the modem connects to the internet.

## Additional Resources

- **Library Source Code:**
  [GitHub Repository](https://github.com/QuickSpot/walter-arduino)
