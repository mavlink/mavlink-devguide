<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_gitbook.py -->

# MAVLINK Message Set: autoquad.xml

*This is a human-readable form of the XML definition file: [autoquad.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/autoquad.xml).*

<span></span>

> **Note** MAVLink 2 messages have an ID > 255 and are marked up using **(MAVLink 2)** in their description.

<span id="mav2_extension_field"></span>

> **Note** MAVLink 2 extension fields that have been added to MAVLink 1 messages are displayed in blue. 

<style>
td {
    vertical-align:top;
}
</style>

 <html>
 <body></p>

<p>
   <strong>MAVLink Include Files:</strong>
   <a href="common.md">common.xml</a>
  </p>

<h2>MAVLink Protocol Version</h2>

<p>The current MAVLink version is 2.3. The minor version numbers (after the dot) range from 1-255.</p>

<h2>MAVLink Type Enumerations</h2>

<h3 id="AUTOQUAD_MAVLINK_DEFS_VERSION">
   <a href="#AUTOQUAD_MAVLINK_DEFS_VERSION">AUTOQUAD_MAVLINK_DEFS_VERSION</a>
  </h3>

<p>Track current version of these definitions (can be used by checking value of AUTOQUAD_MAVLINK_DEFS_VERSION_ENUM_END). Append a new entry for each published change.</p>

<table class="sortable">
   <thead>
    <tr>
     <th>Value</th>
     <th>Field Name</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr id="AQ_MAVLINK_DEFS_VERSION_1">
     <td>
     </td>
     <td>
      <a href="#AQ_MAVLINK_DEFS_VERSION_1">AQ_MAVLINK_DEFS_VERSION_1</a>
     </td>
     <td>
     </td>
    </tr>
   </tbody>
  </table>

<h3 id="AUTOQUAD_NAV_STATUS">
   <a href="#AUTOQUAD_NAV_STATUS">AUTOQUAD_NAV_STATUS</a>
  </h3>

<p>Available operating modes/statuses for AutoQuad flight controller. 
                Bitmask up to 32 bits. Low side bits for base modes, high side for 
                additional active features/modifiers/constraints.</p>

