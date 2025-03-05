## Software Development

### Are there OTA (Over-The-Air) update options?

Yes, there are several options for OTA updates:

- Using BlueCherry's OTA system with CoAP + DTLS
- Using ESP-IDF's built-in OTA functionality
- Using Zephyr's OTA capabilities
- Custom implementation using CoAP or other protocols

### How do I get the current time?

After establishing an LTE connection,
you can get the network time using the modem's getClock() function:

```cpp
if(modem.getClock(&rsp)) {
    if(rsp.data.clock > 0) {
        // rsp.data.clock contains UTC timestamp
    }
}
```

### Is the WalterModem library thread-safe?

No, thread locking is not implemented in the library
and is left to the application level.

### Where can I find example code?

Examples can be found in:

- GitHub repository
  (<https://github.com/QuickSpot/walter-arduino/tree/main/examples>)
- QuickSpot documentation
  (<https://www.quickspot.io/documentation>)

### How do I enable debugging?

You can enable debug output in the Arduino IDE under Tools menu
by setting the debug level to 'DEBUG'.
This will show more detailed output including AT commands.
