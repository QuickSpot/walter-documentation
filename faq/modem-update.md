## Modem update

### How can I see the Sequans GM02SP firmware version

First flash the [modem passthrough](https://github.com/QuickSpot/walter-arduino/tree/main/examples/ModemPassthrough)
example onto Walter to get direct access to the AT command interface of the modem. You can now
issue the following commands:
 - `ATI1`: to get the firmware revision of the modem
 - `ATI3`: to get the hardware revision of the modem

### How can I update the Sequans GM02SP firmware

The latest official firmware version is **LR8.2.1.0-61488**. This release includes significant improvements in **NB-IoT performance**. The first step in the upgrade process is to flash the [modem passthrough](https://github.com/QuickSpot/walter-arduino/tree/main/examples/ModemPassthrough) example onto Walter to get direct access to the AT command interface of the modem. 

Now use the `ATI1` command to make sure that the modem is currently running version **LR8.2.0.3-60186**. You cannot
use the below update method starting from other firmware versions.

> [!WARNING]
> The upgrade **resets hardware configurations** such as UART speed and wake source settings. Ensure that you follow > the instructions below to preserve or restore these settings.

> [!note]
> The update can take a long time. Depending on the network connection it can take between 10 and 30 minutes 
> to complete, please do not power-cycle the modem. 

Follow these steps to perform the FOTA upgrade:
1. **Avoid a power cut** during the upgrade process (the modem can recover from it, but uninterrupted power is recommended).
2. **Create a factory restore point**:
     ```bash
     AT+CFUN=5
     AT+SQNFACTORYSAVE="quickspot"
     ```
3. **Enable security configuration**:  
   ```bash
   AT+SQNSPCFG=1,2
   ```

4. **Enable full functionality**:  
   ```bash
   AT+CFUN=1
   ```

5. **Initiate upgrade** after you received CEREG 1 or 5:  
   ```bash
   AT+SQNSUPGRADE="https://quickspot.io/firmware/GP02RBAQ-DM_LR8.2.0.3-60186_to_LR8.2.1.0-61488_Bootrom.dup",1,10,1,1
   ```
6. **Factory reset the HW config**:
   ```bash
   AT+SQNSFACTORYRESET
   ```