import os
import time
import unittest

from pymavlink import mavutil

""" Helper functions """


class MavlinkUDPConnection:
    def __init__(self):
        os.environ["MAVLINK20"] = "1"
        os.environ["MAVLINK_DIALECT"] = "common"
        self.udpin = mavutil.mavlink_connection("udpin:localhost:14541", dialect="common")
        self.udpout = mavutil.mavlink_connection("udpout:localhost:14540", dialect="common")

    def close(self):
        self.udpin.close()
        self.udpout.close()


def set_illuminator_status_stream(interval, mavlink_connection, timeout):
    message = mavlink_connection.udpout.mav.command_long_encode(
        mavlink_connection.udpout.target_system,  # Target System
        mavlink_connection.udpout.target_component,  # Target Component
        mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL,  # Command
        0,  # Confirmation
        mavutil.mavlink.MAVLINK_MSG_ID_ILLUMINATOR_STATUS,  # param1: Message ID
        interval,  # param2: Interval - default
        0,  # param3 (unused)
        0,  # param4 (unused)
        0,  # param5 (unused)
        0,  # param6 (unused)
        0,  # param7: Response Target - flight-stack default
    )
    mavlink_connection.udpout.mav.send(message)
    response_ack = mavlink_connection.udpin.recv_match(
        type="COMMAND_ACK", blocking=True, timeout=timeout
    )
    if not response_ack:
        raise Exception("Failed to receive COMMAND_ACK message")
    response_status = mavlink_connection.udpin.recv_match(
        type="ILLUMINATOR_STATUS", blocking=True, timeout=timeout
    )
    if interval == -1 and response_status is not None:
        raise Exception("Failed to disable ILLUMINATOR_STATUS message stream")
    elif interval != -1 and response_status is None:
        raise Exception("Failed to enable ILLUMINATOR_STATUS message stream")


def turn_illuminator_on_off(enable, mavlink_connection, timeout):
    message = mavlink_connection.udpout.mav.command_long_encode(
        mavlink_connection.udpout.target_system,  # Target System
        mavlink_connection.udpout.target_component,  # Target Component
        mavutil.mavlink.MAV_CMD_ILLUMINATOR_ON_OFF,  # Command
        0,  # Confirmation
        enable,  # param1: Enable
        0,  # param2 (unused)
        0,  # param3 (unused)
        0,  # param4 (unused)
        0,  # param5 (unused)
        0,  # param6 (unused)
        0,  # param7 (unused)
    )
    mavlink_connection.udpout.mav.send(message)
    response_ack = mavlink_connection.udpin.recv_match(
        type="COMMAND_ACK", blocking=True, timeout=timeout
    )
    if not response_ack:
        raise Exception("Failed to receive COMMAND_ACK message")
    response_status = mavlink_connection.udpin.recv_match(
        type="ILLUMINATOR_STATUS", blocking=True, timeout=timeout
    )
    if not response_status:
        raise Exception("Failed to receive ILLUMINATOR_STATUS message")
    if response_status.enable != enable:
        print(response_status)
        raise Exception("Failed to turn illuminator {}".format("ON" if enable else "OFF"))


def configure_illuminator(
    mode, brightness, strobe_period, strobe_duty_cycle, mavlink_connection, timeout
):
    message = mavlink_connection.udpout.mav.command_long_encode(
        mavlink_connection.udpout.target_system,  # Target System
        mavlink_connection.udpout.target_component,  # Target Component
        mavutil.mavlink.MAV_CMD_DO_ILLUMINATOR_CONFIGURE,  # Command
        0,  # Confirmation
        mode,  # param1: Mode
        brightness,  # param2: Brightness
        strobe_period,  # param3: Strobe Period
        strobe_duty_cycle,  # param4: Strobe Duty Cycle
        0,  # param5 (unused)
        0,  # param6 (unused)
        0,  # param7 (unused)
    )
    mavlink_connection.udpout.mav.send(message)
    response_ack = mavlink_connection.udpin.recv_match(
        type="COMMAND_ACK", blocking=True, timeout=timeout
    )
    if not response_ack:
        raise Exception("Failed to receive COMMAND_ACK message")
    response_status = mavlink_connection.udpin.recv_match(
        type="ILLUMINATOR_STATUS", blocking=True, timeout=timeout
    )
    if (
        not response_status
        or response_status.mode != mode
        or response_status.brightness != brightness
        or response_status.strobe_period != strobe_period
        or response_status.strobe_duty_cycle != strobe_duty_cycle
    ):
        raise Exception(
            "Failed to configure illuminator to mode={}, brightness={}, strobe_period={}, strobe_duty_cycle={}".format(
                mode, brightness, strobe_period, strobe_duty_cycle
            )
        )


""" Test Cases """


