"""
Example: Linux computer connecting to an autopilot via a serial link 
"""

# Import mavutil
from pymavlink import mavutil

# Create the connection. Provide serial port and baudrate.
master = mavutil.mavlink_connection("/dev/ttyACM0", baud=115200)

# Restart the autopilot
master.reboot_autopilot()
