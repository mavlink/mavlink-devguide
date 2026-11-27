import os
import unittest

from pymavlink import mavutil
from pymavlink.dialects.v20 import common as mavlink


class UnittestMavlinkUDPConnection:
    """Class to handle MAVLink UDP connections"""

    def __init__(self):
        """Initialize UDP connections for unittests based on environment variables"""
        dialect = os.getenv("MAVLINK_DIALECT", "common")
        udpin = os.getenv("MAVLINK_UDPIN", "udpin:localhost:14541")
        udpout = os.getenv("MAVLINK_UDPOUT", "udpout:localhost:14540")
        self.udpin = mavutil.mavlink_connection(udpin, dialect=dialect)
        self.udpout = mavutil.mavlink_connection(udpout, dialect=dialect)

    def close(self):
        """Close UDP connections"""
        self.udpin.close()
        self.udpout.close()


class ParachuteMavlinkTestCaseBase(unittest.TestCase):
    """Base class for parachute MAVLink test cases"""

    MSG_TIMEOUT = 3

    @classmethod
    def setUpClass(cls):
        cls.parachute_connection = UnittestMavlinkUDPConnection()

    @classmethod
    def tearDownClass(cls):
        cls.parachute_connection.close()

    def encode_and_send_mavlink_command_long(
        self, command: int, param1: float, param2: float = 0
    ) -> None:
        """Encode and send a MAVLink COMMAND_LONG message"""
        msg = self.parachute_connection.udpout.mav.command_long_encode(
            self.parachute_connection.udpout.target_system,  # Target System
            self.parachute_connection.udpout.target_component,  # Target Component
            command,  # Command
            0,  # Confirmation
            param1,  # param1
            param2,  # param2
            0,  # param3 (unused)
            0,  # param4 (unused)
            0,  # param5 (unused)
            0,  # param6 (unused)
            0,  # param7: Response Target - flight-stack default
        )
        self.parachute_connection.udpout.mav.send(msg)

    def assert_mavlink_command_ack(self, command: int, result: int):
        """Assert that a COMMAND_ACK message is recieved"""
        ack = self.parachute_connection.udpin.recv_match(
            type="COMMAND_ACK", blocking=True, timeout=self.MSG_TIMEOUT
        )
        self.assertIsNotNone(ack, "Did not recieve a COMMAND_ACK message")
        self.assertEqual(
            ack.command, command, f"Did not recieve a COMMAND_ACK message for {command}"
        )
        self.assertEqual(ack.result, result, f"Did not recieve a {result} COMMAND_ACK message")

    def receive_parachute_status_with_assert(self) -> mavlink.MAVLink_parachute_status_message:
        """Assert that a PARACHUTE_STATUS message is recieved"""
        msg = self.parachute_connection.udpin.recv_match(
            type="PARACHUTE_STATUS", blocking=True, timeout=self.MSG_TIMEOUT
        )
        self.assertIsNotNone(msg, "Did not recieve a PARACHUTE_STATUS message")
        return msg


class ParachuteBasicMavlinkMessagesTestCase(ParachuteMavlinkTestCaseBase):
    """Test cases for recieving basic MAVLink messages"""

    def test_heartbeat(self):
        """Test recieving a MAVLink heartbeat message from parachute"""
        msg = self.parachute_connection.udpin.recv_match(
            type="HEARTBEAT", blocking=True, timeout=self.MSG_TIMEOUT
        )
        self.assertIsNotNone(msg, "Did not recieve a HEARTBEAT message")
        self.assertEqual(
            msg.type, mavlink.MAV_TYPE_PARACHUTE, "HEARTBEAT message type is not parachute"
        )

    def test_component_information_basic_request(self):
        """Test requesting and receiving a parachute information basic message"""
        # Request component information basic message
        self.encode_and_send_mavlink_command_long(
            mavlink.MAV_CMD_REQUEST_MESSAGE,
            mavlink.MAVLINK_MSG_ID_COMPONENT_INFORMATION_BASIC,
        )
        self.assert_mavlink_command_ack(
            mavlink.MAV_CMD_REQUEST_MESSAGE, mavlink.MAV_RESULT_ACCEPTED
        )
        msg = self.parachute_connection.udpin.recv_match(
            type="COMPONENT_INFORMATION_BASIC", blocking=True, timeout=self.MSG_TIMEOUT
        )
        self.assertIsNotNone(msg, "Did not recieve a COMPONENT_INFORMATION_BASIC message")

    def test_parachute_status(self):
        """Test recieving a parachute status message"""
        self.receive_parachute_status_with_assert()


