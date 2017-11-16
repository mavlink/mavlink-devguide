<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_gitbook.py -->
# MAVLINK ArduPilotMega Message Set

These messages define the APM specific message set, which is custom to [http://ardupilot.org](http://ardupilot.org).

*This is a human-readable form of the XML definition file: [ardupilotmega.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/ardupilotmega.xml).*

> **Note** The ArduPilot MAVLink fork of [ardupilotmega.xml](https://github.com/ArduPilot/mavlink/blob/master/message_definitions/v1.0/ardupilotmega.xml) may contain messages that have not yet been merged into this documentation.

<html>
 <body>
  <p>
   <strong>MAVLink Include Files:</strong>
   <a href="common.md">common.xml</a>
  </p>
  <p>
   <strong>MAVLink Include Files:</strong>
   <a href="uAvionix.md">uAvionix.xml</a>
  </p>
  <p>This file has protocol dialect: 2.</p>
  <h2>MAVLink Type Enumerations</h2>
  <h3 class="mavlink_message_name" id="ENUM_ACCELCAL_VEHICLE_POS">
   <a href="#ENUM_ACCELCAL_VEHICLE_POS">ACCELCAL_VEHICLE_POS</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="ACCELCAL_VEHICLE_POS_LEVEL">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#ACCELCAL_VEHICLE_POS_LEVEL">ACCELCAL_VEHICLE_POS_LEVEL</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="ACCELCAL_VEHICLE_POS_LEFT">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#ACCELCAL_VEHICLE_POS_LEFT">ACCELCAL_VEHICLE_POS_LEFT</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="ACCELCAL_VEHICLE_POS_RIGHT">
     <td class="mavlink_type" valign="top">3</td>
     <td class="mavlink_name" valign="top">
      <a href="#ACCELCAL_VEHICLE_POS_RIGHT">ACCELCAL_VEHICLE_POS_RIGHT</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="ACCELCAL_VEHICLE_POS_NOSEDOWN">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#ACCELCAL_VEHICLE_POS_NOSEDOWN">ACCELCAL_VEHICLE_POS_NOSEDOWN</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="ACCELCAL_VEHICLE_POS_NOSEUP">
     <td class="mavlink_type" valign="top">5</td>
     <td class="mavlink_name" valign="top">
      <a href="#ACCELCAL_VEHICLE_POS_NOSEUP">ACCELCAL_VEHICLE_POS_NOSEUP</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="ACCELCAL_VEHICLE_POS_BACK">
     <td class="mavlink_type" valign="top">6</td>
     <td class="mavlink_name" valign="top">
      <a href="#ACCELCAL_VEHICLE_POS_BACK">ACCELCAL_VEHICLE_POS_BACK</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_MAV_CMD">
   <a href="#ENUM_MAV_CMD">MAV_CMD</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="MAV_CMD_DO_GRIPPER">
     <td class="mavlink_type" valign="top">211</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_DO_GRIPPER">MAV_CMD_DO_GRIPPER</a>
     </td>
     <td class="mavlink_comment">Mission command to operate EPM gripper</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #1</td>
     <td class="mavlink_comment">gripper number (a number from 1 to max number of grippers on the vehicle)</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #2</td>
     <td class="mavlink_comment">gripper action (0=release, 1=grab. See GRIPPER_ACTIONS enum)</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #3</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #4</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #5</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #6</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #7</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td colspan="3">
      <br/>
     </td>
    </tr>
    <tr class="mavlink_field" id="MAV_CMD_DO_AUTOTUNE_ENABLE">
     <td class="mavlink_type" valign="top">212</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_DO_AUTOTUNE_ENABLE">MAV_CMD_DO_AUTOTUNE_ENABLE</a>
     </td>
     <td class="mavlink_comment">Enable/disable autotune</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #1</td>
     <td class="mavlink_comment">enable (1: enable, 0:disable)</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #2</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #3</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #4</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #5</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #6</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #7</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td colspan="3">
      <br/>
     </td>
    </tr>
    <tr class="mavlink_field" id="MAV_CMD_NAV_ALTITUDE_WAIT">
     <td class="mavlink_type" valign="top">83</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_NAV_ALTITUDE_WAIT">MAV_CMD_NAV_ALTITUDE_WAIT</a>
     </td>
     <td class="mavlink_comment">Mission command to wait for an altitude or downwards vertical speed. This is meant for high altitude balloon launches, allowing the aircraft to be idle until either an altitude is reached or a negative vertical speed is reached (indicating early balloon burst). The wiggle time is how often to wiggle the control surfaces to prevent them seizing up.</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #1</td>
     <td class="mavlink_comment">altitude (m)</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #2</td>
     <td class="mavlink_comment">descent speed (m/s)</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #3</td>
     <td class="mavlink_comment">Wiggle Time (s)</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #4</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #5</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #6</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #7</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td colspan="3">
      <br/>
     </td>
    </tr>
    <tr class="mavlink_field" id="MAV_CMD_POWER_OFF_INITIATED">
     <td class="mavlink_type" valign="top">42000</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_POWER_OFF_INITIATED">MAV_CMD_POWER_OFF_INITIATED</a>
     </td>
     <td class="mavlink_comment">A system wide power-off event has been initiated.</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #1</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #2</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #3</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #4</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #5</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #6</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #7</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td colspan="3">
      <br/>
     </td>
    </tr>
    <tr class="mavlink_field" id="MAV_CMD_SOLO_BTN_FLY_CLICK">
     <td class="mavlink_type" valign="top">42001</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_SOLO_BTN_FLY_CLICK">MAV_CMD_SOLO_BTN_FLY_CLICK</a>
     </td>
     <td class="mavlink_comment">FLY button has been clicked.</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #1</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #2</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #3</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #4</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #5</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #6</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #7</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td colspan="3">
      <br/>
     </td>
    </tr>
    <tr class="mavlink_field" id="MAV_CMD_SOLO_BTN_FLY_HOLD">
     <td class="mavlink_type" valign="top">42002</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_SOLO_BTN_FLY_HOLD">MAV_CMD_SOLO_BTN_FLY_HOLD</a>
     </td>
     <td class="mavlink_comment">FLY button has been held for 1.5 seconds.</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #1</td>
     <td class="mavlink_comment">Takeoff altitude</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #2</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #3</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #4</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #5</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #6</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #7</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td colspan="3">
      <br/>
     </td>
    </tr>
    <tr class="mavlink_field" id="MAV_CMD_SOLO_BTN_PAUSE_CLICK">
     <td class="mavlink_type" valign="top">42003</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_SOLO_BTN_PAUSE_CLICK">MAV_CMD_SOLO_BTN_PAUSE_CLICK</a>
     </td>
     <td class="mavlink_comment">PAUSE button has been clicked.</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #1</td>
     <td class="mavlink_comment">1 if Solo is in a shot mode, 0 otherwise</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #2</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #3</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #4</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #5</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #6</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #7</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td colspan="3">
      <br/>
     </td>
    </tr>
    <tr class="mavlink_field" id="MAV_CMD_DO_START_MAG_CAL">
     <td class="mavlink_type" valign="top">42424</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_DO_START_MAG_CAL">MAV_CMD_DO_START_MAG_CAL</a>
     </td>
     <td class="mavlink_comment">Initiate a magnetometer calibration</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #1</td>
     <td class="mavlink_comment">uint8_t bitmask of magnetometers (0 means all)</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #2</td>
     <td class="mavlink_comment">Automatically retry on failure (0=no retry, 1=retry).</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #3</td>
     <td class="mavlink_comment">Save without user input (0=require input, 1=autosave).</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #4</td>
     <td class="mavlink_comment">Delay (seconds)</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #5</td>
     <td class="mavlink_comment">Autoreboot (0=user reboot, 1=autoreboot)</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #6</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #7</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td colspan="3">
      <br/>
     </td>
    </tr>
    <tr class="mavlink_field" id="MAV_CMD_DO_ACCEPT_MAG_CAL">
     <td class="mavlink_type" valign="top">42425</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_DO_ACCEPT_MAG_CAL">MAV_CMD_DO_ACCEPT_MAG_CAL</a>
     </td>
     <td class="mavlink_comment">Initiate a magnetometer calibration</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #1</td>
     <td class="mavlink_comment">uint8_t bitmask of magnetometers (0 means all)</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #2</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #3</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #4</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #5</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #6</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #7</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td colspan="3">
      <br/>
     </td>
    </tr>
    <tr class="mavlink_field" id="MAV_CMD_DO_CANCEL_MAG_CAL">
     <td class="mavlink_type" valign="top">42426</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_DO_CANCEL_MAG_CAL">MAV_CMD_DO_CANCEL_MAG_CAL</a>
     </td>
     <td class="mavlink_comment">Cancel a running magnetometer calibration</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #1</td>
     <td class="mavlink_comment">uint8_t bitmask of magnetometers (0 means all)</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #2</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #3</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #4</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #5</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #6</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #7</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td colspan="3">
      <br/>
     </td>
    </tr>
    <tr class="mavlink_field" id="MAV_CMD_ACCELCAL_VEHICLE_POS">
     <td class="mavlink_type" valign="top">42429</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_ACCELCAL_VEHICLE_POS">MAV_CMD_ACCELCAL_VEHICLE_POS</a>
     </td>
     <td class="mavlink_comment">Used when doing accelerometer calibration. When sent to the GCS tells it what position to put the vehicle in. When sent to the vehicle says what position the vehicle is in.</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #1</td>
     <td class="mavlink_comment">Position, one of the ACCELCAL_VEHICLE_POS enum values</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #2</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #3</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #4</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #5</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #6</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #7</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td colspan="3">
      <br/>
     </td>
    </tr>
    <tr class="mavlink_field" id="MAV_CMD_DO_SEND_BANNER">
     <td class="mavlink_type" valign="top">42428</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_DO_SEND_BANNER">MAV_CMD_DO_SEND_BANNER</a>
     </td>
     <td class="mavlink_comment">Reply with the version banner</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #1</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #2</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #3</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #4</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #5</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #6</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #7</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td colspan="3">
      <br/>
     </td>
    </tr>
    <tr class="mavlink_field" id="MAV_CMD_GIMBAL_RESET">
     <td class="mavlink_type" valign="top">42501</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_GIMBAL_RESET">MAV_CMD_GIMBAL_RESET</a>
     </td>
     <td class="mavlink_comment">Causes the gimbal to reset and boot as if it was just powered on</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #1</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #2</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #3</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #4</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #5</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #6</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #7</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td colspan="3">
      <br/>
     </td>
    </tr>
    <tr class="mavlink_field" id="MAV_CMD_SET_FACTORY_TEST_MODE">
     <td class="mavlink_type" valign="top">42427</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_SET_FACTORY_TEST_MODE">MAV_CMD_SET_FACTORY_TEST_MODE</a>
     </td>
     <td class="mavlink_comment">Command autopilot to get into factory test/diagnostic mode</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #1</td>
     <td class="mavlink_comment">0 means get out of test mode, 1 means get into test mode</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #2</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #3</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #4</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #5</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #6</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #7</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td colspan="3">
      <br/>
     </td>
    </tr>
    <tr class="mavlink_field" id="MAV_CMD_GIMBAL_AXIS_CALIBRATION_STATUS">
     <td class="mavlink_type" valign="top">42502</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_GIMBAL_AXIS_CALIBRATION_STATUS">MAV_CMD_GIMBAL_AXIS_CALIBRATION_STATUS</a>
     </td>
     <td class="mavlink_comment">Reports progress and success or failure of gimbal axis calibration procedure</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #1</td>
     <td class="mavlink_comment">Gimbal axis we're reporting calibration progress for</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #2</td>
     <td class="mavlink_comment">Current calibration progress for this axis, 0x64=100%</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #3</td>
     <td class="mavlink_comment">Status of the calibration</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #4</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #5</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #6</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #7</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td colspan="3">
      <br/>
     </td>
    </tr>
    <tr class="mavlink_field" id="MAV_CMD_GIMBAL_REQUEST_AXIS_CALIBRATION">
     <td class="mavlink_type" valign="top">42503</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_GIMBAL_REQUEST_AXIS_CALIBRATION">MAV_CMD_GIMBAL_REQUEST_AXIS_CALIBRATION</a>
     </td>
     <td class="mavlink_comment">Starts commutation calibration on the gimbal</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #1</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #2</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #3</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #4</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #5</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #6</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #7</td>
     <td class="mavlink_comment">Empty</td>
    </tr>
    <tr>
     <td colspan="3">
      <br/>
     </td>
    </tr>
    <tr class="mavlink_field" id="MAV_CMD_GIMBAL_FULL_RESET">
     <td class="mavlink_type" valign="top">42505</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_GIMBAL_FULL_RESET">MAV_CMD_GIMBAL_FULL_RESET</a>
     </td>
     <td class="mavlink_comment">Erases gimbal application and parameters</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #1</td>
     <td class="mavlink_comment">Magic number</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #2</td>
     <td class="mavlink_comment">Magic number</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #3</td>
     <td class="mavlink_comment">Magic number</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #4</td>
     <td class="mavlink_comment">Magic number</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #5</td>
     <td class="mavlink_comment">Magic number</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #6</td>
     <td class="mavlink_comment">Magic number</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #7</td>
     <td class="mavlink_comment">Magic number</td>
    </tr>
    <tr>
     <td colspan="3">
      <br/>
     </td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_LIMITS_STATE">
   <a href="#ENUM_LIMITS_STATE">LIMITS_STATE</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="LIMITS_INIT">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#LIMITS_INIT">LIMITS_INIT</a>
     </td>
     <td class="mavlink_comment">pre-initialization</td>
    </tr>
    <tr class="mavlink_field" id="LIMITS_DISABLED">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#LIMITS_DISABLED">LIMITS_DISABLED</a>
     </td>
     <td class="mavlink_comment">disabled</td>
    </tr>
    <tr class="mavlink_field" id="LIMITS_ENABLED">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#LIMITS_ENABLED">LIMITS_ENABLED</a>
     </td>
     <td class="mavlink_comment">checking limits</td>
    </tr>
    <tr class="mavlink_field" id="LIMITS_TRIGGERED">
     <td class="mavlink_type" valign="top">3</td>
     <td class="mavlink_name" valign="top">
      <a href="#LIMITS_TRIGGERED">LIMITS_TRIGGERED</a>
     </td>
     <td class="mavlink_comment">a limit has been breached</td>
    </tr>
    <tr class="mavlink_field" id="LIMITS_RECOVERING">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#LIMITS_RECOVERING">LIMITS_RECOVERING</a>
     </td>
     <td class="mavlink_comment">taking action eg. RTL</td>
    </tr>
    <tr class="mavlink_field" id="LIMITS_RECOVERED">
     <td class="mavlink_type" valign="top">5</td>
     <td class="mavlink_name" valign="top">
      <a href="#LIMITS_RECOVERED">LIMITS_RECOVERED</a>
     </td>
     <td class="mavlink_comment">we're no longer in breach of a limit</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_LIMIT_MODULE">
   <a href="#ENUM_LIMIT_MODULE">LIMIT_MODULE</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="LIMIT_GPSLOCK">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#LIMIT_GPSLOCK">LIMIT_GPSLOCK</a>
     </td>
     <td class="mavlink_comment">pre-initialization</td>
    </tr>
    <tr class="mavlink_field" id="LIMIT_GEOFENCE">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#LIMIT_GEOFENCE">LIMIT_GEOFENCE</a>
     </td>
     <td class="mavlink_comment">disabled</td>
    </tr>
    <tr class="mavlink_field" id="LIMIT_ALTITUDE">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#LIMIT_ALTITUDE">LIMIT_ALTITUDE</a>
     </td>
     <td class="mavlink_comment">checking limits</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_RALLY_FLAGS">
   <a href="#ENUM_RALLY_FLAGS">RALLY_FLAGS</a>
  </h3>
  <p class="description">Flags in RALLY_POINT message</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="FAVORABLE_WIND">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#FAVORABLE_WIND">FAVORABLE_WIND</a>
     </td>
     <td class="mavlink_comment">Flag set when requiring favorable winds for landing.</td>
    </tr>
    <tr class="mavlink_field" id="LAND_IMMEDIATELY">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#LAND_IMMEDIATELY">LAND_IMMEDIATELY</a>
     </td>
     <td class="mavlink_comment">Flag set when plane is to immediately descend to break altitude and land without GCS intervention. Flag not set when plane is to loiter at Rally point until commanded to land.</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_PARACHUTE_ACTION">
   <a href="#ENUM_PARACHUTE_ACTION">PARACHUTE_ACTION</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="PARACHUTE_DISABLE">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#PARACHUTE_DISABLE">PARACHUTE_DISABLE</a>
     </td>
     <td class="mavlink_comment">Disable parachute release</td>
    </tr>
    <tr class="mavlink_field" id="PARACHUTE_ENABLE">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#PARACHUTE_ENABLE">PARACHUTE_ENABLE</a>
     </td>
     <td class="mavlink_comment">Enable parachute release</td>
    </tr>
    <tr class="mavlink_field" id="PARACHUTE_RELEASE">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#PARACHUTE_RELEASE">PARACHUTE_RELEASE</a>
     </td>
     <td class="mavlink_comment">Release parachute</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_GRIPPER_ACTIONS">
   <a href="#ENUM_GRIPPER_ACTIONS">GRIPPER_ACTIONS</a>
  </h3>
  <p class="description">Gripper actions.</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="GRIPPER_ACTION_RELEASE">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#GRIPPER_ACTION_RELEASE">GRIPPER_ACTION_RELEASE</a>
     </td>
     <td class="mavlink_comment">gripper release of cargo</td>
    </tr>
    <tr class="mavlink_field" id="GRIPPER_ACTION_GRAB">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#GRIPPER_ACTION_GRAB">GRIPPER_ACTION_GRAB</a>
     </td>
     <td class="mavlink_comment">gripper grabs onto cargo</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_CAMERA_STATUS_TYPES">
   <a href="#ENUM_CAMERA_STATUS_TYPES">CAMERA_STATUS_TYPES</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="CAMERA_STATUS_TYPE_HEARTBEAT">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#CAMERA_STATUS_TYPE_HEARTBEAT">CAMERA_STATUS_TYPE_HEARTBEAT</a>
     </td>
     <td class="mavlink_comment">Camera heartbeat, announce camera component ID at 1hz</td>
    </tr>
    <tr class="mavlink_field" id="CAMERA_STATUS_TYPE_TRIGGER">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#CAMERA_STATUS_TYPE_TRIGGER">CAMERA_STATUS_TYPE_TRIGGER</a>
     </td>
     <td class="mavlink_comment">Camera image triggered</td>
    </tr>
    <tr class="mavlink_field" id="CAMERA_STATUS_TYPE_DISCONNECT">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#CAMERA_STATUS_TYPE_DISCONNECT">CAMERA_STATUS_TYPE_DISCONNECT</a>
     </td>
     <td class="mavlink_comment">Camera connection lost</td>
    </tr>
    <tr class="mavlink_field" id="CAMERA_STATUS_TYPE_ERROR">
     <td class="mavlink_type" valign="top">3</td>
     <td class="mavlink_name" valign="top">
      <a href="#CAMERA_STATUS_TYPE_ERROR">CAMERA_STATUS_TYPE_ERROR</a>
     </td>
     <td class="mavlink_comment">Camera unknown error</td>
    </tr>
    <tr class="mavlink_field" id="CAMERA_STATUS_TYPE_LOWBATT">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#CAMERA_STATUS_TYPE_LOWBATT">CAMERA_STATUS_TYPE_LOWBATT</a>
     </td>
     <td class="mavlink_comment">Camera battery low. Parameter p1 shows reported voltage</td>
    </tr>
    <tr class="mavlink_field" id="CAMERA_STATUS_TYPE_LOWSTORE">
     <td class="mavlink_type" valign="top">5</td>
     <td class="mavlink_name" valign="top">
      <a href="#CAMERA_STATUS_TYPE_LOWSTORE">CAMERA_STATUS_TYPE_LOWSTORE</a>
     </td>
     <td class="mavlink_comment">Camera storage low. Parameter p1 shows reported shots remaining</td>
    </tr>
    <tr class="mavlink_field" id="CAMERA_STATUS_TYPE_LOWSTOREV">
     <td class="mavlink_type" valign="top">6</td>
     <td class="mavlink_name" valign="top">
      <a href="#CAMERA_STATUS_TYPE_LOWSTOREV">CAMERA_STATUS_TYPE_LOWSTOREV</a>
     </td>
     <td class="mavlink_comment">Camera storage low. Parameter p1 shows reported video minutes remaining</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_CAMERA_FEEDBACK_FLAGS">
   <a href="#ENUM_CAMERA_FEEDBACK_FLAGS">CAMERA_FEEDBACK_FLAGS</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="CAMERA_FEEDBACK_PHOTO">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#CAMERA_FEEDBACK_PHOTO">CAMERA_FEEDBACK_PHOTO</a>
     </td>
     <td class="mavlink_comment">Shooting photos, not video</td>
    </tr>
    <tr class="mavlink_field" id="CAMERA_FEEDBACK_VIDEO">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#CAMERA_FEEDBACK_VIDEO">CAMERA_FEEDBACK_VIDEO</a>
     </td>
     <td class="mavlink_comment">Shooting video, not stills</td>
    </tr>
    <tr class="mavlink_field" id="CAMERA_FEEDBACK_BADEXPOSURE">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#CAMERA_FEEDBACK_BADEXPOSURE">CAMERA_FEEDBACK_BADEXPOSURE</a>
     </td>
     <td class="mavlink_comment">Unable to achieve requested exposure (e.g. shutter speed too low)</td>
    </tr>
    <tr class="mavlink_field" id="CAMERA_FEEDBACK_CLOSEDLOOP">
     <td class="mavlink_type" valign="top">3</td>
     <td class="mavlink_name" valign="top">
      <a href="#CAMERA_FEEDBACK_CLOSEDLOOP">CAMERA_FEEDBACK_CLOSEDLOOP</a>
     </td>
     <td class="mavlink_comment">Closed loop feedback from camera, we know for sure it has successfully taken a picture</td>
    </tr>
    <tr class="mavlink_field" id="CAMERA_FEEDBACK_OPENLOOP">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#CAMERA_FEEDBACK_OPENLOOP">CAMERA_FEEDBACK_OPENLOOP</a>
     </td>
     <td class="mavlink_comment">Open loop camera, an image trigger has been requested but we can't know for sure it has successfully taken a picture</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_MAV_MODE_GIMBAL">
   <a href="#ENUM_MAV_MODE_GIMBAL">MAV_MODE_GIMBAL</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="MAV_MODE_GIMBAL_UNINITIALIZED">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_MODE_GIMBAL_UNINITIALIZED">MAV_MODE_GIMBAL_UNINITIALIZED</a>
     </td>
     <td class="mavlink_comment">Gimbal is powered on but has not started initializing yet</td>
    </tr>
    <tr class="mavlink_field" id="MAV_MODE_GIMBAL_CALIBRATING_PITCH">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_MODE_GIMBAL_CALIBRATING_PITCH">MAV_MODE_GIMBAL_CALIBRATING_PITCH</a>
     </td>
     <td class="mavlink_comment">Gimbal is currently running calibration on the pitch axis</td>
    </tr>
    <tr class="mavlink_field" id="MAV_MODE_GIMBAL_CALIBRATING_ROLL">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_MODE_GIMBAL_CALIBRATING_ROLL">MAV_MODE_GIMBAL_CALIBRATING_ROLL</a>
     </td>
     <td class="mavlink_comment">Gimbal is currently running calibration on the roll axis</td>
    </tr>
    <tr class="mavlink_field" id="MAV_MODE_GIMBAL_CALIBRATING_YAW">
     <td class="mavlink_type" valign="top">3</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_MODE_GIMBAL_CALIBRATING_YAW">MAV_MODE_GIMBAL_CALIBRATING_YAW</a>
     </td>
     <td class="mavlink_comment">Gimbal is currently running calibration on the yaw axis</td>
    </tr>
    <tr class="mavlink_field" id="MAV_MODE_GIMBAL_INITIALIZED">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_MODE_GIMBAL_INITIALIZED">MAV_MODE_GIMBAL_INITIALIZED</a>
     </td>
     <td class="mavlink_comment">Gimbal has finished calibrating and initializing, but is relaxed pending reception of first rate command from copter</td>
    </tr>
    <tr class="mavlink_field" id="MAV_MODE_GIMBAL_ACTIVE">
     <td class="mavlink_type" valign="top">5</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_MODE_GIMBAL_ACTIVE">MAV_MODE_GIMBAL_ACTIVE</a>
     </td>
     <td class="mavlink_comment">Gimbal is actively stabilizing</td>
    </tr>
    <tr class="mavlink_field" id="MAV_MODE_GIMBAL_RATE_CMD_TIMEOUT">
     <td class="mavlink_type" valign="top">6</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_MODE_GIMBAL_RATE_CMD_TIMEOUT">MAV_MODE_GIMBAL_RATE_CMD_TIMEOUT</a>
     </td>
     <td class="mavlink_comment">Gimbal is relaxed because it missed more than 10 expected rate command messages in a row. Gimbal will move back to active mode when it receives a new rate command</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_GIMBAL_AXIS">
   <a href="#ENUM_GIMBAL_AXIS">GIMBAL_AXIS</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="GIMBAL_AXIS_YAW">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#GIMBAL_AXIS_YAW">GIMBAL_AXIS_YAW</a>
     </td>
     <td class="mavlink_comment">Gimbal yaw axis</td>
    </tr>
    <tr class="mavlink_field" id="GIMBAL_AXIS_PITCH">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#GIMBAL_AXIS_PITCH">GIMBAL_AXIS_PITCH</a>
     </td>
     <td class="mavlink_comment">Gimbal pitch axis</td>
    </tr>
    <tr class="mavlink_field" id="GIMBAL_AXIS_ROLL">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#GIMBAL_AXIS_ROLL">GIMBAL_AXIS_ROLL</a>
     </td>
     <td class="mavlink_comment">Gimbal roll axis</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_GIMBAL_AXIS_CALIBRATION_STATUS">
   <a href="#ENUM_GIMBAL_AXIS_CALIBRATION_STATUS">GIMBAL_AXIS_CALIBRATION_STATUS</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="GIMBAL_AXIS_CALIBRATION_STATUS_IN_PROGRESS">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#GIMBAL_AXIS_CALIBRATION_STATUS_IN_PROGRESS">GIMBAL_AXIS_CALIBRATION_STATUS_IN_PROGRESS</a>
     </td>
     <td class="mavlink_comment">Axis calibration is in progress</td>
    </tr>
    <tr class="mavlink_field" id="GIMBAL_AXIS_CALIBRATION_STATUS_SUCCEEDED">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#GIMBAL_AXIS_CALIBRATION_STATUS_SUCCEEDED">GIMBAL_AXIS_CALIBRATION_STATUS_SUCCEEDED</a>
     </td>
     <td class="mavlink_comment">Axis calibration succeeded</td>
    </tr>
    <tr class="mavlink_field" id="GIMBAL_AXIS_CALIBRATION_STATUS_FAILED">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#GIMBAL_AXIS_CALIBRATION_STATUS_FAILED">GIMBAL_AXIS_CALIBRATION_STATUS_FAILED</a>
     </td>
     <td class="mavlink_comment">Axis calibration failed</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_GIMBAL_AXIS_CALIBRATION_REQUIRED">
   <a href="#ENUM_GIMBAL_AXIS_CALIBRATION_REQUIRED">GIMBAL_AXIS_CALIBRATION_REQUIRED</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="GIMBAL_AXIS_CALIBRATION_REQUIRED_UNKNOWN">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#GIMBAL_AXIS_CALIBRATION_REQUIRED_UNKNOWN">GIMBAL_AXIS_CALIBRATION_REQUIRED_UNKNOWN</a>
     </td>
     <td class="mavlink_comment">Whether or not this axis requires calibration is unknown at this time</td>
    </tr>
    <tr class="mavlink_field" id="GIMBAL_AXIS_CALIBRATION_REQUIRED_TRUE">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#GIMBAL_AXIS_CALIBRATION_REQUIRED_TRUE">GIMBAL_AXIS_CALIBRATION_REQUIRED_TRUE</a>
     </td>
     <td class="mavlink_comment">This axis requires calibration</td>
    </tr>
    <tr class="mavlink_field" id="GIMBAL_AXIS_CALIBRATION_REQUIRED_FALSE">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#GIMBAL_AXIS_CALIBRATION_REQUIRED_FALSE">GIMBAL_AXIS_CALIBRATION_REQUIRED_FALSE</a>
     </td>
     <td class="mavlink_comment">This axis does not require calibration</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_GOPRO_HEARTBEAT_STATUS">
   <a href="#ENUM_GOPRO_HEARTBEAT_STATUS">GOPRO_HEARTBEAT_STATUS</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="GOPRO_HEARTBEAT_STATUS_DISCONNECTED">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_HEARTBEAT_STATUS_DISCONNECTED">GOPRO_HEARTBEAT_STATUS_DISCONNECTED</a>
     </td>
     <td class="mavlink_comment">No GoPro connected</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_HEARTBEAT_STATUS_INCOMPATIBLE">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_HEARTBEAT_STATUS_INCOMPATIBLE">GOPRO_HEARTBEAT_STATUS_INCOMPATIBLE</a>
     </td>
     <td class="mavlink_comment">The detected GoPro is not HeroBus compatible</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_HEARTBEAT_STATUS_CONNECTED">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_HEARTBEAT_STATUS_CONNECTED">GOPRO_HEARTBEAT_STATUS_CONNECTED</a>
     </td>
     <td class="mavlink_comment">A HeroBus compatible GoPro is connected</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_HEARTBEAT_STATUS_ERROR">
     <td class="mavlink_type" valign="top">3</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_HEARTBEAT_STATUS_ERROR">GOPRO_HEARTBEAT_STATUS_ERROR</a>
     </td>
     <td class="mavlink_comment">An unrecoverable error was encountered with the connected GoPro, it may require a power cycle</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_GOPRO_HEARTBEAT_FLAGS">
   <a href="#ENUM_GOPRO_HEARTBEAT_FLAGS">GOPRO_HEARTBEAT_FLAGS</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="GOPRO_FLAG_RECORDING">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_FLAG_RECORDING">GOPRO_FLAG_RECORDING</a>
     </td>
     <td class="mavlink_comment">GoPro is currently recording</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_GOPRO_REQUEST_STATUS">
   <a href="#ENUM_GOPRO_REQUEST_STATUS">GOPRO_REQUEST_STATUS</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="GOPRO_REQUEST_SUCCESS">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_REQUEST_SUCCESS">GOPRO_REQUEST_SUCCESS</a>
     </td>
     <td class="mavlink_comment">The write message with ID indicated succeeded</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_REQUEST_FAILED">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_REQUEST_FAILED">GOPRO_REQUEST_FAILED</a>
     </td>
     <td class="mavlink_comment">The write message with ID indicated failed</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_GOPRO_COMMAND">
   <a href="#ENUM_GOPRO_COMMAND">GOPRO_COMMAND</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="GOPRO_COMMAND_POWER">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_COMMAND_POWER">GOPRO_COMMAND_POWER</a>
     </td>
     <td class="mavlink_comment">
      (Get/Set)
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_COMMAND_CAPTURE_MODE">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_COMMAND_CAPTURE_MODE">GOPRO_COMMAND_CAPTURE_MODE</a>
     </td>
     <td class="mavlink_comment">
      (Get/Set)
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_COMMAND_SHUTTER">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_COMMAND_SHUTTER">GOPRO_COMMAND_SHUTTER</a>
     </td>
     <td class="mavlink_comment">
      (___/Set)
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_COMMAND_BATTERY">
     <td class="mavlink_type" valign="top">3</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_COMMAND_BATTERY">GOPRO_COMMAND_BATTERY</a>
     </td>
     <td class="mavlink_comment">
      (Get/___)
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_COMMAND_MODEL">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_COMMAND_MODEL">GOPRO_COMMAND_MODEL</a>
     </td>
     <td class="mavlink_comment">
      (Get/___)
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_COMMAND_VIDEO_SETTINGS">
     <td class="mavlink_type" valign="top">5</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_COMMAND_VIDEO_SETTINGS">GOPRO_COMMAND_VIDEO_SETTINGS</a>
     </td>
     <td class="mavlink_comment">
      (Get/Set)
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_COMMAND_LOW_LIGHT">
     <td class="mavlink_type" valign="top">6</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_COMMAND_LOW_LIGHT">GOPRO_COMMAND_LOW_LIGHT</a>
     </td>
     <td class="mavlink_comment">
      (Get/Set)
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_COMMAND_PHOTO_RESOLUTION">
     <td class="mavlink_type" valign="top">7</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_COMMAND_PHOTO_RESOLUTION">GOPRO_COMMAND_PHOTO_RESOLUTION</a>
     </td>
     <td class="mavlink_comment">
      (Get/Set)
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_COMMAND_PHOTO_BURST_RATE">
     <td class="mavlink_type" valign="top">8</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_COMMAND_PHOTO_BURST_RATE">GOPRO_COMMAND_PHOTO_BURST_RATE</a>
     </td>
     <td class="mavlink_comment">
      (Get/Set)
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_COMMAND_PROTUNE">
     <td class="mavlink_type" valign="top">9</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_COMMAND_PROTUNE">GOPRO_COMMAND_PROTUNE</a>
     </td>
     <td class="mavlink_comment">
      (Get/Set)
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_COMMAND_PROTUNE_WHITE_BALANCE">
     <td class="mavlink_type" valign="top">10</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_COMMAND_PROTUNE_WHITE_BALANCE">GOPRO_COMMAND_PROTUNE_WHITE_BALANCE</a>
     </td>
     <td class="mavlink_comment">
      (Get/Set) Hero 3+ Only
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_COMMAND_PROTUNE_COLOUR">
     <td class="mavlink_type" valign="top">11</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_COMMAND_PROTUNE_COLOUR">GOPRO_COMMAND_PROTUNE_COLOUR</a>
     </td>
     <td class="mavlink_comment">
      (Get/Set) Hero 3+ Only
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_COMMAND_PROTUNE_GAIN">
     <td class="mavlink_type" valign="top">12</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_COMMAND_PROTUNE_GAIN">GOPRO_COMMAND_PROTUNE_GAIN</a>
     </td>
     <td class="mavlink_comment">
      (Get/Set) Hero 3+ Only
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_COMMAND_PROTUNE_SHARPNESS">
     <td class="mavlink_type" valign="top">13</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_COMMAND_PROTUNE_SHARPNESS">GOPRO_COMMAND_PROTUNE_SHARPNESS</a>
     </td>
     <td class="mavlink_comment">
      (Get/Set) Hero 3+ Only
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_COMMAND_PROTUNE_EXPOSURE">
     <td class="mavlink_type" valign="top">14</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_COMMAND_PROTUNE_EXPOSURE">GOPRO_COMMAND_PROTUNE_EXPOSURE</a>
     </td>
     <td class="mavlink_comment">
      (Get/Set) Hero 3+ Only
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_COMMAND_TIME">
     <td class="mavlink_type" valign="top">15</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_COMMAND_TIME">GOPRO_COMMAND_TIME</a>
     </td>
     <td class="mavlink_comment">
      (Get/Set)
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_COMMAND_CHARGING">
     <td class="mavlink_type" valign="top">16</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_COMMAND_CHARGING">GOPRO_COMMAND_CHARGING</a>
     </td>
     <td class="mavlink_comment">
      (Get/Set)
     </td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_GOPRO_CAPTURE_MODE">
   <a href="#ENUM_GOPRO_CAPTURE_MODE">GOPRO_CAPTURE_MODE</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="GOPRO_CAPTURE_MODE_VIDEO">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_CAPTURE_MODE_VIDEO">GOPRO_CAPTURE_MODE_VIDEO</a>
     </td>
     <td class="mavlink_comment">Video mode</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_CAPTURE_MODE_PHOTO">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_CAPTURE_MODE_PHOTO">GOPRO_CAPTURE_MODE_PHOTO</a>
     </td>
     <td class="mavlink_comment">Photo mode</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_CAPTURE_MODE_BURST">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_CAPTURE_MODE_BURST">GOPRO_CAPTURE_MODE_BURST</a>
     </td>
     <td class="mavlink_comment">Burst mode, hero 3+ only</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_CAPTURE_MODE_TIME_LAPSE">
     <td class="mavlink_type" valign="top">3</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_CAPTURE_MODE_TIME_LAPSE">GOPRO_CAPTURE_MODE_TIME_LAPSE</a>
     </td>
     <td class="mavlink_comment">Time lapse mode, hero 3+ only</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_CAPTURE_MODE_MULTI_SHOT">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_CAPTURE_MODE_MULTI_SHOT">GOPRO_CAPTURE_MODE_MULTI_SHOT</a>
     </td>
     <td class="mavlink_comment">Multi shot mode, hero 4 only</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_CAPTURE_MODE_PLAYBACK">
     <td class="mavlink_type" valign="top">5</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_CAPTURE_MODE_PLAYBACK">GOPRO_CAPTURE_MODE_PLAYBACK</a>
     </td>
     <td class="mavlink_comment">Playback mode, hero 4 only, silver only except when LCD or HDMI is connected to black</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_CAPTURE_MODE_SETUP">
     <td class="mavlink_type" valign="top">6</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_CAPTURE_MODE_SETUP">GOPRO_CAPTURE_MODE_SETUP</a>
     </td>
     <td class="mavlink_comment">Playback mode, hero 4 only</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_CAPTURE_MODE_UNKNOWN">
     <td class="mavlink_type" valign="top">255</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_CAPTURE_MODE_UNKNOWN">GOPRO_CAPTURE_MODE_UNKNOWN</a>
     </td>
     <td class="mavlink_comment">Mode not yet known</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_GOPRO_RESOLUTION">
   <a href="#ENUM_GOPRO_RESOLUTION">GOPRO_RESOLUTION</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="GOPRO_RESOLUTION_480p">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_RESOLUTION_480p">GOPRO_RESOLUTION_480p</a>
     </td>
     <td class="mavlink_comment">848 x 480 (480p)</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_RESOLUTION_720p">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_RESOLUTION_720p">GOPRO_RESOLUTION_720p</a>
     </td>
     <td class="mavlink_comment">1280 x 720 (720p)</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_RESOLUTION_960p">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_RESOLUTION_960p">GOPRO_RESOLUTION_960p</a>
     </td>
     <td class="mavlink_comment">1280 x 960 (960p)</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_RESOLUTION_1080p">
     <td class="mavlink_type" valign="top">3</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_RESOLUTION_1080p">GOPRO_RESOLUTION_1080p</a>
     </td>
     <td class="mavlink_comment">1920 x 1080 (1080p)</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_RESOLUTION_1440p">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_RESOLUTION_1440p">GOPRO_RESOLUTION_1440p</a>
     </td>
     <td class="mavlink_comment">1920 x 1440 (1440p)</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_RESOLUTION_2_7k_17_9">
     <td class="mavlink_type" valign="top">5</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_RESOLUTION_2_7k_17_9">GOPRO_RESOLUTION_2_7k_17_9</a>
     </td>
     <td class="mavlink_comment">2704 x 1440 (2.7k-17:9)</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_RESOLUTION_2_7k_16_9">
     <td class="mavlink_type" valign="top">6</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_RESOLUTION_2_7k_16_9">GOPRO_RESOLUTION_2_7k_16_9</a>
     </td>
     <td class="mavlink_comment">2704 x 1524 (2.7k-16:9)</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_RESOLUTION_2_7k_4_3">
     <td class="mavlink_type" valign="top">7</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_RESOLUTION_2_7k_4_3">GOPRO_RESOLUTION_2_7k_4_3</a>
     </td>
     <td class="mavlink_comment">2704 x 2028 (2.7k-4:3)</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_RESOLUTION_4k_16_9">
     <td class="mavlink_type" valign="top">8</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_RESOLUTION_4k_16_9">GOPRO_RESOLUTION_4k_16_9</a>
     </td>
     <td class="mavlink_comment">3840 x 2160 (4k-16:9)</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_RESOLUTION_4k_17_9">
     <td class="mavlink_type" valign="top">9</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_RESOLUTION_4k_17_9">GOPRO_RESOLUTION_4k_17_9</a>
     </td>
     <td class="mavlink_comment">4096 x 2160 (4k-17:9)</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_RESOLUTION_720p_SUPERVIEW">
     <td class="mavlink_type" valign="top">10</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_RESOLUTION_720p_SUPERVIEW">GOPRO_RESOLUTION_720p_SUPERVIEW</a>
     </td>
     <td class="mavlink_comment">1280 x 720 (720p-SuperView)</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_RESOLUTION_1080p_SUPERVIEW">
     <td class="mavlink_type" valign="top">11</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_RESOLUTION_1080p_SUPERVIEW">GOPRO_RESOLUTION_1080p_SUPERVIEW</a>
     </td>
     <td class="mavlink_comment">1920 x 1080 (1080p-SuperView)</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_RESOLUTION_2_7k_SUPERVIEW">
     <td class="mavlink_type" valign="top">12</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_RESOLUTION_2_7k_SUPERVIEW">GOPRO_RESOLUTION_2_7k_SUPERVIEW</a>
     </td>
     <td class="mavlink_comment">2704 x 1520 (2.7k-SuperView)</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_RESOLUTION_4k_SUPERVIEW">
     <td class="mavlink_type" valign="top">13</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_RESOLUTION_4k_SUPERVIEW">GOPRO_RESOLUTION_4k_SUPERVIEW</a>
     </td>
     <td class="mavlink_comment">3840 x 2160 (4k-SuperView)</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_GOPRO_FRAME_RATE">
   <a href="#ENUM_GOPRO_FRAME_RATE">GOPRO_FRAME_RATE</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="GOPRO_FRAME_RATE_12">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_FRAME_RATE_12">GOPRO_FRAME_RATE_12</a>
     </td>
     <td class="mavlink_comment">12 FPS</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_FRAME_RATE_15">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_FRAME_RATE_15">GOPRO_FRAME_RATE_15</a>
     </td>
     <td class="mavlink_comment">15 FPS</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_FRAME_RATE_24">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_FRAME_RATE_24">GOPRO_FRAME_RATE_24</a>
     </td>
     <td class="mavlink_comment">24 FPS</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_FRAME_RATE_25">
     <td class="mavlink_type" valign="top">3</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_FRAME_RATE_25">GOPRO_FRAME_RATE_25</a>
     </td>
     <td class="mavlink_comment">25 FPS</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_FRAME_RATE_30">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_FRAME_RATE_30">GOPRO_FRAME_RATE_30</a>
     </td>
     <td class="mavlink_comment">30 FPS</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_FRAME_RATE_48">
     <td class="mavlink_type" valign="top">5</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_FRAME_RATE_48">GOPRO_FRAME_RATE_48</a>
     </td>
     <td class="mavlink_comment">48 FPS</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_FRAME_RATE_50">
     <td class="mavlink_type" valign="top">6</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_FRAME_RATE_50">GOPRO_FRAME_RATE_50</a>
     </td>
     <td class="mavlink_comment">50 FPS</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_FRAME_RATE_60">
     <td class="mavlink_type" valign="top">7</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_FRAME_RATE_60">GOPRO_FRAME_RATE_60</a>
     </td>
     <td class="mavlink_comment">60 FPS</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_FRAME_RATE_80">
     <td class="mavlink_type" valign="top">8</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_FRAME_RATE_80">GOPRO_FRAME_RATE_80</a>
     </td>
     <td class="mavlink_comment">80 FPS</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_FRAME_RATE_90">
     <td class="mavlink_type" valign="top">9</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_FRAME_RATE_90">GOPRO_FRAME_RATE_90</a>
     </td>
     <td class="mavlink_comment">90 FPS</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_FRAME_RATE_100">
     <td class="mavlink_type" valign="top">10</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_FRAME_RATE_100">GOPRO_FRAME_RATE_100</a>
     </td>
     <td class="mavlink_comment">100 FPS</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_FRAME_RATE_120">
     <td class="mavlink_type" valign="top">11</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_FRAME_RATE_120">GOPRO_FRAME_RATE_120</a>
     </td>
     <td class="mavlink_comment">120 FPS</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_FRAME_RATE_240">
     <td class="mavlink_type" valign="top">12</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_FRAME_RATE_240">GOPRO_FRAME_RATE_240</a>
     </td>
     <td class="mavlink_comment">240 FPS</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_FRAME_RATE_12_5">
     <td class="mavlink_type" valign="top">13</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_FRAME_RATE_12_5">GOPRO_FRAME_RATE_12_5</a>
     </td>
     <td class="mavlink_comment">12.5 FPS</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_GOPRO_FIELD_OF_VIEW">
   <a href="#ENUM_GOPRO_FIELD_OF_VIEW">GOPRO_FIELD_OF_VIEW</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="GOPRO_FIELD_OF_VIEW_WIDE">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_FIELD_OF_VIEW_WIDE">GOPRO_FIELD_OF_VIEW_WIDE</a>
     </td>
     <td class="mavlink_comment">0x00: Wide</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_FIELD_OF_VIEW_MEDIUM">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_FIELD_OF_VIEW_MEDIUM">GOPRO_FIELD_OF_VIEW_MEDIUM</a>
     </td>
     <td class="mavlink_comment">0x01: Medium</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_FIELD_OF_VIEW_NARROW">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_FIELD_OF_VIEW_NARROW">GOPRO_FIELD_OF_VIEW_NARROW</a>
     </td>
     <td class="mavlink_comment">0x02: Narrow</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_GOPRO_VIDEO_SETTINGS_FLAGS">
   <a href="#ENUM_GOPRO_VIDEO_SETTINGS_FLAGS">GOPRO_VIDEO_SETTINGS_FLAGS</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="GOPRO_VIDEO_SETTINGS_TV_MODE">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_VIDEO_SETTINGS_TV_MODE">GOPRO_VIDEO_SETTINGS_TV_MODE</a>
     </td>
     <td class="mavlink_comment">0=NTSC, 1=PAL</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_GOPRO_PHOTO_RESOLUTION">
   <a href="#ENUM_GOPRO_PHOTO_RESOLUTION">GOPRO_PHOTO_RESOLUTION</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="GOPRO_PHOTO_RESOLUTION_5MP_MEDIUM">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PHOTO_RESOLUTION_5MP_MEDIUM">GOPRO_PHOTO_RESOLUTION_5MP_MEDIUM</a>
     </td>
     <td class="mavlink_comment">5MP Medium</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PHOTO_RESOLUTION_7MP_MEDIUM">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PHOTO_RESOLUTION_7MP_MEDIUM">GOPRO_PHOTO_RESOLUTION_7MP_MEDIUM</a>
     </td>
     <td class="mavlink_comment">7MP Medium</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PHOTO_RESOLUTION_7MP_WIDE">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PHOTO_RESOLUTION_7MP_WIDE">GOPRO_PHOTO_RESOLUTION_7MP_WIDE</a>
     </td>
     <td class="mavlink_comment">7MP Wide</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PHOTO_RESOLUTION_10MP_WIDE">
     <td class="mavlink_type" valign="top">3</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PHOTO_RESOLUTION_10MP_WIDE">GOPRO_PHOTO_RESOLUTION_10MP_WIDE</a>
     </td>
     <td class="mavlink_comment">10MP Wide</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PHOTO_RESOLUTION_12MP_WIDE">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PHOTO_RESOLUTION_12MP_WIDE">GOPRO_PHOTO_RESOLUTION_12MP_WIDE</a>
     </td>
     <td class="mavlink_comment">12MP Wide</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_GOPRO_PROTUNE_WHITE_BALANCE">
   <a href="#ENUM_GOPRO_PROTUNE_WHITE_BALANCE">GOPRO_PROTUNE_WHITE_BALANCE</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_WHITE_BALANCE_AUTO">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_WHITE_BALANCE_AUTO">GOPRO_PROTUNE_WHITE_BALANCE_AUTO</a>
     </td>
     <td class="mavlink_comment">Auto</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_WHITE_BALANCE_3000K">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_WHITE_BALANCE_3000K">GOPRO_PROTUNE_WHITE_BALANCE_3000K</a>
     </td>
     <td class="mavlink_comment">3000K</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_WHITE_BALANCE_5500K">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_WHITE_BALANCE_5500K">GOPRO_PROTUNE_WHITE_BALANCE_5500K</a>
     </td>
     <td class="mavlink_comment">5500K</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_WHITE_BALANCE_6500K">
     <td class="mavlink_type" valign="top">3</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_WHITE_BALANCE_6500K">GOPRO_PROTUNE_WHITE_BALANCE_6500K</a>
     </td>
     <td class="mavlink_comment">6500K</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_WHITE_BALANCE_RAW">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_WHITE_BALANCE_RAW">GOPRO_PROTUNE_WHITE_BALANCE_RAW</a>
     </td>
     <td class="mavlink_comment">Camera Raw</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_GOPRO_PROTUNE_COLOUR">
   <a href="#ENUM_GOPRO_PROTUNE_COLOUR">GOPRO_PROTUNE_COLOUR</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_COLOUR_STANDARD">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_COLOUR_STANDARD">GOPRO_PROTUNE_COLOUR_STANDARD</a>
     </td>
     <td class="mavlink_comment">Auto</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_COLOUR_NEUTRAL">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_COLOUR_NEUTRAL">GOPRO_PROTUNE_COLOUR_NEUTRAL</a>
     </td>
     <td class="mavlink_comment">Neutral</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_GOPRO_PROTUNE_GAIN">
   <a href="#ENUM_GOPRO_PROTUNE_GAIN">GOPRO_PROTUNE_GAIN</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_GAIN_400">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_GAIN_400">GOPRO_PROTUNE_GAIN_400</a>
     </td>
     <td class="mavlink_comment">ISO 400</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_GAIN_800">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_GAIN_800">GOPRO_PROTUNE_GAIN_800</a>
     </td>
     <td class="mavlink_comment">ISO 800 (Only Hero 4)</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_GAIN_1600">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_GAIN_1600">GOPRO_PROTUNE_GAIN_1600</a>
     </td>
     <td class="mavlink_comment">ISO 1600</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_GAIN_3200">
     <td class="mavlink_type" valign="top">3</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_GAIN_3200">GOPRO_PROTUNE_GAIN_3200</a>
     </td>
     <td class="mavlink_comment">ISO 3200 (Only Hero 4)</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_GAIN_6400">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_GAIN_6400">GOPRO_PROTUNE_GAIN_6400</a>
     </td>
     <td class="mavlink_comment">ISO 6400</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_GOPRO_PROTUNE_SHARPNESS">
   <a href="#ENUM_GOPRO_PROTUNE_SHARPNESS">GOPRO_PROTUNE_SHARPNESS</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_SHARPNESS_LOW">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_SHARPNESS_LOW">GOPRO_PROTUNE_SHARPNESS_LOW</a>
     </td>
     <td class="mavlink_comment">Low Sharpness</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_SHARPNESS_MEDIUM">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_SHARPNESS_MEDIUM">GOPRO_PROTUNE_SHARPNESS_MEDIUM</a>
     </td>
     <td class="mavlink_comment">Medium Sharpness</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_SHARPNESS_HIGH">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_SHARPNESS_HIGH">GOPRO_PROTUNE_SHARPNESS_HIGH</a>
     </td>
     <td class="mavlink_comment">High Sharpness</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_GOPRO_PROTUNE_EXPOSURE">
   <a href="#ENUM_GOPRO_PROTUNE_EXPOSURE">GOPRO_PROTUNE_EXPOSURE</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_EXPOSURE_NEG_5_0">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_EXPOSURE_NEG_5_0">GOPRO_PROTUNE_EXPOSURE_NEG_5_0</a>
     </td>
     <td class="mavlink_comment">
      -5.0 EV (Hero 3+ Only)
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_EXPOSURE_NEG_4_5">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_EXPOSURE_NEG_4_5">GOPRO_PROTUNE_EXPOSURE_NEG_4_5</a>
     </td>
     <td class="mavlink_comment">
      -4.5 EV (Hero 3+ Only)
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_EXPOSURE_NEG_4_0">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_EXPOSURE_NEG_4_0">GOPRO_PROTUNE_EXPOSURE_NEG_4_0</a>
     </td>
     <td class="mavlink_comment">
      -4.0 EV (Hero 3+ Only)
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_EXPOSURE_NEG_3_5">
     <td class="mavlink_type" valign="top">3</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_EXPOSURE_NEG_3_5">GOPRO_PROTUNE_EXPOSURE_NEG_3_5</a>
     </td>
     <td class="mavlink_comment">
      -3.5 EV (Hero 3+ Only)
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_EXPOSURE_NEG_3_0">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_EXPOSURE_NEG_3_0">GOPRO_PROTUNE_EXPOSURE_NEG_3_0</a>
     </td>
     <td class="mavlink_comment">
      -3.0 EV (Hero 3+ Only)
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_EXPOSURE_NEG_2_5">
     <td class="mavlink_type" valign="top">5</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_EXPOSURE_NEG_2_5">GOPRO_PROTUNE_EXPOSURE_NEG_2_5</a>
     </td>
     <td class="mavlink_comment">
      -2.5 EV (Hero 3+ Only)
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_EXPOSURE_NEG_2_0">
     <td class="mavlink_type" valign="top">6</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_EXPOSURE_NEG_2_0">GOPRO_PROTUNE_EXPOSURE_NEG_2_0</a>
     </td>
     <td class="mavlink_comment">
      -2.0 EV
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_EXPOSURE_NEG_1_5">
     <td class="mavlink_type" valign="top">7</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_EXPOSURE_NEG_1_5">GOPRO_PROTUNE_EXPOSURE_NEG_1_5</a>
     </td>
     <td class="mavlink_comment">
      -1.5 EV
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_EXPOSURE_NEG_1_0">
     <td class="mavlink_type" valign="top">8</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_EXPOSURE_NEG_1_0">GOPRO_PROTUNE_EXPOSURE_NEG_1_0</a>
     </td>
     <td class="mavlink_comment">
      -1.0 EV
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_EXPOSURE_NEG_0_5">
     <td class="mavlink_type" valign="top">9</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_EXPOSURE_NEG_0_5">GOPRO_PROTUNE_EXPOSURE_NEG_0_5</a>
     </td>
     <td class="mavlink_comment">
      -0.5 EV
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_EXPOSURE_ZERO">
     <td class="mavlink_type" valign="top">10</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_EXPOSURE_ZERO">GOPRO_PROTUNE_EXPOSURE_ZERO</a>
     </td>
     <td class="mavlink_comment">0.0 EV</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_EXPOSURE_POS_0_5">
     <td class="mavlink_type" valign="top">11</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_EXPOSURE_POS_0_5">GOPRO_PROTUNE_EXPOSURE_POS_0_5</a>
     </td>
     <td class="mavlink_comment">
      +0.5 EV
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_EXPOSURE_POS_1_0">
     <td class="mavlink_type" valign="top">12</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_EXPOSURE_POS_1_0">GOPRO_PROTUNE_EXPOSURE_POS_1_0</a>
     </td>
     <td class="mavlink_comment">
      +1.0 EV
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_EXPOSURE_POS_1_5">
     <td class="mavlink_type" valign="top">13</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_EXPOSURE_POS_1_5">GOPRO_PROTUNE_EXPOSURE_POS_1_5</a>
     </td>
     <td class="mavlink_comment">
      +1.5 EV
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_EXPOSURE_POS_2_0">
     <td class="mavlink_type" valign="top">14</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_EXPOSURE_POS_2_0">GOPRO_PROTUNE_EXPOSURE_POS_2_0</a>
     </td>
     <td class="mavlink_comment">
      +2.0 EV
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_EXPOSURE_POS_2_5">
     <td class="mavlink_type" valign="top">15</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_EXPOSURE_POS_2_5">GOPRO_PROTUNE_EXPOSURE_POS_2_5</a>
     </td>
     <td class="mavlink_comment">
      +2.5 EV (Hero 3+ Only)
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_EXPOSURE_POS_3_0">
     <td class="mavlink_type" valign="top">16</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_EXPOSURE_POS_3_0">GOPRO_PROTUNE_EXPOSURE_POS_3_0</a>
     </td>
     <td class="mavlink_comment">
      +3.0 EV (Hero 3+ Only)
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_EXPOSURE_POS_3_5">
     <td class="mavlink_type" valign="top">17</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_EXPOSURE_POS_3_5">GOPRO_PROTUNE_EXPOSURE_POS_3_5</a>
     </td>
     <td class="mavlink_comment">
      +3.5 EV (Hero 3+ Only)
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_EXPOSURE_POS_4_0">
     <td class="mavlink_type" valign="top">18</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_EXPOSURE_POS_4_0">GOPRO_PROTUNE_EXPOSURE_POS_4_0</a>
     </td>
     <td class="mavlink_comment">
      +4.0 EV (Hero 3+ Only)
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_EXPOSURE_POS_4_5">
     <td class="mavlink_type" valign="top">19</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_EXPOSURE_POS_4_5">GOPRO_PROTUNE_EXPOSURE_POS_4_5</a>
     </td>
     <td class="mavlink_comment">
      +4.5 EV (Hero 3+ Only)
     </td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_PROTUNE_EXPOSURE_POS_5_0">
     <td class="mavlink_type" valign="top">20</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_PROTUNE_EXPOSURE_POS_5_0">GOPRO_PROTUNE_EXPOSURE_POS_5_0</a>
     </td>
     <td class="mavlink_comment">
      +5.0 EV (Hero 3+ Only)
     </td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_GOPRO_CHARGING">
   <a href="#ENUM_GOPRO_CHARGING">GOPRO_CHARGING</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="GOPRO_CHARGING_DISABLED">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_CHARGING_DISABLED">GOPRO_CHARGING_DISABLED</a>
     </td>
     <td class="mavlink_comment">Charging disabled</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_CHARGING_ENABLED">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_CHARGING_ENABLED">GOPRO_CHARGING_ENABLED</a>
     </td>
     <td class="mavlink_comment">Charging enabled</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_GOPRO_MODEL">
   <a href="#ENUM_GOPRO_MODEL">GOPRO_MODEL</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="GOPRO_MODEL_UNKNOWN">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_MODEL_UNKNOWN">GOPRO_MODEL_UNKNOWN</a>
     </td>
     <td class="mavlink_comment">Unknown gopro model</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_MODEL_HERO_3_PLUS_SILVER">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_MODEL_HERO_3_PLUS_SILVER">GOPRO_MODEL_HERO_3_PLUS_SILVER</a>
     </td>
     <td class="mavlink_comment">Hero 3+ Silver (HeroBus not supported by GoPro)</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_MODEL_HERO_3_PLUS_BLACK">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_MODEL_HERO_3_PLUS_BLACK">GOPRO_MODEL_HERO_3_PLUS_BLACK</a>
     </td>
     <td class="mavlink_comment">Hero 3+ Black</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_MODEL_HERO_4_SILVER">
     <td class="mavlink_type" valign="top">3</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_MODEL_HERO_4_SILVER">GOPRO_MODEL_HERO_4_SILVER</a>
     </td>
     <td class="mavlink_comment">Hero 4 Silver</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_MODEL_HERO_4_BLACK">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_MODEL_HERO_4_BLACK">GOPRO_MODEL_HERO_4_BLACK</a>
     </td>
     <td class="mavlink_comment">Hero 4 Black</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_GOPRO_BURST_RATE">
   <a href="#ENUM_GOPRO_BURST_RATE">GOPRO_BURST_RATE</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="GOPRO_BURST_RATE_3_IN_1_SECOND">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_BURST_RATE_3_IN_1_SECOND">GOPRO_BURST_RATE_3_IN_1_SECOND</a>
     </td>
     <td class="mavlink_comment">3 Shots / 1 Second</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_BURST_RATE_5_IN_1_SECOND">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_BURST_RATE_5_IN_1_SECOND">GOPRO_BURST_RATE_5_IN_1_SECOND</a>
     </td>
     <td class="mavlink_comment">5 Shots / 1 Second</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_BURST_RATE_10_IN_1_SECOND">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_BURST_RATE_10_IN_1_SECOND">GOPRO_BURST_RATE_10_IN_1_SECOND</a>
     </td>
     <td class="mavlink_comment">10 Shots / 1 Second</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_BURST_RATE_10_IN_2_SECOND">
     <td class="mavlink_type" valign="top">3</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_BURST_RATE_10_IN_2_SECOND">GOPRO_BURST_RATE_10_IN_2_SECOND</a>
     </td>
     <td class="mavlink_comment">10 Shots / 2 Second</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_BURST_RATE_10_IN_3_SECOND">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_BURST_RATE_10_IN_3_SECOND">GOPRO_BURST_RATE_10_IN_3_SECOND</a>
     </td>
     <td class="mavlink_comment">10 Shots / 3 Second (Hero 4 Only)</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_BURST_RATE_30_IN_1_SECOND">
     <td class="mavlink_type" valign="top">5</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_BURST_RATE_30_IN_1_SECOND">GOPRO_BURST_RATE_30_IN_1_SECOND</a>
     </td>
     <td class="mavlink_comment">30 Shots / 1 Second</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_BURST_RATE_30_IN_2_SECOND">
     <td class="mavlink_type" valign="top">6</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_BURST_RATE_30_IN_2_SECOND">GOPRO_BURST_RATE_30_IN_2_SECOND</a>
     </td>
     <td class="mavlink_comment">30 Shots / 2 Second</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_BURST_RATE_30_IN_3_SECOND">
     <td class="mavlink_type" valign="top">7</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_BURST_RATE_30_IN_3_SECOND">GOPRO_BURST_RATE_30_IN_3_SECOND</a>
     </td>
     <td class="mavlink_comment">30 Shots / 3 Second</td>
    </tr>
    <tr class="mavlink_field" id="GOPRO_BURST_RATE_30_IN_6_SECOND">
     <td class="mavlink_type" valign="top">8</td>
     <td class="mavlink_name" valign="top">
      <a href="#GOPRO_BURST_RATE_30_IN_6_SECOND">GOPRO_BURST_RATE_30_IN_6_SECOND</a>
     </td>
     <td class="mavlink_comment">30 Shots / 6 Second</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_LED_CONTROL_PATTERN">
   <a href="#ENUM_LED_CONTROL_PATTERN">LED_CONTROL_PATTERN</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="LED_CONTROL_PATTERN_OFF">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#LED_CONTROL_PATTERN_OFF">LED_CONTROL_PATTERN_OFF</a>
     </td>
     <td class="mavlink_comment">LED patterns off (return control to regular vehicle control)</td>
    </tr>
    <tr class="mavlink_field" id="LED_CONTROL_PATTERN_FIRMWAREUPDATE">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#LED_CONTROL_PATTERN_FIRMWAREUPDATE">LED_CONTROL_PATTERN_FIRMWAREUPDATE</a>
     </td>
     <td class="mavlink_comment">LEDs show pattern during firmware update</td>
    </tr>
    <tr class="mavlink_field" id="LED_CONTROL_PATTERN_CUSTOM">
     <td class="mavlink_type" valign="top">255</td>
     <td class="mavlink_name" valign="top">
      <a href="#LED_CONTROL_PATTERN_CUSTOM">LED_CONTROL_PATTERN_CUSTOM</a>
     </td>
     <td class="mavlink_comment">Custom Pattern using custom bytes fields</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_EKF_STATUS_FLAGS">
   <a href="#ENUM_EKF_STATUS_FLAGS">EKF_STATUS_FLAGS</a>
  </h3>
  <p class="description">Flags in EKF_STATUS message</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="EKF_ATTITUDE">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#EKF_ATTITUDE">EKF_ATTITUDE</a>
     </td>
     <td class="mavlink_comment">set if EKF's attitude estimate is good</td>
    </tr>
    <tr class="mavlink_field" id="EKF_VELOCITY_HORIZ">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#EKF_VELOCITY_HORIZ">EKF_VELOCITY_HORIZ</a>
     </td>
     <td class="mavlink_comment">set if EKF's horizontal velocity estimate is good</td>
    </tr>
    <tr class="mavlink_field" id="EKF_VELOCITY_VERT">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#EKF_VELOCITY_VERT">EKF_VELOCITY_VERT</a>
     </td>
     <td class="mavlink_comment">set if EKF's vertical velocity estimate is good</td>
    </tr>
    <tr class="mavlink_field" id="EKF_POS_HORIZ_REL">
     <td class="mavlink_type" valign="top">8</td>
     <td class="mavlink_name" valign="top">
      <a href="#EKF_POS_HORIZ_REL">EKF_POS_HORIZ_REL</a>
     </td>
     <td class="mavlink_comment">set if EKF's horizontal position (relative) estimate is good</td>
    </tr>
    <tr class="mavlink_field" id="EKF_POS_HORIZ_ABS">
     <td class="mavlink_type" valign="top">16</td>
     <td class="mavlink_name" valign="top">
      <a href="#EKF_POS_HORIZ_ABS">EKF_POS_HORIZ_ABS</a>
     </td>
     <td class="mavlink_comment">set if EKF's horizontal position (absolute) estimate is good</td>
    </tr>
    <tr class="mavlink_field" id="EKF_POS_VERT_ABS">
     <td class="mavlink_type" valign="top">32</td>
     <td class="mavlink_name" valign="top">
      <a href="#EKF_POS_VERT_ABS">EKF_POS_VERT_ABS</a>
     </td>
     <td class="mavlink_comment">set if EKF's vertical position (absolute) estimate is good</td>
    </tr>
    <tr class="mavlink_field" id="EKF_POS_VERT_AGL">
     <td class="mavlink_type" valign="top">64</td>
     <td class="mavlink_name" valign="top">
      <a href="#EKF_POS_VERT_AGL">EKF_POS_VERT_AGL</a>
     </td>
     <td class="mavlink_comment">set if EKF's vertical position (above ground) estimate is good</td>
    </tr>
    <tr class="mavlink_field" id="EKF_CONST_POS_MODE">
     <td class="mavlink_type" valign="top">128</td>
     <td class="mavlink_name" valign="top">
      <a href="#EKF_CONST_POS_MODE">EKF_CONST_POS_MODE</a>
     </td>
     <td class="mavlink_comment">EKF is in constant position mode and does not know it's absolute or relative position</td>
    </tr>
    <tr class="mavlink_field" id="EKF_PRED_POS_HORIZ_REL">
     <td class="mavlink_type" valign="top">256</td>
     <td class="mavlink_name" valign="top">
      <a href="#EKF_PRED_POS_HORIZ_REL">EKF_PRED_POS_HORIZ_REL</a>
     </td>
     <td class="mavlink_comment">set if EKF's predicted horizontal position (relative) estimate is good</td>
    </tr>
    <tr class="mavlink_field" id="EKF_PRED_POS_HORIZ_ABS">
     <td class="mavlink_type" valign="top">512</td>
     <td class="mavlink_name" valign="top">
      <a href="#EKF_PRED_POS_HORIZ_ABS">EKF_PRED_POS_HORIZ_ABS</a>
     </td>
     <td class="mavlink_comment">set if EKF's predicted horizontal position (absolute) estimate is good</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_PID_TUNING_AXIS">
   <a href="#ENUM_PID_TUNING_AXIS">PID_TUNING_AXIS</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="PID_TUNING_ROLL">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#PID_TUNING_ROLL">PID_TUNING_ROLL</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="PID_TUNING_PITCH">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#PID_TUNING_PITCH">PID_TUNING_PITCH</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="PID_TUNING_YAW">
     <td class="mavlink_type" valign="top">3</td>
     <td class="mavlink_name" valign="top">
      <a href="#PID_TUNING_YAW">PID_TUNING_YAW</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="PID_TUNING_ACCZ">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#PID_TUNING_ACCZ">PID_TUNING_ACCZ</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="PID_TUNING_STEER">
     <td class="mavlink_type" valign="top">5</td>
     <td class="mavlink_name" valign="top">
      <a href="#PID_TUNING_STEER">PID_TUNING_STEER</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="PID_TUNING_LANDING">
     <td class="mavlink_type" valign="top">6</td>
     <td class="mavlink_name" valign="top">
      <a href="#PID_TUNING_LANDING">PID_TUNING_LANDING</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_MAG_CAL_STATUS">
   <a href="#ENUM_MAG_CAL_STATUS">MAG_CAL_STATUS</a>
  </h3>
  <p class="description">
  </p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="MAG_CAL_NOT_STARTED">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAG_CAL_NOT_STARTED">MAG_CAL_NOT_STARTED</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="MAG_CAL_WAITING_TO_START">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAG_CAL_WAITING_TO_START">MAG_CAL_WAITING_TO_START</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="MAG_CAL_RUNNING_STEP_ONE">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAG_CAL_RUNNING_STEP_ONE">MAG_CAL_RUNNING_STEP_ONE</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="MAG_CAL_RUNNING_STEP_TWO">
     <td class="mavlink_type" valign="top">3</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAG_CAL_RUNNING_STEP_TWO">MAG_CAL_RUNNING_STEP_TWO</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="MAG_CAL_SUCCESS">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAG_CAL_SUCCESS">MAG_CAL_SUCCESS</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="MAG_CAL_FAILED">
     <td class="mavlink_type" valign="top">5</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAG_CAL_FAILED">MAG_CAL_FAILED</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_MAV_REMOTE_LOG_DATA_BLOCK_COMMANDS">
   <a href="#ENUM_MAV_REMOTE_LOG_DATA_BLOCK_COMMANDS">MAV_REMOTE_LOG_DATA_BLOCK_COMMANDS</a>
  </h3>
  <p class="description">Special ACK block numbers control activation of dataflash log streaming</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="MAV_REMOTE_LOG_DATA_BLOCK_STOP">
     <td class="mavlink_type" valign="top">2147483645</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_REMOTE_LOG_DATA_BLOCK_STOP">MAV_REMOTE_LOG_DATA_BLOCK_STOP</a>
     </td>
     <td class="mavlink_comment">UAV to stop sending DataFlash blocks</td>
    </tr>
    <tr class="mavlink_field" id="MAV_REMOTE_LOG_DATA_BLOCK_START">
     <td class="mavlink_type" valign="top">2147483646</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_REMOTE_LOG_DATA_BLOCK_START">MAV_REMOTE_LOG_DATA_BLOCK_START</a>
     </td>
     <td class="mavlink_comment">UAV to start sending DataFlash blocks</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_MAV_REMOTE_LOG_DATA_BLOCK_STATUSES">
   <a href="#ENUM_MAV_REMOTE_LOG_DATA_BLOCK_STATUSES">MAV_REMOTE_LOG_DATA_BLOCK_STATUSES</a>
  </h3>
  <p class="description">Possible remote log data block statuses</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="MAV_REMOTE_LOG_DATA_BLOCK_NACK">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_REMOTE_LOG_DATA_BLOCK_NACK">MAV_REMOTE_LOG_DATA_BLOCK_NACK</a>
     </td>
     <td class="mavlink_comment">This block has NOT been received</td>
    </tr>
    <tr class="mavlink_field" id="MAV_REMOTE_LOG_DATA_BLOCK_ACK">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_REMOTE_LOG_DATA_BLOCK_ACK">MAV_REMOTE_LOG_DATA_BLOCK_ACK</a>
     </td>
     <td class="mavlink_comment">This block has been received</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_DEVICE_OP_BUSTYPE">
   <a href="#ENUM_DEVICE_OP_BUSTYPE">DEVICE_OP_BUSTYPE</a>
  </h3>
  <p class="description">Bus types for device operations</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="DEVICE_OP_BUSTYPE_I2C">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#DEVICE_OP_BUSTYPE_I2C">DEVICE_OP_BUSTYPE_I2C</a>
     </td>
     <td class="mavlink_comment">I2C Device operation</td>
    </tr>
    <tr class="mavlink_field" id="DEVICE_OP_BUSTYPE_SPI">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#DEVICE_OP_BUSTYPE_SPI">DEVICE_OP_BUSTYPE_SPI</a>
     </td>
     <td class="mavlink_comment">SPI Device operation</td>
    </tr>
   </tbody>
  </table>
  <h2>MAVLink Messages</h2>
  <h3 class="mavlink_message_name" id="SENSOR_OFFSETS">SENSOR_OFFSETS (<a href="#SENSOR_OFFSETS">
    #150
   </a>
   )
  </h3>
  <p class="description">Offsets and calibrations values for hardware sensors. This makes it easier to debug the calibration process.</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">mag_ofs_x</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">magnetometer X offset</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">mag_ofs_y</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">magnetometer Y offset</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">mag_ofs_z</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">magnetometer Z offset</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">mag_declination</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">magnetic declination (radians)
     (Units: rad)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">raw_press</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">raw pressure from barometer</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">raw_temp</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">raw temperature from barometer</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">gyro_cal_x</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">gyro X calibration</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">gyro_cal_y</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">gyro Y calibration</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">gyro_cal_z</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">gyro Z calibration</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">accel_cal_x</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">accel X calibration</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">accel_cal_y</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">accel Y calibration</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">accel_cal_z</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">accel Z calibration</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SET_MAG_OFFSETS">SET_MAG_OFFSETS (<a href="#SET_MAG_OFFSETS">
    #151
   </a>
   )
  </h3>
  <p class="description">Deprecated. Use MAV_CMD_PREFLIGHT_SET_SENSOR_OFFSETS instead. Set the magnetometer offsets</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_system</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">System ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_component</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Component ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">mag_ofs_x</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">magnetometer X offset</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">mag_ofs_y</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">magnetometer Y offset</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">mag_ofs_z</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">magnetometer Z offset</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="MEMINFO">MEMINFO (<a href="#MEMINFO">
    #152
   </a>
   )
  </h3>
  <p class="description">state of APM memory</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">brkval</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">heap top</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">freemem</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">free memory
     (Units: bytes)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" style="color:blue;" valign="top">freemem32</td>
     <td class="mavlink_type" valign="top">uint32_t</td>
     <td class="mavlink_comment">free memory (32 bit)
     (Units: bytes)</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="AP_ADC">AP_ADC (<a href="#AP_ADC">
    #153
   </a>
   )
  </h3>
  <p class="description">raw ADC output</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">adc1</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">ADC output 1</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">adc2</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">ADC output 2</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">adc3</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">ADC output 3</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">adc4</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">ADC output 4</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">adc5</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">ADC output 5</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">adc6</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">ADC output 6</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="DIGICAM_CONFIGURE">DIGICAM_CONFIGURE (<a href="#DIGICAM_CONFIGURE">
    #154
   </a>
   )
  </h3>
  <p class="description">Configure on-board Camera Control System.</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_system</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">System ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_component</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Component ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">mode</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Mode enumeration from 1 to N //P, TV, AV, M, Etc (0 means ignore)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">shutter_speed</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Divisor number //e.g. 1000 means 1/1000 (0 means ignore)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">aperture</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">F stop number x 10 //e.g. 28 means 2.8 (0 means ignore)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">iso</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">ISO enumeration from 1 to N //e.g. 80, 100, 200, Etc (0 means ignore)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">exposure_type</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Exposure type enumeration from 1 to N (0 means ignore)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">command_id</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Command Identity (incremental loop: 0 to 255)//A command sent multiple times will be executed or pooled just once</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">engine_cut_off</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Main engine cut-off time before camera trigger in seconds/10 (0 means no cut-off)
     (Units: ds)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">extra_param</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Extra parameters enumeration (0 means ignore)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">extra_value</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Correspondent value to given extra_param</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="DIGICAM_CONTROL">DIGICAM_CONTROL (<a href="#DIGICAM_CONTROL">
    #155
   </a>
   )
  </h3>
  <p class="description">Control on-board Camera Control System to take shots.</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_system</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">System ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_component</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Component ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">session</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">0: stop, 1: start or keep it up //Session control e.g. show/hide lens</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">zoom_pos</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">1 to N //Zoom's absolute position (0 means ignore)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">zoom_step</td>
     <td class="mavlink_type" valign="top">int8_t</td>
     <td class="mavlink_comment">
      -100 to 100 //Zooming step value to offset zoom from the current position
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">focus_lock</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">0: unlock focus or keep unlocked, 1: lock focus or keep locked, 3: re-lock focus</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">shot</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">0: ignore, 1: shot or start filming</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">command_id</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Command Identity (incremental loop: 0 to 255)//A command sent multiple times will be executed or pooled just once</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">extra_param</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Extra parameters enumeration (0 means ignore)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">extra_value</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Correspondent value to given extra_param</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="MOUNT_CONFIGURE">MOUNT_CONFIGURE (<a href="#MOUNT_CONFIGURE">
    #156
   </a>
   )
  </h3>
  <p class="description">Message to configure a camera mount, directional antenna, etc.</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_system</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">System ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_component</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Component ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">mount_mode</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">mount operating mode (see MAV_MOUNT_MODE enum)
     (Enum:<a href="#ENUM_MAV_MOUNT_MODE">MAV_MOUNT_MODE</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">stab_roll</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">
      (1 = yes, 0 = no)
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">stab_pitch</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">
      (1 = yes, 0 = no)
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">stab_yaw</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">
      (1 = yes, 0 = no)
     </td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="MOUNT_CONTROL">MOUNT_CONTROL (<a href="#MOUNT_CONTROL">
    #157
   </a>
   )
  </h3>
  <p class="description">Message to control a camera mount, directional antenna, etc.</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_system</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">System ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_component</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Component ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">input_a</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">pitch(deg*100) or lat, depending on mount mode</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">input_b</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">roll(deg*100) or lon depending on mount mode</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">input_c</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">yaw(deg*100) or alt (in cm) depending on mount mode</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">save_position</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">if "1" it will save current trimmed position on EEPROM (just valid for NEUTRAL and LANDING)</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="MOUNT_STATUS">MOUNT_STATUS (<a href="#MOUNT_STATUS">
    #158
   </a>
   )
  </h3>
  <p class="description">Message with some status from APM to GCS about camera or antenna mount</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_system</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">System ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_component</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Component ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">pointing_a</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">pitch(deg*100)
     (Units: cdeg)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">pointing_b</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">roll(deg*100)
     (Units: cdeg)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">pointing_c</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">yaw(deg*100)
     (Units: cdeg)</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="FENCE_POINT">FENCE_POINT (<a href="#FENCE_POINT">
    #160
   </a>
   )
  </h3>
  <p class="description">A fence point. Used to set a point when from GCS -&gt; MAV. Also used to return a point from MAV -&gt; GCS</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_system</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">System ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_component</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Component ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">idx</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">point index (first point is 1, 0 is for return point)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">count</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">total number of points (for sanity checking)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">lat</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Latitude of point
     (Units: deg)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">lng</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Longitude of point
     (Units: deg)</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="FENCE_FETCH_POINT">FENCE_FETCH_POINT (<a href="#FENCE_FETCH_POINT">
    #161
   </a>
   )
  </h3>
  <p class="description">Request a current fence point from MAV</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_system</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">System ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_component</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Component ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">idx</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">point index (first point is 1, 0 is for return point)</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="FENCE_STATUS">FENCE_STATUS (<a href="#FENCE_STATUS">
    #162
   </a>
   )
  </h3>
  <p class="description">Status of geo-fencing. Sent in extended status stream when fencing enabled</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">breach_status</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">0 if currently inside fence, 1 if outside</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">breach_count</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">number of fence breaches</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">breach_type</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">last breach type (see FENCE_BREACH_* enum)
     (Enum:<a href="#ENUM_FENCE_BREACH">FENCE_BREACH</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">breach_time</td>
     <td class="mavlink_type" valign="top">uint32_t</td>
     <td class="mavlink_comment">time of last breach in milliseconds since boot
     (Units: ms)</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="AHRS">AHRS (<a href="#AHRS">
    #163
   </a>
   )
  </h3>
  <p class="description">Status of DCM attitude estimator</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">omegaIx</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">X gyro drift estimate rad/s
     (Units: rad/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">omegaIy</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Y gyro drift estimate rad/s
     (Units: rad/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">omegaIz</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Z gyro drift estimate rad/s
     (Units: rad/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">accel_weight</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">average accel_weight</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">renorm_val</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">average renormalisation value</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">error_rp</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">average error_roll_pitch value</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">error_yaw</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">average error_yaw value</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SIMSTATE">SIMSTATE (<a href="#SIMSTATE">
    #164
   </a>
   )
  </h3>
  <p class="description">Status of simulation environment, if used</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">roll</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Roll angle (rad)
     (Units: rad)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">pitch</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Pitch angle (rad)
     (Units: rad)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">yaw</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Yaw angle (rad)
     (Units: rad)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">xacc</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">X acceleration m/s/s
     (Units: m/s/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">yacc</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Y acceleration m/s/s
     (Units: m/s/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">zacc</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Z acceleration m/s/s
     (Units: m/s/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">xgyro</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Angular speed around X axis rad/s
     (Units: rad/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">ygyro</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Angular speed around Y axis rad/s
     (Units: rad/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">zgyro</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Angular speed around Z axis rad/s
     (Units: rad/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">lat</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">Latitude in degrees * 1E7
     (Units: degE7)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">lng</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">Longitude in degrees * 1E7
     (Units: degE7)</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="HWSTATUS">HWSTATUS (<a href="#HWSTATUS">
    #165
   </a>
   )
  </h3>
  <p class="description">Status of key hardware</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">Vcc</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">board voltage (mV)
     (Units: mV)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">I2Cerr</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">I2C error count</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="RADIO">RADIO (<a href="#RADIO">
    #166
   </a>
   )
  </h3>
  <p class="description">Status generated by radio</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">rssi</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">local signal strength</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">remrssi</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">remote signal strength</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">txbuf</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">how full the tx buffer is as a percentage
     (Units: %)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">noise</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">background noise level</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">remnoise</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">remote background noise level</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">rxerrors</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">receive errors</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">fixed</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">count of error corrected packets</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="LIMITS_STATUS">LIMITS_STATUS (<a href="#LIMITS_STATUS">
    #167
   </a>
   )
  </h3>
  <p class="description">Status of AP_Limits. Sent in extended status stream when AP_Limits is enabled</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">limits_state</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">state of AP_Limits, (see enum LimitState, LIMITS_STATE)
     (Enum:<a href="#ENUM_LIMITS_STATE">LIMITS_STATE</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">last_trigger</td>
     <td class="mavlink_type" valign="top">uint32_t</td>
     <td class="mavlink_comment">time of last breach in milliseconds since boot
     (Units: ms)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">last_action</td>
     <td class="mavlink_type" valign="top">uint32_t</td>
     <td class="mavlink_comment">time of last recovery action in milliseconds since boot
     (Units: ms)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">last_recovery</td>
     <td class="mavlink_type" valign="top">uint32_t</td>
     <td class="mavlink_comment">time of last successful recovery in milliseconds since boot
     (Units: ms)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">last_clear</td>
     <td class="mavlink_type" valign="top">uint32_t</td>
     <td class="mavlink_comment">time of last all-clear in milliseconds since boot
     (Units: ms)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">breach_count</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">number of fence breaches</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">mods_enabled</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">AP_Limit_Module bitfield of enabled modules, (see enum moduleid or LIMIT_MODULE)
     (Enum:<a href="#ENUM_LIMIT_MODULE">LIMIT_MODULE</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">mods_required</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">AP_Limit_Module bitfield of required modules, (see enum moduleid or LIMIT_MODULE)
     (Enum:<a href="#ENUM_LIMIT_MODULE">LIMIT_MODULE</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">mods_triggered</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">AP_Limit_Module bitfield of triggered modules, (see enum moduleid or LIMIT_MODULE)
     (Enum:<a href="#ENUM_LIMIT_MODULE">LIMIT_MODULE</a>
      )
     </td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="WIND">WIND (<a href="#WIND">
    #168
   </a>
   )
  </h3>
  <p class="description">Wind estimation</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">direction</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">wind direction that wind is coming from (degrees)
     (Units: deg)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">speed</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">wind speed in ground plane (m/s)
     (Units: m/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">speed_z</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">vertical wind speed (m/s)
     (Units: m/s)</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="DATA16">DATA16 (<a href="#DATA16">
    #169
   </a>
   )
  </h3>
  <p class="description">Data packet, size 16</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">type</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">data type</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">len</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">data length
     (Units: bytes)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">data</td>
     <td class="mavlink_type" valign="top">uint8_t[16]</td>
     <td class="mavlink_comment">raw data</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="DATA32">DATA32 (<a href="#DATA32">
    #170
   </a>
   )
  </h3>
  <p class="description">Data packet, size 32</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">type</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">data type</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">len</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">data length
     (Units: bytes)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">data</td>
     <td class="mavlink_type" valign="top">uint8_t[32]</td>
     <td class="mavlink_comment">raw data</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="DATA64">DATA64 (<a href="#DATA64">
    #171
   </a>
   )
  </h3>
  <p class="description">Data packet, size 64</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">type</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">data type</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">len</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">data length
     (Units: bytes)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">data</td>
     <td class="mavlink_type" valign="top">uint8_t[64]</td>
     <td class="mavlink_comment">raw data</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="DATA96">DATA96 (<a href="#DATA96">
    #172
   </a>
   )
  </h3>
  <p class="description">Data packet, size 96</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">type</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">data type</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">len</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">data length
     (Units: bytes)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">data</td>
     <td class="mavlink_type" valign="top">uint8_t[96]</td>
     <td class="mavlink_comment">raw data</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="RANGEFINDER">RANGEFINDER (<a href="#RANGEFINDER">
    #173
   </a>
   )
  </h3>
  <p class="description">Rangefinder reporting</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">distance</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">distance in meters
     (Units: m)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">voltage</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">raw voltage if available, zero otherwise
     (Units: V)</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="AIRSPEED_AUTOCAL">AIRSPEED_AUTOCAL (<a href="#AIRSPEED_AUTOCAL">
    #174
   </a>
   )
  </h3>
  <p class="description">Airspeed auto-calibration</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">vx</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">GPS velocity north m/s
     (Units: m/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">vy</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">GPS velocity east m/s
     (Units: m/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">vz</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">GPS velocity down m/s
     (Units: m/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">diff_pressure</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Differential pressure pascals
     (Units: Pa)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">EAS2TAS</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Estimated to true airspeed ratio</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">ratio</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Airspeed ratio</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">state_x</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">EKF state x</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">state_y</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">EKF state y</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">state_z</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">EKF state z</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">Pax</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">EKF Pax</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">Pby</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">EKF Pby</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">Pcz</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">EKF Pcz</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="RALLY_POINT">RALLY_POINT (<a href="#RALLY_POINT">
    #175
   </a>
   )
  </h3>
  <p class="description">A rally point. Used to set a point when from GCS -&gt; MAV. Also used to return a point from MAV -&gt; GCS</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_system</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">System ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_component</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Component ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">idx</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">point index (first point is 0)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">count</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">total number of points (for sanity checking)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">lat</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">Latitude of point in degrees * 1E7
     (Units: degE7)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">lng</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">Longitude of point in degrees * 1E7
     (Units: degE7)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">alt</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Transit / loiter altitude in meters relative to home
     (Units: m)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">break_alt</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Break altitude in meters relative to home
     (Units: m)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">land_dir</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Heading to aim for when landing. In centi-degrees.
     (Units: cdeg)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">flags</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">See RALLY_FLAGS enum for definition of the bitmask.
     (Enum:<a href="#ENUM_RALLY_FLAGS">RALLY_FLAGS</a>
      )
     </td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="RALLY_FETCH_POINT">RALLY_FETCH_POINT (<a href="#RALLY_FETCH_POINT">
    #176
   </a>
   )
  </h3>
  <p class="description">Request a current rally point from MAV. MAV should respond with a RALLY_POINT message. MAV should not respond if the request is invalid.</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_system</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">System ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_component</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Component ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">idx</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">point index (first point is 0)</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="COMPASSMOT_STATUS">COMPASSMOT_STATUS (<a href="#COMPASSMOT_STATUS">
    #177
   </a>
   )
  </h3>
  <p class="description">Status of compassmot calibration</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">throttle</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">throttle (percent*10)
     (Units: d%)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">current</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">current (Ampere)
     (Units: A)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">interference</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">interference (percent)
     (Units: %)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">CompensationX</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Motor Compensation X</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">CompensationY</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Motor Compensation Y</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">CompensationZ</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Motor Compensation Z</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="AHRS2">AHRS2 (<a href="#AHRS2">
    #178
   </a>
   )
  </h3>
  <p class="description">Status of secondary AHRS filter if available</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">roll</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Roll angle (rad)
     (Units: rad)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">pitch</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Pitch angle (rad)
     (Units: rad)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">yaw</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Yaw angle (rad)
     (Units: rad)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">altitude</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Altitude (MSL)
     (Units: m)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">lat</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">Latitude in degrees * 1E7
     (Units: degE7)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">lng</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">Longitude in degrees * 1E7
     (Units: degE7)</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="CAMERA_STATUS">CAMERA_STATUS (<a href="#CAMERA_STATUS">
    #179
   </a>
   )
  </h3>
  <p class="description">Camera Event</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">time_usec</td>
     <td class="mavlink_type" valign="top">uint64_t</td>
     <td class="mavlink_comment">Image timestamp (microseconds since UNIX epoch, according to camera clock)
     (Units: us)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_system</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">System ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">cam_idx</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Camera ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">img_idx</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Image index</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">event_id</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">See CAMERA_STATUS_TYPES enum for definition of the bitmask
     (Enum:<a href="#ENUM_CAMERA_STATUS_TYPES">CAMERA_STATUS_TYPES</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">p1</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Parameter 1 (meaning depends on event, see CAMERA_STATUS_TYPES enum)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">p2</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Parameter 2 (meaning depends on event, see CAMERA_STATUS_TYPES enum)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">p3</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Parameter 3 (meaning depends on event, see CAMERA_STATUS_TYPES enum)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">p4</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Parameter 4 (meaning depends on event, see CAMERA_STATUS_TYPES enum)</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="CAMERA_FEEDBACK">CAMERA_FEEDBACK (<a href="#CAMERA_FEEDBACK">
    #180
   </a>
   )
  </h3>
  <p class="description">Camera Capture Feedback</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">time_usec</td>
     <td class="mavlink_type" valign="top">uint64_t</td>
     <td class="mavlink_comment">Image timestamp (microseconds since UNIX epoch), as passed in by CAMERA_STATUS message (or autopilot if no CCB)
     (Units: us)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_system</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">System ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">cam_idx</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Camera ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">img_idx</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Image index</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">lat</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">Latitude in (deg * 1E7)
     (Units: degE7)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">lng</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">Longitude in (deg * 1E7)
     (Units: degE7)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">alt_msl</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Altitude Absolute (meters AMSL)
     (Units: m)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">alt_rel</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Altitude Relative (meters above HOME location)
     (Units: m)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">roll</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Camera Roll angle (earth frame, degrees, +-180)
     (Units: deg)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">pitch</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Camera Pitch angle (earth frame, degrees, +-180)
     (Units: deg)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">yaw</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Camera Yaw (earth frame, degrees, 0-360, true)
     (Units: deg)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">foc_len</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Focal Length (mm)
     (Units: mm)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">flags</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">See CAMERA_FEEDBACK_FLAGS enum for definition of the bitmask
     (Enum:<a href="#ENUM_CAMERA_FEEDBACK_FLAGS">CAMERA_FEEDBACK_FLAGS</a>
      )
     </td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="BATTERY2">BATTERY2 (<a href="#BATTERY2">
    #181
   </a>
   )
  </h3>
  <p class="description">2nd Battery status</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">voltage</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">voltage in millivolts
     (Units: mV)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">current_battery</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Battery current, in 10*milliamperes (1 = 10 milliampere), -1: autopilot does not measure the current
     (Units: cA)</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="AHRS3">AHRS3 (<a href="#AHRS3">
    #182
   </a>
   )
  </h3>
  <p class="description">Status of third AHRS filter if available. This is for ANU research group (Ali and Sean)</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">roll</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Roll angle (rad)
     (Units: rad)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">pitch</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Pitch angle (rad)
     (Units: rad)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">yaw</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Yaw angle (rad)
     (Units: rad)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">altitude</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Altitude (MSL)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">lat</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">Latitude in degrees * 1E7
     (Units: degE7)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">lng</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">Longitude in degrees * 1E7
     (Units: degE7)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">v1</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">test variable1</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">v2</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">test variable2</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">v3</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">test variable3</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">v4</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">test variable4</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="AUTOPILOT_VERSION_REQUEST">AUTOPILOT_VERSION_REQUEST (<a href="#AUTOPILOT_VERSION_REQUEST">
    #183
   </a>
   )
  </h3>
  <p class="description">Request the autopilot version from the system/component.</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_system</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">System ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_component</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Component ID</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="REMOTE_LOG_DATA_BLOCK">REMOTE_LOG_DATA_BLOCK (<a href="#REMOTE_LOG_DATA_BLOCK">
    #184
   </a>
   )
  </h3>
  <p class="description">Send a block of log data to remote location</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_system</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">System ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_component</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Component ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">seqno</td>
     <td class="mavlink_type" valign="top">uint32_t</td>
     <td class="mavlink_comment">log data block sequence number
     (Enum:<a href="#ENUM_MAV_REMOTE_LOG_DATA_BLOCK_COMMANDS">MAV_REMOTE_LOG_DATA_BLOCK_COMMANDS</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">data</td>
     <td class="mavlink_type" valign="top">uint8_t[200]</td>
     <td class="mavlink_comment">log data block</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="REMOTE_LOG_BLOCK_STATUS">REMOTE_LOG_BLOCK_STATUS (<a href="#REMOTE_LOG_BLOCK_STATUS">
    #185
   </a>
   )
  </h3>
  <p class="description">Send Status of each log block that autopilot board might have sent</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_system</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">System ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_component</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Component ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">seqno</td>
     <td class="mavlink_type" valign="top">uint32_t</td>
     <td class="mavlink_comment">log data block sequence number</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">status</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">log data block status
     (Enum:<a href="#ENUM_MAV_REMOTE_LOG_DATA_BLOCK_STATUSES">MAV_REMOTE_LOG_DATA_BLOCK_STATUSES</a>
      )
     </td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="LED_CONTROL">LED_CONTROL (<a href="#LED_CONTROL">
    #186
   </a>
   )
  </h3>
  <p class="description">Control vehicle LEDs</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_system</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">System ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_component</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Component ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">instance</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Instance (LED instance to control or 255 for all LEDs)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">pattern</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Pattern (see LED_PATTERN_ENUM)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">custom_len</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Custom Byte Length</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">custom_bytes</td>
     <td class="mavlink_type" valign="top">uint8_t[24]</td>
     <td class="mavlink_comment">Custom Bytes</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="MAG_CAL_PROGRESS">MAG_CAL_PROGRESS (<a href="#MAG_CAL_PROGRESS">
    #191
   </a>
   )
  </h3>
  <p class="description">Reports progress of compass calibration.</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">compass_id</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Compass being calibrated</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">cal_mask</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Bitmask of compasses being calibrated</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">cal_status</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Status (see MAG_CAL_STATUS enum)
     (Enum:<a href="#ENUM_MAG_CAL_STATUS">MAG_CAL_STATUS</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">attempt</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Attempt number</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">completion_pct</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Completion percentage
     (Units: %)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">completion_mask</td>
     <td class="mavlink_type" valign="top">uint8_t[10]</td>
     <td class="mavlink_comment">Bitmask of sphere sections (see http://en.wikipedia.org/wiki/Geodesic_grid)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">direction_x</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Body frame direction vector for display</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">direction_y</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Body frame direction vector for display</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">direction_z</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Body frame direction vector for display</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="MAG_CAL_REPORT">MAG_CAL_REPORT (<a href="#MAG_CAL_REPORT">
    #192
   </a>
   )
  </h3>
  <p class="description">Reports results of completed compass calibration. Sent until MAG_CAL_ACK received.</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">compass_id</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Compass being calibrated</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">cal_mask</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Bitmask of compasses being calibrated</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">cal_status</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Status (see MAG_CAL_STATUS enum)
     (Enum:<a href="#ENUM_MAG_CAL_STATUS">MAG_CAL_STATUS</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">autosaved</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">0=requires a MAV_CMD_DO_ACCEPT_MAG_CAL, 1=saved to parameters</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">fitness</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">RMS milligauss residuals
     (Units: mgauss)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">ofs_x</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">X offset</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">ofs_y</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Y offset</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">ofs_z</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Z offset</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">diag_x</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">X diagonal (matrix 11)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">diag_y</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Y diagonal (matrix 22)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">diag_z</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Z diagonal (matrix 33)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">offdiag_x</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">X off-diagonal (matrix 12 and 21)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">offdiag_y</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Y off-diagonal (matrix 13 and 31)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">offdiag_z</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Z off-diagonal (matrix 32 and 23)</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="EKF_STATUS_REPORT">EKF_STATUS_REPORT (<a href="#EKF_STATUS_REPORT">
    #193
   </a>
   )
  </h3>
  <p class="description">EKF Status message including flags and variances</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">flags</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Flags
     (Enum:<a href="#ENUM_EKF_STATUS_FLAGS">EKF_STATUS_FLAGS</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">velocity_variance</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Velocity variance</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">pos_horiz_variance</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Horizontal Position variance</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">pos_vert_variance</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Vertical Position variance</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">compass_variance</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Compass variance</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">terrain_alt_variance</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Terrain Altitude variance</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="PID_TUNING">PID_TUNING (<a href="#PID_TUNING">
    #194
   </a>
   )
  </h3>
  <p class="description">PID tuning information</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">axis</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">axis
     (Enum:<a href="#ENUM_PID_TUNING_AXIS">PID_TUNING_AXIS</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">desired</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">desired rate (degrees/s)
     (Units: deg/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">achieved</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">achieved rate (degrees/s)
     (Units: deg/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">FF</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">FF component</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">P</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">P component</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">I</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">I component</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">D</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">D component</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="GIMBAL_REPORT">GIMBAL_REPORT (<a href="#GIMBAL_REPORT">
    #200
   </a>
   )
  </h3>
  <p class="description">3 axis gimbal mesuraments</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_system</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">System ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_component</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Component ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">delta_time</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Time since last update (seconds)
     (Units: s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">delta_angle_x</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Delta angle X (radians)
     (Units: rad)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">delta_angle_y</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Delta angle Y (radians)
     (Units: rad)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">delta_angle_z</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Delta angle X (radians)
     (Units: rad)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">delta_velocity_x</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Delta velocity X (m/s)
     (Units: m/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">delta_velocity_y</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Delta velocity Y (m/s)
     (Units: m/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">delta_velocity_z</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Delta velocity Z (m/s)
     (Units: m/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">joint_roll</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Joint ROLL (radians)
     (Units: rad)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">joint_el</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Joint EL (radians)
     (Units: rad)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">joint_az</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Joint AZ (radians)
     (Units: rad)</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="GIMBAL_CONTROL">GIMBAL_CONTROL (<a href="#GIMBAL_CONTROL">
    #201
   </a>
   )
  </h3>
  <p class="description">Control message for rate gimbal</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_system</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">System ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_component</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Component ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">demanded_rate_x</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Demanded angular rate X (rad/s)
     (Units: rad/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">demanded_rate_y</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Demanded angular rate Y (rad/s)
     (Units: rad/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">demanded_rate_z</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Demanded angular rate Z (rad/s)
     (Units: rad/s)</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="GIMBAL_TORQUE_CMD_REPORT">GIMBAL_TORQUE_CMD_REPORT (<a href="#GIMBAL_TORQUE_CMD_REPORT">
    #214
   </a>
   )
  </h3>
  <p class="description">100 Hz gimbal torque command telemetry</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_system</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">System ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_component</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Component ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">rl_torque_cmd</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Roll Torque Command</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">el_torque_cmd</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Elevation Torque Command</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">az_torque_cmd</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Azimuth Torque Command</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="GOPRO_HEARTBEAT">GOPRO_HEARTBEAT (<a href="#GOPRO_HEARTBEAT">
    #215
   </a>
   )
  </h3>
  <p class="description">Heartbeat from a HeroBus attached GoPro</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">status</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Status
     (Enum:<a href="#ENUM_GOPRO_HEARTBEAT_STATUS">GOPRO_HEARTBEAT_STATUS</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">capture_mode</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Current capture mode
     (Enum:<a href="#ENUM_GOPRO_CAPTURE_MODE">GOPRO_CAPTURE_MODE</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">flags</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">additional status bits
     (Enum:<a href="#ENUM_GOPRO_HEARTBEAT_FLAGS">GOPRO_HEARTBEAT_FLAGS</a>
      )
     </td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="GOPRO_GET_REQUEST">GOPRO_GET_REQUEST (<a href="#GOPRO_GET_REQUEST">
    #216
   </a>
   )
  </h3>
  <p class="description">Request a GOPRO_COMMAND response from the GoPro</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_system</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">System ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_component</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Component ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">cmd_id</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Command ID
     (Enum:<a href="#ENUM_GOPRO_COMMAND">GOPRO_COMMAND</a>
      )
     </td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="GOPRO_GET_RESPONSE">GOPRO_GET_RESPONSE (<a href="#GOPRO_GET_RESPONSE">
    #217
   </a>
   )
  </h3>
  <p class="description">Response from a GOPRO_COMMAND get request</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">cmd_id</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Command ID
     (Enum:<a href="#ENUM_GOPRO_COMMAND">GOPRO_COMMAND</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">status</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Status
     (Enum:<a href="#ENUM_GOPRO_REQUEST_STATUS">GOPRO_REQUEST_STATUS</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">value</td>
     <td class="mavlink_type" valign="top">uint8_t[4]</td>
     <td class="mavlink_comment">Value</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="GOPRO_SET_REQUEST">GOPRO_SET_REQUEST (<a href="#GOPRO_SET_REQUEST">
    #218
   </a>
   )
  </h3>
  <p class="description">Request to set a GOPRO_COMMAND with a desired</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_system</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">System ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_component</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Component ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">cmd_id</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Command ID
     (Enum:<a href="#ENUM_GOPRO_COMMAND">GOPRO_COMMAND</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">value</td>
     <td class="mavlink_type" valign="top">uint8_t[4]</td>
     <td class="mavlink_comment">Value</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="GOPRO_SET_RESPONSE">GOPRO_SET_RESPONSE (<a href="#GOPRO_SET_RESPONSE">
    #219
   </a>
   )
  </h3>
  <p class="description">Response from a GOPRO_COMMAND set request</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">cmd_id</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Command ID
     (Enum:<a href="#ENUM_GOPRO_COMMAND">GOPRO_COMMAND</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">status</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Status
     (Enum:<a href="#ENUM_GOPRO_REQUEST_STATUS">GOPRO_REQUEST_STATUS</a>
      )
     </td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="RPM">RPM (<a href="#RPM">
    #226
   </a>
   )
  </h3>
  <p class="description">RPM sensor output</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">rpm1</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">RPM Sensor1</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">rpm2</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">RPM Sensor2</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="DEVICE_OP_READ">DEVICE_OP_READ (<a href="#DEVICE_OP_READ">
    #11000
   </a>
   )
  </h3>
  <p class="description">
   <strong>
    (MAVLink 2)
   </strong>Read registers for a device</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_system</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">System ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_component</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Component ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">request_id</td>
     <td class="mavlink_type" valign="top">uint32_t</td>
     <td class="mavlink_comment">request ID - copied to reply</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">bustype</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">The bus type
     (Enum:<a href="#ENUM_DEVICE_OP_BUSTYPE">DEVICE_OP_BUSTYPE</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">bus</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Bus number</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">address</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Bus address</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">busname</td>
     <td class="mavlink_type" valign="top">char[40]</td>
     <td class="mavlink_comment">Name of device on bus (for SPI)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">regstart</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">First register to read</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">count</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">count of registers to read</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="DEVICE_OP_READ_REPLY">DEVICE_OP_READ_REPLY (<a href="#DEVICE_OP_READ_REPLY">
    #11001
   </a>
   )
  </h3>
  <p class="description">
   <strong>
    (MAVLink 2)
   </strong>Read registers reply</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">request_id</td>
     <td class="mavlink_type" valign="top">uint32_t</td>
     <td class="mavlink_comment">request ID - copied from request</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">result</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">0 for success, anything else is failure code</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">regstart</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">starting register</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">count</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">count of bytes read</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">data</td>
     <td class="mavlink_type" valign="top">uint8_t[128]</td>
     <td class="mavlink_comment">reply data</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="DEVICE_OP_WRITE">DEVICE_OP_WRITE (<a href="#DEVICE_OP_WRITE">
    #11002
   </a>
   )
  </h3>
  <p class="description">
   <strong>
    (MAVLink 2)
   </strong>Write registers for a device</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_system</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">System ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">target_component</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Component ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">request_id</td>
     <td class="mavlink_type" valign="top">uint32_t</td>
     <td class="mavlink_comment">request ID - copied to reply</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">bustype</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">The bus type
     (Enum:<a href="#ENUM_DEVICE_OP_BUSTYPE">DEVICE_OP_BUSTYPE</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">bus</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Bus number</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">address</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Bus address</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">busname</td>
     <td class="mavlink_type" valign="top">char[40]</td>
     <td class="mavlink_comment">Name of device on bus (for SPI)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">regstart</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">First register to write</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">count</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">count of registers to write</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">data</td>
     <td class="mavlink_type" valign="top">uint8_t[128]</td>
     <td class="mavlink_comment">write data</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="DEVICE_OP_WRITE_REPLY">DEVICE_OP_WRITE_REPLY (<a href="#DEVICE_OP_WRITE_REPLY">
    #11003
   </a>
   )
  </h3>
  <p class="description">
   <strong>
    (MAVLink 2)
   </strong>Write registers reply</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">request_id</td>
     <td class="mavlink_type" valign="top">uint32_t</td>
     <td class="mavlink_comment">request ID - copied from request</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">result</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">0 for success, anything else is failure code</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ADAP_TUNING">ADAP_TUNING (<a href="#ADAP_TUNING">
    #11010
   </a>
   )
  </h3>
  <p class="description">
   <strong>
    (MAVLink 2)
   </strong>Adaptive Controller tuning information</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">axis</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">axis
     (Enum:<a href="#ENUM_PID_TUNING_AXIS">PID_TUNING_AXIS</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">desired</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">desired rate (degrees/s)
     (Units: deg/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">achieved</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">achieved rate (degrees/s)
     (Units: deg/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">error</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">error between model and vehicle</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">theta</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">theta estimated state predictor</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">omega</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">omega estimated state predictor</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sigma</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">sigma estimated state predictor</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">theta_dot</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">theta derivative</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">omega_dot</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">omega derivative</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sigma_dot</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">sigma derivative</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">f</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">projection operator value</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">f_dot</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">projection operator derivative</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">u</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">u adaptive controlled output command</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="VISION_POSITION_DELTA">VISION_POSITION_DELTA (<a href="#VISION_POSITION_DELTA">
    #11011
   </a>
   )
  </h3>
  <p class="description">
   <strong>
    (MAVLink 2)
   </strong>camera vision based attitude and position deltas</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Type</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">time_usec</td>
     <td class="mavlink_type" valign="top">uint64_t</td>
     <td class="mavlink_comment">Timestamp (microseconds, synced to UNIX time or since system boot)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">time_delta_usec</td>
     <td class="mavlink_type" valign="top">uint64_t</td>
     <td class="mavlink_comment">Time in microseconds since the last reported camera frame</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">angle_delta</td>
     <td class="mavlink_type" valign="top">float[3]</td>
     <td class="mavlink_comment">Defines a rotation vector in body frame that rotates the vehicle from the previous to the current orientation</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">position_delta</td>
     <td class="mavlink_type" valign="top">float[3]</td>
     <td class="mavlink_comment">Change in position in meters from previous to current frame rotated into body frame (0=forward, 1=right, 2=down)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">confidence</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">normalised confidence value from 0 to 100</td>
    </tr>
   </tbody>
  </table>
 </body>
</html>