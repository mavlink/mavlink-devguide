# Using Generated Source Files

The generated MAVLink [dialect](../messages/README.md#dialects) libraries are used differently depending on the programming language. Language-specific details are given in each of the following sections.

> **Note** At time of writing we only have usage instructions for the [C source files](#c). If you have experience with the other [supported languages](../README.md#supported_languages) please help us update those sections!

## C {#c}

To use MAVLink, include the **mavlink.h** header file in your project:

```c
#include <mavlink/mavlink.h>
```

If headers for multiple dialects and/or versions are installed, your include path might instead look similar to the following:

```c
#include <mavlink/v2.0/common/mavlink.h>
```

> **Tip** *Do not include the individual message files.* If you generate your own headers, you will have to add their output location to your C compiler's search path. 

When compiling the project, we recommend that you specify the top-level output directory AND 
all generated dialects and versions (this will give the greatest compatibility with existing code and examples):
```sh
$ gcc ... -I generated/include -I generated/include/mavlink/v2.0/common ...
```


### Multiple streams, a.k.a. "channels"

The C MAVLink library utilizes a "channel" metaphor to allow for simultaneous processing of multiple, independent MAVLink streams in the same program. It is therefore important to use the correct channel for each operation as all receiving and transmitting functions provided by MAVLink require a channel. If only one MAVLink stream exists, channel 0 should be used by specifying the `MAVLINK_COMM_0` constant.

### Receiving

MAVLink reception is then done using `mavlink_helpers.h:mavlink_parse_char()`.

### Transmitting

Transmitting can be done by using the `mavlink_msg_*_pack()` function, where one is defined for every message. The packed message can then be serialized with `mavlink_helpers.h:mavlink_msg_to_send_buffer()` and then writing the resultant byte array out over the appropriate serial interface.

It is possible to simplify the above by writing wrappers around the transmitting/receiving code. A multi-byte writing macro can be defined, `MAVLINK_SEND_UART_BYTES()`, or a single-byte function can be defined, `comm_send_ch()`, that wrap the low-level driver for transmitting the data. If this is done, `MAVLINK_USE_CONVENIENCE_FUNCTIONS` must be defined.


## C++11

TBD

## C-Sharp

TBD

## Objective C

TBD

## Java

TBD

## JavaScript

TBD

## Lua

TBD

## Swift

TBD

## Python

TBD