class MavlinkSetParachuteArmTestCase(ParachuteMavlinkTestCaseBase):
    """Test cases for arming parachute"""

    def setUp(self):
        self.receive_parachute_status_with_assert()

    def tearDown(self):
        # Disarm all triggers
        self.encode_and_send_mavlink_command_long(
            mavlink.MAV_CMD_SET_PARACHUTE_ARM,
            0,
            ((mavlink.PARACHUTE_TRIGGER_FLAGS_ENUM_END - 1) << 1) - 1,
        )
        self.assert_mavlink_command_ack(
            mavlink.MAV_CMD_SET_PARACHUTE_ARM, mavlink.MAV_RESULT_ACCEPTED
        )
        msg = self.receive_parachute_status_with_assert()
        self.assertFalse(msg.arm_status, f"Parachute arm status not disarmed: {msg}")

    def test_arm_ats(self):
        """Test arming parachute with just ATS trigger"""
        self.encode_and_send_mavlink_command_long(
            mavlink.MAV_CMD_SET_PARACHUTE_ARM,
            mavlink.PARACHUTE_TRIGGER_FLAGS_ATS,
            mavlink.PARACHUTE_TRIGGER_FLAGS_ATS,
        )
        self.assert_mavlink_command_ack(
            mavlink.MAV_CMD_SET_PARACHUTE_ARM, mavlink.MAV_RESULT_ACCEPTED
        )
        msg = self.receive_parachute_status_with_assert()
        self.assertTrue(
            msg.arm_status == mavlink.PARACHUTE_TRIGGER_FLAGS_ATS,
            "Parachute is not armed with just ATS trigger",
        )

    def test_arm_fc(self):
        """Test arming parachute with just FC trigger"""
        self.encode_and_send_mavlink_command_long(
            mavlink.MAV_CMD_SET_PARACHUTE_ARM,
            mavlink.PARACHUTE_TRIGGER_FLAGS_FC,
            mavlink.PARACHUTE_TRIGGER_FLAGS_FC,
        )
        self.assert_mavlink_command_ack(
            mavlink.MAV_CMD_SET_PARACHUTE_ARM, mavlink.MAV_RESULT_ACCEPTED
        )
        msg = self.receive_parachute_status_with_assert()
        self.assertTrue(
            msg.arm_status == mavlink.PARACHUTE_TRIGGER_FLAGS_FC,
            "Parachute is not armed with just FC trigger",
        )

    def test_arm_ats_and_fc(self):
        """Test arming parachute with both ATS and FC triggers at the same time"""
        self.encode_and_send_mavlink_command_long(
            mavlink.MAV_CMD_SET_PARACHUTE_ARM,
            mavlink.PARACHUTE_TRIGGER_FLAGS_ATS | mavlink.PARACHUTE_TRIGGER_FLAGS_FC,
            mavlink.PARACHUTE_TRIGGER_FLAGS_ATS | mavlink.PARACHUTE_TRIGGER_FLAGS_FC,
        )
        self.assert_mavlink_command_ack(
            mavlink.MAV_CMD_SET_PARACHUTE_ARM, mavlink.MAV_RESULT_ACCEPTED
        )
        msg = self.receive_parachute_status_with_assert()
        self.assertTrue(
            msg.arm_status
            == (mavlink.PARACHUTE_TRIGGER_FLAGS_ATS | mavlink.PARACHUTE_TRIGGER_FLAGS_FC),
            "Parachute is not armed with both ATS and FC triggers",
        )

    def test_arm_ats_then_fc(self):
        """Test arming parachute with ATS trigger and then FC trigger"""
        self.encode_and_send_mavlink_command_long(
            mavlink.MAV_CMD_SET_PARACHUTE_ARM,
            mavlink.PARACHUTE_TRIGGER_FLAGS_ATS,
            mavlink.PARACHUTE_TRIGGER_FLAGS_ATS,
        )
        self.assert_mavlink_command_ack(
            mavlink.MAV_CMD_SET_PARACHUTE_ARM, mavlink.MAV_RESULT_ACCEPTED
        )
        msg = self.receive_parachute_status_with_assert()
        self.assertTrue(
            msg.arm_status == mavlink.PARACHUTE_TRIGGER_FLAGS_ATS,
            "Parachute is not armed with just ATS trigger",
        )
        self.encode_and_send_mavlink_command_long(
            mavlink.MAV_CMD_SET_PARACHUTE_ARM,
            mavlink.PARACHUTE_TRIGGER_FLAGS_FC,
            mavlink.PARACHUTE_TRIGGER_FLAGS_FC,
        )
        self.assert_mavlink_command_ack(
            mavlink.MAV_CMD_SET_PARACHUTE_ARM, mavlink.MAV_RESULT_ACCEPTED
        )
        msg = self.receive_parachute_status_with_assert()
        self.assertTrue(
            msg.arm_status
            == (mavlink.PARACHUTE_TRIGGER_FLAGS_ATS | mavlink.PARACHUTE_TRIGGER_FLAGS_FC),
            "Parachute is not armed with both ATS and FC triggers",
        )

    def test_arm_invalid_upper_bound(self):
        """Test arming parachute with invalid upper bound trigger flag"""
        self.encode_and_send_mavlink_command_long(
            mavlink.MAV_CMD_SET_PARACHUTE_ARM,
            mavlink.PARACHUTE_TRIGGER_FLAGS_ENUM_END << 1,
            mavlink.PARACHUTE_TRIGGER_FLAGS_ENUM_END << 1,
        )
        self.assert_mavlink_command_ack(
            mavlink.MAV_CMD_SET_PARACHUTE_ARM, mavlink.MAV_RESULT_DENIED
        )
        msg = self.receive_parachute_status_with_assert()
        self.assertFalse(msg.arm_status, f"Upper bound trigger flag set in arm status: {msg}")


