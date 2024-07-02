import os
import threading
import time
from enum import Enum

from pymavlink import mavutil


class IlluminatorStatusFields(Enum):
    UPTIME_MS = 0
    ENABLE = 1
    MODE_BITMASK = 2
    ERROR_STATUS = 3
    MODE = 4
    BRIGHTNESS = 5
    STROBE_PERIOD = 6
    STROBE_DUTY_CYCLE = 7
    TEMP_C = 8
    MIN_STROBE_PERIOD = 9
    MAX_STROBE_PERIOD = 10


def stream_heartbeat(event, mavlink_connection_out):
    while True:
        event.wait()
        mavlink_connection_out.mav.heartbeat_send(
            mavutil.mavlink.MAV_TYPE_ILLUMINATOR, mavutil.mavlink.MAV_AUTOPILOT_INVALID, 0, 0, 0
        )
        time.sleep(1)


def stream_illuminator_status(event, mavlink_connection_out):
    while True:
        event.wait()
        mavlink_connection_out.mav.illuminator_status_send(*illuminator_status)
        time.sleep(1)


def publish_iluminator_status(mavlink_connection_out):
    mavlink_connection_out.mav.illuminator_status_send(*illuminator_status)


def publish_component_information_basic(mavlink_connection_out):
    mavlink_connection_out.mav.component_information_basic_send(
        0,  # time_boot_ms
        0,  # capabilities
        0,  # time_manufacture_s
        "Illuminator Vendor".encode(),  # vendor_name
        "Illuminator Model".encode(),  # model_name
        "Illuminator Software Version".encode(),  # software_version
        "Illuminator Hardware Version".encode(),  # hardware_version
        "Illuminator Serial Number".encode(),  # serial_number
    )


def update_illuminator_status(field, value):
    global illuminator_status
    tmp = list(illuminator_status)
    tmp[field.value] = value
    illuminator_status = tuple(tmp)


def handle_command_long(msg, mavlink_connection_out):
    # MAV_CMD_REQUEST_MESSAGE
    if msg.command == mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE:
        if msg.param1 == mavutil.mavlink.MAVLINK_MSG_ID_ILLUMINATOR_STATUS:
            mavlink_connection_out.mav.command_ack_send(
                msg.command, result=mavutil.mavlink.MAV_RESULT_ACCEPTED
            )
            publish_iluminator_status(mavlink_connection_out)
        elif msg.param1 == mavutil.mavlink.MAVLINK_MSG_ID_COMPONENT_INFORMATION_BASIC:
            mavlink_connection_out.mav.command_ack_send(
                msg.command, result=mavutil.mavlink.MAV_RESULT_ACCEPTED
            )
            publish_component_information_basic(mavlink_connection_out)
        else:
            mavlink_connection_out.mav.command_ack_send(
                msg.command, result=mavutil.mavlink.MAV_RESULT_DENIED
            )

    # MAV_CMD_SET_MESSAGE_INTERVAL
    elif msg.command == mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL:
        if msg.param1 == mavutil.mavlink.MAVLINK_MSG_ID_ILLUMINATOR_STATUS:
            if msg.param2 == -1:
                illuminator_status_thread_event.clear()
            else:
                illuminator_status_thread_event.set()
            mavlink_connection_out.mav.command_ack_send(
                msg.command, result=mavutil.mavlink.MAV_RESULT_ACCEPTED
            )
        else:
            mavlink_connection_out.mav.command_ack_send(
                msg.command, result=mavutil.mavlink.MAV_RESULT_DENIED
            )

    # MAV_CMD_ILLUMINATOR_ON_OFF
    elif msg.command == mavutil.mavlink.MAV_CMD_ILLUMINATOR_ON_OFF:
        if msg.param1 == 0 or msg.param1 == 1:
            mavlink_connection_out.mav.command_ack_send(
                msg.command, result=mavutil.mavlink.MAV_RESULT_ACCEPTED
            )
            update_illuminator_status(IlluminatorStatusFields.ENABLE, int(msg.param1))
        else:
            mavlink_connection_out.mav.command_ack_send(
                msg.command, result=mavutil.mavlink.MAV_RESULT_DENIED
            )

    # MAV_CMD_DO_ILLUMINATOR_CONFIGURE
    elif msg.command == mavutil.mavlink.MAV_CMD_DO_ILLUMINATOR_CONFIGURE:
        if (
            msg.param1 != mavutil.mavlink.ILLUMINATOR_MODE_INTERNAL_CONTROL
            and msg.param1 != mavutil.mavlink.ILLUMINATOR_MODE_EXTERNAL_SYNC
        ):
            mavlink_connection_out.mav.command_ack_send(
                msg.command, result=mavutil.mavlink.MAV_RESULT_DENIED
            )
        elif msg.param2 < 0 or msg.param2 > 100:
            mavlink_connection_out.mav.command_ack_send(
                msg.command, result=mavutil.mavlink.MAV_RESULT_DENIED
            )
        elif (
            msg.param3 < illuminator_status[IlluminatorStatusFields.MIN_STROBE_PERIOD.value]
            or msg.param3 > illuminator_status[IlluminatorStatusFields.MAX_STROBE_PERIOD.value]
        ):
            mavlink_connection_out.mav.command_ack_send(
                msg.command, result=mavutil.mavlink.MAV_RESULT_DENIED
            )
        elif msg.param4 < 0 or msg.param4 > 100:
            mavlink_connection_out.mav.command_ack_send(
                msg.command, result=mavutil.mavlink.MAV_RESULT_DENIED
            )
        else:
            mavlink_connection_out.mav.command_ack_send(
                msg.command, result=mavutil.mavlink.MAV_RESULT_ACCEPTED
            )
            update_illuminator_status(IlluminatorStatusFields.MODE, int(msg.param1))
            update_illuminator_status(IlluminatorStatusFields.BRIGHTNESS, msg.param2)
            update_illuminator_status(IlluminatorStatusFields.STROBE_PERIOD, msg.param3)
            update_illuminator_status(IlluminatorStatusFields.STROBE_DUTY_CYCLE, msg.param4)

    else:
        mavlink_connection_out.mav.command_ack_send(
            msg.command, result=mavutil.mavlink.MAV_RESULT_UNSUPPORTED
        )


