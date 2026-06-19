import datetime
import os
import threading
import time

from pymavlink import mavutil
from pymavlink.dialects.v20 import common as mavlink


class ParachuteMavlinkUDPConnection:
    """Class to handle parachute's MAVLink v2 UDP connections"""

    def __init__(self, udpin_conn: str, udpout_conn: str, dialect: str) -> None:
        """Initialize UDP connections"""
        # Setting MAVLink version and dialect
        os.environ["MAVLINK20"] = "1"
        os.environ["MAVLINK_DIALECT"] = dialect
        # Setting up UDP connections
        self.udpin = mavutil.mavlink_connection(udpin_conn, dialect)
        self.udpout = mavutil.mavlink_connection(udpout_conn, dialect)

    def close(self):
        """Close UDP connections"""
        self.udpin.close()
        self.udpout.close()


class Parachute:
    """Parachute class that uses MAVLink v2 UDP to broadcast heartbeat/status and handle commands"""

    def __init__(
        self,
        dialect: str,
        time_manufacture_s: int,
        vendor_name: bytes,
        model_name: bytes,
        software_version: bytes,
        hardware_version: bytes,
        serial_number: bytes,
        parachute_packed_date: bytes,
    ) -> None:
        # Initialize parachute info and status
        self.info = mavlink.MAVLink_component_information_basic_message(
            time_boot_ms=0,
            capabilities=0,
            time_manufacture_s=time_manufacture_s,
            vendor_name=vendor_name,
            model_name=model_name,
            software_version=software_version,
            hardware_version=hardware_version,
            serial_number=serial_number,
        )
        self.status = mavlink.MAVLink_parachute_status_message(
            time_boot_ms=0,
            error_status=0,
            arm_status=0,
            deployment_status=mavlink.PARACHUTE_DEPLOYMENT_TRIGGER_NONE,
            safety_status=mavlink.PARACHUTE_SAFETY_FLAGS_GROUND_CLEARED,
            ats_arm_altitude=50,
            parachute_packed_date=parachute_packed_date,
        )
        # Start parachute MAVLink UDP connections
        self.mavlink_udp_connection = ParachuteMavlinkUDPConnection(
            udpin_conn="udpin:localhost:14540",
            udpout_conn="udpout:localhost:14541",
            dialect=dialect,
        )
        # Start publishing heartbeat at 1Hz
        self.heartbeat_thread_event = threading.Event()
        heartbeat_thread = threading.Thread(
            target=self.stream_heartbeat,
            daemon=True,
        )
        heartbeat_thread.start()
        self.heartbeat_thread_event.set()
        # Start publish parachute status at 1Hz
        self.parachute_status_thread_event = threading.Event()
        parachute_status_thread = threading.Thread(
            target=self.stream_parachute_status,
            daemon=True,
        )
        parachute_status_thread.start()
        self.parachute_status_thread_event.set()

    def stream_heartbeat(self) -> None:
        """Stream parachute heartbeat at 1Hz"""
        while True:
            self.heartbeat_thread_event.wait()
            self.mavlink_udp_connection.udpout.mav.heartbeat_send(
                mavlink.MAV_TYPE_PARACHUTE, mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0
            )
            time.sleep(1)

    def stream_parachute_status(self) -> None:
        """Stream parachute status at 1Hz"""
        while True:
            self.parachute_status_thread_event.wait()
            self.mavlink_udp_connection.udpout.mav.send(self.status)
            time.sleep(1)

    def listen_for_commands(self) -> None:
        """Listen for MAVLink commands"""
        while True:
            msg = self.mavlink_udp_connection.udpin.recv_match(type="COMMAND_LONG", blocking=True)
            if msg:
                self.handle_command_long(msg)

    def handle_command_long(self, msg: mavlink.MAVLink_command_long_message) -> None:
        """Handle MAVLink command long messages"""
        if msg.command == mavlink.MAV_CMD_REQUEST_MESSAGE:
            self.handle_command_request_message(msg)
        elif msg.command == mavlink.MAV_CMD_DO_PARACHUTE:
            self.handle_command_do_parachute(msg)
        elif msg.command == mavlink.MAV_CMD_SET_PARACHUTE_ARM:
            self.handle_command_set_parachute_arm(msg)
        else:
            self.mavlink_udp_connection.udpout.mav.command_ack_send(
                msg.command, result=mavlink.MAV_RESULT_UNSUPPORTED
            )

    def handle_command_request_message(self, msg: mavlink.MAVLink_command_long_message) -> None:
        """Handle MAVLink request message command"""
        if msg.param1 == mavlink.MAVLINK_MSG_ID_PARACHUTE_STATUS:
            self.mavlink_udp_connection.udpout.mav.command_ack_send(
                msg.command, result=mavlink.MAV_RESULT_ACCEPTED
            )
            self.mavlink_udp_connection.udpout.mav.send(self.status)
        elif msg.param1 == mavlink.MAVLINK_MSG_ID_COMPONENT_INFORMATION_BASIC:
            self.mavlink_udp_connection.udpout.mav.command_ack_send(
                msg.command, result=mavlink.MAV_RESULT_ACCEPTED
            )
            self.mavlink_udp_connection.udpout.mav.send(self.info)
        else:
            self.mavlink_udp_connection.udpout.mav.command_ack_send(
                msg.command, result=mavlink.MAV_RESULT_DENIED
            )

    def handle_command_do_parachute(self, msg: mavlink.MAVLink_command_long_message) -> None:
        """Handle MAVLink do parachute command"""
        result = mavlink.MAV_RESULT_DENIED
        if msg.param1 == mavlink.PARACHUTE_RELEASE:
            if self.status.arm_status & mavlink.PARACHUTE_TRIGGER_FLAGS_FC:
                if self.status.safety_status & mavlink.PARACHUTE_SAFETY_FLAGS_GROUND_CLEARED:
                    result = mavlink.MAV_RESULT_ACCEPTED
                    self.status.deployment_status = mavlink.PARACHUTE_DEPLOYMENT_TRIGGER_DRONE
                else:
                    result = mavlink.MAV_RESULT_TEMPORARILY_REJECTED
            else:
                result = mavlink.MAV_RESULT_FAILED
        self.mavlink_udp_connection.udpout.mav.command_ack_send(msg.command, result=result)

    def handle_command_set_parachute_arm(self, msg: mavlink.MAVLink_command_long_message) -> None:
        """Handle MAVLink set parachute arm command"""
        arm_flags = int(msg.param1)
        bitmask = int(msg.param2)
        valid_parachute_trigger_flags = ((mavlink.PARACHUTE_TRIGGER_FLAGS_ENUM_END - 1) << 1) - 1
        if arm_flags & ~valid_parachute_trigger_flags or bitmask & ~valid_parachute_trigger_flags:
            self.mavlink_udp_connection.udpout.mav.command_ack_send(
                msg.command, result=mavlink.MAV_RESULT_DENIED
            )
        else:
            new_arm_status = self.status.arm_status & ~bitmask
            new_arm_status |= arm_flags & bitmask
            self.status.arm_status = new_arm_status
            self.mavlink_udp_connection.udpout.mav.command_ack_send(
                msg.command, result=mavlink.MAV_RESULT_ACCEPTED
            )


if __name__ == "__main__":
    # Create parachute object and start listening for commands
    parachute = Parachute(
        dialect="common",
        time_manufacture_s=int(time.time()),
        vendor_name=b"Vendor",
        model_name=b"Model",
        software_version=b"1.2.3",
        hardware_version=b"4.5.6",
        serial_number=b"123456",
        parachute_packed_date=datetime.date.today().strftime("%Y-%m-%d").encode(),
    )
    parachute.listen_for_commands()
