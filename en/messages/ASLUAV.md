<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_gitbook.py -->
# MAVLINK Message Set: ASLUAV.xml

*This is a human-readable form of the XML definition file: [ASLUAV.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/ASLUAV.xml).*

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
 <body>
  <p>
   <strong>MAVLink Include Files:</strong>
   <a href="common.md">common.xml</a>
  </p>
  <h2>MAVLink Type Enumerations</h2>
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
    <tr id="MAV_CMD_RESET_MPPT">
     <td>40001</td>
     <td>
      <a href="#MAV_CMD_RESET_MPPT">MAV_CMD_RESET_MPPT</a>
     </td>
     <td>Mission command to reset Maximum Power Point Tracker (MPPT)</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td>Mission Param #1</td>
     <td>MPPT number</td>
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
    <tr id="MAV_CMD_PAYLOAD_CONTROL">
     <td>40002</td>
     <td>
      <a href="#MAV_CMD_PAYLOAD_CONTROL">MAV_CMD_PAYLOAD_CONTROL</a>
     </td>
     <td>Mission command to perform a power cycle on payload</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td>Mission Param #1</td>
     <td>Complete power cycle</td>
    </tr>
    <tr>
     <td>
     </td>
     <td>Mission Param #2</td>
     <td>VISensor power cycle</td>
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
  <h3 id="GSM_LINK_TYPE">
   <a href="#GSM_LINK_TYPE">GSM_LINK_TYPE</a>
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
    <tr id="GSM_LINK_TYPE_NONE">
     <td>0</td>
     <td>
      <a href="#GSM_LINK_TYPE_NONE">GSM_LINK_TYPE_NONE</a>
     </td>
     <td>no service</td>
    </tr>
    <tr id="GSM_LINK_TYPE_UNKNOWN">
     <td>1</td>
     <td>
      <a href="#GSM_LINK_TYPE_UNKNOWN">GSM_LINK_TYPE_UNKNOWN</a>
     </td>
     <td>link type unknown</td>
    </tr>
    <tr id="GSM_LINK_TYPE_2G">
     <td>2</td>
     <td>
      <a href="#GSM_LINK_TYPE_2G">GSM_LINK_TYPE_2G</a>
     </td>
     <td>2G (GSM/GRPS/EDGE) link</td>
    </tr>
    <tr id="GSM_LINK_TYPE_3G">
     <td>3</td>
     <td>
      <a href="#GSM_LINK_TYPE_3G">GSM_LINK_TYPE_3G</a>
     </td>
     <td>3G link (WCDMA/HSDPA/HSPA)</td>
    </tr>
    <tr id="GSM_LINK_TYPE_4G">
     <td>4</td>
     <td>
      <a href="#GSM_LINK_TYPE_4G">GSM_LINK_TYPE_4G</a>
     </td>
     <td>4G link (LTE)</td>
    </tr>
   </tbody>
  </table>
  <h3 id="GSM_MODEM_TYPE">
   <a href="#GSM_MODEM_TYPE">GSM_MODEM_TYPE</a>
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
    <tr id="GSM_MODEM_TYPE_UNKNOWN">
     <td>0</td>
     <td>
      <a href="#GSM_MODEM_TYPE_UNKNOWN">GSM_MODEM_TYPE_UNKNOWN</a>
     </td>
     <td>not specified</td>
    </tr>
    <tr id="GSM_MODEM_TYPE_HUAWEI_E3372">
     <td>
     </td>
     <td>
      <a href="#GSM_MODEM_TYPE_HUAWEI_E3372">GSM_MODEM_TYPE_HUAWEI_E3372</a>
     </td>
     <td>HUAWEI LTE USB Stick E3372</td>
    </tr>
   </tbody>
  </table>
  <h2>MAVLink Messages</h2>
  <h3 id="COMMAND_INT_STAMPED">COMMAND_INT_STAMPED (<a href="#COMMAND_INT_STAMPED">
    #78
   </a>
   )
  </h3>
  <p>Message encoding a command with parameters as scaled integers and additional metadata. Scaling depends on the actual command value.</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Values</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>utc_time</td>
     <td>uint32_t</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>UTC time, seconds elapsed since 01.01.1970</td>
    </tr>
    <tr>
     <td>vehicle_timestamp</td>
     <td>uint64_t</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>Microseconds elapsed since vehicle boot</td>
    </tr>
    <tr>
     <td>target_system</td>
     <td>uint8_t</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>System ID</td>
    </tr>
    <tr>
     <td>target_component</td>
     <td>uint8_t</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>Component ID</td>
    </tr>
    <tr>
     <td>frame</td>
     <td>uint8_t</td>
     <td>
      <a href="#MAV_FRAME">MAV_FRAME</a>
     </td>
     <td>The coordinate system of the COMMAND, as defined by MAV_FRAME enum</td>
    </tr>
    <tr>
     <td>command</td>
     <td>uint16_t</td>
     <td>
      <a href="#MAV_CMD">MAV_CMD</a>
     </td>
     <td>The scheduled action for the mission item, as defined by MAV_CMD enum</td>
    </tr>
    <tr>
     <td>current</td>
     <td>uint8_t</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>false:0, true:1</td>
    </tr>
    <tr>
     <td>autocontinue</td>
     <td>uint8_t</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>autocontinue to next wp</td>
    </tr>
    <tr>
     <td>param1</td>
     <td>float</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>PARAM1, see MAV_CMD enum</td>
    </tr>
    <tr>
     <td>param2</td>
     <td>float</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>PARAM2, see MAV_CMD enum</td>
    </tr>
    <tr>
     <td>param3</td>
     <td>float</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>PARAM3, see MAV_CMD enum</td>
    </tr>
    <tr>
     <td>param4</td>
     <td>float</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>PARAM4, see MAV_CMD enum</td>
    </tr>
    <tr>
     <td>x</td>
     <td>int32_t</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>PARAM5 / local: x position in meters * 1e4, global: latitude in degrees * 10^7</td>
    </tr>
    <tr>
     <td>y</td>
     <td>int32_t</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>PARAM6 / local: y position in meters * 1e4, global: longitude in degrees * 10^7</td>
    </tr>
    <tr>
     <td>z</td>
     <td>float</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>PARAM7 / z position: global: altitude in meters (relative or absolute, depending on frame.</td>
    </tr>
   </tbody>
  </table>
  <h3 id="COMMAND_LONG_STAMPED">COMMAND_LONG_STAMPED (<a href="#COMMAND_LONG_STAMPED">
    #79
   </a>
   )
  </h3>
  <p>Send a command with up to seven parameters to the MAV and additional metadata</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Values</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>utc_time</td>
     <td>uint32_t</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>UTC time, seconds elapsed since 01.01.1970</td>
    </tr>
    <tr>
     <td>vehicle_timestamp</td>
     <td>uint64_t</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>Microseconds elapsed since vehicle boot</td>
    </tr>
    <tr>
     <td>target_system</td>
     <td>uint8_t</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>System which should execute the command</td>
    </tr>
    <tr>
     <td>target_component</td>
     <td>uint8_t</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>Component which should execute the command, 0 for all components</td>
    </tr>
    <tr>
     <td>command</td>
     <td>uint16_t</td>
     <td>
      <a href="#MAV_CMD">MAV_CMD</a>
     </td>
     <td>Command ID, as defined by MAV_CMD enum.</td>
    </tr>
    <tr>
     <td>confirmation</td>
     <td>uint8_t</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>0: First transmission of this command. 1-255: Confirmation transmissions (e.g. for kill command)</td>
    </tr>
    <tr>
     <td>param1</td>
     <td>float</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>Parameter 1, as defined by MAV_CMD enum.</td>
    </tr>
    <tr>
     <td>param2</td>
     <td>float</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>Parameter 2, as defined by MAV_CMD enum.</td>
    </tr>
    <tr>
     <td>param3</td>
     <td>float</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>Parameter 3, as defined by MAV_CMD enum.</td>
    </tr>
    <tr>
     <td>param4</td>
     <td>float</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>Parameter 4, as defined by MAV_CMD enum.</td>
    </tr>
    <tr>
     <td>param5</td>
     <td>float</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>Parameter 5, as defined by MAV_CMD enum.</td>
    </tr>
    <tr>
     <td>param6</td>
     <td>float</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>Parameter 6, as defined by MAV_CMD enum.</td>
    </tr>
    <tr>
     <td>param7</td>
     <td>float</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>Parameter 7, as defined by MAV_CMD enum.</td>
    </tr>
   </tbody>
  </table>
  <h3 id="SENS_POWER">SENS_POWER (<a href="#SENS_POWER">
    #201
   </a>
   )
  </h3>
  <p>Voltage and current sensor data</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Units</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>adc121_vspb_volt</td>
     <td>float</td>
     <td>V</td>
     <td>Power board voltage sensor reading</td>
    </tr>
    <tr>
     <td>adc121_cspb_amp</td>
     <td>float</td>
     <td>A</td>
     <td>Power board current sensor reading</td>
    </tr>
    <tr>
     <td>adc121_cs1_amp</td>
     <td>float</td>
     <td>A</td>
     <td>Board current sensor 1 reading</td>
    </tr>
    <tr>
     <td>adc121_cs2_amp</td>
     <td>float</td>
     <td>A</td>
     <td>Board current sensor 2 reading</td>
    </tr>
   </tbody>
  </table>
  <h3 id="SENS_MPPT">SENS_MPPT (<a href="#SENS_MPPT">
    #202
   </a>
   )
  </h3>
  <p>Maximum Power Point Tracker (MPPT) sensor data for solar module power performance tracking</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Units</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>mppt_timestamp</td>
     <td>uint64_t</td>
     <td>us</td>
     <td>MPPT last timestamp</td>
    </tr>
    <tr>
     <td>mppt1_volt</td>
     <td>float</td>
     <td>V</td>
     <td>MPPT1 voltage</td>
    </tr>
    <tr>
     <td>mppt1_amp</td>
     <td>float</td>
     <td>A</td>
     <td>MPPT1 current</td>
    </tr>
    <tr>
     <td>mppt1_pwm</td>
     <td>uint16_t</td>
     <td>us</td>
     <td>MPPT1 pwm</td>
    </tr>
    <tr>
     <td>mppt1_status</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>MPPT1 status</td>
    </tr>
    <tr>
     <td>mppt2_volt</td>
     <td>float</td>
     <td>V</td>
     <td>MPPT2 voltage</td>
    </tr>
    <tr>
     <td>mppt2_amp</td>
     <td>float</td>
     <td>A</td>
     <td>MPPT2 current</td>
    </tr>
    <tr>
     <td>mppt2_pwm</td>
     <td>uint16_t</td>
     <td>us</td>
     <td>MPPT2 pwm</td>
    </tr>
    <tr>
     <td>mppt2_status</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>MPPT2 status</td>
    </tr>
    <tr>
     <td>mppt3_volt</td>
     <td>float</td>
     <td>V</td>
     <td>MPPT3 voltage</td>
    </tr>
    <tr>
     <td>mppt3_amp</td>
     <td>float</td>
     <td>A</td>
     <td>MPPT3 current</td>
    </tr>
    <tr>
     <td>mppt3_pwm</td>
     <td>uint16_t</td>
     <td>us</td>
     <td>MPPT3 pwm</td>
    </tr>
    <tr>
     <td>mppt3_status</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>MPPT3 status</td>
    </tr>
   </tbody>
  </table>
  <h3 id="ASLCTRL_DATA">ASLCTRL_DATA (<a href="#ASLCTRL_DATA">
    #203
   </a>
   )
  </h3>
  <p>ASL-fixed-wing controller data</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Units</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>timestamp</td>
     <td>uint64_t</td>
     <td>us</td>
     <td>Timestamp</td>
    </tr>
    <tr>
     <td>aslctrl_mode</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>ASLCTRL control-mode (manual, stabilized, auto, etc...)</td>
    </tr>
    <tr>
     <td>h</td>
     <td>float</td>
     <td>
     </td>
     <td>See sourcecode for a description of these values...</td>
    </tr>
    <tr>
     <td>hRef</td>
     <td>float</td>
     <td>
     </td>
     <td>
     </td>
    </tr>
    <tr>
     <td>hRef_t</td>
     <td>float</td>
     <td>
     </td>
     <td>
     </td>
    </tr>
    <tr>
     <td>PitchAngle</td>
     <td>float</td>
     <td>deg</td>
     <td>Pitch angle</td>
    </tr>
    <tr>
     <td>PitchAngleRef</td>
     <td>float</td>
     <td>deg</td>
     <td>Pitch angle reference</td>
    </tr>
    <tr>
     <td>q</td>
     <td>float</td>
     <td>
     </td>
     <td>
     </td>
    </tr>
    <tr>
     <td>qRef</td>
     <td>float</td>
     <td>
     </td>
     <td>
     </td>
    </tr>
    <tr>
     <td>uElev</td>
     <td>float</td>
     <td>
     </td>
     <td>
     </td>
    </tr>
    <tr>
     <td>uThrot</td>
     <td>float</td>
     <td>
     </td>
     <td>
     </td>
    </tr>
    <tr>
     <td>uThrot2</td>
     <td>float</td>
     <td>
     </td>
     <td>
     </td>
    </tr>
    <tr>
     <td>nZ</td>
     <td>float</td>
     <td>
     </td>
     <td>
     </td>
    </tr>
    <tr>
     <td>AirspeedRef</td>
     <td>float</td>
     <td>m/s</td>
     <td>Airspeed reference</td>
    </tr>
    <tr>
     <td>SpoilersEngaged</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>
     </td>
    </tr>
    <tr>
     <td>YawAngle</td>
     <td>float</td>
     <td>deg</td>
     <td>Yaw angle</td>
    </tr>
    <tr>
     <td>YawAngleRef</td>
     <td>float</td>
     <td>deg</td>
     <td>Yaw angle reference</td>
    </tr>
    <tr>
     <td>RollAngle</td>
     <td>float</td>
     <td>deg</td>
     <td>Roll angle</td>
    </tr>
    <tr>
     <td>RollAngleRef</td>
     <td>float</td>
     <td>deg</td>
     <td>Roll angle reference</td>
    </tr>
    <tr>
     <td>p</td>
     <td>float</td>
     <td>
     </td>
     <td>
     </td>
    </tr>
    <tr>
     <td>pRef</td>
     <td>float</td>
     <td>
     </td>
     <td>
     </td>
    </tr>
    <tr>
     <td>r</td>
     <td>float</td>
     <td>
     </td>
     <td>
     </td>
    </tr>
    <tr>
     <td>rRef</td>
     <td>float</td>
     <td>
     </td>
     <td>
     </td>
    </tr>
    <tr>
     <td>uAil</td>
     <td>float</td>
     <td>
     </td>
     <td>
     </td>
    </tr>
    <tr>
     <td>uRud</td>
     <td>float</td>
     <td>
     </td>
     <td>
     </td>
    </tr>
   </tbody>
  </table>
  <h3 id="ASLCTRL_DEBUG">ASLCTRL_DEBUG (<a href="#ASLCTRL_DEBUG">
    #204
   </a>
   )
  </h3>
  <p>ASL-fixed-wing controller debug data</p>
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
     <td>i32_1</td>
     <td>uint32_t</td>
     <td>Debug data</td>
    </tr>
    <tr>
     <td>i8_1</td>
     <td>uint8_t</td>
     <td>Debug data</td>
    </tr>
    <tr>
     <td>i8_2</td>
     <td>uint8_t</td>
     <td>Debug data</td>
    </tr>
    <tr>
     <td>f_1</td>
     <td>float</td>
     <td>Debug data</td>
    </tr>
    <tr>
     <td>f_2</td>
     <td>float</td>
     <td>Debug data</td>
    </tr>
    <tr>
     <td>f_3</td>
     <td>float</td>
     <td>Debug data</td>
    </tr>
    <tr>
     <td>f_4</td>
     <td>float</td>
     <td>Debug data</td>
    </tr>
    <tr>
     <td>f_5</td>
     <td>float</td>
     <td>Debug data</td>
    </tr>
    <tr>
     <td>f_6</td>
     <td>float</td>
     <td>Debug data</td>
    </tr>
    <tr>
     <td>f_7</td>
     <td>float</td>
     <td>Debug data</td>
    </tr>
    <tr>
     <td>f_8</td>
     <td>float</td>
     <td>Debug data</td>
    </tr>
   </tbody>
  </table>
  <h3 id="ASLUAV_STATUS">ASLUAV_STATUS (<a href="#ASLUAV_STATUS">
    #205
   </a>
   )
  </h3>
  <p>Extended state information for ASLUAVs</p>
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
     <td>LED_status</td>
     <td>uint8_t</td>
     <td>Status of the position-indicator LEDs</td>
    </tr>
    <tr>
     <td>SATCOM_status</td>
     <td>uint8_t</td>
     <td>Status of the IRIDIUM satellite communication system</td>
    </tr>
    <tr>
     <td>Servo_status</td>
     <td>uint8_t[8]</td>
     <td>Status vector for up to 8 servos</td>
    </tr>
    <tr>
     <td>Motor_rpm</td>
     <td>float</td>
     <td>Motor RPM</td>
    </tr>
   </tbody>
  </table>
  <h3 id="EKF_EXT">EKF_EXT (<a href="#EKF_EXT">
    #206
   </a>
   )
  </h3>
  <p>Extended EKF state estimates for ASLUAVs</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Units</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>timestamp</td>
     <td>uint64_t</td>
     <td>us</td>
     <td>Time since system start</td>
    </tr>
    <tr>
     <td>Windspeed</td>
     <td>float</td>
     <td>m/s</td>
     <td>Magnitude of wind velocity (in lateral inertial plane)</td>
    </tr>
    <tr>
     <td>WindDir</td>
     <td>float</td>
     <td>rad</td>
     <td>Wind heading angle from North</td>
    </tr>
    <tr>
     <td>WindZ</td>
     <td>float</td>
     <td>m/s</td>
     <td>Z (Down) component of inertial wind velocity</td>
    </tr>
    <tr>
     <td>Airspeed</td>
     <td>float</td>
     <td>m/s</td>
     <td>Magnitude of air velocity</td>
    </tr>
    <tr>
     <td>beta</td>
     <td>float</td>
     <td>rad</td>
     <td>Sideslip angle</td>
    </tr>
    <tr>
     <td>alpha</td>
     <td>float</td>
     <td>rad</td>
     <td>Angle of attack</td>
    </tr>
   </tbody>
  </table>
  <h3 id="ASL_OBCTRL">ASL_OBCTRL (<a href="#ASL_OBCTRL">
    #207
   </a>
   )
  </h3>
  <p>Off-board controls/commands for ASLUAVs</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Units</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>timestamp</td>
     <td>uint64_t</td>
     <td>us</td>
     <td>Time since system start</td>
    </tr>
    <tr>
     <td>uElev</td>
     <td>float</td>
     <td>
     </td>
     <td>Elevator command [~]</td>
    </tr>
    <tr>
     <td>uThrot</td>
     <td>float</td>
     <td>
     </td>
     <td>Throttle command [~]</td>
    </tr>
    <tr>
     <td>uThrot2</td>
     <td>float</td>
     <td>
     </td>
     <td>Throttle 2 command [~]</td>
    </tr>
    <tr>
     <td>uAilL</td>
     <td>float</td>
     <td>
     </td>
     <td>Left aileron command [~]</td>
    </tr>
    <tr>
     <td>uAilR</td>
     <td>float</td>
     <td>
     </td>
     <td>Right aileron command [~]</td>
    </tr>
    <tr>
     <td>uRud</td>
     <td>float</td>
     <td>
     </td>
     <td>Rudder command [~]</td>
    </tr>
    <tr>
     <td>obctrl_status</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>Off-board computer status</td>
    </tr>
   </tbody>
  </table>
  <h3 id="SENS_ATMOS">SENS_ATMOS (<a href="#SENS_ATMOS">
    #208
   </a>
   )
  </h3>
  <p>Atmospheric sensors (temperature, humidity, ...)</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Units</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>TempAmbient</td>
     <td>float</td>
     <td>degC</td>
     <td>Ambient temperature</td>
    </tr>
    <tr>
     <td>Humidity</td>
     <td>float</td>
     <td>
      %
     </td>
     <td>Relative humidity</td>
    </tr>
   </tbody>
  </table>
  <h3 id="SENS_BATMON">SENS_BATMON (<a href="#SENS_BATMON">
    #209
   </a>
   )
  </h3>
  <p>Battery pack monitoring data for Li-Ion batteries</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Units</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>batmon_timestamp</td>
     <td>uint64_t</td>
     <td>us</td>
     <td>Time since system start</td>
    </tr>
    <tr>
     <td>temperature</td>
     <td>float</td>
     <td>degC</td>
     <td>Battery pack temperature</td>
    </tr>
    <tr>
     <td>voltage</td>
     <td>uint16_t</td>
     <td>mV</td>
     <td>Battery pack voltage</td>
    </tr>
    <tr>
     <td>current</td>
     <td>int16_t</td>
     <td>mA</td>
     <td>Battery pack current</td>
    </tr>
    <tr>
     <td>SoC</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>Battery pack state-of-charge</td>
    </tr>
    <tr>
     <td>batterystatus</td>
     <td>uint16_t</td>
     <td>
     </td>
     <td>Battery monitor status report bits in Hex</td>
    </tr>
    <tr>
     <td>serialnumber</td>
     <td>uint16_t</td>
     <td>
     </td>
     <td>Battery monitor serial number in Hex</td>
    </tr>
    <tr>
     <td>safetystatus</td>
     <td>uint32_t</td>
     <td>
     </td>
     <td>Battery monitor safetystatus report bits in Hex</td>
    </tr>
    <tr>
     <td>operationstatus</td>
     <td>uint32_t</td>
     <td>
     </td>
     <td>Battery monitor operation status report bits in Hex</td>
    </tr>
    <tr>
     <td>cellvoltage1</td>
     <td>uint16_t</td>
     <td>mV</td>
     <td>Battery pack cell 1 voltage</td>
    </tr>
    <tr>
     <td>cellvoltage2</td>
     <td>uint16_t</td>
     <td>mV</td>
     <td>Battery pack cell 2 voltage</td>
    </tr>
    <tr>
     <td>cellvoltage3</td>
     <td>uint16_t</td>
     <td>mV</td>
     <td>Battery pack cell 3 voltage</td>
    </tr>
    <tr>
     <td>cellvoltage4</td>
     <td>uint16_t</td>
     <td>mV</td>
     <td>Battery pack cell 4 voltage</td>
    </tr>
    <tr>
     <td>cellvoltage5</td>
     <td>uint16_t</td>
     <td>mV</td>
     <td>Battery pack cell 5 voltage</td>
    </tr>
    <tr>
     <td>cellvoltage6</td>
     <td>uint16_t</td>
     <td>mV</td>
     <td>Battery pack cell 6 voltage</td>
    </tr>
   </tbody>
  </table>
  <h3 id="FW_SOARING_DATA">FW_SOARING_DATA (<a href="#FW_SOARING_DATA">
    #210
   </a>
   )
  </h3>
  <p>Fixed-wing soaring (i.e. thermal seeking) data</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Units</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>timestamp</td>
     <td>uint64_t</td>
     <td>ms</td>
     <td>Timestamp</td>
    </tr>
    <tr>
     <td>timestampModeChanged</td>
     <td>uint64_t</td>
     <td>ms</td>
     <td>Timestamp since last mode change</td>
    </tr>
    <tr>
     <td>xW</td>
     <td>float</td>
     <td>m/s</td>
     <td>Thermal core updraft strength</td>
    </tr>
    <tr>
     <td>xR</td>
     <td>float</td>
     <td>m</td>
     <td>Thermal radius</td>
    </tr>
    <tr>
     <td>xLat</td>
     <td>float</td>
     <td>deg</td>
     <td>Thermal center latitude</td>
    </tr>
    <tr>
     <td>xLon</td>
     <td>float</td>
     <td>deg</td>
     <td>Thermal center longitude</td>
    </tr>
    <tr>
     <td>VarW</td>
     <td>float</td>
     <td>
     </td>
     <td>Variance W</td>
    </tr>
    <tr>
     <td>VarR</td>
     <td>float</td>
     <td>
     </td>
     <td>Variance R</td>
    </tr>
    <tr>
     <td>VarLat</td>
     <td>float</td>
     <td>
     </td>
     <td>Variance Lat</td>
    </tr>
    <tr>
     <td>VarLon</td>
     <td>float</td>
     <td>
     </td>
     <td>Variance Lon</td>
    </tr>
    <tr>
     <td>LoiterRadius</td>
     <td>float</td>
     <td>m</td>
     <td>Suggested loiter radius</td>
    </tr>
    <tr>
     <td>LoiterDirection</td>
     <td>float</td>
     <td>
     </td>
     <td>Suggested loiter direction</td>
    </tr>
    <tr>
     <td>DistToSoarPoint</td>
     <td>float</td>
     <td>m</td>
     <td>Distance to soar point</td>
    </tr>
    <tr>
     <td>vSinkExp</td>
     <td>float</td>
     <td>m/s</td>
     <td>Expected sink rate at current airspeed, roll and throttle</td>
    </tr>
    <tr>
     <td>z1_LocalUpdraftSpeed</td>
     <td>float</td>
     <td>m/s</td>
     <td>Measurement / updraft speed at current/local airplane position</td>
    </tr>
    <tr>
     <td>z2_DeltaRoll</td>
     <td>float</td>
     <td>deg</td>
     <td>Measurement / roll angle tracking error</td>
    </tr>
    <tr>
     <td>z1_exp</td>
     <td>float</td>
     <td>
     </td>
     <td>Expected measurement 1</td>
    </tr>
    <tr>
     <td>z2_exp</td>
     <td>float</td>
     <td>
     </td>
     <td>Expected measurement 2</td>
    </tr>
    <tr>
     <td>ThermalGSNorth</td>
     <td>float</td>
     <td>m/s</td>
     <td>Thermal drift (from estimator prediction step only)</td>
    </tr>
    <tr>
     <td>ThermalGSEast</td>
     <td>float</td>
     <td>m/s</td>
     <td>Thermal drift (from estimator prediction step only)</td>
    </tr>
    <tr>
     <td>TSE_dot</td>
     <td>float</td>
     <td>m/s</td>
     <td>Total specific energy change (filtered)</td>
    </tr>
    <tr>
     <td>DebugVar1</td>
     <td>float</td>
     <td>
     </td>
     <td>Debug variable 1</td>
    </tr>
    <tr>
     <td>DebugVar2</td>
     <td>float</td>
     <td>
     </td>
     <td>Debug variable 2</td>
    </tr>
    <tr>
     <td>ControlMode</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>Control Mode [-]</td>
    </tr>
    <tr>
     <td>valid</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>Data valid [-]</td>
    </tr>
   </tbody>
  </table>
  <h3 id="SENSORPOD_STATUS">SENSORPOD_STATUS (<a href="#SENSORPOD_STATUS">
    #211
   </a>
   )
  </h3>
  <p>Monitoring of sensorpod status</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Units</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>timestamp</td>
     <td>uint64_t</td>
     <td>ms</td>
     <td>Timestamp in linuxtime (since 1.1.1970)</td>
    </tr>
    <tr>
     <td>visensor_rate_1</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>Rate of ROS topic 1</td>
    </tr>
    <tr>
     <td>visensor_rate_2</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>Rate of ROS topic 2</td>
    </tr>
    <tr>
     <td>visensor_rate_3</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>Rate of ROS topic 3</td>
    </tr>
    <tr>
     <td>visensor_rate_4</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>Rate of ROS topic 4</td>
    </tr>
    <tr>
     <td>recording_nodes_count</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>Number of recording nodes</td>
    </tr>
    <tr>
     <td>cpu_temp</td>
     <td>uint8_t</td>
     <td>degC</td>
     <td>Temperature of sensorpod CPU in</td>
    </tr>
    <tr>
     <td>free_space</td>
     <td>uint16_t</td>
     <td>
     </td>
     <td>Free space available in recordings directory in [Gb] * 1e2</td>
    </tr>
   </tbody>
  </table>
  <h3 id="SENS_POWER_BOARD">SENS_POWER_BOARD (<a href="#SENS_POWER_BOARD">
    #212
   </a>
   )
  </h3>
  <p>Monitoring of power board status</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Units</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>timestamp</td>
     <td>uint64_t</td>
     <td>us</td>
     <td>Timestamp</td>
    </tr>
    <tr>
     <td>pwr_brd_status</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>Power board status register</td>
    </tr>
    <tr>
     <td>pwr_brd_led_status</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>Power board leds status</td>
    </tr>
    <tr>
     <td>pwr_brd_system_volt</td>
     <td>float</td>
     <td>V</td>
     <td>Power board system voltage</td>
    </tr>
    <tr>
     <td>pwr_brd_servo_volt</td>
     <td>float</td>
     <td>V</td>
     <td>Power board servo voltage</td>
    </tr>
    <tr>
     <td>pwr_brd_digital_volt</td>
     <td>float</td>
     <td>V</td>
     <td>Power board digital voltage</td>
    </tr>
    <tr>
     <td>pwr_brd_mot_l_amp</td>
     <td>float</td>
     <td>A</td>
     <td>Power board left motor current sensor</td>
    </tr>
    <tr>
     <td>pwr_brd_mot_r_amp</td>
     <td>float</td>
     <td>A</td>
     <td>Power board right motor current sensor</td>
    </tr>
    <tr>
     <td>pwr_brd_analog_amp</td>
     <td>float</td>
     <td>A</td>
     <td>Power board analog current sensor</td>
    </tr>
    <tr>
     <td>pwr_brd_digital_amp</td>
     <td>float</td>
     <td>A</td>
     <td>Power board digital current sensor</td>
    </tr>
    <tr>
     <td>pwr_brd_ext_amp</td>
     <td>float</td>
     <td>A</td>
     <td>Power board extension current sensor</td>
    </tr>
    <tr>
     <td>pwr_brd_aux_amp</td>
     <td>float</td>
     <td>A</td>
     <td>Power board aux current sensor</td>
    </tr>
   </tbody>
  </table>
  <h3 id="GSM_LINK_STATUS">GSM_LINK_STATUS (<a href="#GSM_LINK_STATUS">
    #213
   </a>
   )
  </h3>
  <p>Status of GSM modem (connected to onboard computer)</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Field Name</th>
     <th>Type</th>
     <th>Units</th>
     <th>Values</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr>
     <td>timestamp</td>
     <td>uint64_t</td>
     <td>us</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>Timestamp (of OBC)</td>
    </tr>
    <tr>
     <td>gsm_modem_type</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>
      <a href="#GSM_MODEM_TYPE">GSM_MODEM_TYPE</a>
     </td>
     <td>GSM modem used</td>
    </tr>
    <tr>
     <td>gsm_link_type</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>
      <a href="#GSM_LINK_TYPE">GSM_LINK_TYPE</a>
     </td>
     <td>GSM link type</td>
    </tr>
    <tr>
     <td>rssi</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>RSSI as reported by modem (unconverted)</td>
    </tr>
    <tr>
     <td>rsrp_rscp</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>RSRP (LTE) or RSCP (WCDMA) as reported by modem (unconverted)</td>
    </tr>
    <tr>
     <td>sinr_ecio</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>SINR (LTE) or ECIO (WCDMA) as reported by modem (unconverted)</td>
    </tr>
    <tr>
     <td>rsrq</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>RSRQ (LTE only) as reported by modem (unconverted)</td>
    </tr>
   </tbody>
  </table>
 </body>
</html>