# @unittest.skip("reason for skipping ILLUMINATOR_STATUS")
class MavlinkIlluminatorStatusTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.illuminator_connection = MavlinkUDPConnection()
        cls.ack_timeout = 3
        cls.status_timeout = 5

    @classmethod
    def tearDownClass(cls):
        # Re-enable the stream of ILLUMINATOR_STATUS messages
        set_illuminator_status_stream(0, cls.illuminator_connection, cls.status_timeout)
        cls.illuminator_connection.close()

    def setUp(self):
        # Disable the stream of ILLUMINATOR_STATUS messages
        set_illuminator_status_stream(-1, self.illuminator_connection, self.status_timeout)

    def test_illuminator_status_request(self):
        message = self.illuminator_connection.udpout.mav.command_long_encode(
            self.illuminator_connection.udpout.target_system,  # Target System
            self.illuminator_connection.udpout.target_component,  # Target Component
            mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE,  # Command
            0,  # Confirmation
            mavutil.mavlink.MAVLINK_MSG_ID_ILLUMINATOR_STATUS,  # param1: Message ID
            0,  # param2 (unused)
            0,  # param3 (unused)
            0,  # param4 (unused)
            0,  # param5 (unused)
            0,  # param6 (unused)
            0,  # param7: Response Target - Flight-stack default
        )
        self.illuminator_connection.udpout.mav.send(message)
        # Wait for COMMAND_ACK to the MAV_CMD_REQUEST_MESSAGE command
        response = self.illuminator_connection.udpin.recv_match(
            type="COMMAND_ACK", blocking=True, timeout=self.ack_timeout
        )
        if (
            response
            and response.command == mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE
            and response.result == mavutil.mavlink.MAV_RESULT_ACCEPTED
        ):
            # Wait for a ILLUMINATOR_STATUS message
            response = self.illuminator_connection.udpin.recv_match(
                type="ILLUMINATOR_STATUS", blocking=True, timeout=self.status_timeout
            )
            if response:
                self.assertTrue(True)
            else:
                self.assertTrue(False, "Did not receive a ILLUMINATOR_STATUS message")
        else:
            self.assertTrue(False, "Did not receive a MAV_RESULT_ACCEPTED COMMAND_ACK message")

    def test_illuminator_status_stream(self):
        message = self.illuminator_connection.udpout.mav.command_long_encode(
            self.illuminator_connection.udpout.target_system,  # Target System
            self.illuminator_connection.udpout.target_component,  # Target Component
            mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL,  # Command
            0,  # Confirmation
            mavutil.mavlink.MAVLINK_MSG_ID_ILLUMINATOR_STATUS,  # param1: Message ID
            0,  # param2: Interval - request default rate
            0,  # param3 (unused)
            0,  # param4 (unused)
            0,  # param5 (unused)
            0,  # param6 (unused)
            0,  # param7: Response Target - flight-stack default
        )
        self.illuminator_connection.udpout.mav.send(message)
        # Wait for COMMAND_ACK to the MAV_CMD_SET_MESSAGE_INTERVAL command
        response = self.illuminator_connection.udpin.recv_match(
            type="COMMAND_ACK", blocking=True, timeout=self.ack_timeout
        )
        if (
            response
            and response.command == mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL
            and response.result == mavutil.mavlink.MAV_RESULT_ACCEPTED
        ):
            # Wait for multiple ILLUMINATOR_STATUS messages
            response_status_1 = self.illuminator_connection.udpin.recv_match(
                type="ILLUMINATOR_STATUS", blocking=True, timeout=self.status_timeout
            )
            response_status_2 = self.illuminator_connection.udpin.recv_match(
                type="ILLUMINATOR_STATUS", blocking=True, timeout=self.status_timeout
            )
            if response_status_1 and response_status_2:
                self.assertTrue(True)
            else:
                self.assertTrue(False, "Did not receive a stream of ILLUMINATOR_STATUS messages")
        else:
            print(response)
            self.assertTrue(False, "Did not receive a MAV_RESULT_ACCEPTED COMMAND_ACK message")


# @unittest.skip("reason for skipping COMPONENT_INFORMATION_BASIC")
class MavlinkComponentInformationBasicTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.illuminator_connection = MavlinkUDPConnection()
        cls.ack_timeout = 3
        cls.msg_timeout = 5
        # Ensure that there is no stream of COMPONENT_INFORMATION_BASIC messages
        response = cls.illuminator_connection.udpin.recv_match(
            type="COMPONENT_INFORMATION_BASIC", blocking=True, timeout=cls.msg_timeout
        )
        if response:
            cls.illuminator_connection.close()
            raise Exception(
                "Cannot test COMPONENT_INFORMATION_BASIC because it is already streaming"
            )

    @classmethod
    def tearDownClass(cls):
        cls.illuminator_connection.close()

    def test_component_information_basic_request(self):
        message = self.illuminator_connection.udpout.mav.command_long_encode(
            self.illuminator_connection.udpout.target_system,  # Target System
            self.illuminator_connection.udpout.target_component,  # Target Component
            mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE,  # Command
            0,  # Confirmation
            mavutil.mavlink.MAVLINK_MSG_ID_COMPONENT_INFORMATION_BASIC,  # param1: Message ID
            0,  # param2 (unused)
            0,  # param3 (unused)
            0,  # param4 (unused)
            0,  # param5 (unused)
            0,  # param6 (unused)
            0,  # param7: Response Target - Flight-stack default
        )
        self.illuminator_connection.udpout.mav.send(message)
        # Wait for COMMAND_ACK to the MAV_CMD_REQUEST_MESSAGE command
        response = self.illuminator_connection.udpin.recv_match(
            type="COMMAND_ACK", blocking=True, timeout=self.ack_timeout
        )
        if (
            response
            and response.command == mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE
            and response.result == mavutil.mavlink.MAV_RESULT_ACCEPTED
        ):
            # Wait for a COMPONENT_INFORMATION_BASIC message
            response = self.illuminator_connection.udpin.recv_match(
                type="COMPONENT_INFORMATION_BASIC", blocking=True, timeout=self.msg_timeout
            )
            if response:
                self.assertTrue(True)
            else:
                self.assertTrue(False, "Did not receive a COMPONENT_INFORMATION_BASIC message")
        else:
            self.assertTrue(False, "Did not receive a MAV_RESULT_ACCEPTED COMMAND_ACK message")


