<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_gitbook.py -->
# MAVLINK Message Set: icarous.xml

*This is a human-readable form of the XML definition file: [icarous.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/icarous.xml).*

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

<h2>MAVLink Type Enumerations</h2>

<h3 id="ICAROUS_TRACK_BAND_TYPES">
   <a href="#ICAROUS_TRACK_BAND_TYPES">ICAROUS_TRACK_BAND_TYPES</a>
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
    <tr id="ICAROUS_TRACK_BAND_TYPE_NONE">
     <td>0</td>
     <td>
      <a href="#ICAROUS_TRACK_BAND_TYPE_NONE">ICAROUS_TRACK_BAND_TYPE_NONE</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="ICAROUS_TRACK_BAND_TYPE_NEAR">
     <td>1</td>
     <td>
      <a href="#ICAROUS_TRACK_BAND_TYPE_NEAR">ICAROUS_TRACK_BAND_TYPE_NEAR</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="ICAROUS_TRACK_BAND_TYPE_RECOVERY">
     <td>2</td>
     <td>
      <a href="#ICAROUS_TRACK_BAND_TYPE_RECOVERY">ICAROUS_TRACK_BAND_TYPE_RECOVERY</a>
     </td>
     <td>
     </td>
    </tr>
   </tbody>
  </table>

<h3 id="ICAROUS_FMS_STATE">
   <a href="#ICAROUS_FMS_STATE">ICAROUS_FMS_STATE</a>
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
    <tr id="ICAROUS_FMS_STATE_IDLE">
     <td>0</td>
     <td>
      <a href="#ICAROUS_FMS_STATE_IDLE">ICAROUS_FMS_STATE_IDLE</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="ICAROUS_FMS_STATE_TAKEOFF">
     <td>1</td>
     <td>
      <a href="#ICAROUS_FMS_STATE_TAKEOFF">ICAROUS_FMS_STATE_TAKEOFF</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="ICAROUS_FMS_STATE_CLIMB">
     <td>2</td>
     <td>
      <a href="#ICAROUS_FMS_STATE_CLIMB">ICAROUS_FMS_STATE_CLIMB</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="ICAROUS_FMS_STATE_CRUISE">
     <td>3</td>
     <td>
      <a href="#ICAROUS_FMS_STATE_CRUISE">ICAROUS_FMS_STATE_CRUISE</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="ICAROUS_FMS_STATE_APPROACH">
     <td>4</td>
     <td>
      <a href="#ICAROUS_FMS_STATE_APPROACH">ICAROUS_FMS_STATE_APPROACH</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="ICAROUS_FMS_STATE_LAND">
     <td>5</td>
     <td>
      <a href="#ICAROUS_FMS_STATE_LAND">ICAROUS_FMS_STATE_LAND</a>
     </td>
     <td>
     </td>
    </tr>
   </tbody>
  </table>

<h2>MAVLink Messages</h2>

<h3 id="ICAROUS_HEARTBEAT">ICAROUS_HEARTBEAT (<a href="#ICAROUS_HEARTBEAT">
    #42000
   </a>
   )
  </h3>

<p>
   <strong>
    (MAVLink 2)
   </strong>ICAROUS heartbeat</p>

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
     <td>status</td>
     <td>uint8_t</td>
     <td>
      <a href="#ICAROUS_FMS_STATE">ICAROUS_FMS_STATE</a>
     </td>
     <td>See the FMS_STATE enum.</td>
    </tr>
   </tbody>
  </table>

<h3 id="ICAROUS_KINEMATIC_BANDS">ICAROUS_KINEMATIC_BANDS (<a href="#ICAROUS_KINEMATIC_BANDS">
    #42001
   </a>
   )
  </h3>

<p>
   <strong>
    (MAVLink 2)
   </strong>Kinematic multi bands (track) output from Daidalus</p>

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
     <td>numBands</td>
     <td>int8_t</td>
     <td>
     </td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>Number of track bands</td>
    </tr>
    <tr>
     <td>type1</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>
      <a href="#ICAROUS_TRACK_BAND_TYPES">ICAROUS_TRACK_BAND_TYPES</a>
     </td>
     <td>See the TRACK_BAND_TYPES enum.</td>
    </tr>
    <tr>
     <td>min1</td>
     <td>float</td>
     <td>deg</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>min angle (degrees)</td>
    </tr>
    <tr>
     <td>max1</td>
     <td>float</td>
     <td>deg</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>max angle (degrees)</td>
    </tr>
    <tr>
     <td>type2</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>
      <a href="#ICAROUS_TRACK_BAND_TYPES">ICAROUS_TRACK_BAND_TYPES</a>
     </td>
     <td>See the TRACK_BAND_TYPES enum.</td>
    </tr>
    <tr>
     <td>min2</td>
     <td>float</td>
     <td>deg</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>min angle (degrees)</td>
    </tr>
    <tr>
     <td>max2</td>
     <td>float</td>
     <td>deg</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>max angle (degrees)</td>
    </tr>
    <tr>
     <td>type3</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>
      <a href="#ICAROUS_TRACK_BAND_TYPES">ICAROUS_TRACK_BAND_TYPES</a>
     </td>
     <td>See the TRACK_BAND_TYPES enum.</td>
    </tr>
    <tr>
     <td>min3</td>
     <td>float</td>
     <td>deg</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>min angle (degrees)</td>
    </tr>
    <tr>
     <td>max3</td>
     <td>float</td>
     <td>deg</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>max angle (degrees)</td>
    </tr>
    <tr>
     <td>type4</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>
      <a href="#ICAROUS_TRACK_BAND_TYPES">ICAROUS_TRACK_BAND_TYPES</a>
     </td>
     <td>See the TRACK_BAND_TYPES enum.</td>
    </tr>
    <tr>
     <td>min4</td>
     <td>float</td>
     <td>deg</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>min angle (degrees)</td>
    </tr>
    <tr>
     <td>max4</td>
     <td>float</td>
     <td>deg</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>max angle (degrees)</td>
    </tr>
    <tr>
     <td>type5</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>
      <a href="#ICAROUS_TRACK_BAND_TYPES">ICAROUS_TRACK_BAND_TYPES</a>
     </td>
     <td>See the TRACK_BAND_TYPES enum.</td>
    </tr>
    <tr>
     <td>min5</td>
     <td>float</td>
     <td>deg</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>min angle (degrees)</td>
    </tr>
    <tr>
     <td>max5</td>
     <td>float</td>
     <td>deg</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>max angle (degrees)</td>
    </tr>
   </tbody>
  </table>

<p></body>
</html>
