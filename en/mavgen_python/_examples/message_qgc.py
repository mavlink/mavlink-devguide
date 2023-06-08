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
