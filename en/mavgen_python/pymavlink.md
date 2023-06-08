# Pymavlink

ArduSub communicates with a protocol called MAVLink. Pymavlink is a python implementation of the MAVLink protocol. With pymavlink, it is possible to create a python script to read sensor data and send commands to an ArduSub vehicle.

Please reference the pymavlink [documentation](https://mavlink.io/en/mavgen_python/), [repository](https://github.com/ArduPilot/pymavlink) and [chat](https://gitter.im/ArduPilot/pymavlink) for further information.

## Safety

The autopilot employs a some failsafe mechanisms to keep you and your equipement safe, as well as to prevent your ROV from running away from you during experiments.

All system components that communicate via MAVLink are expected to send a HEARTBEAT message at a constant rate of at least 1 Hz. If the autopilot does not receive a heartbeat from your application after this interval, it will trigger a [failsafe](/operators-manual/failsafes.html).

When the autopilot is being commanded to move via RC_CHANNELS_RAW or MANUAL_CONTROL messages, the messages must be sent at a constant rate like the HEARTBEAT message. Otherwise, the autopilot will execute a failsafe if it has not received an updated command after a timeout period.

## Installation

### Ubuntu 20.04

```sh
# Update list of available packages
sudo apt update
sudo apt -y upgrade

# Install some dependencies
sudo apt install -y python3-pip

# Install mavproxy module and everything else needed
pip3 install mavproxy
```

### Mac/Windows

With Python and pip installed, run `pip install wheel mavproxy`.

#### Test installation

You can test your installation with python interactive shell.

```bash
python
import pymavlink
print(pymavlink.__doc__)
```

Output:

```bash
Python MAVLink library - see http://www.qgroundcontrol.org/mavlink/mavproxy_startpage
```

Note that `pymavlink.__doc__` will show some information about the package.
This is a record of this example running in python interactive shell:

[![asciicast](https://asciinema.org/a/237333.svg)](https://asciinema.org/a/237333)


## Examples

Pymavlink has 3 types of messages:

* `command_long_send`: To create a raw package
* `<message_name>_send`: To send simple mavlink messages
* `mavutil`: Functions to abstract some MAVLink messages

### Connect

There are 3 types of udp connections for `mavlink_connection`:

- **udpout**: Outputs data to a specified `address:port` (client).
- **udpbcast**: Broadcasts and locks to the first client to respond (does not handle multiple clients properly)
    * Using the IP `192.168.1.255` all devices from  `192.168.1.1` to `192.168.1.255` will receive the data.
- **udpin**: Binds to a specific port in `address:port` (server).
  You must receive data from clients (**udpout**) before you can connect and send any data.
- **udp**: Don't use (deprecated alias for **udpin**).


### Connect to Autopilot from Linux Computer Serial Port

```py
"""
Example: Linux computer connecting to an autopilot via a serial link 
"""

# Import mavutil
from pymavlink import mavutil

# Create the connection. Provide serial port and baudrate.
master = mavutil.mavlink_connection("/dev/ttyACM0", baud=115200)

# Restart the autopilot
master.reboot_autopilot()
```

[File link](_examples/serial_connection.py)

### Connect to Autopilot via UDP

```py
"""
Example: Connect pymavlink to an autopilot via a UDP connection
"""

# Disable "Bare exception" warning
# pylint: disable=W0702

import time
from pymavlink import mavutil

# Create the connection
#  If using a companion computer the default connection is available 192.168.2.1:14550.
# Note: The connection is done with 'udpin' and not 'udpout'.
#  You can check in http:192.168.2.2:2770/mavproxy that the communication made for 14550
#  uses a 'udpbcast' (client) and not 'udpin' (server).
#  If you want to use QGroundControl in parallel with your python script,
#  it's possible to add a new output port in http:192.168.2.2:2770/mavproxy as a new line.
#  E.g: --out udpbcast:192.168.2.255:yourport
master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')

# Make sure the connection is valid
master.wait_heartbeat()

# Get some information !
while True:
    try:
        print(master.recv_match().to_dict())
    except:
        pass
    time.sleep(0.1)

# Output:
# {'mavpackettype': 'AHRS2', 'roll': -0.11364290863275528, 'pitch': -0.02841472253203392, 'yaw': 2.0993032455444336, 'altitude': 0.0, 'lat': 0, 'lng': 0}
# {'mavpackettype': 'AHRS3', 'roll': 0.025831475853919983, 'pitch': 0.006112074479460716, 'yaw': 2.1514968872070312, 'altitude': 0.0, 'lat': 0, 'lng': 0, 'v1': 0.0, 'v2': 0.0, 'v3': 0.0, 'v4': 0.0}
# {'mavpackettype': 'VFR_HUD', 'airspeed': 0.0, 'groundspeed': 0.0, 'heading': 123, 'throttle': 0, 'alt': 3.129999876022339, 'climb': 3.2699999809265137}
# {'mavpackettype': 'AHRS', 'omegaIx': 0.0014122836291790009, 'omegaIy': -0.022567369043827057, 'omegaIz': 0.02394154854118824, 'accel_weight': 0.0, 'renorm_val': 0.0, 'error_rp': 0.08894175291061401, 'error_yaw': 0.0990816056728363}
```

[File link](_examples/udp_connection.py)

### Run Pymavlink on the companion computer


```py
"""
Example of how to connect to the autopilot by using mavproxy's
--udpin:0.0.0.0:9000 endpoint from the companion computer itself
"""

# Disable "Bare exception" warning
# pylint: disable=W0702

import time
# Import mavutil
from pymavlink import mavutil

def wait_conn():
    """
    Sends a ping to stabilish the UDP communication and awaits for a response
    """
    msg = None
    while not msg:
        master.mav.ping_send(
            int(time.time() * 1e6), # Unix time in microseconds
            0, # Ping number
            0, # Request ping of all systems
            0 # Request ping of all components
        )
        msg = master.recv_match()
        time.sleep(0.5)

# Create the connection
#  Companion is already configured to allow script connections under the port 9000
# Note: The connection is done with 'udpout' and not 'udpin'.
#  You can check in http:192.168.1.2:2770/mavproxy that the communication made for 9000
#  uses a 'udp' (server) and not 'udpout' (client).
master = mavutil.mavlink_connection('udpout:0.0.0.0:9000')

# Send a ping to start connection and wait for any reply.
#  This function is necessary when using 'udpout',
#  as described before, 'udpout' connects to 'udpin',
#  and needs to send something to allow 'udpin' to start
#  sending data.
wait_conn()

# Get some information !
while True:
    try:
        print(master.recv_match().to_dict())
    except:
        pass
    time.sleep(0.1)

# Output:
# {'mavpackettype': 'AHRS2', 'roll': -0.11364290863275528, 'pitch': -0.02841472253203392, 'yaw': 2.0993032455444336, 'altitude': 0.0, 'lat': 0, 'lng': 0}
# {'mavpackettype': 'AHRS3', 'roll': 0.025831475853919983, 'pitch': 0.006112074479460716, 'yaw': 2.1514968872070312, 'altitude': 0.0, 'lat': 0, 'lng': 0, 'v1': 0.0, 'v2': 0.0, 'v3': 0.0, 'v4': 0.0}
# {'mavpackettype': 'VFR_HUD', 'airspeed': 0.0, 'groundspeed': 0.0, 'heading': 123, 'throttle': 0, 'alt': 3.129999876022339, 'climb': 3.2699999809265137}
# {'mavpackettype': 'AHRS', 'omegaIx': 0.0014122836291790009, 'omegaIy': -0.022567369043827057, 'omegaIz': 0.02394154854118824, 'accel_weight': 0.0, 'renorm_val': 0.0, 'error_rp': 0.08894175291061401, 'error_yaw': 0.0990816056728363}
```

[File link](_examples/companion_computer.py)


### Send Message to QGroundControl

```py
"""
Example of sending a message to QGroundControl using pymavlink

Full workflow of connecting and displaying readings from a custom sensor at:
  https://discuss.bluerobotics.com/t/adding-a-sensor-to-mavlink-stream/7985/22

"""

# Import mavutil
from pymavlink import mavutil

# Create the connection to the top-side computer as companion computer/autopilot
master = mavutil.mavlink_connection('udpout:localhost:14550', source_system=1)

# Send a message for QGC to read out loud
#  Severity from https://mavlink.io/en/messages/common.html#MAV_SEVERITY
master.mav.statustext_send(mavutil.mavlink.MAV_SEVERITY_NOTICE,
                           "QGC will read this".encode())
```

[include](_examples/message_qgc.py)

### Arm/Disarm the vehicle

[include](_examples/arm_disarm.py)

```py
"""
Example of how to Arm and Disarm an Autopilot with pymavlink
"""
# Import mavutil
from pymavlink import mavutil

# Create the connection
master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
# Wait a heartbeat before sending commands
master.wait_heartbeat()

# https://mavlink.io/en/messages/common.html#MAV_CMD_COMPONENT_ARM_DISARM

# Arm
# master.arducopter_arm() or:
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    1, 0, 0, 0, 0, 0, 0)

# wait until arming confirmed (can manually check with master.motors_armed())
print("Waiting for the vehicle to arm")
master.motors_armed_wait()
print('Armed!')

# Disarm
# master.arducopter_disarm() or:
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    0, 0, 0, 0, 0, 0, 0)

# wait until disarming confirmed
master.motors_disarmed_wait()
```


### Change flight mode

[include](_examples/change_flight_mode.py)

```py
"""
Example of how to change flight modes using pymavlink
"""

import sys
# Import mavutil
from pymavlink import mavutil

# Create the connection
master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
# Wait a heartbeat before sending commands
master.wait_heartbeat()

# Choose a mode
mode = 'STABILIZE'

# Check if mode is available
if mode not in master.mode_mapping():
    print('Unknown mode : {}'.format(mode))
    print('Try:', list(master.mode_mapping().keys()))
    sys.exit(1)

# Get mode ID
mode_id = master.mode_mapping()[mode]
# Set new mode
# master.mav.command_long_send(
#    master.target_system, master.target_component,
#    mavutil.mavlink.MAV_CMD_DO_SET_MODE, 0,
#    0, mode_id, 0, 0, 0, 0, 0) or:
# master.set_mode(mode_id) or:
master.mav.set_mode_send(
    master.target_system,
    mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
    mode_id)

while True:
    # Wait for ACK command
    # Would be good to add mechanism to avoid endlessly blocking
    # if the autopilot sends a NACK or never receives the message
    ack_msg = master.recv_match(type='COMMAND_ACK', blocking=True)
    ack_msg = ack_msg.to_dict()

    # Continue waiting if the acknowledged command is not `set_mode`
    if ack_msg['command'] != mavutil.mavlink.MAV_CMD_DO_SET_MODE:
        continue

    # Print the ACK result !
    print(mavutil.mavlink.enums['MAV_RESULT'][ack_msg['result']].description)
    break
```

### Send RC \(Joystick\)


```py
"""
Example of how to use RC_CHANNEL_OVERRIDE messages to force input channels
in Ardupilot. These effectively replace the input channels (from joystick
or radio), NOT the output channels going to thrusters and servos.
"""

# Import mavutil
from pymavlink import mavutil

# Create the connection
master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
# Wait a heartbeat before sending commands
master.wait_heartbeat()

# Create a function to send RC values
# More information about Joystick channels
# here: https://www.ardusub.com/operators-manual/rc-input-and-output.html#rc-inputs
def set_rc_channel_pwm(channel_id, pwm=1500):
    """ Set RC channel pwm value
    Args:
        channel_id (TYPE): Channel ID
        pwm (int, optional): Channel pwm value 1100-1900
    """
    if channel_id < 1 or channel_id > 18:
        print("Channel does not exist.")
        return

    # Mavlink 2 supports up to 18 channels:
    # https://mavlink.io/en/messages/common.html#RC_CHANNELS_OVERRIDE
    rc_channel_values = [65535 for _ in range(18)]
    rc_channel_values[channel_id - 1] = pwm
    master.mav.rc_channels_override_send(
        master.target_system,                # target_system
        master.target_component,             # target_component
        *rc_channel_values)                  # RC channel list, in microseconds.


# Set some roll
set_rc_channel_pwm(2, 1600)

# Set some yaw
set_rc_channel_pwm(4, 1600)

# The camera pwm value sets the servo speed of a sweep from the current angle to
#  the min/max camera angle. It does not set the servo position.
# Set camera tilt to 45º (max) with full speed
set_rc_channel_pwm(8, 1900)

# Set channel 12 to 1500us
# This can be used to control a device connected to a servo output by setting the
# SERVO[N]_Function to RCIN12 (Where N is one of the PWM outputs)
set_rc_channel_pwm(12, 1500)
```

[include](_examples/rc_joystick.py)


### Send Manual Control

```py
"""
Example of how to send MANUAL_CONTROL messages to the autopilot using
pymavlink.
This message is able to fully replace the joystick inputs.
"""

# Import mavutil
from pymavlink import mavutil

# Create the connection
master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
# Wait a heartbeat before sending commands
master.wait_heartbeat()

# Send a positive x value, negative y, negative z,
# positive rotation and no button.
# https://mavlink.io/en/messages/common.html#MANUAL_CONTROL
# Warning: Because of some legacy workaround, z will work between [0-1000]
# where 0 is full reverse, 500 is no output and 1000 is full throttle.
# x,y and r will be between [-1000 and 1000].
master.mav.manual_control_send(
    master.target_system,
    500,
    -500,
    250,
    500,
    0)

# To active button 0 (first button), 3 (fourth button) and 7 (eighth button)
# It's possible to check and configure this buttons in the Joystick menu of QGC
buttons = 1 + 1 << 3 + 1 << 7
master.mav.manual_control_send(
    master.target_system,
    0,
    0,
    500, # 500 means neutral throttle
    0,
    buttons)
```

[include](_examples/manual_control.py)


### Read all parameters

```py
"""
Example of how to read all the parameters from the Autopilot with pymavlink
"""

# Disable "Broad exception" warning
# pylint: disable=W0703

import time
import sys

# Import mavutil
from pymavlink import mavutil


# Create the connection
master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
# Wait a heartbeat before sending commands
master.wait_heartbeat()

# Request all parameters
master.mav.param_request_list_send(
    master.target_system, master.target_component
)
while True:
    time.sleep(0.01)
    try:
        message = master.recv_match(type='PARAM_VALUE', blocking=True).to_dict()
        print('name: %s\tvalue: %d' % (message['param_id'],
                                       message['param_value']))
    except Exception as error:
        print(error)
        sys.exit(0)
```

[include](_examples/read_params.py)

### Read and write parameters

```py
"""
Example code of how to read and write vehicle parameters using pymavlink
"""

import time
# Import mavutil
from pymavlink import mavutil

# Create the connection
master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
# Wait a heartbeat before sending commands
master.wait_heartbeat()

# Request parameter
master.mav.param_request_read_send(
    master.target_system, master.target_component,
    b'SURFACE_DEPTH',
    -1
)

# Print old parameter value
message = master.recv_match(type='PARAM_VALUE', blocking=True).to_dict()
print('name: %s\tvalue: %d' %
      (message['param_id'].decode("utf-8"), message['param_value']))

time.sleep(1)

# Set parameter value
# Set a parameter value TEMPORARILY to RAM. It will be reset to default on system reboot.
# Send the ACTION MAV_ACTION_STORAGE_WRITE to PERMANENTLY write the RAM contents to EEPROM.
# The parameter variable type is described by MAV_PARAM_TYPE in http://mavlink.org/messages/common.
master.mav.param_set_send(
    master.target_system, master.target_component,
    b'SURFACE_DEPTH',
    -12,
    mavutil.mavlink.MAV_PARAM_TYPE_REAL32
)

# Read ACK
# IMPORTANT: The receiving component should acknowledge the new parameter value by sending a
# param_value message to all communication partners.
# This will also ensure that multiple GCS all have an up-to-date list of all parameters.
# If the sending GCS did not receive a PARAM_VALUE message within its timeout time,
# it should re-send the PARAM_SET message.
message = master.recv_match(type='PARAM_VALUE', blocking=True).to_dict()
print('name: %s\tvalue: %d' %
      (message['param_id'].decode("utf-8"), message['param_value']))

time.sleep(1)

# Request parameter value to confirm
master.mav.param_request_read_send(
    master.target_system, master.target_component,
    b'SURFACE_DEPTH',
    -1
)

# Print new value in RAM
message = master.recv_match(type='PARAM_VALUE', blocking=True).to_dict()
print('name: %s\tvalue: %d' %
      (message['param_id'].decode("utf-8"), message['param_value']))
```

[include](_examples/read_write_params.py)

### Receive data and filter by message type

```py
"""
Example of how to filter for specific mavlink messages coming from the
autopilot using pymavlink.

Can also filter within recv_match command - see "Read all parameters" example
"""
# Import mavutil
from pymavlink import mavutil

# Create the connection
# From topside computer
master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')

while True:
    msg = master.recv_match()
    if not msg:
        continue
    if msg.get_type() == 'HEARTBEAT':
        print("\n\n*****Got message: %s*****" % msg.get_type())
        print("Message: %s" % msg)
        print("\nAs dictionary: %s" % msg.to_dict())
        # Armed = MAV_STATE_STANDBY (4), Disarmed = MAV_STATE_ACTIVE (3)
        print("\nSystem status: %s" % msg.system_status)
```

[include](_examples/filter_messages.py)

### Request message interval

```py
"""
Example of how to request a message in a desired interval
"""

# Disable "Bare exception" warning
# pylint: disable=W0702

import time
# Import mavutil
from pymavlink import mavutil

# Create the connection
master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
# Wait a heartbeat before sending commands
master.wait_heartbeat()

def request_message_interval(message_id: int, frequency_hz: float):
    """
    Request MAVLink message in a desired frequency,
    documentation for SET_MESSAGE_INTERVAL:
        https://mavlink.io/en/messages/common.html#MAV_CMD_SET_MESSAGE_INTERVAL

    Args:
        message_id (int): MAVLink message ID
        frequency_hz (float): Desired frequency in Hz
    """
    master.mav.command_long_send(
        master.target_system, master.target_component,
        mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL, 0,
        message_id, # The MAVLink message ID
        1e6 / frequency_hz, # The interval between two messages in microseconds. Set to -1 to disable and 0 to request default rate.
        0, 0, 0, 0, # Unused parameters
        0, # Target address of message stream (if message has target address fields). 0: Flight-stack default (recommended), 1: address of requestor, 2: broadcast.
    )

# Configure AHRS2 message to be sent at 1Hz
request_message_interval(mavutil.mavlink.MAVLINK_MSG_ID_AHRS2, 1)

# Configure ATTITUDE message to be sent at 2Hz
request_message_interval(mavutil.mavlink.MAVLINK_MSG_ID_ATTITUDE, 2)

# Get some information !
while True:
    try:
        print(master.recv_match().to_dict())
    except:
        pass
    time.sleep(0.1)
```

[include](_examples/request_message_interval.py)

### Control Camera Gimbal

<!-- Note, this is the old way! -->

```py
"""
Example of controlling a camera gimbal using pymavlink
"""

import time
# Import mavutil
from pymavlink import mavutil

# Create the connection
master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
# Wait a heartbeat before sending commands
master.wait_heartbeat()


def look_at(tilt, roll=0, pan=0):
    """
    Moves gimbal to given position
    Args:
        tilt (float): tilt angle in centidegrees (0 is forward)
        roll (float, optional): pan angle in centidegrees (0 is forward)
        pan  (float, optional): pan angle in centidegrees (0 is forward)
    """
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_DO_MOUNT_CONTROL,
        1,
        tilt,
        roll,
        pan,
        0, 0, 0,
        mavutil.mavlink.MAV_MOUNT_MODE_MAVLINK_TARGETING)


# cycles the camera up and down
while True:
    for angle in range(-50, 50):
        look_at(angle*100)
        time.sleep(0.1)
    for angle in range(-50, 50):
        look_at(-angle*100)
        time.sleep(0.1)
```

[include](_examples/camera_gimbal.py)

### Set Servo PWM

```py
"""
Example of how to directly control a Pixhawk servo output with pymavlink.
"""

import time
# Import mavutil
from pymavlink import mavutil

def set_servo_pwm(servo_n, microseconds):
    """ Sets AUX 'servo_n' output PWM pulse-width.

    Uses https://mavlink.io/en/messages/common.html#MAV_CMD_DO_SET_SERVO

    'servo_n' is the AUX port to set (assumes port is configured as a servo).
        Valid values are 1-3 in a normal BlueROV2 setup, but can go up to 8
        depending on Pixhawk type and firmware.
    'microseconds' is the PWM pulse-width to set the output to. Commonly
        between 1100 and 1900 microseconds.

    """
    # master.set_servo(servo_n+8, microseconds) or:
    master.mav.command_long_send(
        master.target_system, master.target_component,
        mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
        0,            # first transmission of this command
        servo_n + 8,  # servo instance, offset by 8 MAIN outputs
        microseconds, # PWM pulse-width
        0,0,0,0,0     # unused parameters
    )

# Create the connection
master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
# Wait a heartbeat before sending commands
master.wait_heartbeat()

# command servo_1 to go from min to max in steps of 50us, over 2 seconds
for us in range(1100, 1900, 50):
    set_servo_pwm(1, us)
    time.sleep(0.125)
```

[include](_examples/set_servo.py)

### Advanced Servo/Gripper Example

```py
"""
Advanced example of how to control servo outputs with pymavlink.
Includes extended example for controlling a Blue Robotics' gripper.

Requires Python 3.

"""

# Import mavutil
from pymavlink import mavutil

class RawServoOutput:
    """ A class for commanding a mavlink-controlled servo output port. """
    # https://mavlink.io/en/messages/common.html#MAV_CMD_DO_SET_SERVO
    CMD_SET = mavutil.mavlink.MAV_CMD_DO_SET_SERVO

    def __init__(self, master, instance, pwm_limits=(1100, 1500, 1900),
                 set_default=True):
        """ Initialise a RawServoOutput instance.

        'master' is a mavlink connection
        'instance' is the servo output (e.g. Pixhawk MAIN 1-8, AUX 9-16)
        'pwm_limits' is a tuple of min, default, and max pwm pulse-widths
            in microseconds (default (1100, 1500, 1900)).
        'set_default' is a boolean specifying whether to command the output
            to the specified default pulse-width (default True).

        """
        self.master     = master
        self.instance   = instance
        self.min_us, self._current, self.max_us = pwm_limits
        self._diff      = self.max_us - self.min_us

        if set_default:
            self.set_direct(self._current)

    def set_direct(self, us):
        """ Directly set the PWM pulse width.

        'us' is the PWM pulse width in microseconds.
            Must be between self.min_us and self.max_us.

        """
        assert self.min_us <= us <= self.max_us, "Invalid input value."

        # self.master.set_servo(self.instance, us) or:
        self.master.mav.command_long_send(
            self.master.target_system, self.master.target_component,
            self.CMD_SET,
            0, # first transmission of this command
            self.instance, us,
            0,0,0,0,0 # unused parameters
        )
        self._current = us

    def set_ratio(self, proportion):
        """ Set the PWM pulse-width ratio (auto-scale between min and max).

        'proportion' is a 0-1 value, where 0 corresponds to self.min_us, and
            1 corresponds to self.max_us.

        """
        self.set_direct(proportion * self._diff + self.min_us)

    def inc(self, us=50):
        """ Increment the PWM pulse width by 'us' microseconds. """
        self.set_direct(max(self.max_us, self._current+us))

    def dec(self, us=50):
        """ Decrement the PWM pulse width by 'us' microseconds. """
        self.set_direct(min(self.min_us, self._current-us))

    def set_min(self):
        """ Set the PWM to self.min_us. """
        self.set_ratio(0)

    def set_max(self):
        """ Set the PWM to self.max_us. """
        self.set_ratio(1)

    def center(self):
        """ Set the PWM to half-way between self.min_us and self.max_us. """
        self.set_ratio(0.5)


class AuxServoOutput(RawServoOutput):
    """ A class representing a mavlink-controlled auxiliary servo output. """
    def __init__(self, master, servo_n, main_outputs=8, **kwargs):
        """ Initiliase a servo instance.

        'master' is a mavlink connection.
        'servo_n' is one of the auxiliary servo outputs, like the servo_n
            outputs with QGroundControl joystick control.
            Most likely a value between 1-3, but possibly up to 6 or 8
            depending on setup.
        'main_outputs' is the number of MAIN outputs are present on the
            autopilot device (default 8).
        **kwargs are passed to RawServoOutput.

        """
        super().__init__(master, servo_n+main_outputs, **kwargs)
        self._main_outputs = main_outputs

    @property
    def servo_n(self):
        """ Return the AUX servo number of this output. """
        return self.instance - self._main_outputs


class Gripper(AuxServoOutput):
    """ A class representing a Blue Robotics' gripper. """
    def __init__(self, master, servo_n, pwm_limits=(1100, 1100, 1500),
                 **kwargs):
        """ Initialise a Gripper instance.

        'master' is a mavlink connection.
        'servo_n' is one of the auxiliary servo outputs, like the servo_n
            outputs with QGroundControl joystick control.
            Most likely a value between 1-3, but possibly up to 6 or 8
            depending on setup.
        'pwm_limits' is a tuple of min, default, and max pwm pulse-widths
            in microseconds (default (1100, 1100, 1900)).
        **kwargs are passed to AuxServoOutput.

        """
        super().__init__(master, servo_n, pwm_limits=pwm_limits, **kwargs)

    def open(self):
        """ Command the gripper to open. """
        self.set_max()

    def close(self):
        """ Command the gripper to close. """
        self.set_min()


# if running this file as a script:
if __name__ == '__main__':
    from time import sleep

    # Connect to the autopilot (pixhawk) from the surface computer,
    #  via the companion.
    autopilot = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
    # Wait for a heartbeat from the autopilot before sending commands
    autopilot.wait_heartbeat()

    # create a gripper instance on servo_1 (AUX output 1)
    gripper = Gripper(autopilot, 1)

    # open and close the gripper a few times
    for _ in range(3):
        gripper.open()
        sleep(2)
        gripper.close()
        sleep(1)
```

[include](_examples/advanced_servo_gripper.py)

### Set Target Depth/Attitude

```py
"""
Example of how to set target depth in depth hold mode with pymavlink
"""

import time
import math
# Import mavutil
from pymavlink import mavutil
# Imports for attitude
from pymavlink.quaternion import QuaternionBase

def set_target_depth(depth):
    """ Sets the target depth while in depth-hold mode.

    Uses https://mavlink.io/en/messages/common.html#SET_POSITION_TARGET_GLOBAL_INT

    'depth' is technically an altitude, so set as negative meters below the surface
        -> set_target_depth(-1.5) # sets target to 1.5m below the water surface.

    """
    master.mav.set_position_target_global_int_send(
        int(1e3 * (time.time() - boot_time)), # ms since boot
        master.target_system, master.target_component,
        coordinate_frame=mavutil.mavlink.MAV_FRAME_GLOBAL_INT,
        type_mask=( # ignore everything except z position
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_X_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_Y_IGNORE |
            # DON'T mavutil.mavlink.POSITION_TARGET_TYPEMASK_Z_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_VX_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_VY_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_VZ_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_AX_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_AY_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_AZ_IGNORE |
            # DON'T mavutil.mavlink.POSITION_TARGET_TYPEMASK_FORCE_SET |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_YAW_IGNORE |
            mavutil.mavlink.POSITION_TARGET_TYPEMASK_YAW_RATE_IGNORE
        ), lat_int=0, lon_int=0, alt=depth, # (x, y WGS84 frame pos - not used), z [m]
        vx=0, vy=0, vz=0, # velocities in NED frame [m/s] (not used)
        afx=0, afy=0, afz=0, yaw=0, yaw_rate=0
        # accelerations in NED frame [N], yaw, yaw_rate
        #  (all not supported yet, ignored in GCS Mavlink)
    )

def set_target_attitude(roll, pitch, yaw):
    """ Sets the target attitude while in depth-hold mode.

    'roll', 'pitch', and 'yaw' are angles in degrees.

    """
    master.mav.set_attitude_target_send(
        int(1e3 * (time.time() - boot_time)), # ms since boot
        master.target_system, master.target_component,
        # allow throttle to be controlled by depth_hold mode
        mavutil.mavlink.ATTITUDE_TARGET_TYPEMASK_THROTTLE_IGNORE,
        # -> attitude quaternion (w, x, y, z | zero-rotation is 1, 0, 0, 0)
        QuaternionBase([math.radians(angle) for angle in (roll, pitch, yaw)]),
        0, 0, 0, 0 # roll rate, pitch rate, yaw rate, thrust
    )

# Create the connection
master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
boot_time = time.time()
# Wait a heartbeat before sending commands
master.wait_heartbeat()

# arm ArduSub autopilot and wait until confirmed
master.arducopter_arm()
master.motors_armed_wait()

# set the desired operating mode
DEPTH_HOLD = 'ALT_HOLD'
DEPTH_HOLD_MODE = master.mode_mapping()[DEPTH_HOLD]
while not master.wait_heartbeat().custom_mode == DEPTH_HOLD_MODE:
    master.set_mode(DEPTH_HOLD)

# set a depth target
set_target_depth(-0.5)

# go for a spin
# (set target yaw from 0 to 500 degrees in steps of 10, one update per second)
roll_angle = pitch_angle = 0
for yaw_angle in range(0, 500, 10):
    set_target_attitude(roll_angle, pitch_angle, yaw_angle)
    time.sleep(1) # wait for a second

# spin the other way with 3x larger steps
for yaw_angle in range(500, 0, -30):
    set_target_attitude(roll_angle, pitch_angle, yaw_angle)
    time.sleep(1)

# clean up (disarm) at the end
master.arducopter_disarm()
master.motors_disarmed_wait()
```

[include](_examples/set_target_depth_attitude.py)

### Send GPS position

```py
"""
Example of how to send GPS_INPUT messages to autopilot
"""

import time
# Import mavutil
from pymavlink import mavutil

# Create the connection
master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
# Wait a heartbeat before sending commands
master.wait_heartbeat()

# GPS_TYPE need to be MAV
while True:
    time.sleep(0.2)
    master.mav.gps_input_send(
        0,  # Timestamp (micros since boot or Unix epoch)
        0,  # ID of the GPS for multiple GPS inputs
        # Flags indicating which fields to ignore (see GPS_INPUT_IGNORE_FLAGS enum).
        # All other fields must be provided.
        (mavutil.mavlink.GPS_INPUT_IGNORE_FLAG_VEL_HORIZ |
         mavutil.mavlink.GPS_INPUT_IGNORE_FLAG_VEL_VERT |
         mavutil.mavlink.GPS_INPUT_IGNORE_FLAG_SPEED_ACCURACY),
        0,  # GPS time (milliseconds from start of GPS week)
        0,  # GPS week number
        3,  # 0-1: no fix, 2: 2D fix, 3: 3D fix. 4: 3D with DGPS. 5: 3D with RTK
        0,  # Latitude (WGS84), in degrees * 1E7
        0,  # Longitude (WGS84), in degrees * 1E7
        0,  # Altitude (AMSL, not WGS84), in m (positive for up)
        1,  # GPS HDOP horizontal dilution of position in m
        1,  # GPS VDOP vertical dilution of position in m
        0,  # GPS velocity in m/s in NORTH direction in earth-fixed NED frame
        0,  # GPS velocity in m/s in EAST direction in earth-fixed NED frame
        0,  # GPS velocity in m/s in DOWN direction in earth-fixed NED frame
        0,  # GPS speed accuracy in m/s
        0,  # GPS horizontal accuracy in m
        0,  # GPS vertical accuracy in m
        7   # Number of satellites visible.
    )
```

[include](_examples/send_gps.py)

### Send rangefinder/computer vision distance measurement to the autopilot

```py
"""
Example of how to send MAV_DISTANCE_SENSOR messages to integrate a custom distance sensor
to the autopilot using pymavlink
"""

import time

# Import mavutil
from pymavlink import mavutil

# Wait for server connection
def wait_conn():
    """
    Sends a ping to the autopilot to stabilish the UDP connection and waits for a reply
    """
    msg = None
    while not msg:
        master.mav.ping_send(
            int(time.time() * 1e6), # Unix time in microseconds
            0, # Ping number
            0, # Request ping of all systems
            0 # Request ping of all components
        )
        msg = master.recv_match()
        time.sleep(0.5)

# Connect to the default listening port for
# mavproxy on Blue Robotics companion computer
master = mavutil.mavlink_connection('udpout:localhost:9000')

# Send a ping to start connection and wait for any reply.
wait_conn()

# Configure the autopilot to use mavlink rangefinder, the autopilot
# will need to be rebooted after this to use the updated setting
master.mav.param_set_send(
    1,
    1,
    b"RNGFND_TYPE",
    10, # "MAVLink"
    mavutil.mavlink.MAV_PARAM_TYPE_INT8)

min_measurement = 10 # minimum valid measurement that the autopilot should use
max_measurement = 40 # maximum valid measurement that the autopilot should use
distance = 20 # You will need to supply the distance measurement
sensor_type = mavutil.mavlink.MAV_DISTANCE_SENSOR_UNKNOWN
sensor_id = 1
orientation = mavutil.mavlink.MAV_SENSOR_ROTATION_PITCH_270 # downward facing
covariance = 0

tstart = time.time()
while True:
    time.sleep(0.5)
    master.mav.distance_sensor_send(
        int((time.time() - tstart) * 1000),
        min_measurement,
        max_measurement,
        distance,
        sensor_type,
        sensor_id,
        orientation,
        covariance)
```

[include](_examples/send_rangefinder_vision.py)