# @unittest.skip("reason for skipping MAV_CMD_ILLUMINATOR_ON_OFF")
class MavlinkIlluminatorOnOffCommTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.illuminator_connection = MavlinkUDPConnection()
        cls.ack_timeout = 3
        cls.status_timeout = 5
        # Ensure there is a stream of ILLUMINATOR_STATUS messages
        response = cls.illuminator_connection.udpin.recv_match(
            type="ILLUMINATOR_STATUS", blocking=True, timeout=cls.status_timeout
        )
        if not response:
            raise Exception("Cannot test because there is no stream of ILLUMINATOR_STATUS messages")

    @classmethod
    def tearDownClass(cls):
        # Turn off the illuminator
        turn_illuminator_on_off(0, cls.illuminator_connection, cls.status_timeout)
        cls.illuminator_connection.close()

    def test_reject_invalid_illuminator_on_off_request_lowerbound(self):
        message = self.illuminator_connection.udpout.mav.command_long_encode(
            self.illuminator_connection.udpout.target_system,  # Target System
            self.illuminator_connection.udpout.target_component,  # Target Component
            mavutil.mavlink.MAV_CMD_ILLUMINATOR_ON_OFF,  # Command
            0,  # Confirmation
            -1,  # param1: Enable - invalid
            0,  # param2 (unused)
            0,  # param3 (unused)
            0,  # param4 (unused)
            0,  # param5 (unused)
            0,  # param6 (unused)
            0,  # param7 (unused)
        )
        self.illuminator_connection.udpout.mav.send(message)
        # Wait for COMMAND_ACK to the MAV_CMD_ILLUMINATOR_ON_OFF command
        response_ack = self.illuminator_connection.udpin.recv_match(
            type="COMMAND_ACK", blocking=True, timeout=self.ack_timeout
        )
        if (
            response_ack
            and response_ack.command == mavutil.mavlink.MAV_CMD_ILLUMINATOR_ON_OFF
            and response_ack.result == mavutil.mavlink.MAV_RESULT_DENIED
        ):
            self.assertTrue(True)
        else:
            self.assertTrue(False, "Did not receive a MAV_RESULT_DENIED COMMAND_ACK message")

    def test_reject_invalid_illuminator_on_off_request_upperbound(self):
        message = self.illuminator_connection.udpout.mav.command_long_encode(
            self.illuminator_connection.udpout.target_system,  # Target System
            self.illuminator_connection.udpout.target_component,  # Target Component
            mavutil.mavlink.MAV_CMD_ILLUMINATOR_ON_OFF,  # Command
            0,  # Confirmation
            2,  # param1: Enable - invalid
            0,  # param2 (unused)
            0,  # param3 (unused)
            0,  # param4 (unused)
            0,  # param5 (unused)
            0,  # param6 (unused)
            0,  # param7 (unused)
        )
        self.illuminator_connection.udpout.mav.send(message)
        # Wait for COMMAND_ACK to the MAV_CMD_ILLUMINATOR_ON_OFF command
        response_ack = self.illuminator_connection.udpin.recv_match(
            type="COMMAND_ACK", blocking=True, timeout=self.ack_timeout
        )
        if (
            response_ack
            and response_ack.command == mavutil.mavlink.MAV_CMD_ILLUMINATOR_ON_OFF
            and response_ack.result == mavutil.mavlink.MAV_RESULT_DENIED
        ):
            self.assertTrue(True)
        else:
            self.assertTrue(False, "Did not receive a MAV_RESULT_DENIED COMMAND_ACK message")


# @unittest.skip("reason for skipping MAV_CMD_ILLUMINATOR_ON_OFF - ON")
class MavlinkIlluminatorOnTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.illuminator_connection = MavlinkUDPConnection()
        cls.ack_timeout = 3
        cls.status_timeout = 5
        # Ensure there is a stream of ILLUMINATOR_STATUS messages
        response = cls.illuminator_connection.udpin.recv_match(
            type="ILLUMINATOR_STATUS", blocking=True, timeout=cls.status_timeout
        )
        if not response:
            raise Exception("Cannot test because there is no stream of ILLUMINATOR_STATUS messages")

    @classmethod
    def tearDownClass(cls):
        # Turn off the illuminator
        turn_illuminator_on_off(0, cls.illuminator_connection, cls.status_timeout)
        cls.illuminator_connection.close()

    def setUp(self):
        # Ensure that the illuminator is off
        turn_illuminator_on_off(0, self.illuminator_connection, self.status_timeout)

    def test_turning_illuminator_on(self):
        message = self.illuminator_connection.udpout.mav.command_long_encode(
            self.illuminator_connection.udpout.target_system,  # Target System
            self.illuminator_connection.udpout.target_component,  # Target Component
            mavutil.mavlink.MAV_CMD_ILLUMINATOR_ON_OFF,  # Command
            0,  # Confirmation
            1,  # param1: Enable - on
            0,  # param2 (unused)
            0,  # param3 (unused)
            0,  # param4 (unused)
            0,  # param5 (unused)
            0,  # param6 (unused)
            0,  # param7 (unused)
        )
        self.illuminator_connection.udpout.mav.send(message)
        # Wait for COMMAND_ACK to the MAV_CMD_ILLUMINATOR_ON_OFF command
        response_ack = self.illuminator_connection.udpin.recv_match(
            type="COMMAND_ACK", blocking=True, timeout=self.ack_timeout
        )
        if (
            response_ack
            and response_ack.command == mavutil.mavlink.MAV_CMD_ILLUMINATOR_ON_OFF
            and response_ack.result == mavutil.mavlink.MAV_RESULT_ACCEPTED
        ):
            # Wait for ILLUMINATOR_STATUS to check if the illuminator is on
            response_status = self.illuminator_connection.udpin.recv_match(
                type="ILLUMINATOR_STATUS", blocking=True, timeout=self.status_timeout
            )
            if response_status and response_status.enable == 1:
                self.assertTrue(True)
            else:
                self.assertTrue(
                    False, "Did not receive a ILLUMINATOR_STATUS message with enable ON"
                )
        else:
            self.assertTrue(False, "Did not receive a MAV_RESULT_ACCEPTED COMMAND_ACK message")


