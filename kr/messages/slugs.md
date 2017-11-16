<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_gitbook.py -->
# MAVLINK Message Set: slugs.xml

*This is a human-readable form of the XML definition file: [slugs.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/slugs.xml).*

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
    <tr class="mavlink_field" id="MAV_CMD_DO_NOTHING">
     <td class="mavlink_type" valign="top">10001</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_DO_NOTHING">MAV_CMD_DO_NOTHING</a>
     </td>
     <td class="mavlink_comment">Does nothing.</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #1</td>
     <td class="mavlink_comment">1 to arm, 0 to disarm</td>
    </tr>
    <tr>
     <td colspan="3">
      <br/>
     </td>
    </tr>
    <tr class="mavlink_field" id="MAV_CMD_RETURN_TO_BASE">
     <td class="mavlink_type" valign="top">10011</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_RETURN_TO_BASE">MAV_CMD_RETURN_TO_BASE</a>
     </td>
     <td class="mavlink_comment">Return vehicle to base.</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #1</td>
     <td class="mavlink_comment">0: return to base, 1: track mobile base</td>
    </tr>
    <tr>
     <td colspan="3">
      <br/>
     </td>
    </tr>
    <tr class="mavlink_field" id="MAV_CMD_STOP_RETURN_TO_BASE">
     <td class="mavlink_type" valign="top">10012</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_STOP_RETURN_TO_BASE">MAV_CMD_STOP_RETURN_TO_BASE</a>
     </td>
     <td class="mavlink_comment">Stops the vehicle from returning to base and resumes flight.</td>
    </tr>
    <tr class="mavlink_field" id="MAV_CMD_TURN_LIGHT">
     <td class="mavlink_type" valign="top">10013</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_TURN_LIGHT">MAV_CMD_TURN_LIGHT</a>
     </td>
     <td class="mavlink_comment">Turns the vehicle's visible or infrared lights on or off.</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #1</td>
     <td class="mavlink_comment">0: visible lights, 1: infrared lights</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #2</td>
     <td class="mavlink_comment">0: turn on, 1: turn off</td>
    </tr>
    <tr>
     <td colspan="3">
      <br/>
     </td>
    </tr>
    <tr class="mavlink_field" id="MAV_CMD_GET_MID_LEVEL_COMMANDS">
     <td class="mavlink_type" valign="top">10014</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_GET_MID_LEVEL_COMMANDS">MAV_CMD_GET_MID_LEVEL_COMMANDS</a>
     </td>
     <td class="mavlink_comment">Requests vehicle to send current mid-level commands to ground station.</td>
    </tr>
    <tr class="mavlink_field" id="MAV_CMD_MIDLEVEL_STORAGE">
     <td class="mavlink_type" valign="top">10015</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_MIDLEVEL_STORAGE">MAV_CMD_MIDLEVEL_STORAGE</a>
     </td>
     <td class="mavlink_comment">Requests storage of mid-level commands.</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #1</td>
     <td class="mavlink_comment">Mid-level command storage: 0: read from flash/EEPROM, 1: write to flash/EEPROM</td>
    </tr>
    <tr>
     <td colspan="3">
      <br/>
     </td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_SLUGS_MODE">
   <a href="#ENUM_SLUGS_MODE">SLUGS_MODE</a>
  </h3>
  <p class="description">Slugs-specific navigation modes.</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="SLUGS_MODE_NONE">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#SLUGS_MODE_NONE">SLUGS_MODE_NONE</a>
     </td>
     <td class="mavlink_comment">No change to SLUGS mode.</td>
    </tr>
    <tr class="mavlink_field" id="SLUGS_MODE_LIFTOFF">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#SLUGS_MODE_LIFTOFF">SLUGS_MODE_LIFTOFF</a>
     </td>
     <td class="mavlink_comment">Vehicle is in liftoff mode.</td>
    </tr>
    <tr class="mavlink_field" id="SLUGS_MODE_PASSTHROUGH">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#SLUGS_MODE_PASSTHROUGH">SLUGS_MODE_PASSTHROUGH</a>
     </td>
     <td class="mavlink_comment">Vehicle is in passthrough mode, being controlled by a pilot.</td>
    </tr>
    <tr class="mavlink_field" id="SLUGS_MODE_WAYPOINT">
     <td class="mavlink_type" valign="top">3</td>
     <td class="mavlink_name" valign="top">
      <a href="#SLUGS_MODE_WAYPOINT">SLUGS_MODE_WAYPOINT</a>
     </td>
     <td class="mavlink_comment">Vehicle is in waypoint mode, navigating to waypoints.</td>
    </tr>
    <tr class="mavlink_field" id="SLUGS_MODE_MID_LEVEL">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#SLUGS_MODE_MID_LEVEL">SLUGS_MODE_MID_LEVEL</a>
     </td>
     <td class="mavlink_comment">Vehicle is executing mid-level commands.</td>
    </tr>
    <tr class="mavlink_field" id="SLUGS_MODE_RETURNING">
     <td class="mavlink_type" valign="top">5</td>
     <td class="mavlink_name" valign="top">
      <a href="#SLUGS_MODE_RETURNING">SLUGS_MODE_RETURNING</a>
     </td>
     <td class="mavlink_comment">Vehicle is returning to the home location.</td>
    </tr>
    <tr class="mavlink_field" id="SLUGS_MODE_LANDING">
     <td class="mavlink_type" valign="top">6</td>
     <td class="mavlink_name" valign="top">
      <a href="#SLUGS_MODE_LANDING">SLUGS_MODE_LANDING</a>
     </td>
     <td class="mavlink_comment">Vehicle is landing.</td>
    </tr>
    <tr class="mavlink_field" id="SLUGS_MODE_LOST">
     <td class="mavlink_type" valign="top">7</td>
     <td class="mavlink_name" valign="top">
      <a href="#SLUGS_MODE_LOST">SLUGS_MODE_LOST</a>
     </td>
     <td class="mavlink_comment">Lost connection with vehicle.</td>
    </tr>
    <tr class="mavlink_field" id="SLUGS_MODE_SELECTIVE_PASSTHROUGH">
     <td class="mavlink_type" valign="top">8</td>
     <td class="mavlink_name" valign="top">
      <a href="#SLUGS_MODE_SELECTIVE_PASSTHROUGH">SLUGS_MODE_SELECTIVE_PASSTHROUGH</a>
     </td>
     <td class="mavlink_comment">Vehicle is in selective passthrough mode, where selected surfaces are being manually controlled.</td>
    </tr>
    <tr class="mavlink_field" id="SLUGS_MODE_ISR">
     <td class="mavlink_type" valign="top">9</td>
     <td class="mavlink_name" valign="top">
      <a href="#SLUGS_MODE_ISR">SLUGS_MODE_ISR</a>
     </td>
     <td class="mavlink_comment">Vehicle is in ISR mode, performing reconaissance at a point specified by ISR_LOCATION message.</td>
    </tr>
    <tr class="mavlink_field" id="SLUGS_MODE_LINE_PATROL">
     <td class="mavlink_type" valign="top">10</td>
     <td class="mavlink_name" valign="top">
      <a href="#SLUGS_MODE_LINE_PATROL">SLUGS_MODE_LINE_PATROL</a>
     </td>
     <td class="mavlink_comment">Vehicle is patrolling along lines between waypoints.</td>
    </tr>
    <tr class="mavlink_field" id="SLUGS_MODE_GROUNDED">
     <td class="mavlink_type" valign="top">11</td>
     <td class="mavlink_name" valign="top">
      <a href="#SLUGS_MODE_GROUNDED">SLUGS_MODE_GROUNDED</a>
     </td>
     <td class="mavlink_comment">Vehicle is grounded or an error has occurred.</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_CONTROL_SURFACE_FLAG">
   <a href="#ENUM_CONTROL_SURFACE_FLAG">CONTROL_SURFACE_FLAG</a>
  </h3>
  <p class="description">These flags encode the control surfaces for selective passthrough mode. If a bit is set then the pilot console
            has control of the surface, and if not then the autopilot has control of the surface.</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="CONTROL_SURFACE_FLAG_THROTTLE">
     <td class="mavlink_type" valign="top">128</td>
     <td class="mavlink_name" valign="top">
      <a href="#CONTROL_SURFACE_FLAG_THROTTLE">CONTROL_SURFACE_FLAG_THROTTLE</a>
     </td>
     <td class="mavlink_comment">0b10000000 Throttle control passes through to pilot console.</td>
    </tr>
    <tr class="mavlink_field" id="CONTROL_SURFACE_FLAG_LEFT_AILERON">
     <td class="mavlink_type" valign="top">64</td>
     <td class="mavlink_name" valign="top">
      <a href="#CONTROL_SURFACE_FLAG_LEFT_AILERON">CONTROL_SURFACE_FLAG_LEFT_AILERON</a>
     </td>
     <td class="mavlink_comment">0b01000000 Left aileron control passes through to pilot console.</td>
    </tr>
    <tr class="mavlink_field" id="CONTROL_SURFACE_FLAG_RIGHT_AILERON">
     <td class="mavlink_type" valign="top">32</td>
     <td class="mavlink_name" valign="top">
      <a href="#CONTROL_SURFACE_FLAG_RIGHT_AILERON">CONTROL_SURFACE_FLAG_RIGHT_AILERON</a>
     </td>
     <td class="mavlink_comment">0b00100000 Right aileron control passes through to pilot console.</td>
    </tr>
    <tr class="mavlink_field" id="CONTROL_SURFACE_FLAG_RUDDER">
     <td class="mavlink_type" valign="top">16</td>
     <td class="mavlink_name" valign="top">
      <a href="#CONTROL_SURFACE_FLAG_RUDDER">CONTROL_SURFACE_FLAG_RUDDER</a>
     </td>
     <td class="mavlink_comment">0b00010000 Rudder control passes through to pilot console.</td>
    </tr>
    <tr class="mavlink_field" id="CONTROL_SURFACE_FLAG_LEFT_ELEVATOR">
     <td class="mavlink_type" valign="top">8</td>
     <td class="mavlink_name" valign="top">
      <a href="#CONTROL_SURFACE_FLAG_LEFT_ELEVATOR">CONTROL_SURFACE_FLAG_LEFT_ELEVATOR</a>
     </td>
     <td class="mavlink_comment">0b00001000 Left elevator control passes through to pilot console.</td>
    </tr>
    <tr class="mavlink_field" id="CONTROL_SURFACE_FLAG_RIGHT_ELEVATOR">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#CONTROL_SURFACE_FLAG_RIGHT_ELEVATOR">CONTROL_SURFACE_FLAG_RIGHT_ELEVATOR</a>
     </td>
     <td class="mavlink_comment">0b00000100 Right elevator control passes through to pilot console.</td>
    </tr>
    <tr class="mavlink_field" id="CONTROL_SURFACE_FLAG_LEFT_FLAP">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#CONTROL_SURFACE_FLAG_LEFT_FLAP">CONTROL_SURFACE_FLAG_LEFT_FLAP</a>
     </td>
     <td class="mavlink_comment">0b00000010 Left flap control passes through to pilot console.</td>
    </tr>
    <tr class="mavlink_field" id="CONTROL_SURFACE_FLAG_RIGHT_FLAP">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#CONTROL_SURFACE_FLAG_RIGHT_FLAP">CONTROL_SURFACE_FLAG_RIGHT_FLAP</a>
     </td>
     <td class="mavlink_comment">0b00000001 Right flap control passes through to pilot console.</td>
    </tr>
   </tbody>
  </table>
  <h2>MAVLink Messages</h2>
  <h3 class="mavlink_message_name" id="CPU_LOAD">CPU_LOAD (<a href="#CPU_LOAD">
    #170
   </a>
   )
  </h3>
  <p class="description">Sensor and DSC control loads.</p>
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
     <td class="mavlink_name" valign="top">sensLoad</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Sensor DSC Load</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">ctrlLoad</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Control DSC Load</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">batVolt</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Battery Voltage in millivolts</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SENSOR_BIAS">SENSOR_BIAS (<a href="#SENSOR_BIAS">
    #172
   </a>
   )
  </h3>
  <p class="description">Accelerometer and gyro biases.</p>
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
     <td class="mavlink_name" valign="top">axBias</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Accelerometer X bias (m/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">ayBias</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Accelerometer Y bias (m/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">azBias</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Accelerometer Z bias (m/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">gxBias</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Gyro X bias (rad/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">gyBias</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Gyro Y bias (rad/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">gzBias</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Gyro Z bias (rad/s)</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="DIAGNOSTIC">DIAGNOSTIC (<a href="#DIAGNOSTIC">
    #173
   </a>
   )
  </h3>
  <p class="description">Configurable diagnostic messages.</p>
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
     <td class="mavlink_name" valign="top">diagFl1</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Diagnostic float 1</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">diagFl2</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Diagnostic float 2</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">diagFl3</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Diagnostic float 3</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">diagSh1</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Diagnostic short 1</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">diagSh2</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Diagnostic short 2</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">diagSh3</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Diagnostic short 3</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SLUGS_NAVIGATION">SLUGS_NAVIGATION (<a href="#SLUGS_NAVIGATION">
    #176
   </a>
   )
  </h3>
  <p class="description">Data used in the navigation algorithm.</p>
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
     <td class="mavlink_name" valign="top">u_m</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Measured Airspeed prior to the nav filter in m/s</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">phi_c</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Commanded Roll</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">theta_c</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Commanded Pitch</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">psiDot_c</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Commanded Turn rate</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">ay_body</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Y component of the body acceleration</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">totalDist</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Total Distance to Run on this leg of Navigation</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">dist2Go</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Remaining distance to Run on this leg of Navigation</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">fromWP</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Origin WP</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">toWP</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Destination WP</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">h_c</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Commanded altitude in 0.1 m</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="DATA_LOG">DATA_LOG (<a href="#DATA_LOG">
    #177
   </a>
   )
  </h3>
  <p class="description">Configurable data log probes to be used inside Simulink</p>
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
     <td class="mavlink_name" valign="top">fl_1</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Log value 1</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">fl_2</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Log value 2</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">fl_3</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Log value 3</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">fl_4</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Log value 4</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">fl_5</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Log value 5</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">fl_6</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Log value 6</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="GPS_DATE_TIME">GPS_DATE_TIME (<a href="#GPS_DATE_TIME">
    #179
   </a>
   )
  </h3>
  <p class="description">Pilot console PWM messges.</p>
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
     <td class="mavlink_name" valign="top">year</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Year reported by Gps</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">month</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Month reported by Gps</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">day</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Day reported by Gps</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">hour</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Hour reported by Gps</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">min</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Min reported by Gps</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sec</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Sec reported by Gps</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">clockStat</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Clock Status. See table 47 page 211 OEMStar Manual</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">visSat</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Visible satellites reported by Gps</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">useSat</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Used satellites in Solution</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">GppGl</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">GPS+GLONASS satellites in Solution</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sigUsedMask</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">GPS and GLONASS usage mask (bit 0 GPS_used? bit_4 GLONASS_used?)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">percentUsed</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Percent used GPS</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="MID_LVL_CMDS">MID_LVL_CMDS (<a href="#MID_LVL_CMDS">
    #180
   </a>
   )
  </h3>
  <p class="description">Mid Level commands sent from the GS to the autopilot. These are only sent when being operated in mid-level commands mode from the ground.</p>
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
     <td class="mavlink_name" valign="top">target</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">The system setting the commands</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">hCommand</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Commanded Altitude in meters</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">uCommand</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Commanded Airspeed in m/s</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">rCommand</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Commanded Turnrate in rad/s</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="CTRL_SRFC_PT">CTRL_SRFC_PT (<a href="#CTRL_SRFC_PT">
    #181
   </a>
   )
  </h3>
  <p class="description">This message sets the control surfaces for selective passthrough mode.</p>
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
     <td class="mavlink_name" valign="top">target</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">The system setting the commands</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">bitfieldPt</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Bitfield containing the passthrough configuration, see CONTROL_SURFACE_FLAG ENUM.</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SLUGS_CAMERA_ORDER">SLUGS_CAMERA_ORDER (<a href="#SLUGS_CAMERA_ORDER">
    #184
   </a>
   )
  </h3>
  <p class="description">Orders generated to the SLUGS camera mount.</p>
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
     <td class="mavlink_name" valign="top">target</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">The system reporting the action</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">pan</td>
     <td class="mavlink_type" valign="top">int8_t</td>
     <td class="mavlink_comment">Order the mount to pan: -1 left, 0 No pan motion, +1 right</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">tilt</td>
     <td class="mavlink_type" valign="top">int8_t</td>
     <td class="mavlink_comment">Order the mount to tilt: -1 down, 0 No tilt motion, +1 up</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">zoom</td>
     <td class="mavlink_type" valign="top">int8_t</td>
     <td class="mavlink_comment">Order the zoom values 0 to 10</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">moveHome</td>
     <td class="mavlink_type" valign="top">int8_t</td>
     <td class="mavlink_comment">Orders the camera mount to move home. The other fields are ignored when this field is set. 1: move home, 0 ignored</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="CONTROL_SURFACE">CONTROL_SURFACE (<a href="#CONTROL_SURFACE">
    #185
   </a>
   )
  </h3>
  <p class="description">Control for surface; pending and order to origin.</p>
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
     <td class="mavlink_name" valign="top">target</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">The system setting the commands</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">idSurface</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">ID control surface send 0: throttle 1: aileron 2: elevator 3: rudder</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">mControl</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Pending</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">bControl</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Order to origin</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SLUGS_MOBILE_LOCATION">SLUGS_MOBILE_LOCATION (<a href="#SLUGS_MOBILE_LOCATION">
    #186
   </a>
   )
  </h3>
  <p class="description">Transmits the last known position of the mobile GS to the UAV. Very relevant when Track Mobile is enabled</p>
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
     <td class="mavlink_name" valign="top">target</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">The system reporting the action</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">latitude</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Mobile Latitude</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">longitude</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Mobile Longitude</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SLUGS_CONFIGURATION_CAMERA">SLUGS_CONFIGURATION_CAMERA (<a href="#SLUGS_CONFIGURATION_CAMERA">
    #188
   </a>
   )
  </h3>
  <p class="description">Control for camara.</p>
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
     <td class="mavlink_name" valign="top">target</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">The system setting the commands</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">idOrder</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">ID 0: brightness 1: aperture 2: iris 3: ICR 4: backlight</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">order</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">1: up/on 2: down/off 3: auto/reset/no action</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ISR_LOCATION">ISR_LOCATION (<a href="#ISR_LOCATION">
    #189
   </a>
   )
  </h3>
  <p class="description">Transmits the position of watch</p>
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
     <td class="mavlink_name" valign="top">target</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">The system reporting the action</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">latitude</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">ISR Latitude</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">longitude</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">ISR Longitude</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">height</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">ISR Height</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">option1</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Option 1</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">option2</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Option 2</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">option3</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Option 3</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="VOLT_SENSOR">VOLT_SENSOR (<a href="#VOLT_SENSOR">
    #191
   </a>
   )
  </h3>
  <p class="description">Transmits the readings from the voltage and current sensors</p>
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
     <td class="mavlink_name" valign="top">r2Type</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">It is the value of reading 2: 0 - Current, 1 - Foreward Sonar, 2 - Back Sonar, 3 - RPM</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">voltage</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Voltage in uS of PWM. 0 uS = 0V, 20 uS = 21.5V</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">reading2</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Depends on the value of r2Type (0) Current consumption in uS of PWM, 20 uS = 90Amp (1) Distance in cm (2) Distance in cm (3) Absolute value</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="PTZ_STATUS">PTZ_STATUS (<a href="#PTZ_STATUS">
    #192
   </a>
   )
  </h3>
  <p class="description">Transmits the actual Pan, Tilt and Zoom values of the camera unit</p>
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
     <td class="mavlink_name" valign="top">zoom</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">The actual Zoom Value</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">pan</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">The Pan value in 10ths of degree</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">tilt</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">The Tilt value in 10ths of degree</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="UAV_STATUS">UAV_STATUS (<a href="#UAV_STATUS">
    #193
   </a>
   )
  </h3>
  <p class="description">Transmits the actual status values UAV in flight</p>
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
     <td class="mavlink_name" valign="top">target</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">The ID system reporting the action</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">latitude</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Latitude UAV</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">longitude</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Longitude UAV</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">altitude</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Altitude UAV</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">speed</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Speed UAV</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">course</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Course UAV</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="STATUS_GPS">STATUS_GPS (<a href="#STATUS_GPS">
    #194
   </a>
   )
  </h3>
  <p class="description">This contains the status of the GPS readings</p>
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
     <td class="mavlink_name" valign="top">csFails</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Number of times checksum has failed</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">gpsQuality</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">The quality indicator, 0=fix not available or invalid, 1=GPS fix, 2=C/A differential GPS, 6=Dead reckoning mode, 7=Manual input mode (fixed position), 8=Simulator mode, 9= WAAS a</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">msgsType</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Indicates if GN, GL or GP messages are being received</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">posStatus</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">A = data valid, V = data invalid</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">magVar</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Magnetic variation, degrees</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">magDir</td>
     <td class="mavlink_type" valign="top">int8_t</td>
     <td class="mavlink_comment">Magnetic variation direction E/W. Easterly variation (E) subtracts from True course and Westerly variation (W) adds to True course</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">modeInd</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Positioning system mode indicator. A - Autonomous;D-Differential; E-Estimated (dead reckoning) mode;M-Manual input; N-Data not valid</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="NOVATEL_DIAG">NOVATEL_DIAG (<a href="#NOVATEL_DIAG">
    #195
   </a>
   )
  </h3>
  <p class="description">Transmits the diagnostics data from the Novatel OEMStar GPS</p>
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
     <td class="mavlink_name" valign="top">timeStatus</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">The Time Status. See Table 8 page 27 Novatel OEMStar Manual</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">receiverStatus</td>
     <td class="mavlink_type" valign="top">uint32_t</td>
     <td class="mavlink_comment">Status Bitfield. See table 69 page 350 Novatel OEMstar Manual</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">solStatus</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">solution Status. See table 44 page 197</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">posType</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">position type. See table 43 page 196</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">velType</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">velocity type. See table 43 page 196</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">posSolAge</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Age of the position solution in seconds</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">csFails</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Times the CRC has failed since boot</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SENSOR_DIAG">SENSOR_DIAG (<a href="#SENSOR_DIAG">
    #196
   </a>
   )
  </h3>
  <p class="description">Diagnostic data Sensor MCU</p>
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
     <td class="mavlink_name" valign="top">float1</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Float field 1</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">float2</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Float field 2</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">int1</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Int 16 field 1</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">char1</td>
     <td class="mavlink_type" valign="top">int8_t</td>
     <td class="mavlink_comment">Int 8 field 1</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="BOOT">BOOT (<a href="#BOOT">
    #197
   </a>
   )
  </h3>
  <p class="description">The boot message indicates that a system is starting. The onboard software version allows to keep track of onboard soft/firmware revisions. This message allows the sensor and control MCUs to communicate version numbers on startup.</p>
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
     <td class="mavlink_name" valign="top">version</td>
     <td class="mavlink_type" valign="top">uint32_t</td>
     <td class="mavlink_comment">The onboard software version</td>
    </tr>
   </tbody>
  </table>
 </body>
</html>