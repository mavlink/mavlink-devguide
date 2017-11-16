<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_gitbook.py -->
# MAVLINK Message Set: ASLUAV.xml

*This is a human-readable form of the XML definition file: [ASLUAV.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/ASLUAV.xml).*

<html>
 <body>
  <p>
   <strong>MAVLink Include Files:</strong>
   <a href="common.md">common.xml</a>
  </p>
  <h2>MAVLink Type Enumerations</h2>
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
    <tr class="mavlink_field" id="MAV_CMD_RESET_MPPT">
     <td class="mavlink_type" valign="top">40001</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_RESET_MPPT">MAV_CMD_RESET_MPPT</a>
     </td>
     <td class="mavlink_comment">Mission command to reset Maximum Power Point Tracker (MPPT)</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #1</td>
     <td class="mavlink_comment">MPPT number</td>
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
    <tr class="mavlink_field" id="MAV_CMD_PAYLOAD_CONTROL">
     <td class="mavlink_type" valign="top">40002</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_PAYLOAD_CONTROL">MAV_CMD_PAYLOAD_CONTROL</a>
     </td>
     <td class="mavlink_comment">Mission command to perform a power cycle on payload</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #1</td>
     <td class="mavlink_comment">Complete power cycle</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #2</td>
     <td class="mavlink_comment">VISensor power cycle</td>
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
  <h2>MAVLink Messages</h2>
  <h3 class="mavlink_message_name" id="SENS_POWER">SENS_POWER (<a href="#SENS_POWER">
    #201
   </a>
   )
  </h3>
  <p class="description">Voltage and current sensor data</p>
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
     <td class="mavlink_name" valign="top">adc121_vspb_volt</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Power board voltage sensor reading in volts</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">adc121_cspb_amp</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Power board current sensor reading in amps</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">adc121_cs1_amp</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Board current sensor 1 reading in amps</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">adc121_cs2_amp</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Board current sensor 2 reading in amps</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SENS_MPPT">SENS_MPPT (<a href="#SENS_MPPT">
    #202
   </a>
   )
  </h3>
  <p class="description">Maximum Power Point Tracker (MPPT) sensor data for solar module power performance tracking</p>
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
     <td class="mavlink_name" valign="top">mppt_timestamp</td>
     <td class="mavlink_type" valign="top">uint64_t</td>
     <td class="mavlink_comment">MPPT last timestamp</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">mppt1_volt</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">MPPT1 voltage</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">mppt1_amp</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">MPPT1 current</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">mppt1_pwm</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">MPPT1 pwm</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">mppt1_status</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">MPPT1 status</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">mppt2_volt</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">MPPT2 voltage</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">mppt2_amp</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">MPPT2 current</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">mppt2_pwm</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">MPPT2 pwm</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">mppt2_status</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">MPPT2 status</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">mppt3_volt</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">MPPT3 voltage</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">mppt3_amp</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">MPPT3 current</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">mppt3_pwm</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">MPPT3 pwm</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">mppt3_status</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">MPPT3 status</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ASLCTRL_DATA">ASLCTRL_DATA (<a href="#ASLCTRL_DATA">
    #203
   </a>
   )
  </h3>
  <p class="description">ASL-fixed-wing controller data</p>
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
     <td class="mavlink_name" valign="top">timestamp</td>
     <td class="mavlink_type" valign="top">uint64_t</td>
     <td class="mavlink_comment">Timestamp</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">aslctrl_mode</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">ASLCTRL control-mode (manual, stabilized, auto, etc...)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">h</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">See sourcecode for a description of these values...</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">hRef</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">hRef_t</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">PitchAngle</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Pitch angle [deg]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">PitchAngleRef</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Pitch angle reference[deg]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">q</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">qRef</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">uElev</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">uThrot</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">uThrot2</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">nZ</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">AirspeedRef</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Airspeed reference [m/s]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">SpoilersEngaged</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">YawAngle</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Yaw angle [deg]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">YawAngleRef</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Yaw angle reference[deg]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">RollAngle</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Roll angle [deg]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">RollAngleRef</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Roll angle reference[deg]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">p</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">pRef</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">r</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">rRef</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">uAil</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">uRud</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">
     </td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ASLCTRL_DEBUG">ASLCTRL_DEBUG (<a href="#ASLCTRL_DEBUG">
    #204
   </a>
   )
  </h3>
  <p class="description">ASL-fixed-wing controller debug data</p>
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
     <td class="mavlink_name" valign="top">i32_1</td>
     <td class="mavlink_type" valign="top">uint32_t</td>
     <td class="mavlink_comment">Debug data</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">i8_1</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Debug data</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">i8_2</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Debug data</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">f_1</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Debug data</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">f_2</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Debug data</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">f_3</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Debug data</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">f_4</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Debug data</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">f_5</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Debug data</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">f_6</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Debug data</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">f_7</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Debug data</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">f_8</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Debug data</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ASLUAV_STATUS">ASLUAV_STATUS (<a href="#ASLUAV_STATUS">
    #205
   </a>
   )
  </h3>
  <p class="description">Extended state information for ASLUAVs</p>
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
     <td class="mavlink_name" valign="top">LED_status</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Status of the position-indicator LEDs</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">SATCOM_status</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Status of the IRIDIUM satellite communication system</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">Servo_status</td>
     <td class="mavlink_type" valign="top">uint8_t[8]</td>
     <td class="mavlink_comment">Status vector for up to 8 servos</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">Motor_rpm</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Motor RPM</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="EKF_EXT">EKF_EXT (<a href="#EKF_EXT">
    #206
   </a>
   )
  </h3>
  <p class="description">Extended EKF state estimates for ASLUAVs</p>
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
     <td class="mavlink_name" valign="top">timestamp</td>
     <td class="mavlink_type" valign="top">uint64_t</td>
     <td class="mavlink_comment">Time since system start [us]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">Windspeed</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Magnitude of wind velocity (in lateral inertial plane) [m/s]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">WindDir</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Wind heading angle from North [rad]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">WindZ</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Z (Down) component of inertial wind velocity [m/s]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">Airspeed</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Magnitude of air velocity [m/s]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">beta</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Sideslip angle [rad]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">alpha</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Angle of attack [rad]</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ASL_OBCTRL">ASL_OBCTRL (<a href="#ASL_OBCTRL">
    #207
   </a>
   )
  </h3>
  <p class="description">Off-board controls/commands for ASLUAVs</p>
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
     <td class="mavlink_name" valign="top">timestamp</td>
     <td class="mavlink_type" valign="top">uint64_t</td>
     <td class="mavlink_comment">Time since system start [us]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">uElev</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Elevator command [~]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">uThrot</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Throttle command [~]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">uThrot2</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Throttle 2 command [~]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">uAilL</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Left aileron command [~]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">uAilR</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Right aileron command [~]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">uRud</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Rudder command [~]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">obctrl_status</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Off-board computer status</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SENS_ATMOS">SENS_ATMOS (<a href="#SENS_ATMOS">
    #208
   </a>
   )
  </h3>
  <p class="description">Atmospheric sensors (temperature, humidity, ...)</p>
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
     <td class="mavlink_name" valign="top">TempAmbient</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Ambient temperature [degrees Celsius]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">Humidity</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Relative humidity [%]</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SENS_BATMON">SENS_BATMON (<a href="#SENS_BATMON">
    #209
   </a>
   )
  </h3>
  <p class="description">Battery pack monitoring data for Li-Ion batteries</p>
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
     <td class="mavlink_name" valign="top">temperature</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Battery pack temperature in [deg C]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">voltage</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Battery pack voltage in [mV]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">current</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Battery pack current in [mA]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">SoC</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Battery pack state-of-charge</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">batterystatus</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Battery monitor status report bits in Hex</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">serialnumber</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Battery monitor serial number in Hex</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">hostfetcontrol</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Battery monitor sensor host FET control in Hex</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">cellvoltage1</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Battery pack cell 1 voltage in [mV]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">cellvoltage2</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Battery pack cell 2 voltage in [mV]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">cellvoltage3</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Battery pack cell 3 voltage in [mV]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">cellvoltage4</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Battery pack cell 4 voltage in [mV]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">cellvoltage5</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Battery pack cell 5 voltage in [mV]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">cellvoltage6</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Battery pack cell 6 voltage in [mV]</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="FW_SOARING_DATA">FW_SOARING_DATA (<a href="#FW_SOARING_DATA">
    #210
   </a>
   )
  </h3>
  <p class="description">Fixed-wing soaring (i.e. thermal seeking) data</p>
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
     <td class="mavlink_name" valign="top">timestamp</td>
     <td class="mavlink_type" valign="top">uint64_t</td>
     <td class="mavlink_comment">Timestamp [ms]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">timestampModeChanged</td>
     <td class="mavlink_type" valign="top">uint64_t</td>
     <td class="mavlink_comment">Timestamp since last mode change[ms]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">xW</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Thermal core updraft strength [m/s]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">xR</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Thermal radius [m]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">xLat</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Thermal center latitude [deg]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">xLon</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Thermal center longitude [deg]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">VarW</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Variance W</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">VarR</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Variance R</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">VarLat</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Variance Lat</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">VarLon</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Variance Lon</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">LoiterRadius</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Suggested loiter radius [m]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">LoiterDirection</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Suggested loiter direction</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">DistToSoarPoint</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Distance to soar point [m]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">vSinkExp</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Expected sink rate at current airspeed, roll and throttle [m/s]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">z1_LocalUpdraftSpeed</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Measurement / updraft speed at current/local airplane position [m/s]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">z2_DeltaRoll</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Measurement / roll angle tracking error [deg]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">z1_exp</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Expected measurement 1</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">z2_exp</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Expected measurement 2</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">ThermalGSNorth</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Thermal drift (from estimator prediction step only) [m/s]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">ThermalGSEast</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Thermal drift (from estimator prediction step only) [m/s]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">TSE_dot</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Total specific energy change (filtered) [m/s]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">DebugVar1</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Debug variable 1</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">DebugVar2</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Debug variable 2</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">ControlMode</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Control Mode [-]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">valid</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Data valid [-]</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SENSORPOD_STATUS">SENSORPOD_STATUS (<a href="#SENSORPOD_STATUS">
    #211
   </a>
   )
  </h3>
  <p class="description">Monitoring of sensorpod status</p>
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
     <td class="mavlink_name" valign="top">timestamp</td>
     <td class="mavlink_type" valign="top">uint64_t</td>
     <td class="mavlink_comment">Timestamp in linuxtime [ms] (since 1.1.1970)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">visensor_rate_1</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Rate of ROS topic 1</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">visensor_rate_2</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Rate of ROS topic 2</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">visensor_rate_3</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Rate of ROS topic 3</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">visensor_rate_4</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Rate of ROS topic 4</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">recording_nodes_count</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Number of recording nodes</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">cpu_temp</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Temperature of sensorpod CPU in [deg C]</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">free_space</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Free space available in recordings directory in [Gb] * 1e2</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SENS_POWER_BOARD">SENS_POWER_BOARD (<a href="#SENS_POWER_BOARD">
    #212
   </a>
   )
  </h3>
  <p class="description">Monitoring of power board status</p>
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
     <td class="mavlink_name" valign="top">timestamp</td>
     <td class="mavlink_type" valign="top">uint64_t</td>
     <td class="mavlink_comment">Timestamp</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">pwr_brd_status</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Power board status register</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">pwr_brd_led_status</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Power board leds status</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">pwr_brd_system_volt</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Power board system voltage</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">pwr_brd_servo_volt</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Power board servo voltage</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">pwr_brd_mot_l_amp</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Power board left motor current sensor</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">pwr_brd_mot_r_amp</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Power board right motor current sensor</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">pwr_brd_servo_1_amp</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Power board servo1 current sensor</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">pwr_brd_servo_2_amp</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Power board servo1 current sensor</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">pwr_brd_servo_3_amp</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Power board servo1 current sensor</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">pwr_brd_servo_4_amp</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Power board servo1 current sensor</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">pwr_brd_aux_amp</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Power board aux current sensor</td>
    </tr>
   </tbody>
  </table>
 </body>
</html>