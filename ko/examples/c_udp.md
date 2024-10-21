# MAVLink C UDP Example

The [MAVLink UDP Example](https://github.com/mavlink/mavlink/tree/master/examples/linux) is a simple C example that sends some data to *QGroundControl* using MAVLink over UDP. *QGroundControl* responds with heartbeats and other messages, which are then printed by this program.

> **Note** The example should work on any Unix-like system (Linux, MacOS, BSD, etc.). These instructions were tested on a clean *Ubuntu LTS 16.04* installation using the default version of *gcc* (5.4.0).

## Building/Running the Example

The following instructions show how to build and run the example.

1. [Install MAVLink](../getting_started/installation.md) and [generate](../getting_started/generate_libraries.md) the MAVLink 1.0 libraries into the **mavlink/include** directory.
    
    > **Tip** Alternatively you can clone the [mavlink/mavlink](https://github.com/mavlink/mavlink/) repository and [Download prebuilt headers](../index.md#prebuilt_libraries) to the same location. We recommend that you use MAVLink 1.0 headers as some ground control software may not yet support MAVLink 2.0.
    
    <span></span>
    
    > **Note** You can put/generate the library wherever you like, but the build command below assumes they are located in directory named **include** below the MAVLink root directory.

2. Open a terminal and navigate to [examples/linux](https://github.com/mavlink/mavlink/tree/master/examples/linux)

3. Compile with GCC using the following command:
    
    ```bash
    gcc -std=c99 -I ../../include/common -o mavlink_udp mavlink_udp.c
    ```
    
    > **Note** The MAVLink header directory must be added to the include path. The path here assumes you are building the code from the example directory, and that have installed the headers in **mavlink/include**.

4. Run the executable from the terminal:
    
    ```bash
    ./mavlink_udp
    ```
    
    By default, the example will listen for data on the localhost IP address, port 14551. You can specify another IP address as a command line argument (use `./mavlink_udp --help` to see usage).

5. Open *QGroundControl* on the same machine.
    
    *QGroundControl* immediately starts broadcasting its `HEARTBEAT` on port 14551.
    
    > **Note** *QGroundControl* returns data, but will not actually "connect" to the example (it will continue to display the message *Waiting for Vehicle Connection*).

6. The example should start displaying the received data in the terminal:
    
        ~/github/mavlink/examples/linux$ ./mavlink_udp
        Bytes Received: 17
        Datagram: fe 09 00 ff 00 00 00 00 00 00 06 08 c0 04 03 19 87 
        Received packet: SYS: 255, COMP: 0, LEN: 9, MSG ID: 0
        
        Bytes Received: 17
        Datagram: fe 09 01 ff 00 00 00 00 00 00 06 08 c0 04 03 f3 f9 
        Received packet: SYS: 255, COMP: 0, LEN: 9, MSG ID: 0
        
        ...