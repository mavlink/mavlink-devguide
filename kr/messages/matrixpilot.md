<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_gitbook.py -->
# MAVLINK Message Set: matrixpilot.xml

*This is a human-readable form of the XML definition file: [matrixpilot.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/matrixpilot.xml).*

<html>
 <body>
  <p>
   <strong>MAVLink Include Files:</strong>
   <a href="common.md">common.xml</a>
  </p>
  <h2>MAVLink Type Enumerations</h2>
  <h3 class="mavlink_message_name" id="ENUM_MAV_PREFLIGHT_STORAGE_ACTION">
   <a href="#ENUM_MAV_PREFLIGHT_STORAGE_ACTION">MAV_PREFLIGHT_STORAGE_ACTION</a>
  </h3>
  <p class="description">Action required when performing CMD_PREFLIGHT_STORAGE</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="MAV_PFS_CMD_READ_ALL">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_PFS_CMD_READ_ALL">MAV_PFS_CMD_READ_ALL</a>
     </td>
     <td class="mavlink_comment">Read all parameters from storage</td>
    </tr>
    <tr class="mavlink_field" id="MAV_PFS_CMD_WRITE_ALL">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_PFS_CMD_WRITE_ALL">MAV_PFS_CMD_WRITE_ALL</a>
     </td>
     <td class="mavlink_comment">Write all parameters to storage</td>
    </tr>
    <tr class="mavlink_field" id="MAV_PFS_CMD_CLEAR_ALL">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_PFS_CMD_CLEAR_ALL">MAV_PFS_CMD_CLEAR_ALL</a>
     </td>
     <td class="mavlink_comment">Clear all  parameters in storage</td>
    </tr>
    <tr class="mavlink_field" id="MAV_PFS_CMD_READ_SPECIFIC">
     <td class="mavlink_type" valign="top">3</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_PFS_CMD_READ_SPECIFIC">MAV_PFS_CMD_READ_SPECIFIC</a>
     </td>
     <td class="mavlink_comment">Read specific parameters from storage</td>
    </tr>
    <tr class="mavlink_field" id="MAV_PFS_CMD_WRITE_SPECIFIC">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_PFS_CMD_WRITE_SPECIFIC">MAV_PFS_CMD_WRITE_SPECIFIC</a>
     </td>
     <td class="mavlink_comment">Write specific parameters to storage</td>
    </tr>
    <tr class="mavlink_field" id="MAV_PFS_CMD_CLEAR_SPECIFIC">
     <td class="mavlink_type" valign="top">5</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_PFS_CMD_CLEAR_SPECIFIC">MAV_PFS_CMD_CLEAR_SPECIFIC</a>
     </td>
     <td class="mavlink_comment">Clear specific parameters in storage</td>
    </tr>
    <tr class="mavlink_field" id="MAV_PFS_CMD_DO_NOTHING">
     <td class="mavlink_type" valign="top">6</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_PFS_CMD_DO_NOTHING">MAV_PFS_CMD_DO_NOTHING</a>
     </td>
     <td class="mavlink_comment">do nothing</td>
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
    <tr class="mavlink_field" id="MAV_CMD_PREFLIGHT_STORAGE_ADVANCED">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#MAV_CMD_PREFLIGHT_STORAGE_ADVANCED">MAV_CMD_PREFLIGHT_STORAGE_ADVANCED</a>
     </td>
     <td class="mavlink_comment">Request storage of different parameter values and logs. This command will be only accepted if in pre-flight mode.</td>
    </tr>
    <tr>
     <td>
     </td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #1</td>
     <td class="mavlink_comment">Storage action: Action defined by MAV_PREFLIGHT_STORAGE_ACTION_ADVANCED</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #2</td>
     <td class="mavlink_comment">Storage area as defined by parameter database</td>
    </tr>
    <tr>
     <td>
     </td>
     <td class="mavlink_mission_param" valign="top">Mission Param #3</td>
     <td class="mavlink_comment">Storage flags as defined by parameter database</td>
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
  <h3 class="mavlink_message_name" id="FLEXIFUNCTION_SET">FLEXIFUNCTION_SET (<a href="#FLEXIFUNCTION_SET">
    #150
   </a>
   )
  </h3>
  <p class="description">Depreciated but used as a compiler flag.  Do not remove</p>
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
  <h3 class="mavlink_message_name" id="FLEXIFUNCTION_READ_REQ">FLEXIFUNCTION_READ_REQ (<a href="#FLEXIFUNCTION_READ_REQ">
    #151
   </a>
   )
  </h3>
  <p class="description">Reqest reading of flexifunction data</p>
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
     <td class="mavlink_name" valign="top">read_req_type</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Type of flexifunction data requested</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">data_index</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">index into data where needed</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="FLEXIFUNCTION_BUFFER_FUNCTION">FLEXIFUNCTION_BUFFER_FUNCTION (<a href="#FLEXIFUNCTION_BUFFER_FUNCTION">
    #152
   </a>
   )
  </h3>
  <p class="description">Flexifunction type and parameters for component at function index from buffer</p>
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
     <td class="mavlink_name" valign="top">func_index</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Function index</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">func_count</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Total count of functions</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">data_address</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Address in the flexifunction data, Set to 0xFFFF to use address in target memory</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">data_size</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Size of the</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">data</td>
     <td class="mavlink_type" valign="top">int8_t[48]</td>
     <td class="mavlink_comment">Settings data</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="FLEXIFUNCTION_BUFFER_FUNCTION_ACK">FLEXIFUNCTION_BUFFER_FUNCTION_ACK (<a href="#FLEXIFUNCTION_BUFFER_FUNCTION_ACK">
    #153
   </a>
   )
  </h3>
  <p class="description">Flexifunction type and parameters for component at function index from buffer</p>
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
     <td class="mavlink_name" valign="top">func_index</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Function index</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">result</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">result of acknowledge, 0=fail, 1=good</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="FLEXIFUNCTION_DIRECTORY">FLEXIFUNCTION_DIRECTORY (<a href="#FLEXIFUNCTION_DIRECTORY">
    #155
   </a>
   )
  </h3>
  <p class="description">Acknowldge sucess or failure of a flexifunction command</p>
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
     <td class="mavlink_name" valign="top">directory_type</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">0=inputs, 1=outputs</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">start_index</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">index of first directory entry to write</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">count</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">count of directory entries to write</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">directory_data</td>
     <td class="mavlink_type" valign="top">int8_t[48]</td>
     <td class="mavlink_comment">Settings data</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="FLEXIFUNCTION_DIRECTORY_ACK">FLEXIFUNCTION_DIRECTORY_ACK (<a href="#FLEXIFUNCTION_DIRECTORY_ACK">
    #156
   </a>
   )
  </h3>
  <p class="description">Acknowldge sucess or failure of a flexifunction command</p>
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
     <td class="mavlink_name" valign="top">directory_type</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">0=inputs, 1=outputs</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">start_index</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">index of first directory entry to write</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">count</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">count of directory entries to write</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">result</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">result of acknowledge, 0=fail, 1=good</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="FLEXIFUNCTION_COMMAND">FLEXIFUNCTION_COMMAND (<a href="#FLEXIFUNCTION_COMMAND">
    #157
   </a>
   )
  </h3>
  <p class="description">Acknowldge sucess or failure of a flexifunction command</p>
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
     <td class="mavlink_name" valign="top">command_type</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Flexifunction command type</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="FLEXIFUNCTION_COMMAND_ACK">FLEXIFUNCTION_COMMAND_ACK (<a href="#FLEXIFUNCTION_COMMAND_ACK">
    #158
   </a>
   )
  </h3>
  <p class="description">Acknowldge sucess or failure of a flexifunction command</p>
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
     <td class="mavlink_name" valign="top">command_type</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Command acknowledged</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">result</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">result of acknowledge</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SERIAL_UDB_EXTRA_F2_A">SERIAL_UDB_EXTRA_F2_A (<a href="#SERIAL_UDB_EXTRA_F2_A">
    #170
   </a>
   )
  </h3>
  <p class="description">Backwards compatible MAVLink version of SERIAL_UDB_EXTRA - F2: Format Part A</p>
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
     <td class="mavlink_name" valign="top">sue_time</td>
     <td class="mavlink_type" valign="top">uint32_t</td>
     <td class="mavlink_comment">Serial UDB Extra Time</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_status</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Serial UDB Extra Status</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_latitude</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">Serial UDB Extra Latitude</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_longitude</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">Serial UDB Extra Longitude</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_altitude</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">Serial UDB Extra Altitude</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_waypoint_index</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Serial UDB Extra Waypoint Index</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_rmat0</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra Rmat 0</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_rmat1</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra Rmat 1</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_rmat2</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra Rmat 2</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_rmat3</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra Rmat 3</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_rmat4</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra Rmat 4</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_rmat5</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra Rmat 5</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_rmat6</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra Rmat 6</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_rmat7</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra Rmat 7</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_rmat8</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra Rmat 8</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_cog</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Serial UDB Extra GPS Course Over Ground</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_sog</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra Speed Over Ground</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_cpu_load</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Serial UDB Extra CPU Load</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_air_speed_3DIMU</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Serial UDB Extra 3D IMU Air Speed</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_estimated_wind_0</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra Estimated Wind 0</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_estimated_wind_1</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra Estimated Wind 1</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_estimated_wind_2</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra Estimated Wind 2</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_magFieldEarth0</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra Magnetic Field Earth 0</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_magFieldEarth1</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra Magnetic Field Earth 1</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_magFieldEarth2</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra Magnetic Field Earth 2</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_svs</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra Number of Sattelites in View</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_hdop</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra GPS Horizontal Dilution of Precision</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SERIAL_UDB_EXTRA_F2_B">SERIAL_UDB_EXTRA_F2_B (<a href="#SERIAL_UDB_EXTRA_F2_B">
    #171
   </a>
   )
  </h3>
  <p class="description">Backwards compatible version of SERIAL_UDB_EXTRA - F2: Part B</p>
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
     <td class="mavlink_name" valign="top">sue_time</td>
     <td class="mavlink_type" valign="top">uint32_t</td>
     <td class="mavlink_comment">Serial UDB Extra Time</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_pwm_input_1</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra PWM Input Channel 1</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_pwm_input_2</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra PWM Input Channel 2</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_pwm_input_3</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra PWM Input Channel 3</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_pwm_input_4</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra PWM Input Channel 4</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_pwm_input_5</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra PWM Input Channel 5</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_pwm_input_6</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra PWM Input Channel 6</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_pwm_input_7</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra PWM Input Channel 7</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_pwm_input_8</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra PWM Input Channel 8</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_pwm_input_9</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra PWM Input Channel 9</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_pwm_input_10</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra PWM Input Channel 10</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_pwm_input_11</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra PWM Input Channel 11</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_pwm_input_12</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra PWM Input Channel 12</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_pwm_output_1</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra PWM Output Channel 1</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_pwm_output_2</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra PWM Output Channel 2</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_pwm_output_3</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra PWM Output Channel 3</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_pwm_output_4</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra PWM Output Channel 4</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_pwm_output_5</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra PWM Output Channel 5</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_pwm_output_6</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra PWM Output Channel 6</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_pwm_output_7</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra PWM Output Channel 7</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_pwm_output_8</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra PWM Output Channel 8</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_pwm_output_9</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra PWM Output Channel 9</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_pwm_output_10</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra PWM Output Channel 10</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_pwm_output_11</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra PWM Output Channel 11</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_pwm_output_12</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra PWM Output Channel 12</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_imu_location_x</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra IMU Location X</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_imu_location_y</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra IMU Location Y</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_imu_location_z</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra IMU Location Z</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_location_error_earth_x</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Location Error Earth X</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_location_error_earth_y</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Location Error Earth Y</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_location_error_earth_z</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Location Error Earth Z</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_flags</td>
     <td class="mavlink_type" valign="top">uint32_t</td>
     <td class="mavlink_comment">Serial UDB Extra Status Flags</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_osc_fails</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra Oscillator Failure Count</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_imu_velocity_x</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra IMU Velocity X</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_imu_velocity_y</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra IMU Velocity Y</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_imu_velocity_z</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra IMU Velocity Z</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_waypoint_goal_x</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra Current Waypoint Goal X</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_waypoint_goal_y</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra Current Waypoint Goal Y</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_waypoint_goal_z</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra Current Waypoint Goal Z</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_aero_x</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Aeroforce in UDB X Axis</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_aero_y</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Aeroforce in UDB Y Axis</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_aero_z</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Aeroforce in UDB Z axis</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_barom_temp</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">SUE barometer temperature</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_barom_press</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">SUE barometer pressure</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_barom_alt</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">SUE barometer altitude</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_bat_volt</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">SUE battery voltage</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_bat_amp</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">SUE battery current</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_bat_amp_hours</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">SUE battery milli amp hours used</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_desired_height</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Sue autopilot desired height</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_memory_stack_free</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra Stack Memory Free</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SERIAL_UDB_EXTRA_F4">SERIAL_UDB_EXTRA_F4 (<a href="#SERIAL_UDB_EXTRA_F4">
    #172
   </a>
   )
  </h3>
  <p class="description">Backwards compatible version of SERIAL_UDB_EXTRA F4: format</p>
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
     <td class="mavlink_name" valign="top">sue_ROLL_STABILIZATION_AILERONS</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Serial UDB Extra Roll Stabilization with Ailerons Enabled</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_ROLL_STABILIZATION_RUDDER</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Serial UDB Extra Roll Stabilization with Rudder Enabled</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_PITCH_STABILIZATION</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Serial UDB Extra Pitch Stabilization Enabled</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_YAW_STABILIZATION_RUDDER</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Serial UDB Extra Yaw Stabilization using Rudder Enabled</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_YAW_STABILIZATION_AILERON</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Serial UDB Extra Yaw Stabilization using Ailerons Enabled</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_AILERON_NAVIGATION</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Serial UDB Extra Navigation with Ailerons Enabled</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_RUDDER_NAVIGATION</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Serial UDB Extra Navigation with Rudder Enabled</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_ALTITUDEHOLD_STABILIZED</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Serial UDB Extra Type of Alitude Hold when in Stabilized Mode</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_ALTITUDEHOLD_WAYPOINT</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Serial UDB Extra Type of Alitude Hold when in Waypoint Mode</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_RACING_MODE</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Serial UDB Extra Firmware racing mode enabled</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SERIAL_UDB_EXTRA_F5">SERIAL_UDB_EXTRA_F5 (<a href="#SERIAL_UDB_EXTRA_F5">
    #173
   </a>
   )
  </h3>
  <p class="description">Backwards compatible version of SERIAL_UDB_EXTRA F5: format</p>
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
     <td class="mavlink_name" valign="top">sue_YAWKP_AILERON</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Serial UDB YAWKP_AILERON Gain for Proporional control of navigation</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_YAWKD_AILERON</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Serial UDB YAWKD_AILERON Gain for Rate control of navigation</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_ROLLKP</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Serial UDB Extra ROLLKP Gain for Proportional control of roll stabilization</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_ROLLKD</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Serial UDB Extra ROLLKD Gain for Rate control of roll stabilization</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SERIAL_UDB_EXTRA_F6">SERIAL_UDB_EXTRA_F6 (<a href="#SERIAL_UDB_EXTRA_F6">
    #174
   </a>
   )
  </h3>
  <p class="description">Backwards compatible version of SERIAL_UDB_EXTRA F6: format</p>
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
     <td class="mavlink_name" valign="top">sue_PITCHGAIN</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Serial UDB Extra PITCHGAIN Proportional Control</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_PITCHKD</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Serial UDB Extra Pitch Rate Control</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_RUDDER_ELEV_MIX</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Serial UDB Extra Rudder to Elevator Mix</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_ROLL_ELEV_MIX</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Serial UDB Extra Roll to Elevator Mix</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_ELEVATOR_BOOST</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Gain For Boosting Manual Elevator control When Plane Stabilized</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SERIAL_UDB_EXTRA_F7">SERIAL_UDB_EXTRA_F7 (<a href="#SERIAL_UDB_EXTRA_F7">
    #175
   </a>
   )
  </h3>
  <p class="description">Backwards compatible version of SERIAL_UDB_EXTRA F7: format</p>
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
     <td class="mavlink_name" valign="top">sue_YAWKP_RUDDER</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Serial UDB YAWKP_RUDDER Gain for Proporional control of navigation</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_YAWKD_RUDDER</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Serial UDB YAWKD_RUDDER Gain for Rate control of navigation</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_ROLLKP_RUDDER</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Serial UDB Extra ROLLKP_RUDDER Gain for Proportional control of roll stabilization</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_ROLLKD_RUDDER</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Serial UDB Extra ROLLKD_RUDDER Gain for Rate control of roll stabilization</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_RUDDER_BOOST</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">SERIAL UDB EXTRA Rudder Boost Gain to Manual Control when stabilized</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_RTL_PITCH_DOWN</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Serial UDB Extra Return To Landing - Angle to Pitch Plane Down</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SERIAL_UDB_EXTRA_F8">SERIAL_UDB_EXTRA_F8 (<a href="#SERIAL_UDB_EXTRA_F8">
    #176
   </a>
   )
  </h3>
  <p class="description">Backwards compatible version of SERIAL_UDB_EXTRA F8: format</p>
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
     <td class="mavlink_name" valign="top">sue_HEIGHT_TARGET_MAX</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Serial UDB Extra HEIGHT_TARGET_MAX</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_HEIGHT_TARGET_MIN</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Serial UDB Extra HEIGHT_TARGET_MIN</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_ALT_HOLD_THROTTLE_MIN</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Serial UDB Extra ALT_HOLD_THROTTLE_MIN</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_ALT_HOLD_THROTTLE_MAX</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Serial UDB Extra ALT_HOLD_THROTTLE_MAX</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_ALT_HOLD_PITCH_MIN</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Serial UDB Extra ALT_HOLD_PITCH_MIN</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_ALT_HOLD_PITCH_MAX</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Serial UDB Extra ALT_HOLD_PITCH_MAX</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_ALT_HOLD_PITCH_HIGH</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">Serial UDB Extra ALT_HOLD_PITCH_HIGH</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SERIAL_UDB_EXTRA_F13">SERIAL_UDB_EXTRA_F13 (<a href="#SERIAL_UDB_EXTRA_F13">
    #177
   </a>
   )
  </h3>
  <p class="description">Backwards compatible version of SERIAL_UDB_EXTRA F13: format</p>
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
     <td class="mavlink_name" valign="top">sue_week_no</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra GPS Week Number</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_lat_origin</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">Serial UDB Extra MP Origin Latitude</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_lon_origin</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">Serial UDB Extra MP Origin Longitude</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_alt_origin</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">Serial UDB Extra MP Origin Altitude Above Sea Level</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SERIAL_UDB_EXTRA_F14">SERIAL_UDB_EXTRA_F14 (<a href="#SERIAL_UDB_EXTRA_F14">
    #178
   </a>
   )
  </h3>
  <p class="description">Backwards compatible version of SERIAL_UDB_EXTRA F14: format</p>
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
     <td class="mavlink_name" valign="top">sue_WIND_ESTIMATION</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Serial UDB Extra Wind Estimation Enabled</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_GPS_TYPE</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Serial UDB Extra Type of GPS Unit</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_DR</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Serial UDB Extra Dead Reckoning Enabled</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_BOARD_TYPE</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Serial UDB Extra Type of UDB Hardware</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_AIRFRAME</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Serial UDB Extra Type of Airframe</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_RCON</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra Reboot Register of DSPIC</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_TRAP_FLAGS</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra  Last dspic Trap Flags</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_TRAP_SOURCE</td>
     <td class="mavlink_type" valign="top">uint32_t</td>
     <td class="mavlink_comment">Serial UDB Extra Type Program Address of Last Trap</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_osc_fail_count</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Serial UDB Extra Number of Ocillator Failures</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_CLOCK_CONFIG</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Serial UDB Extra UDB Internal Clock Configuration</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_FLIGHT_PLAN_TYPE</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Serial UDB Extra Type of Flight Plan</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SERIAL_UDB_EXTRA_F15">SERIAL_UDB_EXTRA_F15 (<a href="#SERIAL_UDB_EXTRA_F15">
    #179
   </a>
   )
  </h3>
  <p class="description">Backwards compatible version of SERIAL_UDB_EXTRA F15 format</p>
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
     <td class="mavlink_name" valign="top">sue_ID_VEHICLE_MODEL_NAME</td>
     <td class="mavlink_type" valign="top">uint8_t[40]</td>
     <td class="mavlink_comment">Serial UDB Extra Model Name Of Vehicle</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_ID_VEHICLE_REGISTRATION</td>
     <td class="mavlink_type" valign="top">uint8_t[20]</td>
     <td class="mavlink_comment">Serial UDB Extra Registraton Number of Vehicle</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SERIAL_UDB_EXTRA_F16">SERIAL_UDB_EXTRA_F16 (<a href="#SERIAL_UDB_EXTRA_F16">
    #180
   </a>
   )
  </h3>
  <p class="description">Backwards compatible version of SERIAL_UDB_EXTRA F16 format</p>
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
     <td class="mavlink_name" valign="top">sue_ID_LEAD_PILOT</td>
     <td class="mavlink_type" valign="top">uint8_t[40]</td>
     <td class="mavlink_comment">Serial UDB Extra Name of Expected Lead Pilot</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_ID_DIY_DRONES_URL</td>
     <td class="mavlink_type" valign="top">uint8_t[70]</td>
     <td class="mavlink_comment">Serial UDB Extra URL of Lead Pilot or Team</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ALTITUDES">ALTITUDES (<a href="#ALTITUDES">
    #181
   </a>
   )
  </h3>
  <p class="description">The altitude measured by sensors and IMU</p>
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
     <td class="mavlink_comment">Timestamp (milliseconds since system boot)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">alt_gps</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">GPS altitude in meters, expressed as * 1000 (millimeters), above MSL</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">alt_imu</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">IMU altitude above ground in meters, expressed as * 1000 (millimeters)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">alt_barometric</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">barometeric altitude above ground in meters, expressed as * 1000 (millimeters)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">alt_optical_flow</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">Optical flow altitude above ground in meters, expressed as * 1000 (millimeters)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">alt_range_finder</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">Rangefinder Altitude above ground in meters, expressed as * 1000 (millimeters)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">alt_extra</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">Extra altitude above ground in meters, expressed as * 1000 (millimeters)</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="AIRSPEEDS">AIRSPEEDS (<a href="#AIRSPEEDS">
    #182
   </a>
   )
  </h3>
  <p class="description">The airspeed measured by sensors and IMU</p>
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
     <td class="mavlink_comment">Timestamp (milliseconds since system boot)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">airspeed_imu</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Airspeed estimate from IMU, cm/s</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">airspeed_pitot</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Pitot measured forward airpseed, cm/s</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">airspeed_hot_wire</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Hot wire anenometer measured airspeed, cm/s</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">airspeed_ultrasonic</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Ultrasonic measured airspeed, cm/s</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">aoa</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Angle of attack sensor, degrees * 10</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">aoy</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">Yaw angle sensor, degrees * 10</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SERIAL_UDB_EXTRA_F17">SERIAL_UDB_EXTRA_F17 (<a href="#SERIAL_UDB_EXTRA_F17">
    #183
   </a>
   )
  </h3>
  <p class="description">Backwards compatible version of SERIAL_UDB_EXTRA F17 format</p>
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
     <td class="mavlink_name" valign="top">sue_feed_forward</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">SUE Feed Forward Gain</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_turn_rate_nav</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">SUE Max Turn Rate when Navigating</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_turn_rate_fbw</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">SUE Max Turn Rate in Fly By Wire Mode</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SERIAL_UDB_EXTRA_F18">SERIAL_UDB_EXTRA_F18 (<a href="#SERIAL_UDB_EXTRA_F18">
    #184
   </a>
   )
  </h3>
  <p class="description">Backwards compatible version of SERIAL_UDB_EXTRA F18 format</p>
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
     <td class="mavlink_name" valign="top">angle_of_attack_normal</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">SUE Angle of Attack Normal</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">angle_of_attack_inverted</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">SUE Angle of Attack Inverted</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">elevator_trim_normal</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">SUE Elevator Trim Normal</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">elevator_trim_inverted</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">SUE Elevator Trim Inverted</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">reference_speed</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">SUE reference_speed</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SERIAL_UDB_EXTRA_F19">SERIAL_UDB_EXTRA_F19 (<a href="#SERIAL_UDB_EXTRA_F19">
    #185
   </a>
   )
  </h3>
  <p class="description">Backwards compatible version of SERIAL_UDB_EXTRA F19 format</p>
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
     <td class="mavlink_name" valign="top">sue_aileron_output_channel</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">SUE aileron output channel</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_aileron_reversed</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">SUE aileron reversed</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_elevator_output_channel</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">SUE elevator output channel</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_elevator_reversed</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">SUE elevator reversed</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_throttle_output_channel</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">SUE throttle output channel</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_throttle_reversed</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">SUE throttle reversed</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_rudder_output_channel</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">SUE rudder output channel</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_rudder_reversed</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">SUE rudder reversed</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SERIAL_UDB_EXTRA_F20">SERIAL_UDB_EXTRA_F20 (<a href="#SERIAL_UDB_EXTRA_F20">
    #186
   </a>
   )
  </h3>
  <p class="description">Backwards compatible version of SERIAL_UDB_EXTRA F20 format</p>
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
     <td class="mavlink_name" valign="top">sue_number_of_inputs</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">SUE Number of Input Channels</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_trim_value_input_1</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">SUE UDB PWM Trim Value on Input 1</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_trim_value_input_2</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">SUE UDB PWM Trim Value on Input 2</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_trim_value_input_3</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">SUE UDB PWM Trim Value on Input 3</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_trim_value_input_4</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">SUE UDB PWM Trim Value on Input 4</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_trim_value_input_5</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">SUE UDB PWM Trim Value on Input 5</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_trim_value_input_6</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">SUE UDB PWM Trim Value on Input 6</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_trim_value_input_7</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">SUE UDB PWM Trim Value on Input 7</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_trim_value_input_8</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">SUE UDB PWM Trim Value on Input 8</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_trim_value_input_9</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">SUE UDB PWM Trim Value on Input 9</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_trim_value_input_10</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">SUE UDB PWM Trim Value on Input 10</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_trim_value_input_11</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">SUE UDB PWM Trim Value on Input 11</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_trim_value_input_12</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">SUE UDB PWM Trim Value on Input 12</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SERIAL_UDB_EXTRA_F21">SERIAL_UDB_EXTRA_F21 (<a href="#SERIAL_UDB_EXTRA_F21">
    #187
   </a>
   )
  </h3>
  <p class="description">Backwards compatible version of SERIAL_UDB_EXTRA F21 format</p>
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
     <td class="mavlink_name" valign="top">sue_accel_x_offset</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">SUE X accelerometer offset</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_accel_y_offset</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">SUE Y accelerometer offset</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_accel_z_offset</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">SUE Z accelerometer offset</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_gyro_x_offset</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">SUE X gyro offset</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_gyro_y_offset</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">SUE Y gyro offset</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_gyro_z_offset</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">SUE Z gyro offset</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="SERIAL_UDB_EXTRA_F22">SERIAL_UDB_EXTRA_F22 (<a href="#SERIAL_UDB_EXTRA_F22">
    #188
   </a>
   )
  </h3>
  <p class="description">Backwards compatible version of SERIAL_UDB_EXTRA F22 format</p>
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
     <td class="mavlink_name" valign="top">sue_accel_x_at_calibration</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">SUE X accelerometer at calibration time</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_accel_y_at_calibration</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">SUE Y accelerometer at calibration time</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_accel_z_at_calibration</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">SUE Z accelerometer at calibration time</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_gyro_x_at_calibration</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">SUE X gyro at calibration time</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_gyro_y_at_calibration</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">SUE Y gyro at calibration time</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">sue_gyro_z_at_calibration</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">SUE Z gyro at calibration time</td>
    </tr>
   </tbody>
  </table>
 </body>
</html>