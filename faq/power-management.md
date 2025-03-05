## Power Management

### How do I implement sleep mode in Walter?

The modem automatically enters its lowest power mode when:

1. It's disconnected from the network using
   `setOpState(WALTER_MODEM_OPSTATE_MINIMUM)`
2. It finishes a transmission and enters RRC idle mode with PSM or eDRX enabled

Example code for configuring power saving:

```cpp
// Enable PSM (Power Saving Mode)
modem.configPSM(WALTER_MODEM_PSM_ENABLE,"01101011", "00101010");

// or configure eDRX
modem.configEDRX();
```

### What happens when ESP32 goes into deep sleep?

When configuring PSM using
`configPSM(WALTER_MODEM_PSM_ENABLE, "01101011", "00101010")`,
the modem will automatically enter sleep mode when the conditions are met.
You don't need to explicitly disconnect from the network.
The `configPSM()` function only configures the behavior
and doesn't immediately trigger sleep mode.
