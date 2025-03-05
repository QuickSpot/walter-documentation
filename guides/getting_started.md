## TL;DR

  1. Insert the SIM card.
  2. Connect the LTE antenna, **mandatory** when using LTE.
  3. Connect GNSS antenna, Walter requires a passive GNSS antenna.
  4. Make sure Walter and/or the GNSS antenna has a clear view to the sky.
  5. Power up Walter via the USB-C connection.
  6. Browse to [walterdemo.quickspot.io](https://walterdemo.quickspot.io/).
  7. As soon as a GNSS position could be determined or after 7 minutes without
     GNSS reception you should see your Walter appearing on the portal. You can
     recognize your Walter by his MAC address.

![SIM card insertion](../../img/getting_started_walter_sim_insert.jpg)

## Prepare the hardware

Walter comes with a broad range on connectivity options. If you only want to use
the WiFi and Bluetooth connection offered by the ESP32-S3 there is no need to
connect any antenna's.

When you also want to make use of the LTE radio it is **mandatory** to connect
an LTE antenna, failing to do so may irreversibly destroy the RF frontend of the
modem. Walter recommends the following antennas:

- LTE: [Taoglas FXUB63.07.0150C](https://www.taoglas.com/product/fxub63-ultra-wide-band-flex-antenna/)
- GNSS: [Taoglas FXP611.07.0092C](https://www.taoglas.com/product/cloud-fxp611-gps-glonass-compass-flexible-pcb-2/)

> [!note]
> Walter only works with passive GNSS antennas as there is no phantom
> power on the GNSS antenna connector. The LNA and SAW filter are integrated on
> the Walter module. If you would connect an active antenna you will not get a
> fix.

To power up Walter you can use a standard USB-C cable and connect Walter to your
PC or a power bank. You can also power Walter via the header pins (Vin and GND).

> [!warning]
> The USB-C power and Vin pin are internally connected. If you are
> powering Walter through the headers pins it is best to use an USB-C cable of
> which the VCC wire has been cut.

## The pre-flashed firmware

Every Walter comes pre-flashed with an example application which requires you
to connect the LTE and GNSS antennas. The out-of-the box firmware performs the
following tasks:

  1. Configure the modem for LTE-M connectivity with network pushed APN.
  2. Check and update GNSS assistance data if required.
  3. Try to establish a GNSS fix, the firmware will try this up to 5 times and
     the maximum duration of an attempt is approximately 66 seconds.
  4. Upload the data to the
     [walterdemo.quickspot.io](https://walterdemo.quickspot.io/) portal.

To make use of this pre-flashed demonstrator you should
[prepare the hardware](#prepare-the-hardware) by installing LTE and GNSS
antenna. Also insert a SIM card which supports LTE-M. You can now power up
Walter and give him some time to send out his first message. Make sure the GNSS
antenna has a clear view to the sky and allow Walter about 10 minutes to connect
and upload the first data.

On the [walterdemo.quickspot.io](https://walterdemo.quickspot.io/) portal you
can see all Walter boards which have ever sent data to the demonstration portal.
Every Walter identifies itself using his MAC address which is printed on the bag
in which you received your Walter board.

In case you lost the bag you can also watch to the console output from Walter to
discover it's MAC address. To see console output you must connect Walter to
your computer using the built-in USB-C port. After plugging in Walter you should
get a serial port:

- On Windows: COMxx
- On Linux or macOS: /dev/tty*

The serial console of the demonstration application runs with 115200 baud. On
Windows you can use a simple program such as
[PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) to view
the console and on Linux or macOS you can just use the `cat` command. After
opening the serial port you should see the MAC address of your Walter board in
the following format:

```console
Walter Positioning v0.0.2
Walter's MAC is: 48:27:E2:10:DF:30
```
