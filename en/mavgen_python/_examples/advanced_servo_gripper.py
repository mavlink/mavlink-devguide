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
