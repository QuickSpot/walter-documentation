## Communication

### Does Walter support both LTE-M and NB-IoT?

Yes, Walter supports both LTE-M and NB-IoT.
You can force the RAT *(Radio Access Technology)* using:

```cpp
modem.setRAT(WALTER_MODEM_RAT_LTEM) // for LTE-M
modem.setRAT(WALTER_MODEM_RAT_NBIOT) // for NB-IoT
```

Followed by `modem.reset()`.

### What protocols are supported?

Walter supports:

- CoAP + DTLS *(recommended for low data usage as it's UDP-based)*
- MQTT/MQTTS
- HTTP/HTTPS
- Raw UDP
- Raw TCP

### Can I force Walter to connect to a specific network?

Yes, you can manually set the network using AT commands.
Example for Vodafone UK:

```console
AT+SQNMODEACTIVE=2
AT^RESET
AT+CGDCONT=1,"IP","soracom.io"
AT+CFUN=1
AT+CGATT=0
AT+COPS=1,2,"23415"
```

### Should I use MQTT or CoAP?

CoAP is recommended over MQTT for lower data usage
as it's UDP-based instead of TCP-based.
If you are using NB-IoT you should not use TCP-based protocols.
As this might sometimes work it is not guaranteed
and will give bad results when you scale up.

### What should I do if I get CME ERROR 4?

CME ERROR 4 typically indicates a network-related issue. Common solutions:

1. Check if you're in an area with good coverage
2. Verify your SIM card is properly provisioned
3. Consider using an external antenna in areas with poor reception
4. Implement automatic reconnection logic in your code
5. Avoid reconnecting more than 3-6 times per hour to prevent network rejection
