# MAVLink C UDP 示例

The [MAVLink UDP Example](https://github.com/mavlink/mavlink/tree/master/examples/linux) is a simple C example that sends some data to *QGroundControl* using MAVLink over UDP. *QGroundControl* responds with heartbeats and other messages, which are then printed by this program. _QGroundControl_ responds with heartbeats and other messages, which are then printed by this program.

> **Note** The example should work on any Unix-like system (Linux, MacOS, BSD, etc.). These instructions were tested on a clean *Ubuntu LTS 20.04* installation using the default version of *gcc* (9.3.0). These instructions were tested on a clean _Ubuntu LTS 20.04_ installation using the default version of _gcc_ (9.3.0).

## 构建/运行示例

下面的说明演示如何生成和运行该示例。

1. [Install MAVLink](../getting_started/installation.md) and [generate](../getting_started/generate_libraries.md) the MAVLink 2.0 libraries into the **mavlink/include** directory. For example, to generate the headers for common.xml you could use the command line: For example, to generate the headers for common.xml you could use the command line:

   ```sh
   python3 -m pymavlink.tools.mavgen --lang=C --wire-protocol=2.0 --output=./include/ message_definitions/v1.0/common.xml
   ```

   > **Tip** Alternatively you can clone the [mavlink/mavlink](https://github.com/mavlink/mavlink/) repository and [Download prebuilt headers](../README.md#prebuilt_libraries) to the same location.

<span></span>

   > **Note** The example will not work with MAVLink 1 because it uses a message that includes extension fields which do not exist in MAVLink 1 (`SYS_STATUS`).
   
   <span></span>

   > **Note** You can put/generate the library wherever you like, but the build command below assumes they are located in directory named **include** below the MAVLink root directory.

1. 打开终端并导航到 [实例/linux](https://github.com/mavlink/mavlink/tree/master/examples/linux)
1. 使用下列命令编译GCC：

   ```sh
   gc -std=c99 -I./../包括/common-o mavlink_udp mavlink_udp.c
   ```

   > **Note** The MAVLink header directory must be added to the include path. **Note** The MAVLink header directory must be added to the include path. The path here assumes you are building the code from the example directory, and that have installed the headers in **mavlink/include**.

1. 从终端运行可执行文件：

   ```bash
   /mavlink_udp
   ```

   默认情况下，实例将接收本地主机IP地址，1451端口的数据。 By default, the example will listen for data on the localhost IP address, port 14551. You can specify another IP address as a command line argument (use `./mavlink_udp --help` to see usage).

1. Open *QGroundControl* on the same machine.

   *QGroundControl* immediately starts broadcasting its `HEARTBEAT` on port 14551.

   > **Note** *QGroundControl* returns data, but will not actually "connect" to the example (it will continue to display the message *Waiting for Vehicle Connection*).

1. 例子应该开始显示终端收到的数据：

   ```sh
   ~/github/mavlink/examples/linux$ ./mavlink_udp
   Bytes Received: 17
   Datagram: fe 09 00 ff 00 00 00 00 00 00 06 08 c0 04 03 19 87 
   Received packet: SYS: 255, COMP: 0, LEN: 9, MSG ID: 0

    Bytes Received: 17
   Datagram: fe 09 01 ff 00 00 00 00 00 00 06 08 c0 04 03 f3 f9 
   Received packet: SYS: 255, COMP: 0, LEN: 9, MSG ID: 0

   ...
   ```