<table class="sortable">
   <thead>
    <tr>
     <th>Value</th>
     <th>Field Name</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr id="AQ_NAV_STATUS_INIT">
     <td>0</td>
     <td>
      <a href="#AQ_NAV_STATUS_INIT">AQ_NAV_STATUS_INIT</a>
     </td>
     <td>System is initializing</td>
    </tr>
    <tr id="AQ_NAV_STATUS_STANDBY">
     <td>0x00000001</td>
     <td>
      <a href="#AQ_NAV_STATUS_STANDBY">AQ_NAV_STATUS_STANDBY</a>
     </td>
     <td>System is *armed* and standing by, with no throttle input and no autonomous mode</td>
    </tr>
    <tr id="AQ_NAV_STATUS_MANUAL">
     <td>0x00000002</td>
     <td>
      <a href="#AQ_NAV_STATUS_MANUAL">AQ_NAV_STATUS_MANUAL</a>
     </td>
     <td>Flying (throttle input detected), assumed under manual control unless other mode bits are set</td>
    </tr>
    <tr id="AQ_NAV_STATUS_ALTHOLD">
     <td>0x00000004</td>
     <td>
      <a href="#AQ_NAV_STATUS_ALTHOLD">AQ_NAV_STATUS_ALTHOLD</a>
     </td>
     <td>Altitude hold engaged</td>
    </tr>
    <tr id="AQ_NAV_STATUS_POSHOLD">
     <td>0x00000008</td>
     <td>
      <a href="#AQ_NAV_STATUS_POSHOLD">AQ_NAV_STATUS_POSHOLD</a>
     </td>
     <td>Position hold engaged</td>
    </tr>
    <tr id="AQ_NAV_STATUS_GUIDED">
     <td>0x00000010</td>
     <td>
      <a href="#AQ_NAV_STATUS_GUIDED">AQ_NAV_STATUS_GUIDED</a>
     </td>
     <td>Externally-guided (eg. GCS) navigation mode</td>
    </tr>
    <tr id="AQ_NAV_STATUS_MISSION">
     <td>0x00000020</td>
     <td>
      <a href="#AQ_NAV_STATUS_MISSION">AQ_NAV_STATUS_MISSION</a>
     </td>
     <td>Autonomous mission execution mode</td>
    </tr>
    <tr id="AQ_NAV_STATUS_READY">
     <td>0x00000100</td>
     <td>
      <a href="#AQ_NAV_STATUS_READY">AQ_NAV_STATUS_READY</a>
     </td>
     <td>Ready but *not armed*</td>
    </tr>
    <tr id="AQ_NAV_STATUS_CALIBRATING">
     <td>0x00000200</td>
     <td>
      <a href="#AQ_NAV_STATUS_CALIBRATING">AQ_NAV_STATUS_CALIBRATING</a>
     </td>
     <td>Calibration mode active</td>
    </tr>
    <tr id="AQ_NAV_STATUS_NO_RC">
     <td>0x00001000</td>
     <td>
      <a href="#AQ_NAV_STATUS_NO_RC">AQ_NAV_STATUS_NO_RC</a>
     </td>
     <td>No valid control input (eg. no radio link)</td>
    </tr>
    <tr id="AQ_NAV_STATUS_FUEL_LOW">
     <td>0x00002000</td>
     <td>
      <a href="#AQ_NAV_STATUS_FUEL_LOW">AQ_NAV_STATUS_FUEL_LOW</a>
     </td>
     <td>Battery is low (stage 1 warning)</td>
    </tr>
    <tr id="AQ_NAV_STATUS_FUEL_CRITICAL">
     <td>0x00004000</td>
     <td>
      <a href="#AQ_NAV_STATUS_FUEL_CRITICAL">AQ_NAV_STATUS_FUEL_CRITICAL</a>
     </td>
     <td>Battery is depleted (stage 2 warning)</td>
    </tr>
    <tr id="AQ_NAV_STATUS_DVH">
     <td>0x01000000</td>
     <td>
      <a href="#AQ_NAV_STATUS_DVH">AQ_NAV_STATUS_DVH</a>
     </td>
     <td>Dynamic Velocity Hold is active (PH with proportional manual direction override)</td>
    </tr>
    <tr id="AQ_NAV_STATUS_DAO">
     <td>0x02000000</td>
     <td>
      <a href="#AQ_NAV_STATUS_DAO">AQ_NAV_STATUS_DAO</a>
     </td>
     <td>Dynamic Altitude Override is active (AH with proportional manual adjustment)</td>
    </tr>
    <tr id="AQ_NAV_STATUS_CEILING_REACHED">
     <td>0x04000000</td>
     <td>
      <a href="#AQ_NAV_STATUS_CEILING_REACHED">AQ_NAV_STATUS_CEILING_REACHED</a>
     </td>
     <td>Craft is at ceiling altitude</td>
    </tr>
    <tr id="AQ_NAV_STATUS_CEILING">
     <td>0x08000000</td>
     <td>
      <a href="#AQ_NAV_STATUS_CEILING">AQ_NAV_STATUS_CEILING</a>
     </td>
     <td>Ceiling altitude is set</td>
    </tr>
    <tr id="AQ_NAV_STATUS_HF_DYNAMIC">
     <td>0x10000000</td>
     <td>
      <a href="#AQ_NAV_STATUS_HF_DYNAMIC">AQ_NAV_STATUS_HF_DYNAMIC</a>
     </td>
     <td>Heading-Free dynamic mode active</td>
    </tr>
    <tr id="AQ_NAV_STATUS_HF_LOCKED">
     <td>0x20000000</td>
     <td>
      <a href="#AQ_NAV_STATUS_HF_LOCKED">AQ_NAV_STATUS_HF_LOCKED</a>
     </td>
     <td>Heading-Free locked mode active</td>
    </tr>
    <tr id="AQ_NAV_STATUS_RTH">
     <td>0x40000000</td>
     <td>
      <a href="#AQ_NAV_STATUS_RTH">AQ_NAV_STATUS_RTH</a>
     </td>
     <td>Automatic Return to Home is active</td>
    </tr>
    <tr id="AQ_NAV_STATUS_FAILSAFE">
     <td>0x80000000</td>
     <td>
      <a href="#AQ_NAV_STATUS_FAILSAFE">AQ_NAV_STATUS_FAILSAFE</a>
     </td>
     <td>System is in failsafe recovery mode</td>
    </tr>
   </tbody>
  </table>

<h3 id="MAV_CMD">
   <a href="#MAV_CMD">MAV_CMD</a>
  </h3>

<p>
  </p>

