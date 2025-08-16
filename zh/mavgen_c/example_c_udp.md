# MAVLink C UDP 示例

The [MAVLink UDP Example](https://github.com/mavlink/mavlink/tree/master/examples/c) is a simple C example that sends and receives MAVLink HEARTBEATS over UDP.

:::info
The example should work on any Unix-like system (Linux, MacOS, BSD, etc.).
These instructions were tested on a _Ubuntu LTS 22.04_ installation with either PX4 or ArduPilot dependencies installed (such as cmake).
:::

## 构建/运行示例

下面的说明演示如何生成和运行该示例。

1. Clone the [mavlink/mavlink](https://github.com/mavlink/mavlink/) repository

2. Open a terminal in the repository root.

3. Use `cmake` to install MAVLink locally:

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

6. 从终端运行可执行文件：

   ```sh
   ./build/udp_example
   ```

   By default, the example will listen for data on the localhost IP address, port 14550.

7. Open another terminal on the same machine and start either PX4 or ArduPilot.
   These publish to port 14550 on localhost by default.

8. The example should start displaying messages about sent and received HEARTBEAT messages in the terminal.
   The following output is displayed if you connect to PX4:

   ```sh
   ~/github/mavlink/mavlink/examples/c$  ./build/udp_example

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

Note that the build and installation instructions are from [examples/c/README.md](https://github.com/mavlink/mavlink/blob/master/examples/c/README.md).
