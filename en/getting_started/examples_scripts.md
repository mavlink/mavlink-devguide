# Scripts/Examples

## MAVLink C-UART Interface Example

The [C-UART Interface Example](https://github.com/mavlink/c_uart_interface_example) is a simple C example of a MAVLink to UART interface for Unix-like systems.

The example source code demonstrates how to set up serial communication between Pixhawk and an offboard computer via USB or a telemetry radio, how to put the vehicle in offboard mode, and how to send and receive MAVLink messages over the interface.

Source code and instructions for how to run the example can be found in the Github repo: [mavlink/c_uart_interface_example](https://github.com/mavlink/c_uart_interface_example)


## MAVLink UDP Example

The [MAVLink UDP Example](https://github.com/mavlink/mavlink/tree/master/examples/linux) is a simple C example of a MAVLink UDP interface for Unix-like systems.

The example sends some data to *QGroundControl* using MAVLink over UDP. *QGroundControl* responds with heartbeats and other messages, which are then printed by this program. 

Source code and instructions for how to run the example can be found in the Github repo here: [mavlink/mavlink/examples/linux](https://github.com/mavlink/mavlink/tree/master/examples/linux)


## Pymavlink Scripts

This MAVLink library also comes with supporting libraries and scripts for using, manipulating, and parsing MAVLink streams within the [pymavlink](https://github.com/mavlink/pymavlink/), **pymavlink/tools**, and **pymavlink/examples** directories.

The scripts have the following requirements:
* Python 2.7+ and 3.3+
* `PYTHONPATH` specifies the directory path that contains the `mavlink` repository.
* Write access to the entire **mavlink** folder.
* Your [dialect](../messages/README.md#dialects)'s XML file is in `message_definitions/*/`

The scripts can be executed by running Python with the `-m` switch, which indicates that the given script exists on the `PYTHONPATH`. The following code runs **mavlogdump.py** in **/pymavlink/tools/** on the recorded MAVLink stream `test_run.mavlink` (other scripts in **/tools** and **/scripts** can be run in a similar fashion):

```
python -m pymavlink.tools.mavlogdump test_run.mavlink
```

> **Note** Using the `-m` switch is the proper way to run Python scripts that are part of a library as per PEP-328 (and the rejected PEP-3122). 

