# HTTP
## methods overview

- [httpConfigProfile](#httpconfigprofile)
- [httpSend](#httpsend)
- [httpQuery]()
- [httpDidRing]()

## enums overview

## methods
---
### `httpConfigProfile`
> Configure a HTTP profile.
>
> This function will configure a HTTP profile with parameters such as server name and auth info. \
> The profile info is stored persistently in the modem, so it is possible to store connection info once, using an Arduino sketch to prepare all settings, and later rely on this preconfigured profile in the modem without the need to set the parameters again in the actual Arduino sketch used in production.

> [!WARNING]
> you first need call [tlsConfigProfile](). 

> [!NOTE]
> **file uploads/downloads** not supported.

<!-- tabs:start -->
#### **Arduino**
```cpp
/**
 * @brief HTTP profile
 */
#define HTTP_PROFILE 1

/**
 * @brief TLS profile
 */
#define TLS_PROFILE 1

if(modem.httpConfigProfile(HTTP_PROFILE, "tls13.akamai.io", 443, TLS_PROFILE)) {
    Serial.println("http: Successfully configured the http profile");
} else {
    Serial.print("http: Failed to configure HTTP profile\r\n");
}
```
#### **ESP-IDF**
```cpp
/**
 * @brief HTTP profile
 */
#define HTTP_PROFILE 1

/**
 * @brief TLS profile
 */
#define TLS_PROFILE 1

if(modem.httpConfigProfile(HTTP_PROFILE, "tls13.akamai.io", 443, TLS_PROFILE)) {
    ESP_LOGI("http", "Successfully configured the HTTP profile");
} else {
    ESP_LOGE("http", "Failed to configure HTTP profile");
}
```
#### **Micropython**
<!-- tabs:end -->

### params:
<!-- tabs:start -->
#### **Arduino / ESP-IDF**
| Param          | Description                                                                                                           | Default   |
| -------------- | --------------------------------------------------------------------------------------------------------------------- | --------- |
| `profileId`    | HTTP profile id (0, 1 or 2)                                                                                           | **None**  |
| `serverName`   | The server name to connect to.                                                                                        | **None**  |
| `port`         | The port of the server to connect to.                                                                                 | **80**    |
| `tlsProfileId` | If not 0, TLS is used with the given profile (1-6).                                                                   | **0**     |
| `useBasicAuth` | Set true to use basic auth and send username/pw.                                                                      | **false** |
| `authUser`     | Username.                                                                                                             | **""**    |
| `authPass`     | Password.                                                                                                             | **""**    |
| `rsp`          | Pointer to a modem response structure to save the result of the command in. When NULL is given the result is ignored. | **NULL**  |
| `cb`           | Optional callback argument, when not NULL this function will return immediately.                                      | **NULL**  |
| `args`         | Optional argument to pass to the callback.                                                                            | **NULL**  |

#### **Micropython**

<!-- tabs:end -->

### Returns:
`bool`
True on success, false otherwise.

---

### `httpSend`
> Perform a http post or put request.
>
> No need to first open the connection with the buggy httpConnect command unless you need TLS + a private key.

<!-- tabs:start -->


<!-- tabs:end -->
