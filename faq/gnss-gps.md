## GNSS/GPS

### Which GNSS antenna should I use?

The recommended antenna is the passive Taoglas FXP.611.
Active antennas are not supported by the board.

### How sensitive is the built-in GNSS?

The Walter board's GNSS sensitivity varies by start condition:

- Cold start *(no valid assistance)*: -146dBm
- Warm start *(valid assistance, no position)*: -150.5dBm
- Hot start *(valid assistance, position within 100km)*: -153.3dBm

### Why can't I get a GNSS fix indoors?

GNSS is not suited for indoor positioning, even with dedicated modules.
While you might get a signal indoors,
it will likely be noisy with degraded accuracy.
Indoor reception is limited due to:

- Building materials blocking signals
- Window coatings (especially silver/metallic) interfering with reception
- Lower sensitivity compared to dedicated GNSS modules

For indoor applications, consider alternative positioning technologies such as
Bluetooth beacons or WiFi scanning. Both are supported by Walter.