# @unittest.skip("reason for skipping MAV_CMD_ILLUMINATOR_ON_OFF - OFF")
class MavlinkIlluminatorOffTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.illuminator_connection = MavlinkUDPConnection()
        cls.ack_timeout = 3
        cls.status_timeout = 5
        # Ensure there is a stream of ILLUMINATOR_STATUS messages
        response = cls.illuminator_connection.udpin.recv_match(
            type="ILLUMINATOR_STATUS", blocking=True, timeout=cls.status_timeout
        )
        if not response:
            raise Exception("Cannot test because there is no stream of ILLUMINATOR_STATUS messages")

    @classmethod
    def tearDownClass(cls):
        # Turn off the illuminator
        turn_illuminator_on_off(0, cls.illuminator_connection, cls.status_timeout)
        cls.illuminator_connection.close()

    def setUp(self):
        # Ensure that the illuminator is on
        turn_illuminator_on_off(1, self.illuminator_connection, self.status_timeout)

    def test_turning_illuminator_off(self):
        message = self.illuminator_connection.udpout.mav.command_long_encode(
            self.illuminator_connection.udpout.target_system,  # Target System
            self.illuminator_connection.udpout.target_component,  # Target Component
            mavutil.mavlink.MAV_CMD_ILLUMINATOR_ON_OFF,  # Command
            0,  # Confirmation
            0,  # param1: Enable - off
            0,  # param2 (unused)
            0,  # param3 (unused)
            0,  # param4 (unused)
            0,  # param5 (unused)
            0,  # param6 (unused)
            0,  # param7 (unused)
        )
        self.illuminator_connection.udpout.mav.send(message)
        # Wait for COMMAND_ACK to the MAV_CMD_ILLUMINATOR_ON_OFF command
        response_ack = self.illuminator_connection.udpin.recv_match(
            type="COMMAND_ACK", blocking=True, timeout=self.ack_timeout
        )
        if (
            response_ack
            and response_ack.command == mavutil.mavlink.MAV_CMD_ILLUMINATOR_ON_OFF
            and response_ack.result == mavutil.mavlink.MAV_RESULT_ACCEPTED
        ):
            # Wait for ILLUMINATOR_STATUS to check if the illuminator is off
            response_status = self.illuminator_connection.udpin.recv_match(
                type="ILLUMINATOR_STATUS", blocking=True, timeout=self.status_timeout
            )
            if response_status and response_status.enable == 0:
                self.assertTrue(True)
            else:
                self.assertTrue(
                    False, "Did not receive a ILLUMINATOR_STATUS message with enable OFF"
                )
        else:
            self.assertTrue(False, "Did not receive a MAV_RESULT_ACCEPTED COMMAND_ACK message")