class MavlinkDeployParachuteTestCase(ParachuteMavlinkTestCaseBase):
    """Test cases for deploying parachute"""

    def setUp(self):
        msg = self.receive_parachute_status_with_assert()
        self.assertFalse(msg.arm_status, f"Parachute arm status not disarmed: {msg}")
        self.assertFalse(msg.deployment_status, f"Parachute already deployed: {msg}")

    def tearDown(self):
        # Disarm all triggers
        self.encode_and_send_mavlink_command_long(
            mavlink.MAV_CMD_SET_PARACHUTE_ARM,
            0,
            ((mavlink.PARACHUTE_TRIGGER_FLAGS_ENUM_END - 1) << 1) - 1,
        )
        self.assert_mavlink_command_ack(
            mavlink.MAV_CMD_SET_PARACHUTE_ARM, mavlink.MAV_RESULT_ACCEPTED
        )
        msg = self.receive_parachute_status_with_assert()
        self.assertFalse(msg.arm_status, f"Parachute arm status not disarmed: {msg}")

    def test_deploy_parachute_with_ats(self):
        """Test DO_PARACHUTE should not deploy parachute with ATS trigger"""
        # Arm just the ATS trigger
        self.encode_and_send_mavlink_command_long(
            mavlink.MAV_CMD_SET_PARACHUTE_ARM,
            mavlink.PARACHUTE_TRIGGER_FLAGS_ATS,
            mavlink.PARACHUTE_TRIGGER_FLAGS_ATS,
        )
        self.assert_mavlink_command_ack(
            mavlink.MAV_CMD_SET_PARACHUTE_ARM, mavlink.MAV_RESULT_ACCEPTED
        )
        msg = self.receive_parachute_status_with_assert()
        self.assertTrue(
            msg.arm_status == mavlink.PARACHUTE_TRIGGER_FLAGS_ATS,
            "Parachute is not armed with just ATS trigger",
        )
        # Deploy parachute
        self.encode_and_send_mavlink_command_long(
            mavlink.MAV_CMD_DO_PARACHUTE,
            mavlink.PARACHUTE_RELEASE,
        )
        self.assert_mavlink_command_ack(mavlink.MAV_CMD_DO_PARACHUTE, mavlink.MAV_RESULT_FAILED)
        msg = self.receive_parachute_status_with_assert()
        self.assertFalse(msg.deployment_status, f"Parachute deployed: {msg}")

    def test_deploy_parachute_with_fc(self):
        """Test DO_PARACHUTE should deploy parachute with FC trigger armed"""
        # Arm FC trigger
        self.encode_and_send_mavlink_command_long(
            mavlink.MAV_CMD_SET_PARACHUTE_ARM,
            mavlink.PARACHUTE_TRIGGER_FLAGS_FC,
            mavlink.PARACHUTE_TRIGGER_FLAGS_FC,
        )
        self.assert_mavlink_command_ack(
            mavlink.MAV_CMD_SET_PARACHUTE_ARM, mavlink.MAV_RESULT_ACCEPTED
        )
        msg = self.receive_parachute_status_with_assert()
        self.assertTrue(
            msg.arm_status == mavlink.PARACHUTE_TRIGGER_FLAGS_FC,
            "Parachute is not armed with just FC trigger",
        )
        # Deploy parachute
        self.encode_and_send_mavlink_command_long(
            mavlink.MAV_CMD_DO_PARACHUTE,
            mavlink.PARACHUTE_RELEASE,
        )
        self.assert_mavlink_command_ack(mavlink.MAV_CMD_DO_PARACHUTE, mavlink.MAV_RESULT_ACCEPTED)
        msg = self.receive_parachute_status_with_assert()
        self.assertEqual(
            msg.deployment_status,
            mavlink.PARACHUTE_DEPLOYMENT_TRIGGER_DRONE,
            f"Parachute did not deployed: {msg}",
        )


if __name__ == "__main__":
    unittest.main()