<table class="sortable">
   <thead>
    <tr>
     <th>Value</th>
     <th>Field Name</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr id="MAV_CMD_AQ_NAV_LEG_ORBIT">
     <td>1</td>
     <td>
      <a href="#MAV_CMD_AQ_NAV_LEG_ORBIT">MAV_CMD_AQ_NAV_LEG_ORBIT</a>
     </td>
     <td>Orbit a waypoint.</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td>Mission Param #1</td>
     <td>Orbit radius in meters</td>
    </tr>
    <tr>
     <td>
     </td>
     <td>Mission Param #2</td>
     <td>Loiter time in decimal seconds</td>
    </tr>
    <tr>
     <td>
     </td>
     <td>Mission Param #3</td>
     <td>Maximum horizontal speed in m/s</td>
    </tr>
    <tr>
     <td>
     </td>
     <td>Mission Param #4</td>
     <td>Desired yaw angle at waypoint</td>
    </tr>
    <tr>
     <td>
     </td>
     <td>Mission Param #5</td>
     <td>Latitude</td>
    </tr>
    <tr>
     <td>
     </td>
     <td>Mission Param #6</td>
     <td>Longitude</td>
    </tr>
    <tr>
     <td>
     </td>
     <td>Mission Param #7</td>
     <td>Altitude</td>
    </tr>
    <tr>
     <td colspan="3">
      <br/>
     </td>
    </tr>
    <tr id="MAV_CMD_AQ_TELEMETRY">
     <td>2</td>
     <td>
      <a href="#MAV_CMD_AQ_TELEMETRY">MAV_CMD_AQ_TELEMETRY</a>
     </td>
     <td>Start/stop AutoQuad telemetry values stream.</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td>Mission Param #1</td>
     <td>Start or stop (1 or 0)</td>
    </tr>
    <tr>
     <td>
     </td>
     <td>Mission Param #2</td>
     <td>Stream frequency in us</td>
    </tr>
    <tr>
     <td>
     </td>
     <td>Mission Param #3</td>
     <td>Dataset ID (refer to aq_mavlink.h::mavlinkCustomDataSets enum in AQ flight controller code)</td>
    </tr>
    <tr>
     <td>
     </td>
     <td>Mission Param #4</td>
     <td>Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td>Mission Param #5</td>
     <td>Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td>Mission Param #6</td>
     <td>Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td>Mission Param #7</td>
     <td>Empty</td>
    </tr>
    <tr>
     <td colspan="3">
      <br/>
     </td>
    </tr>
    <tr id="MAV_CMD_AQ_REQUEST_VERSION">
     <td>4</td>
     <td>
      <a href="#MAV_CMD_AQ_REQUEST_VERSION">MAV_CMD_AQ_REQUEST_VERSION</a>
     </td>
     <td>Request AutoQuad firmware version number.</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td>Mission Param #1</td>
     <td>Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td>Mission Param #2</td>
     <td>Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td>Mission Param #3</td>
     <td>Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td>Mission Param #4</td>
     <td>Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td>Mission Param #5</td>
     <td>Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td>Mission Param #6</td>
     <td>Empty</td>
    </tr>
    <tr>
     <td>
     </td>
     <td>Mission Param #7</td>
     <td>Empty</td>
    </tr>
    <tr>
     <td colspan="3">
      <br/>
     </td>
    </tr>
   </tbody>
  </table>

<h3 id="MAV_DATA_STREAM">
   <a href="#MAV_DATA_STREAM">MAV_DATA_STREAM</a>
  </h3>

<p>
  </p>

<table class="sortable">
   <thead>
    <tr>
     <th>Value</th>
     <th>Field Name</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr id="MAV_DATA_STREAM_PROPULSION">
     <td>
     </td>
     <td>
      <a href="#MAV_DATA_STREAM_PROPULSION">MAV_DATA_STREAM_PROPULSION</a>
     </td>
     <td>Motor/ESC telemetry data.</td>
    </tr>
   </tbody>
  </table>

<h2>MAVLink Messages</h2>

<h3 id="AQ_TELEMETRY_F">AQ_TELEMETRY_F (<a href="#AQ_TELEMETRY_F">
    #150
   </a>
   )
  </h3>

<p>Sends up to 20 raw float values.</p>

