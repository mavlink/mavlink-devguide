<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_gitbook.py -->
# MAVLINK Message Set: icarous.xml

*This is a human-readable form of the XML definition file: [icarous.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/icarous.xml).*

<span></span>
> **Note** MAVLink 2 messages have an ID > 255 and are marked up using **(MAVLink 2)** in their description.

<span id="mav2_extension_field"></span>
> **Note** MAVLink 2 extension fields that have been added to MAVLink 1 messages are displayed in blue.

<html>
 <body>
  <h2>MAVLink Type Enumerations</h2>
  <h3 class="mavlink_message_name" id="ICAROUS_TRACK_BAND_TYPES">
   <a href="#ICAROUS_TRACK_BAND_TYPES">ICAROUS_TRACK_BAND_TYPES</a>
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
    <tr class="mavlink_field" id="ICAROUS_TRACK_BAND_TYPE_NONE">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#ICAROUS_TRACK_BAND_TYPE_NONE">ICAROUS_TRACK_BAND_TYPE_NONE</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="ICAROUS_TRACK_BAND_TYPE_NEAR">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#ICAROUS_TRACK_BAND_TYPE_NEAR">ICAROUS_TRACK_BAND_TYPE_NEAR</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="ICAROUS_TRACK_BAND_TYPE_RECOVERY">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#ICAROUS_TRACK_BAND_TYPE_RECOVERY">ICAROUS_TRACK_BAND_TYPE_RECOVERY</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ICAROUS_FMS_STATE">
   <a href="#ICAROUS_FMS_STATE">ICAROUS_FMS_STATE</a>
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
    <tr class="mavlink_field" id="ICAROUS_FMS_STATE_IDLE">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#ICAROUS_FMS_STATE_IDLE">ICAROUS_FMS_STATE_IDLE</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="ICAROUS_FMS_STATE_TAKEOFF">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#ICAROUS_FMS_STATE_TAKEOFF">ICAROUS_FMS_STATE_TAKEOFF</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="ICAROUS_FMS_STATE_CLIMB">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#ICAROUS_FMS_STATE_CLIMB">ICAROUS_FMS_STATE_CLIMB</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="ICAROUS_FMS_STATE_CRUISE">
     <td class="mavlink_type" valign="top">3</td>
     <td class="mavlink_name" valign="top">
      <a href="#ICAROUS_FMS_STATE_CRUISE">ICAROUS_FMS_STATE_CRUISE</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="ICAROUS_FMS_STATE_APPROACH">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#ICAROUS_FMS_STATE_APPROACH">ICAROUS_FMS_STATE_APPROACH</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="ICAROUS_FMS_STATE_LAND">
     <td class="mavlink_type" valign="top">5</td>
     <td class="mavlink_name" valign="top">
      <a href="#ICAROUS_FMS_STATE_LAND">ICAROUS_FMS_STATE_LAND</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
   </tbody>
  </table>
  <h2>MAVLink Messages</h2>
  <h3 class="mavlink_message_name" id="ICAROUS_HEARTBEAT">ICAROUS_HEARTBEAT (<a href="#ICAROUS_HEARTBEAT">
    #42000
   </a>
   )
  </h3>
  <p class="description">
   <strong>
    (MAVLink 2)
   </strong>ICAROUS heartbeat</p>
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
     <td class="mavlink_name" valign="top">status</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">See the FMS_STATE enum.
     (Enum:<a href="#ICAROUS_FMS_STATE">ICAROUS_FMS_STATE</a>
      )
     </td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ICAROUS_KINEMATIC_BANDS">ICAROUS_KINEMATIC_BANDS (<a href="#ICAROUS_KINEMATIC_BANDS">
    #42001
   </a>
   )
  </h3>
  <p class="description">
   <strong>
    (MAVLink 2)
   </strong>Kinematic multi bands (track) output from Daidalus</p>
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
     <td class="mavlink_name" valign="top">numBands</td>
     <td class="mavlink_type" valign="top">int8_t</td>
     <td class="mavlink_comment">Number of track bands</td>
    </tr>
    <tr class="mavlink_field">
     <td class="mavlink_name" valign="top">type1</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">See the TRACK_BAND_TYPES enum.
     (Enum:<a href="#ICAROUS_TRACK_BAND_TYPES">ICAROUS_TRACK_BAND_TYPES</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     <td class="mavlink_name" valign="top">min1</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">min angle (degrees)
     (Units: deg)</td>
    </tr>
    <tr class="mavlink_field">
     <td class="mavlink_name" valign="top">max1</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">max angle (degrees)
     (Units: deg)</td>
    </tr>
    <tr class="mavlink_field">
     <td class="mavlink_name" valign="top">type2</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">See the TRACK_BAND_TYPES enum.
     (Enum:<a href="#ICAROUS_TRACK_BAND_TYPES">ICAROUS_TRACK_BAND_TYPES</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     <td class="mavlink_name" valign="top">min2</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">min angle (degrees)
     (Units: deg)</td>
    </tr>
    <tr class="mavlink_field">
     <td class="mavlink_name" valign="top">max2</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">max angle (degrees)
     (Units: deg)</td>
    </tr>
    <tr class="mavlink_field">
     <td class="mavlink_name" valign="top">type3</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">See the TRACK_BAND_TYPES enum.
     (Enum:<a href="#ICAROUS_TRACK_BAND_TYPES">ICAROUS_TRACK_BAND_TYPES</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     <td class="mavlink_name" valign="top">min3</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">min angle (degrees)
     (Units: deg)</td>
    </tr>
    <tr class="mavlink_field">
     <td class="mavlink_name" valign="top">max3</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">max angle (degrees)
     (Units: deg)</td>
    </tr>
    <tr class="mavlink_field">
     <td class="mavlink_name" valign="top">type4</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">See the TRACK_BAND_TYPES enum.
     (Enum:<a href="#ICAROUS_TRACK_BAND_TYPES">ICAROUS_TRACK_BAND_TYPES</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     <td class="mavlink_name" valign="top">min4</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">min angle (degrees)
     (Units: deg)</td>
    </tr>
    <tr class="mavlink_field">
     <td class="mavlink_name" valign="top">max4</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">max angle (degrees)
     (Units: deg)</td>
    </tr>
    <tr class="mavlink_field">
     <td class="mavlink_name" valign="top">type5</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">See the TRACK_BAND_TYPES enum.
     (Enum:<a href="#ICAROUS_TRACK_BAND_TYPES">ICAROUS_TRACK_BAND_TYPES</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     <td class="mavlink_name" valign="top">min5</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">min angle (degrees)
     (Units: deg)</td>
    </tr>
    <tr class="mavlink_field">
     <td class="mavlink_name" valign="top">max5</td>
     <td class="mavlink_type" valign="top">float</td>
     <td class="mavlink_comment">max angle (degrees)
     (Units: deg)</td>
    </tr>
   </tbody>
  </table>
 </body>
</html>