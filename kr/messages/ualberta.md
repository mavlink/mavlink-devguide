<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_gitbook.py -->
# MAVLINK Message Set: ualberta.xml

*This is a human-readable form of the XML definition file: [ualberta.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/ualberta.xml).*

<html>
 <body>
  <p>
   <strong>MAVLink Include Files:</strong>
   <a href="common.md">common.xml</a>
  </p>
  <h2>MAVLink Type Enumerations</h2>
  <h3 class="mavlink_message_name" id="ENUM_UALBERTA_AUTOPILOT_MODE">
   <a href="#ENUM_UALBERTA_AUTOPILOT_MODE">UALBERTA_AUTOPILOT_MODE</a>
  </h3>
  <p class="description">Available autopilot modes for ualberta uav</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="MODE_MANUAL_DIRECT">
     <td class="mavlink_type" valign="top">
     </td>
     <td class="mavlink_name" valign="top">
      <a href="#MODE_MANUAL_DIRECT">MODE_MANUAL_DIRECT</a>
     </td>
     <td class="mavlink_comment">Raw input pulse widts sent to output</td>
    </tr>
    <tr class="mavlink_field" id="MODE_MANUAL_SCALED">
     <td class="mavlink_type" valign="top">
     </td>
     <td class="mavlink_name" valign="top">
      <a href="#MODE_MANUAL_SCALED">MODE_MANUAL_SCALED</a>
     </td>
     <td class="mavlink_comment">Inputs are normalized using calibration, the converted back to raw pulse widths for output</td>
    </tr>
    <tr class="mavlink_field" id="MODE_AUTO_PID_ATT">
     <td class="mavlink_type" valign="top">
     </td>
     <td class="mavlink_name" valign="top">
      <a href="#MODE_AUTO_PID_ATT">MODE_AUTO_PID_ATT</a>
     </td>
     <td class="mavlink_comment">dfsdfs</td>
    </tr>
    <tr class="mavlink_field" id="MODE_AUTO_PID_VEL">
     <td class="mavlink_type" valign="top">
     </td>
     <td class="mavlink_name" valign="top">
      <a href="#MODE_AUTO_PID_VEL">MODE_AUTO_PID_VEL</a>
     </td>
     <td class="mavlink_comment">dfsfds</td>
    </tr>
    <tr class="mavlink_field" id="MODE_AUTO_PID_POS">
     <td class="mavlink_type" valign="top">
     </td>
     <td class="mavlink_name" valign="top">
      <a href="#MODE_AUTO_PID_POS">MODE_AUTO_PID_POS</a>
     </td>
     <td class="mavlink_comment">dfsdfsdfs</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_UALBERTA_NAV_MODE">
   <a href="#ENUM_UALBERTA_NAV_MODE">UALBERTA_NAV_MODE</a>
  </h3>
  <p class="description">Navigation filter mode</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="NAV_AHRS_INIT">
     <td class="mavlink_type" valign="top">
     </td>
     <td class="mavlink_name" valign="top">
      <a href="#NAV_AHRS_INIT">NAV_AHRS_INIT</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="NAV_AHRS">
     <td class="mavlink_type" valign="top">
     </td>
     <td class="mavlink_name" valign="top">
      <a href="#NAV_AHRS">NAV_AHRS</a>
     </td>
     <td class="mavlink_comment">AHRS mode</td>
    </tr>
    <tr class="mavlink_field" id="NAV_INS_GPS_INIT">
     <td class="mavlink_type" valign="top">
     </td>
     <td class="mavlink_name" valign="top">
      <a href="#NAV_INS_GPS_INIT">NAV_INS_GPS_INIT</a>
     </td>
     <td class="mavlink_comment">INS/GPS initialization mode</td>
    </tr>
    <tr class="mavlink_field" id="NAV_INS_GPS">
     <td class="mavlink_type" valign="top">
     </td>
     <td class="mavlink_name" valign="top">
      <a href="#NAV_INS_GPS">NAV_INS_GPS</a>
     </td>
     <td class="mavlink_comment">INS/GPS mode</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_UALBERTA_PILOT_MODE">
   <a href="#ENUM_UALBERTA_PILOT_MODE">UALBERTA_PILOT_MODE</a>
  </h3>
  <p class="description">Mode currently commanded by pilot</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="PILOT_MANUAL">
     <td class="mavlink_type" valign="top">
     </td>
     <td class="mavlink_name" valign="top">
      <a href="#PILOT_MANUAL">PILOT_MANUAL</a>
     </td>
     <td class="mavlink_comment">sdf</td>
    </tr>
    <tr class="mavlink_field" id="PILOT_AUTO">
     <td class="mavlink_type" valign="top">
     </td>
     <td class="mavlink_name" valign="top">
      <a href="#PILOT_AUTO">PILOT_AUTO</a>
     </td>
     <td class="mavlink_comment">dfs</td>
    </tr>
    <tr class="mavlink_field" id="PILOT_ROTO">
     <td class="mavlink_type" valign="top">
     </td>
     <td class="mavlink_name" valign="top">
      <a href="#PILOT_ROTO">PILOT_ROTO</a>
     </td>
     <td class="mavlink_comment">Rotomotion mode</td>
    </tr>
   </tbody>
  </table>
  <h2>MAVLink Messages</h2>
  <h3 class="mavlink_message_name" id="NAV_FILTER_BIAS">NAV_FILTER_BIAS (<a href="#NAV_FILTER_BIAS">
    #220
   </a>
   )
  </h3>
  <p class="description">Accelerometer and Gyro biases from the navigation filter</p>
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
     <td class="mavlink_name" valign="top">usec</td>
     <td class="mavlink_type" valign="top">uint64_t</td>
     <td class="mavlink_comment">Timestamp (microseconds)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">accel_0</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">b_f[0]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">accel_1</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">b_f[1]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">accel_2</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">b_f[2]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">gyro_0</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">b_f[0]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">gyro_1</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">b_f[1]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">gyro_2</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">b_f[2]</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="RADIO_CALIBRATION">RADIO_CALIBRATION (<a href="#RADIO_CALIBRATION">
    #221
   </a>
   )
  </h3>
  <p class="description">Complete set of calibration parameters for the radio</p>
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
     <td class="mavlink_name" valign="top">aileron</td>
     <td class="mavlink_type" valign="top">uint16_t[3]</td>
     <td class="mavlink_comment">Aileron setpoints: left, center, right</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">elevator</td>
     <td class="mavlink_type" valign="top">uint16_t[3]</td>
     <td class="mavlink_comment">Elevator setpoints: nose down, center, nose up</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">rudder</td>
     <td class="mavlink_type" valign="top">uint16_t[3]</td>
     <td class="mavlink_comment">Rudder setpoints: nose left, center, nose right</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">gyro</td>
     <td class="mavlink_type" valign="top">uint16_t[2]</td>
     <td class="mavlink_comment">Tail gyro mode/gain setpoints: heading hold, rate mode</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">pitch</td>
     <td class="mavlink_type" valign="top">uint16_t[5]</td>
     <td class="mavlink_comment">Pitch curve setpoints (every 25%)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">throttle</td>
     <td class="mavlink_type" valign="top">uint16_t[5]</td>
     <td class="mavlink_comment">Throttle curve setpoints (every 25%)</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="UALBERTA_SYS_STATUS">UALBERTA_SYS_STATUS (<a href="#UALBERTA_SYS_STATUS">
    #222
   </a>
   )
  </h3>
  <p class="description">System status specific to ualberta uav</p>
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
     <td class="mavlink_name" valign="top">mode</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">System mode, see UALBERTA_AUTOPILOT_MODE ENUM</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">nav_mode</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Navigation mode, see UALBERTA_NAV_MODE ENUM</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">pilot</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Pilot mode, see UALBERTA_PILOT_MODE</td>
    </tr>
   </tbody>
  </table>
 </body>
</html>