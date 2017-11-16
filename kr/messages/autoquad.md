<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_gitbook.py -->
# MAVLINK Message Set: autoquad.xml

*This is a human-readable form of the XML definition file: [autoquad.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/autoquad.xml).*

<html>
 <body>
  <p>
   <strong>MAVLink Include Files:</strong>
   <a href="common.md">common.xml</a>
  </p>
  <h2>MAVLink Protocol Version</h2>
  <p>This file has protocol version: 3. The version numbers range from 1-255.</p>
  <h2>MAVLink Type Enumerations</h2>
  <h3 class="mavlink_message_name" id="ENUM_AUTOQUAD_MAVLINK_DEFS_VERSION">
   <a href="#ENUM_AUTOQUAD_MAVLINK_DEFS_VERSION">AUTOQUAD_MAVLINK_DEFS_VERSION</a>
  </h3>
  <p class="description">Track current version of these definitions (can be used by checking value of AUTOQUAD_MAVLINK_DEFS_VERSION_ENUM_END). Append a new entry for each published change.</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="AQ_MAVLINK_DEFS_VERSION_1">
     <td class="mavlink_type" valign="top">
     </td>
     <td class="mavlink_name" valign="top">
      <a href="#AQ_MAVLINK_DEFS_VERSION_1">AQ_MAVLINK_DEFS_VERSION_1</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_AUTOQUAD_NAV_STATUS">
   <a href="#ENUM_AUTOQUAD_NAV_STATUS">AUTOQUAD_NAV_STATUS</a>
  </h3>
  <p class="description">Available operating modes/statuses for AutoQuad flight controller. 
				Bitmask up to 32 bits. Low side bits for base modes, high side for 
				additional active features/modifiers/constraints.</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="AQ_NAV_STATUS_INIT">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#AQ_NAV_STATUS_INIT">AQ_NAV_STATUS_INIT</a>
     </td>
     <td class="mavlink_comment">System is initializing</td>
    </tr>
    <tr class="mavlink_field" id="AQ_NAV_STATUS_STANDBY">
     <td class="mavlink_type" valign="top">0x00000001</td>
     <td class="mavlink_name" valign="top">
      <a href="#AQ_NAV_STATUS_STANDBY">AQ_NAV_STATUS_STANDBY</a>
     </td>
     <td class="mavlink_comment">System is *armed* and standing by, with no throttle input and no autonomous mode</td>
    </tr>
    <tr class="mavlink_field" id="AQ_NAV_STATUS_MANUAL">
     <td class="mavlink_type" valign="top">0x00000002</td>
     <td class="mavlink_name" valign="top">
      <a href="#AQ_NAV_STATUS_MANUAL">AQ_NAV_STATUS_MANUAL</a>
     </td>
     <td class="mavlink_comment">Flying (throttle input detected), assumed under manual control unless other mode bits are set</td>
    </tr>
    <tr class="mavlink_field" id="AQ_NAV_STATUS_ALTHOLD">
     <td class="mavlink_type" valign="top">0x00000004</td>
     <td class="mavlink_name" valign="top">
      <a href="#AQ_NAV_STATUS_ALTHOLD">AQ_NAV_STATUS_ALTHOLD</a>
     </td>
     <td class="mavlink_comment">Altitude hold engaged</td>
    </tr>
    <tr class="mavlink_field" id="AQ_NAV_STATUS_POSHOLD">
     <td class="mavlink_type" valign="top">0x00000008</td>
     <td class="mavlink_name" valign="top">
      <a href="#AQ_NAV_STATUS_POSHOLD">AQ_NAV_STATUS_POSHOLD</a>
     </td>
     <td class="mavlink_comment">Position hold engaged</td>
    </tr>
    <tr class="mavlink_field" id="AQ_NAV_STATUS_GUIDED">
     <td class="mavlink_type" valign="top">0x00000010</td>
     <td class="mavlink_name" valign="top">
      <a href="#AQ_NAV_STATUS_GUIDED">AQ_NAV_STATUS_GUIDED</a>
     </td>
     <td class="mavlink_comment">Externally-guided (eg. GCS) navigation mode</td>
    </tr>
    <tr class="mavlink_field" id="AQ_NAV_STATUS_MISSION">
     <td class="mavlink_type" valign="top">0x00000020</td>
     <td class="mavlink_name" valign="top">
      <a href="#AQ_NAV_STATUS_MISSION">AQ_NAV_STATUS_MISSION</a>
     </td>
     <td class="mavlink_comment">Autonomous mission execution mode</td>
    </tr>
    <tr class="mavlink_field" id="AQ_NAV_STATUS_READY">
     <td class="mavlink_type" valign="top">0x00000100</td>
     <td class="mavlink_name" valign="top">
      <a href="#AQ_NAV_STATUS_READY">AQ_NAV_STATUS_READY</a>
     </td>
     <td class="mavlink_comment">Ready but *not armed*</td>
    </tr>
    <tr class="mavlink_field" id="AQ_NAV_STATUS_CALIBRATING">
     <td class="mavlink_type" valign="top">0x00000200</td>
     <td class="mavlink_name" valign="top">
      <a href="#AQ_NAV_STATUS_CALIBRATING">AQ_NAV_STATUS_CALIBRATING</a>
     </td>
     <td class="mavlink_comment">Calibration mode active</td>
    </tr>
    <tr class="mavlink_field" id="AQ_NAV_STATUS_NO_RC">
     <td class="mavlink_type" valign="top">0x00001000</td>
     <td class="mavlink_name" valign="top">
      <a href="#AQ_NAV_STATUS_NO_RC">AQ_NAV_STATUS_NO_RC</a>
     </td>
     <td class="mavlink_comment">No valid control input (eg. no radio link)</td>
    </tr>
    <tr class="mavlink_field" id="AQ_NAV_STATUS_FUEL_LOW">
     <td class="mavlink_type" valign="top">0x00002000</td>
     <td class="mavlink_name" valign="top">
      <a href="#AQ_NAV_STATUS_FUEL_LOW">AQ_NAV_STATUS_FUEL_LOW</a>
     </td>
     <td class="mavlink_comment">Battery is low (stage 1 warning)</td>
    </tr>
    <tr class="mavlink_field" id="AQ_NAV_STATUS_FUEL_CRITICAL">
     <td class="mavlink_type" valign="top">0x00004000</td>
     <td class="mavlink_name" valign="top">
      <a href="#AQ_NAV_STATUS_FUEL_CRITICAL">AQ_NAV_STATUS_FUEL_CRITICAL</a>
     </td>
     <td class="mavlink_comment">Battery is depleted (stage 2 warning)</td>
    </tr>
    <tr class="mavlink_field" id="AQ_NAV_STATUS_DVH">
     <td class="mavlink_type" valign="top">0x01000000</td>
     <td class="mavlink_name" valign="top">
      <a href="#AQ_NAV_STATUS_DVH">AQ_NAV_STATUS_DVH</a>
     </td>
     <td class="mavlink_comment">Dynamic Velocity Hold is active (PH with proportional manual direction override)</td>
    </tr>
    <tr class="mavlink_field" id="AQ_NAV_STATUS_DAO">
     <td class="mavlink_type" valign="top">0x02000000</td>
     <td class="mavlink_name" valign="top">
      <a href="#AQ_NAV_STATUS_DAO">AQ_NAV_STATUS_DAO</a>
     </td>
     <td class="mavlink_comment">ynamic Altitude Override is active (AH with proportional manual adjustment)</td>
    </tr>
    <tr class="mavlink_field" id="AQ_NAV_STATUS_CEILING_REACHED">
     <td class="mavlink_type" valign="top">0x04000000</td>
     <td class="mavlink_name" valign="top">
      <a href="#AQ_NAV_STATUS_CEILING_REACHED">AQ_NAV_STATUS_CEILING_REACHED</a>
     </td>
     <td class="mavlink_comment">Craft is at ceiling altitude</td>
    </tr>
    <tr class="mavlink_field" id="AQ_NAV_STATUS_CEILING">
     <td class="mavlink_type" valign="top">0x08000000</td>
     <td class="mavlink_name" valign="top">
      <a href="#AQ_NAV_STATUS_CEILING">AQ_NAV_STATUS_CEILING</a>
     </td>
     <td class="mavlink_comment">Ceiling altitude is set</td>
    </tr>
    <tr class="mavlink_field" id="AQ_NAV_STATUS_HF_DYNAMIC">
     <td class="mavlink_type" valign="top">0x10000000</td>
     <td class="mavlink_name" valign="top">
      <a href="#AQ_NAV_STATUS_HF_DYNAMIC">AQ_NAV_STATUS_HF_DYNAMIC</a>
     </td>
     <td class="mavlink_comment">Heading-Free dynamic mode active</td>
    </tr>
    <tr class="mavlink_field" id="AQ_NAV_STATUS_HF_LOCKED">
     <td class="mavlink_type" valign="top">0x20000000</td>
     <td class="mavlink_name" valign="top">
      <a href="#AQ_NAV_STATUS_HF_LOCKED">AQ_NAV_STATUS_HF_LOCKED</a>
     </td>
     <td class="mavlink_comment">Heading-Free locked mode active</td>
    </tr>
    <tr class="mavlink_field" id="AQ_NAV_STATUS_RTH">
     <td class="mavlink_type" valign="top">0x40000000</td>
     <td class="mavlink_name" valign="top">
      <a href="#AQ_NAV_STATUS_RTH">AQ_NAV_STATUS_RTH</a>
     </td>
     <td class="mavlink_comment">Automatic Return to Home is active</td>
    </tr>
    <tr class="mavlink_field" id="AQ_NAV_STATUS_FAILSAFE">
     <td class="mavlink_type" valign="top">0x80000000</td>
     <td class="mavlink_name" valign="top">
      <a href="#AQ_NAV_STATUS_FAILSAFE">AQ_NAV_STATUS_FAILSAFE</a>
     </td>
     <td class="mavlink_comment">System is in failsafe recovery mode</td>
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
    <tr class="mavlink_field" id="MAV_CMD_AQ_NAV_LEG_ORBIT">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_AQ_NAV_LEG_ORBIT">MAV_CMD_AQ_NAV_LEG_ORBIT</a>
     </td>
     <td class="mavlink_comment">Orbit a waypoint.</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #1</td>
     <td class="mavlink_comment">Orbit radius in meters</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #2</td>
     <td class="mavlink_comment">Loiter time in decimal seconds</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #3</td>
     <td class="mavlink_comment">Maximum horizontal speed in m/s</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #4</td>
     <td class="mavlink_comment">Desired yaw angle at waypoint</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #5</td>
     <td class="mavlink_comment">Latitude</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #6</td>
     <td class="mavlink_comment">Longitude</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #7</td>
     <td class="mavlink_comment">Altitude</td>
    </tr>
    <tr>
     <td colspan="3">
      <br/>
     </td>
    </tr>
    <tr class="mavlink_field" id="MAV_CMD_AQ_TELEMETRY">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_AQ_TELEMETRY">MAV_CMD_AQ_TELEMETRY</a>
     </td>
     <td class="mavlink_comment">Start/stop AutoQuad telemetry values stream.</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #1</td>
     <td class="mavlink_comment">Start or stop (1 or 0)</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #2</td>
     <td class="mavlink_comment">Stream frequency in us</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #3</td>
     <td class="mavlink_comment">Dataset ID (refer to aq_mavlink.h::mavlinkCustomDataSets enum in AQ flight controller code)</td>
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
    <tr class="mavlink_field" id="MAV_CMD_AQ_REQUEST_VERSION">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_AQ_REQUEST_VERSION">MAV_CMD_AQ_REQUEST_VERSION</a>
     </td>
     <td class="mavlink_comment">Request AutoQuad firmware version number.</td>
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
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_MAV_DATA_STREAM">
   <a href="#ENUM_MAV_DATA_STREAM">MAV_DATA_STREAM</a>
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
    <tr class="mavlink_field" id="MAV_DATA_STREAM_PROPULSION">
     <td class="mavlink_type" valign="top">
     </td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_DATA_STREAM_PROPULSION">MAV_DATA_STREAM_PROPULSION</a>
     </td>
     <td class="mavlink_comment">Motor/ESC telemetry data.</td>
    </tr>
   </tbody>
  </table>
  <h2>MAVLink Messages</h2>
  <h3 class="mavlink_message_name" id="AQ_TELEMETRY_F">AQ_TELEMETRY_F (<a href="#AQ_TELEMETRY_F">
    #150
   </a>
   )
  </h3>
  <p class="description">Sends up to 20 raw float values.</p>
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
     <td class="mavlink_name" valign="top">Index</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Index of message</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">value1</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">value1</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">value2</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">value2</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">value3</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">value3</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">value4</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">value4</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">value5</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">value5</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">value6</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">value6</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">value7</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">value7</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">value8</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">value8</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">value9</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">value9</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">value10</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">value10</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">value11</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">value11</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">value12</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">value12</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">value13</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">value13</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">value14</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">value14</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">value15</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">value15</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">value16</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">value16</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">value17</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">value17</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">value18</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">value18</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">value19</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">value19</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">value20</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">value20</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="AQ_ESC_TELEMETRY">AQ_ESC_TELEMETRY (<a href="#AQ_ESC_TELEMETRY">
    #152
   </a>
   )
  </h3>
  <p class="description">Sends ESC32 telemetry data for up to 4 motors. Multiple messages may be sent in sequence when system has &gt; 4 motors. Data is described as follows: 
				// unsigned int state :   3;
			    // unsigned int vin :	  12;  // x 100
			    // unsigned int amps :	  14;  // x 100
			    // unsigned int rpm :	  15;
			    // unsigned int duty :	  8;   // x (255/100)
			    // - Data Version 2 -
			    //     unsigned int errors :    9;   // Bad detects error count
			    // - Data Version 3 -
			    //     unsigned int temp   :    9;   // (Deg C + 32) * 4
			    // unsigned int errCode : 3;</p>
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
     <td class="mavlink_name" valign="top">time_boot_ms</td>
     <td class="mavlink_type" valign="top">uint32_t</td>
     <td class="mavlink_comment">Timestamp of the component clock since boot time in ms.</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">seq</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Sequence number of message (first set of 4 motors is #1, next 4 is #2, etc).</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">num_motors</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Total number of active ESCs/motors on the system.</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">num_in_seq</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Number of active ESCs in this sequence (1 through this many array members will be populated with data)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">escid</td>
     <td class="mavlink_type" valign="top">uint8_t[4]</td>
     <td class="mavlink_comment">ESC/Motor ID</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">status_age</td>
     <td class="mavlink_type" valign="top">uint16_t[4]</td>
     <td class="mavlink_comment">Age of each ESC telemetry reading in ms compared to boot time. A value of 0xFFFF means timeout/no data.</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">data_version</td>
     <td class="mavlink_type" valign="top">uint8_t[4]</td>
     <td class="mavlink_comment">Version of data structure (determines contents).</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">data0</td>
     <td class="mavlink_type" valign="top">uint32_t[4]</td>
     <td class="mavlink_comment">Data bits 1-32 for each ESC.</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">data1</td>
     <td class="mavlink_type" valign="top">uint32_t[4]</td>
     <td class="mavlink_comment">Data bits 33-64 for each ESC.</td>
    </tr>
   </tbody>
  </table>
 </body>
</html>