# @unittest.skip("reason for skipping MAV_CMD_DO_ILLUMINATOR_CONFIGURE - Mode")
class MavlinkIlluminatorConfigureModeTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.illuminator_connection = MavlinkUDPConnection()
        cls.ack_timeout = 3
        cls.status_timeout = 5
        # Ensure there is a stream of ILLUMINATOR_STATUS messages
        response = cls.illuminator_connection.udpin.recv_match(
            type="ILLUMINATOR_STATUS", blocking=True, timeout=cls.status_timeout
        )
        if not response:
            raise Exception("Cannot test because there is no stream of ILLUMINATOR_STATUS messages")
        cls.original_mode = response.mode
        cls.original_brightness = response.brightness
        cls.original_strobe_period = response.strobe_period
        cls.original_strobe_duty_cycle = response.strobe_duty_cycle
        # Ensure the illuminator is off
        turn_illuminator_on_off(0, cls.illuminator_connection, cls.status_timeout)

    @classmethod
    def tearDownClass(cls):
        # Restore the original configuration
        configure_illuminator(
            cls.original_mode,
            cls.original_brightness,
            cls.original_strobe_period,
            cls.original_strobe_duty_cycle,
            cls.illuminator_connection,
            cls.status_timeout,
        )
        cls.illuminator_connection.close()

    def test_illuminator_configure_mode_internal_control_request(self):
        old_mode = mavutil.mavlink.ILLUMINATOR_MODE_EXTERNAL_SYNC
        new_mode = mavutil.mavlink.ILLUMINATOR_MODE_INTERNAL_CONTROL
        # Setup the test so can compare the change in mode
        configure_illuminator(
            old_mode,
            self.original_brightness,
            self.original_strobe_period,
            self.original_strobe_duty_cycle,
            self.illuminator_connection,
            self.status_timeout,
        )
        # Start the test
        message = self.illuminator_connection.udpout.mav.command_long_encode(
            self.illuminator_connection.udpout.target_system,  # Target System
            self.illuminator_connection.udpout.target_component,  # Target Component
            mavutil.mavlink.MAV_CMD_DO_ILLUMINATOR_CONFIGURE,  # Command
            0,  # Confirmation
            new_mode,  # param1: Mode - ILLUMINATOR_MODE_INTERNAL_CONTROL
            self.original_brightness,  # param2: Brightness - 50%
            self.original_strobe_period,  # param3: Strobe Period - 0s (strobe is not used)
            self.original_strobe_duty_cycle,  # param4: Strobe Duty - 0% (strobe is not used)
            0,  # param5 (unused)
            0,  # param6 (unused)
            0,  # param7 (unused)
        )
        self.illuminator_connection.udpout.mav.send(message)
        # Wait for COMMAND_ACK to the MAV_CMD_DO_ILLUMINATOR_CONFIGURE command
        response_ack = self.illuminator_connection.udpin.recv_match(
            type="COMMAND_ACK", blocking=True, timeout=self.ack_timeout
        )
        if (
            response_ack
            and response_ack.command == mavutil.mavlink.MAV_CMD_DO_ILLUMINATOR_CONFIGURE
            and response_ack.result == mavutil.mavlink.MAV_RESULT_ACCEPTED
        ):
            # Wait for ILLUMINATOR_STATUS to check if the illuminator mode has changed
            response_status = self.illuminator_connection.udpin.recv_match(
                type="ILLUMINATOR_STATUS", blocking=True, timeout=self.status_timeout
            )
            if (
                response_status
                and response_status.mode == new_mode
                and response_status.brightness == self.original_brightness
                and response_status.strobe_period == self.original_strobe_period
                and response_status.strobe_duty_cycle == self.original_strobe_duty_cycle
            ):
                self.assertTrue(True)
            else:
                self.assertTrue(
                    False,
                    "Did not receive a ILLUMINATOR_STATUS message with mode change from {} to {}".format(
                        self.original_mode, new_mode
                    ),
                )
        else:
            self.assertTrue(False, "Did not receive a MAV_RESULT_ACCEPTED COMMAND_ACK message")

    def test_illuminator_configure_mode_external_sync_request(self):
        old_mode = mavutil.mavlink.ILLUMINATOR_MODE_INTERNAL_CONTROL
        new_mode = mavutil.mavlink.ILLUMINATOR_MODE_EXTERNAL_SYNC
        # Setup the test so can compare the change in mode
        configure_illuminator(
            old_mode,
            self.original_brightness,
            self.original_strobe_period,
            self.original_strobe_duty_cycle,
            self.illuminator_connection,
            self.status_timeout,
        )
        # Start the test
        message = self.illuminator_connection.udpout.mav.command_long_encode(
            self.illuminator_connection.udpout.target_system,  # Target System
            self.illuminator_connection.udpout.target_component,  # Target Component
            mavutil.mavlink.MAV_CMD_DO_ILLUMINATOR_CONFIGURE,  # Command
            0,  # Confirmation
            new_mode,  # param1: Mode - ILLUMINATOR_MODE_EXTERNAL_SYNC
            self.original_brightness,  # param2: Brightness - 50%
            self.original_strobe_period,  # param3: Strobe Period - 0s (internal control strobe is not used)
            self.original_strobe_duty_cycle,  # param4: Strobe Duty - 0% (internal control strobe is not used)
            0,  # param5 (unused)
            0,  # param6 (unused)
            0,  # param7 (unused)
        )
        self.illuminator_connection.udpout.mav.send(message)
        # Wait for COMMAND_ACK to the MAV_CMD_DO_ILLUMINATOR_CONFIGURE command
        response_ack = self.illuminator_connection.udpin.recv_match(
            type="COMMAND_ACK", blocking=True, timeout=self.ack_timeout
        )
        if (
            response_ack
            and response_ack.command == mavutil.mavlink.MAV_CMD_DO_ILLUMINATOR_CONFIGURE
            and response_ack.result == mavutil.mavlink.MAV_RESULT_ACCEPTED
        ):
            # Wait for ILLUMINATOR_STATUS to check if the illuminator mode has changed
            response_status = self.illuminator_connection.udpin.recv_match(
                type="ILLUMINATOR_STATUS", blocking=True, timeout=self.status_timeout
            )
            if (
                response_status
                and response_status.mode == new_mode
                and response_status.brightness == self.original_brightness
                and response_status.strobe_period == self.original_strobe_period
                and response_status.strobe_duty_cycle == self.original_strobe_duty_cycle
            ):
                self.assertTrue(True)
            else:
                self.assertTrue(
                    False,
                    "Did not receive a ILLUMINATOR_STATUS message with mode change from {} to {}".format(
                        self.original_mode, new_mode
                    ),
                )
        else:
            self.assertTrue(False, "Did not receive a MAV_RESULT_ACCEPTED COMMAND_ACK message")

    def test_reject_invalid_illuminator_configure_mode_request_lowerbound(self):
        message = self.illuminator_connection.udpout.mav.command_long_encode(
            self.illuminator_connection.udpout.target_system,  # Target System
            self.illuminator_connection.udpout.target_component,  # Target Component
            mavutil.mavlink.MAV_CMD_DO_ILLUMINATOR_CONFIGURE,  # Command
            0,  # Confirmation
            -1,  # param1: Mode - invalid
            self.original_brightness,  # param2: Brightness - 50%
            self.original_strobe_period,  # param3: Strobe Period - 0s (internal control strobe is not used)
            self.original_strobe_duty_cycle,  # param4: Strobe Duty - 0% (internal control strobe is not used)
            0,  # param5 (unused)
            0,  # param6 (unused)
            0,  # param7 (unused)
        )
        self.illuminator_connection.udpout.mav.send(message)
        # Wait for COMMAND_ACK to the MAV_CMD_DO_ILLUMINATOR_CONFIGURE command
        response_ack = self.illuminator_connection.udpin.recv_match(
            type="COMMAND_ACK", blocking=True, timeout=self.ack_timeout
        )
        if (
            response_ack
            and response_ack.command == mavutil.mavlink.MAV_CMD_DO_ILLUMINATOR_CONFIGURE
            and response_ack.result == mavutil.mavlink.MAV_RESULT_DENIED
        ):
            self.assertTrue(True)
        else:
            self.assertTrue(False, "Did not receive a MAV_RESULT_DENIED COMMAND_ACK message")

    def test_reject_invalid_illuminator_configure_mode_request_upperbound(self):
        message = self.illuminator_connection.udpout.mav.command_long_encode(
            self.illuminator_connection.udpout.target_system,  # Target System
            self.illuminator_connection.udpout.target_component,  # Target Component
            mavutil.mavlink.MAV_CMD_DO_ILLUMINATOR_CONFIGURE,  # Command
            0,  # Confirmation
            3,  # param1: Mode - invalid
            self.original_brightness,  # param2: Brightness - 50%
            self.original_strobe_period,  # param3: Strobe Period - 0s (internal control strobe is not used)
            self.original_strobe_duty_cycle,  # param4: Strobe Duty - 0% (internal control strobe is not used)
            0,  # param5 (unused)
            0,  # param6 (unused)
            0,  # param7 (unused)
        )
        self.illuminator_connection.udpout.mav.send(message)
        # Wait for COMMAND_ACK to the MAV_CMD_DO_ILLUMINATOR_CONFIGURE command
        response_ack = self.illuminator_connection.udpin.recv_match(
            type="COMMAND_ACK", blocking=True, timeout=self.ack_timeout
        )
        if (
            response_ack
            and response_ack.command == mavutil.mavlink.MAV_CMD_DO_ILLUMINATOR_CONFIGURE
            and response_ack.result == mavutil.mavlink.MAV_RESULT_DENIED
        ):
            self.assertTrue(True)
        else:
            self.assertTrue(False, "Did not receive a MAV_RESULT_DENIED COMMAND_ACK message")


