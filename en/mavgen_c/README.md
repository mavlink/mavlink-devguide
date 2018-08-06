# Using C MAVLink Libraries (mavgen)

The MAVLink C library is a header-only implementation that is highly optimized for resource-constrained systems with limited RAM and flash memory. 
It is field-proven and deployed in many products where it serves as interoperability interface between components of different manufacturers.

This topic explains how to get and use the library.

## Getting Libraries

If you are using a [standard dialect](../messages/README.md#dialects) then download the *MAVLink 2* library from Github: [c_library_v2](https://github.com/mavlink/c_library_v2).

> **Tip** The MAVLink 2 library supports both MAVLink 2 and MAVLink 1, and has been built with all [standard dialects](../messages/README.md#dialects) in the *mavlink/mavlink* repo.
  It supersedes the MAVLink 1 library ([c_library_v1](https://github.com/mavlink/c_library_v1)), and should be used by preference. 

If you need libraries for a custom dialect then you will need to [install mavgen](../getting_started/installation.md) and [generate](../getting_started/generate_libraries.md) them yourself. These can then be used in the same way as the pre-generated libraries.

The libraries can be placed/generated anywhere in your project tree. 
The example below shows them located in: **generated/include/mavlink/v2.0/**.


## Adding Libraries 

To use MAVLink in your C project, include the **mavlink.h** header file in your project:

```c
#include <mavlink/mavlink.h>
```

If headers for multiple dialects and/or versions are installed, your include path might instead look similar to the following:

```c
#include <mavlink/v2.0/common/mavlink.h>
```

> **Tip** *Do not include the individual message files*. 
  If you generate your own headers, you will have to add their output location to your C compiler's search path. 

When compiling the project, we recommend that you specify the top-level output directory AND 
all generated dialects and versions (this will give the greatest compatibility with existing code and examples):
```sh
$ gcc ... -I generated/include -I generated/include/mavlink/v2.0/common ...
```

## Multiple Streams ("channels") {#streams}

The C MAVLink library utilizes a "channel" metaphor to allow for simultaneous processing of multiple, independent MAVLink streams in the same program. 
It is therefore important to use the correct channel for each operation as all receiving and transmitting functions provided by MAVLink require a channel. 
If only one MAVLink stream exists, channel 0 should be used by specifying the `MAVLINK_COMM_0` constant.

## Receiving

MAVLink reception is then done using `mavlink_helpers.h:mavlink_parse_char()`.

## Transmitting

Transmitting messages can be done by using the `mavlink_msg_*_pack()` function, where one is defined for every message. 
The packed message can then be serialized with `mavlink_helpers.h:mavlink_msg_to_send_buffer()` and then writing the resultant byte array out over the appropriate serial interface.

It is possible to simplify the above by writing wrappers around the transmitting/receiving code. 
A multi-byte writing macro can be defined, `MAVLINK_SEND_UART_BYTES()`, or a single-byte function can be defined, `comm_send_ch()`, 
that wrap the low-level driver for transmitting the data. 
If this is done, `MAVLINK_USE_CONVENIENCE_FUNCTIONS` must be defined.