def main():
    os.environ["MAVLINK20"] = "1"
    os.environ["MAVLINK_DIALECT"] = "common"
    global illuminator_status_thread_event
    global illuminator_status

    # Start UDP connections
    mavlink_connection_udpin = mavutil.mavlink_connection("udpin:localhost:14540", dialect="common")
    mavlink_connection_udpout = mavutil.mavlink_connection(
        "udpout:localhost:14541", dialect="common"
    )

    # Heartbeat
    heartbeat_thread_event = threading.Event()
    heartbeat_thread = threading.Thread(
        target=stream_heartbeat,
        daemon=True,
        args=(heartbeat_thread_event, mavlink_connection_udpout),
    )
    heartbeat_thread.start()

    # Illuminator status
    illuminator_status = (
        0,  # uptime_ms
        0,  # enable
        mavutil.mavlink.ILLUMINATOR_MODE_INTERNAL_CONTROL
        + mavutil.mavlink.ILLUMINATOR_MODE_EXTERNAL_SYNC,  # mode_bitmask
        0,  # error_status
        mavutil.mavlink.ILLUMINATOR_MODE_INTERNAL_CONTROL,  # mode
        100.0,  # brightness
        0.0,  # strobe_period
        0.0,  # strobe_duty_cycle
        25.0,  # temp_c
        0.0,  # min_strobe_period
        10.0,  # max_strobe_period
    )
    illuminator_status_thread_event = threading.Event()
    illuminator_status_thread = threading.Thread(
        target=stream_illuminator_status,
        daemon=True,
        args=(illuminator_status_thread_event, mavlink_connection_udpout),
    )
    illuminator_status_thread.start()

    heartbeat_thread_event.set()
    illuminator_status_thread_event.set()

    while True:
        msg = mavlink_connection_udpin.recv_match(type="COMMAND_LONG", blocking=True)
        if msg:
            # print(msg)
            handle_command_long(msg, mavlink_connection_udpout)


if __name__ == "__main__":
    main()
