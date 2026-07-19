# MAVLink C++ UDP Example

The [MAVLink C++ UDP Example](https://github.com/mavlink/mavlink/tree/master/examples/cpp) is a simple C++ 11 example that sends and receives MAVLink HEARTBEATs over UDP.

It is the C++ 11 counterpart to the [C UDP example](../mavgen_c/example_c_udp.md): instead of the C pack/decode functions, it uses the generated message structs (e.g. `mavlink::minimal::msg::HEARTBEAT`) together with `mavlink::MsgMap` to serialize and deserialize to and from a `mavlink_message_t`.

:::info
The example should work on any Unix-like system (Linux, MacOS, BSD, etc.).
These instructions were tested on a _Ubuntu LTS 22.04_ installation with either PX4 or ArduPilot dependencies installed (such as cmake).
:::

:::warning
The C++ 11 library requires you to provide a `mavlink::mavlink_get_msg_entry()` function so that `mavlink_parse_char()` can look up the length and CRC extra of incoming messages.
This example builds it from the dialect's `MESSAGE_ENTRIES` table (see the top of `udp_example.cpp`, and the [Parsing Packets](index.md#parsing-packets) section for more detail).
:::

## Building/Running the Example

The following instructions show how to build and run the example.

1. Clone the [mavlink/mavlink](https://github.com/mavlink/mavlink/) repository

2. Open a terminal in the repository root.

3. Use `cmake` to install MAVLink locally:

   ```sh
   cmake -Bbuild -H. -DCMAKE_INSTALL_PREFIX=install
   cmake --build build --target install
   ```

   This installs both the C (`*.h`) and C++ 11 (`*.hpp`) headers.

4. Navigate to [examples/cpp](https://github.com/mavlink/mavlink/tree/master/examples/cpp)

   ```sh
   cd examples/cpp
   ```

5. Use `cmake` to compile and build the example:

   ```sh
   cmake -Bbuild -H. -DCMAKE_PREFIX_PATH=$(pwd)/../../install
   cmake --build build
   ```

6. Run the executable from the terminal:

   ```sh
   ./build/udp_example
   ```

   By default, the example will listen for data on the localhost IP address, port 14550.

7. Open another terminal on the same machine and start either PX4 or ArduPilot.
   These publish to port 14550 on localhost by default.

8. The example should start displaying messages about sent and received HEARTBEAT messages in the terminal.
   The following output is displayed if you connect to PX4:

   ```sh
   ~/github/mavlink/mavlink/examples/cpp$  ./build/udp_example

   Sent heartbeat
   Got heartbeat from PX4 autopilot
   Sent heartbeat
   Got heartbeat from PX4 autopilot
   Sent heartbeat
   Got heartbeat from PX4 autopilot
   Sent heartbeat
   Got heartbeat from PX4 autopilot
   Sent heartbeat
   Got heartbeat from PX4 autopilot
   ...
   ```

Note that the build and installation instructions are from [examples/cpp/README.md](https://github.com/mavlink/mavlink/blob/master/examples/cpp/README.md).