# @unittest.skip("reason for skipping MAV_CMD_DO_ILLUMINATOR_CONFIGURE - Brightness")
class MavlinkIlluminatorConfigureBrightnessTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.illuminator_connection = MavlinkUDPConnection()
        cls.ack_timeout = 3
        cls.status_timeout = 5
        # Ensure there is a stream of ILLUMINATOR_STATUS messages
        response = cls.illuminator_connection.udpin.recv_match(
            type="ILLUMINATOR_STATUS", blocking=True, timeout=cls.status_timeout
        )
        if not response:
            raise Exception("Cannot test because there is no stream of ILLUMINATOR_STATUS messages")
        cls.original_mode = response.mode
        cls.original_brightness = response.brightness
        cls.original_strobe_period = response.strobe_period
        cls.original_strobe_duty_cycle = response.strobe_duty_cycle
        # Ensure the illuminator is off
        turn_illuminator_on_off(0, cls.illuminator_connection, cls.status_timeout)

    @classmethod
    def tearDownClass(cls):
        # Restore the original configuration
        configure_illuminator(
            cls.original_mode,
            cls.original_brightness,
            cls.original_strobe_period,
            cls.original_strobe_duty_cycle,
            cls.illuminator_connection,
            cls.status_timeout,
        )
        cls.illuminator_connection.close()

    def test_configure_illuminator_brightness(self):
        # Get current brightness
        current = self.illuminator_connection.udpin.recv_match(
            type="ILLUMINATOR_STATUS", blocking=True, timeout=self.status_timeout
        )
        if not current:
            raise Exception("Cannot test because there is no stream of ILLUMINATOR_STATUS messages")
        if current.brightness == 100:
            new_brightness = 50
        else:
            new_brightness = 100
        # Start the test
        message = self.illuminator_connection.udpout.mav.command_long_encode(
            self.illuminator_connection.udpout.target_system,  # Target System
            self.illuminator_connection.udpout.target_component,  # Target Component
            mavutil.mavlink.MAV_CMD_DO_ILLUMINATOR_CONFIGURE,  # Command
            0,  # Confirmation
            self.original_mode,  # param1: Mode
            new_brightness,  # param2: Brightness
            self.original_strobe_period,  # param3: Strobe Period
            self.original_strobe_duty_cycle,  # param4: Strobe Duty Cycle
            0,  # param5 (unused)
            0,  # param6 (unused)
            0,  # param7 (unused)
        )
        self.illuminator_connection.udpout.mav.send(message)
        # Wait for COMMAND_ACK to the MAV_CMD_DO_ILLUMINATOR_CONFIGURE command
        response_ack = self.illuminator_connection.udpin.recv_match(
            type="COMMAND_ACK", blocking=True, timeout=self.ack_timeout
        )
        if (
            response_ack
            and response_ack.command == mavutil.mavlink.MAV_CMD_DO_ILLUMINATOR_CONFIGURE
            and response_ack.result == mavutil.mavlink.MAV_RESULT_ACCEPTED
        ):
            # Wait for ILLUMINATOR_STATUS to check if the illuminator brightness has changed
            response_status = self.illuminator_connection.udpin.recv_match(
                type="ILLUMINATOR_STATUS", blocking=True, timeout=self.status_timeout
            )
            if (
                response_status
                and response_status.mode == self.original_mode
                and response_status.brightness == new_brightness
                and response_status.strobe_period == self.original_strobe_period
                and response_status.strobe_duty_cycle == self.original_strobe_duty_cycle
            ):
                self.assertTrue(True)
            else:
                self.assertTrue(
                    False,
                    "Did not receive a ILLUMINATOR_STATUS message with brightness change from {} to {}".format(
                        self.original_brightness, new_brightness
                    ),
                )
        else:
            self.assertTrue(False, "Did not receive a MAV_RESULT_DENIED COMMAND_ACK message")

    def test_reject_invalid_illuminator_configure_brightness_request_lowerbound(self):
        message = self.illuminator_connection.udpout.mav.command_long_encode(
            self.illuminator_connection.udpout.target_system,  # Target System
            self.illuminator_connection.udpout.target_component,  # Target Component
            mavutil.mavlink.MAV_CMD_DO_ILLUMINATOR_CONFIGURE,  # Command
            0,  # Confirmation
            self.original_mode,  # param1: Mode - ILLUMINATOR_MODE_UNKNOWN
            -1,  # param2: Brightness - invalid
            self.original_strobe_period,  # param3: Strobe Period - 0s (internal control strobe is not used)
            self.original_strobe_duty_cycle,  # param4: Strobe Duty - 0% (internal control strobe is not used)
            0,  # param5 (unused)
            0,  # param6 (unused)
            0,  # param7 (unused)
        )
        self.illuminator_connection.udpout.mav.send(message)
        # Wait for COMMAND_ACK to the MAV_CMD_DO_ILLUMINATOR_CONFIGURE command
        response_ack = self.illuminator_connection.udpin.recv_match(
            type="COMMAND_ACK", blocking=True, timeout=self.ack_timeout
        )
        if (
            response_ack
            and response_ack.command == mavutil.mavlink.MAV_CMD_DO_ILLUMINATOR_CONFIGURE
            and response_ack.result == mavutil.mavlink.MAV_RESULT_DENIED
        ):
            self.assertTrue(True)
        else:
            self.assertTrue(False, "Did not receive a MAV_RESULT_DENIED COMMAND_ACK message")

    def test_reject_invalid_illuminator_configure_brightness_request_upperbound(self):
        message = self.illuminator_connection.udpout.mav.command_long_encode(
            self.illuminator_connection.udpout.target_system,  # Target System
            self.illuminator_connection.udpout.target_component,  # Target Component
            mavutil.mavlink.MAV_CMD_DO_ILLUMINATOR_CONFIGURE,  # Command
            0,  # Confirmation
            self.original_mode,  # param1: Mode - ILLUMINATOR_MODE_UNKNOWN
            101,  # param2: Brightness - invalid
            self.original_strobe_period,  # param3: Strobe Period - 0s (internal control strobe is not used)
            self.original_strobe_duty_cycle,  # param4: Strobe Duty - 0% (internal control strobe is not used)
            0,  # param5 (unused)
            0,  # param6 (unused)
            0,  # param7 (unused)
        )
        self.illuminator_connection.udpout.mav.send(message)
        # Wait for COMMAND_ACK to the MAV_CMD_DO_ILLUMINATOR_CONFIGURE command
        response_ack = self.illuminator_connection.udpin.recv_match(
            type="COMMAND_ACK", blocking=True, timeout=self.ack_timeout
        )
        if (
            response_ack
            and response_ack.command == mavutil.mavlink.MAV_CMD_DO_ILLUMINATOR_CONFIGURE
            and response_ack.result == mavutil.mavlink.MAV_RESULT_DENIED
        ):
            self.assertTrue(True)
        else:
            self.assertTrue(False, "Did not receive a MAV_RESULT_DENIED COMMAND_ACK message")


