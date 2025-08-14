# MAVLink C UDP Example

The [MAVLink UDP Example](https://github.com/mavlink/mavlink/tree/master/examples/c) is a simple C example that sends some data to _QGroundControl_ using MAVLink over UDP.
_QGroundControl_ responds with heartbeats and other messages, which are then printed by this program.

::: info
The example should work on any Unix-like system (Linux, MacOS, BSD, etc.).
These instructions were tested on a clean _Ubuntu LTS 20.04_ installation using the default version of _gcc_ (9.3.0).
:::

## Building/Running the Example

The following instructions show how to build and run the example.

1. Clone the [mavlink/mavlink](https://github.com/mavlink/mavlink/) repository
2. Open a terminal in the repository root.
3. Use `cmake` to install MAVLink locally (these instructions are from [examples/c/README.md](https://github.com/mavlink/mavlink/blob/master/examples/c/README.md)):

   ```sh
   cmake -Bbuild -H. -DCMAKE_INSTALL_PREFIX=install
   cmake --build build --target install
   ```

4. Navigate to [examples/c](https://github.com/mavlink/mavlink/tree/master/examples/c)
   ```sh
   cd examples/c
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

7. Open _QGroundControl_ on the same machine.

   _QGroundControl_ immediately starts broadcasting its `HEARTBEAT` on port 14550.

   ::: info
   _QGroundControl_ returns data, but will not actually "connect" to the example (it will continue to display the message _Waiting for Vehicle Connection_).
   :::

8. The example should start displaying the received data in the terminal:

   ```sh
   Bytes Received: 17
   Datagram: fe 09 00 ff 00 00 00 00 00 00 06 08 c0 04 03 19 87
   Received packet: SYS: 255, COMP: 0, LEN: 9, MSG ID: 0

   Bytes Received: 17
   Datagram: fe 09 01 ff 00 00 00 00 00 00 06 08 c0 04 03 f3 f9
   Received packet: SYS: 255, COMP: 0, LEN: 9, MSG ID: 0

   ...
   ```
