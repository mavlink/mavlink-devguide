# MAVLink C Library #defines

The following C `#defines` can be set in code in order to tune the setup for use on different platforms.

- `MAVLINK_USE_CONVENIENCE_FUNCTIONS` ([protocol.h](https://github.com/ArduPilot/pymavlink/blob/master/generator/C/include_v2.0/protocol.h)): Causes convenience functions to be defined, including: `_mav_finalize_message_chan_send()`, `_mavlink_send_uart()`, `_mavlink_resend_uart()`. To use, add `#define MAVLINK_USE_CONVENIENCE_FUNCTIONS` to your code.
- `MAVLINK_COMM_NUM_BUFFERS`: Sets the maximum number of comms buffers to be used (comms channels).
  By default this is set to 16 on Linux, Windows and macOS, and to 4 on other platforms.
  You might set `#define MAVLINK_COMM_NUM_BUFFERS 2` on an embedded system that would only ever have two channels, in order to reduce memory overheads.
  A stack overrun will occur if there are more buffers used than allocated.
  See [FAQ > How can I further reduce the generated C library size?](../about/faq.md#developers).
- `MAVLINK_SIGNING_FLAG_SIGN_OUTGOING` ([mavlink_types.h](https://github.com/ArduPilot/pymavlink/blob/master/generator/C/include_v2.0/mavlink_types.h)): Enable/disable outgoing signing.
  See [Enabling Signing on a Channel > Enabling Signing on a Channel](../mavgen_c/message_signing_c.md#enabling_signing_channel)
- `MAVLINK_EXTERNAL_RX_STATUS` ([mavlink_helpers.h](https://github.com/ArduPilot/pymavlink/blob/master/generator/C/include_v2.0/mavlink_helpers.h)): `mavlink_status_t* mavlink_get_channel_status(uint8_t chan)` returns the status of a particular channel using a preallocated `static` array.
  Define `MAVLINK_EXTERNAL_RX_STATUS` if you want to use your own external array (named `m_mavlink_status`) of `mavlink_status_t` objects.
- `MAVLINK_EXTERNAL_RX_BUFFER` ([mavlink_helpers.h](https://github.com/ArduPilot/pymavlink/blob/master/generator/C/include_v2.0/mavlink_helpers.h)): Set if you want to define your own channel comms buffers on the stack or heap, rather than using the pre-allocated `static` buffers.
  If you define this you will need to declare an array of `mavlink_message_t` (one for each channel) named `m_mavlink_buffer`.
- `NATIVE_BIG_ENDIAN` ([protocol.h](https://github.com/ArduPilot/pymavlink/blob/master/generator/C/include_v2.0/protocol.h)): Enable if using MAVLink on a system that is native big-endian (MAVLINK_LITTLE_ENDIAN is true by default).
- `MAVLINK_SEPARATE_HELPERS` ([protocol.h](https://github.com/ArduPilot/pymavlink/blob/master/generator/C/include_v2.0/protocol.h)): Set to remove all the helpers declared `mavlink_helpers.h`, allowing you to provide an alternative implementation.
- `MAVLINK_MAX_PAYLOAD_LEN`: Override the maximum payload length.
  The default maximum payload length is 255 bytes. With care you can override this to reduce memory usage.
  For example, to reduce the maximum payload to the smallest size supported by a dialect you could do:
  
  ```c
  #include <version.h>
  #define MAVLINK_MAX_PAYLOAD_LEN MAVLINK_MAX_DIALECT_PAYLOAD_SIZE
  ```

  See also [FAQ > How can I further reduce the generated C library size?](../about/faq.md#developers).


There are a number of other internal defines that should not be modified.