# @unittest.skip("reason for skipping MAV_CMD_DO_ILLUMINATOR_CONFIGURE - Strobe")
class MavlinkIlluminatorConfigureStrobeTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.illuminator_connection = MavlinkUDPConnection()
        cls.ack_timeout = 3
        cls.status_timeout = 5
        # Ensure there is a stream of ILLUMINATOR_STATUS messages
        response = cls.illuminator_connection.udpin.recv_match(
            type="ILLUMINATOR_STATUS", blocking=True, timeout=cls.status_timeout
        )
        if not response:
            raise Exception("Cannot test because there is no stream of ILLUMINATOR_STATUS messages")
        cls.original_mode = response.mode
        cls.original_brightness = response.brightness
        cls.original_strobe_period = response.strobe_period
        cls.original_strobe_duty_cycle = response.strobe_duty_cycle
        # Ensure the illuminator is off
        turn_illuminator_on_off(0, cls.illuminator_connection, cls.status_timeout)

    @classmethod
    def tearDownClass(cls):
        # Restore the original configuration
        configure_illuminator(
            cls.original_mode,
            cls.original_brightness,
            cls.original_strobe_period,
            cls.original_strobe_duty_cycle,
            cls.illuminator_connection,
            cls.status_timeout,
        )
        cls.illuminator_connection.close()

    def test_configure_illuminator_strobe(self):
        # Get current strobe configuration
        current = self.illuminator_connection.udpin.recv_match(
            type="ILLUMINATOR_STATUS", blocking=True, timeout=self.status_timeout
        )
        if not current:
            raise Exception("Cannot test because there is no stream of ILLUMINATOR_STATUS messages")
        if current.strobe_period != 1:
            new_strobe_period = 1
        else:
            new_strobe_period = 0.5
        if current.strobe_duty_cycle != 50:
            new_strobe_duty_cycle = 50
        else:
            new_strobe_duty_cycle = 25
        # Start the test
        message = self.illuminator_connection.udpout.mav.command_long_encode(
            self.illuminator_connection.udpout.target_system,  # Target System
            self.illuminator_connection.udpout.target_component,  # Target Component
            mavutil.mavlink.MAV_CMD_DO_ILLUMINATOR_CONFIGURE,  # Command
            0,  # Confirmation
            self.original_mode,  # param1: Mode
            self.original_brightness,  # param2: Brightness
            new_strobe_period,  # param3: Strobe Period
            new_strobe_duty_cycle,  # param4: Strobe Duty Cycle
            0,  # param5 (unused)
            0,  # param6 (unused)
            0,  # param7 (unused)
        )
        self.illuminator_connection.udpout.mav.send(message)
        # Wait for COMMAND_ACK to the MAV_CMD_DO_ILLUMINATOR_CONFIGURE command
        response_ack = self.illuminator_connection.udpin.recv_match(
            type="COMMAND_ACK", blocking=True, timeout=self.ack_timeout
        )
        if (
            response_ack
            and response_ack.command == mavutil.mavlink.MAV_CMD_DO_ILLUMINATOR_CONFIGURE
            and response_ack.result == mavutil.mavlink.MAV_RESULT_ACCEPTED
        ):
            # Wait for ILLUMINATOR_STATUS to check if the illuminator strobe settings have changed
            response_status = self.illuminator_connection.udpin.recv_match(
                type="ILLUMINATOR_STATUS", blocking=True, timeout=self.status_timeout
            )
            if (
                response_status
                and response_status.mode == self.original_mode
                and response_status.brightness == self.original_brightness
                and response_status.strobe_period == new_strobe_period
                and response_status.strobe_duty_cycle == new_strobe_duty_cycle
            ):
                self.assertTrue(True)
            else:
                self.assertTrue(
                    False,
                    "Did not receive a ILLUMINATOR_STATUS message with strobe period change from {} to {} and strobe duty cycle change from {} to {}".format(
                        self.original_strobe_period,
                        new_strobe_period,
                        self.original_strobe_duty_cycle,
                        new_strobe_duty_cycle,
                    ),
                )
        else:
            self.assertTrue(False, "Did not receive a MAV_RESULT_ACCEPTED COMMAND_ACK message")

    def test_reject_invalid_illuminator_configure_strobe_period_request_lowerbound(self):
        message = self.illuminator_connection.udpout.mav.command_long_encode(
            self.illuminator_connection.udpout.target_system,  # Target System
            self.illuminator_connection.udpout.target_component,  # Target Component
            mavutil.mavlink.MAV_CMD_DO_ILLUMINATOR_CONFIGURE,  # Command
            0,  # Confirmation
            mavutil.mavlink.ILLUMINATOR_MODE_INTERNAL_CONTROL,  # param1: Mode - ILLUMINATOR_MODE_INTERNAL_CONTROL
            self.original_brightness,  # param2: Brightness - 50%
            -1,  # param3: Strobe Period - invalid
            self.original_strobe_duty_cycle,  # param4: Strobe Duty - 50%
            0,  # param5 (unused)
            0,  # param6 (unused)
            0,  # param7 (unused)
        )
        self.illuminator_connection.udpout.mav.send(message)
        # Wait for COMMAND_ACK to the MAV_CMD_DO_ILLUMINATOR_CONFIGURE command
        response_ack = self.illuminator_connection.udpin.recv_match(
            type="COMMAND_ACK", blocking=True, timeout=self.ack_timeout
        )
        if (
            response_ack
            and response_ack.command == mavutil.mavlink.MAV_CMD_DO_ILLUMINATOR_CONFIGURE
            and response_ack.result == mavutil.mavlink.MAV_RESULT_DENIED
        ):
            self.assertTrue(True)
        else:
            self.assertTrue(False, "Did not receive a MAV_RESULT_DENIED COMMAND_ACK message")

    def test_reject_invalid_illuminator_configure_strobe_duty_cycle_request_lowerbound(self):
        message = self.illuminator_connection.udpout.mav.command_long_encode(
            self.illuminator_connection.udpout.target_system,  # Target System
            self.illuminator_connection.udpout.target_component,  # Target Component
            mavutil.mavlink.MAV_CMD_DO_ILLUMINATOR_CONFIGURE,  # Command
            0,  # Confirmation
            mavutil.mavlink.ILLUMINATOR_MODE_INTERNAL_CONTROL,  # param1: Mode - ILLUMINATOR_MODE_INTERNAL_CONTROL
            self.original_brightness,  # param2: Brightness - 50%
            self.original_strobe_period,  # param3: Strobe Period - 1s
            -1,  # param4: Strobe Duty - invalid
            0,  # param5 (unused)
            0,  # param6 (unused)
            0,  # param7 (unused)
        )
        self.illuminator_connection.udpout.mav.send(message)
        # Wait for COMMAND_ACK to the MAV_CMD_DO_ILLUMINATOR_CONFIGURE command
        response_ack = self.illuminator_connection.udpin.recv_match(
            type="COMMAND_ACK", blocking=True, timeout=self.ack_timeout
        )
        if (
            response_ack
            and response_ack.command == mavutil.mavlink.MAV_CMD_DO_ILLUMINATOR_CONFIGURE
            and response_ack.result == mavutil.mavlink.MAV_RESULT_DENIED
        ):
            self.assertTrue(True)
        else:
            self.assertTrue(False, "Did not receive a MAV_RESULT_DENIED COMMAND_ACK message")

    def test_reject_invalid_illuminator_configure_strobe_duty_cycle_request_upperbound(self):
        message = self.illuminator_connection.udpout.mav.command_long_encode(
            self.illuminator_connection.udpout.target_system,  # Target System
            self.illuminator_connection.udpout.target_component,  # Target Component
            mavutil.mavlink.MAV_CMD_DO_ILLUMINATOR_CONFIGURE,  # Command
            0,  # Confirmation
            mavutil.mavlink.ILLUMINATOR_MODE_INTERNAL_CONTROL,  # param1: Mode - ILLUMINATOR_MODE_INTERNAL_CONTROL
            self.original_brightness,  # param2: Brightness - 50%
            self.original_strobe_period,  # param3: Strobe Period - 1s
            101,  # param4: Strobe Duty - invalid
            0,  # param5 (unused)
            0,  # param6 (unused)
            0,  # param7 (unused)
        )
        self.illuminator_connection.udpout.mav.send(message)
        # Wait for COMMAND_ACK to the MAV_CMD_DO_ILLUMINATOR_CONFIGURE command
        response_ack = self.illuminator_connection.udpin.recv_match(
            type="COMMAND_ACK", blocking=True, timeout=self.ack_timeout
        )
        if (
            response_ack
            and response_ack.command == mavutil.mavlink.MAV_CMD_DO_ILLUMINATOR_CONFIGURE
            and response_ack.result == mavutil.mavlink.MAV_RESULT_DENIED
        ):
            self.assertTrue(True)
        else:
            self.assertTrue(False, "Did not receive a MAV_RESULT_DENIED COMMAND_ACK message")


if __name__ == "__main__":
    unittest.main()