<table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>Index</td>
     <td>uint16_t</td>
     <td>Index of message</td>
    </tr>
    <tr>
     <td>value1</td>
     <td>float</td>
     <td>value1</td>
    </tr>
    <tr>
     <td>value2</td>
     <td>float</td>
     <td>value2</td>
    </tr>
    <tr>
     <td>value3</td>
     <td>float</td>
     <td>value3</td>
    </tr>
    <tr>
     <td>value4</td>
     <td>float</td>
     <td>value4</td>
    </tr>
    <tr>
     <td>value5</td>
     <td>float</td>
     <td>value5</td>
    </tr>
    <tr>
     <td>value6</td>
     <td>float</td>
     <td>value6</td>
    </tr>
    <tr>
     <td>value7</td>
     <td>float</td>
     <td>value7</td>
    </tr>
    <tr>
     <td>value8</td>
     <td>float</td>
     <td>value8</td>
    </tr>
    <tr>
     <td>value9</td>
     <td>float</td>
     <td>value9</td>
    </tr>
    <tr>
     <td>value10</td>
     <td>float</td>
     <td>value10</td>
    </tr>
    <tr>
     <td>value11</td>
     <td>float</td>
     <td>value11</td>
    </tr>
    <tr>
     <td>value12</td>
     <td>float</td>
     <td>value12</td>
    </tr>
    <tr>
     <td>value13</td>
     <td>float</td>
     <td>value13</td>
    </tr>
    <tr>
     <td>value14</td>
     <td>float</td>
     <td>value14</td>
    </tr>
    <tr>
     <td>value15</td>
     <td>float</td>
     <td>value15</td>
    </tr>
    <tr>
     <td>value16</td>
     <td>float</td>
     <td>value16</td>
    </tr>
    <tr>
     <td>value17</td>
     <td>float</td>
     <td>value17</td>
    </tr>
    <tr>
     <td>value18</td>
     <td>float</td>
     <td>value18</td>
    </tr>
    <tr>
     <td>value19</td>
     <td>float</td>
     <td>value19</td>
    </tr>
    <tr>
     <td>value20</td>
     <td>float</td>
     <td>value20</td>
    </tr>
   </tbody>
  </table>

<h3 id="AQ_ESC_TELEMETRY">AQ_ESC_TELEMETRY (<a href="#AQ_ESC_TELEMETRY">
    #152
   </a>
   )
  </h3>

<p>Sends ESC32 telemetry data for up to 4 motors. Multiple messages may be sent in sequence when system has &gt; 4 motors. Data is described as follows: 
                // unsigned int state :   3;
                // unsigned int vin :     12;  // x 100
                // unsigned int amps :    14;  // x 100
                // unsigned int rpm :     15;
                // unsigned int duty :    8;   // x (255/100)
                // - Data Version 2 -
                //     unsigned int errors :    9;   // Bad detects error count
                // - Data Version 3 -
                //     unsigned int temp   :    9;   // (Deg C + 32) * 4
                // unsigned int errCode : 3;</p>

<table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>time_boot_ms</td>
     <td>uint32_t</td>
     <td>Timestamp of the component clock since boot time in ms.</td>
    </tr>
    <tr>
     <td>seq</td>
     <td>uint8_t</td>
     <td>Sequence number of message (first set of 4 motors is #1, next 4 is #2, etc).</td>
    </tr>
    <tr>
     <td>num_motors</td>
     <td>uint8_t</td>
     <td>Total number of active ESCs/motors on the system.</td>
    </tr>
    <tr>
     <td>num_in_seq</td>
     <td>uint8_t</td>
     <td>Number of active ESCs in this sequence (1 through this many array members will be populated with data)</td>
    </tr>
    <tr>
     <td>escid</td>
     <td>uint8_t[4]</td>
     <td>ESC/Motor ID</td>
    </tr>
    <tr>
     <td>status_age</td>
     <td>uint16_t[4]</td>
     <td>Age of each ESC telemetry reading in ms compared to boot time. A value of 0xFFFF means timeout/no data.</td>
    </tr>
    <tr>
     <td>data_version</td>
     <td>uint8_t[4]</td>
     <td>Version of data structure (determines contents).</td>
    </tr>
    <tr>
     <td>data0</td>
     <td>uint32_t[4]</td>
     <td>Data bits 1-32 for each ESC.</td>
    </tr>
    <tr>
     <td>data1</td>
     <td>uint32_t[4]</td>
     <td>Data bits 33-64 for each ESC.</td>
    </tr>
   </tbody>
  </table>

<p></body>
</html>
