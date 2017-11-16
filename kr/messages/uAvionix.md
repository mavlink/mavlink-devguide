<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_gitbook.py -->
# MAVLINK Message Set: uAvionix.xml

*This is a human-readable form of the XML definition file: [uAvionix.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/uAvionix.xml).*

<html>
 <body>
  <h2>MAVLink Type Enumerations</h2>
  <h3 class="mavlink_message_name" id="ENUM_UAVIONIX_ADSB_OUT_DYNAMIC_STATE">
   <a href="#ENUM_UAVIONIX_ADSB_OUT_DYNAMIC_STATE">UAVIONIX_ADSB_OUT_DYNAMIC_STATE</a>
  </h3>
  <p class="description">State flags for ADS-B transponder dynamic report</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_DYNAMIC_STATE_INTENT_CHANGE">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_DYNAMIC_STATE_INTENT_CHANGE">UAVIONIX_ADSB_OUT_DYNAMIC_STATE_INTENT_CHANGE</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_DYNAMIC_STATE_AUTOPILOT_ENABLED">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_DYNAMIC_STATE_AUTOPILOT_ENABLED">UAVIONIX_ADSB_OUT_DYNAMIC_STATE_AUTOPILOT_ENABLED</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_DYNAMIC_STATE_NICBARO_CROSSCHECKED">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_DYNAMIC_STATE_NICBARO_CROSSCHECKED">UAVIONIX_ADSB_OUT_DYNAMIC_STATE_NICBARO_CROSSCHECKED</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_DYNAMIC_STATE_ON_GROUND">
     <td class="mavlink_type" valign="top">8</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_DYNAMIC_STATE_ON_GROUND">UAVIONIX_ADSB_OUT_DYNAMIC_STATE_ON_GROUND</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_DYNAMIC_STATE_IDENT">
     <td class="mavlink_type" valign="top">16</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_DYNAMIC_STATE_IDENT">UAVIONIX_ADSB_OUT_DYNAMIC_STATE_IDENT</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_UAVIONIX_ADSB_OUT_RF_SELECT">
   <a href="#ENUM_UAVIONIX_ADSB_OUT_RF_SELECT">UAVIONIX_ADSB_OUT_RF_SELECT</a>
  </h3>
  <p class="description">Transceiver RF control flags for ADS-B transponder dynamic reports</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_RF_SELECT_STANDBY">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_RF_SELECT_STANDBY">UAVIONIX_ADSB_OUT_RF_SELECT_STANDBY</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_RF_SELECT_RX_ENABLED">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_RF_SELECT_RX_ENABLED">UAVIONIX_ADSB_OUT_RF_SELECT_RX_ENABLED</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_RF_SELECT_TX_ENABLED">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_RF_SELECT_TX_ENABLED">UAVIONIX_ADSB_OUT_RF_SELECT_TX_ENABLED</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX">
   <a href="#ENUM_UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX">UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX</a>
  </h3>
  <p class="description">Status for ADS-B transponder dynamic input</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_NONE_0">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_NONE_0">UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_NONE_0</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_NONE_1">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_NONE_1">UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_NONE_1</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_2D">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_2D">UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_2D</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_3D">
     <td class="mavlink_type" valign="top">3</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_3D">UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_3D</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_DGPS">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_DGPS">UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_DGPS</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_RTK">
     <td class="mavlink_type" valign="top">5</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_RTK">UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_RTK</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_UAVIONIX_ADSB_RF_HEALTH">
   <a href="#ENUM_UAVIONIX_ADSB_RF_HEALTH">UAVIONIX_ADSB_RF_HEALTH</a>
  </h3>
  <p class="description">Status flags for ADS-B transponder dynamic output</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_RF_HEALTH_INITIALIZING">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_RF_HEALTH_INITIALIZING">UAVIONIX_ADSB_RF_HEALTH_INITIALIZING</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_RF_HEALTH_OK">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_RF_HEALTH_OK">UAVIONIX_ADSB_RF_HEALTH_OK</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_RF_HEALTH_FAIL_TX">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_RF_HEALTH_FAIL_TX">UAVIONIX_ADSB_RF_HEALTH_FAIL_TX</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_RF_HEALTH_FAIL_RX">
     <td class="mavlink_type" valign="top">16</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_RF_HEALTH_FAIL_RX">UAVIONIX_ADSB_RF_HEALTH_FAIL_RX</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE">
   <a href="#ENUM_UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE</a>
  </h3>
  <p class="description">Definitions for aircraft size</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_NO_DATA">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_NO_DATA">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_NO_DATA</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L15M_W23M">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L15M_W23M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L15M_W23M</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L25M_W28P5M">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L25M_W28P5M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L25M_W28P5M</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L25_34M">
     <td class="mavlink_type" valign="top">3</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L25_34M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L25_34M</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L35_33M">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L35_33M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L35_33M</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L35_38M">
     <td class="mavlink_type" valign="top">5</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L35_38M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L35_38M</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L45_39P5M">
     <td class="mavlink_type" valign="top">6</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L45_39P5M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L45_39P5M</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L45_45M">
     <td class="mavlink_type" valign="top">7</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L45_45M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L45_45M</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L55_45M">
     <td class="mavlink_type" valign="top">8</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L55_45M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L55_45M</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L55_52M">
     <td class="mavlink_type" valign="top">9</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L55_52M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L55_52M</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L65_59P5M">
     <td class="mavlink_type" valign="top">10</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L65_59P5M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L65_59P5M</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L65_67M">
     <td class="mavlink_type" valign="top">11</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L65_67M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L65_67M</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L75_W72P5M">
     <td class="mavlink_type" valign="top">12</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L75_W72P5M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L75_W72P5M</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L75_W80M">
     <td class="mavlink_type" valign="top">13</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L75_W80M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L75_W80M</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L85_W80M">
     <td class="mavlink_type" valign="top">14</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L85_W80M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L85_W80M</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L85_W90M">
     <td class="mavlink_type" valign="top">15</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L85_W90M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L85_W90M</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT">
   <a href="#ENUM_UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT">UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT</a>
  </h3>
  <p class="description">GPS lataral offset encoding</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_NO_DATA">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_NO_DATA">UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_NO_DATA</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_2M">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_2M">UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_2M</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_4M">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_4M">UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_4M</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_6M">
     <td class="mavlink_type" valign="top">3</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_6M">UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_6M</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_0M">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_0M">UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_0M</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_2M">
     <td class="mavlink_type" valign="top">5</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_2M">UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_2M</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_4M">
     <td class="mavlink_type" valign="top">6</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_4M">UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_4M</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_6M">
     <td class="mavlink_type" valign="top">7</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_6M">UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_6M</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON">
   <a href="#ENUM_UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON">UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON</a>
  </h3>
  <p class="description">GPS longitudinal offset encoding</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON_NO_DATA">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON_NO_DATA">UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON_NO_DATA</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON_APPLIED_BY_SENSOR">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON_APPLIED_BY_SENSOR">UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON_APPLIED_BY_SENSOR</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="ENUM_UAVIONIX_ADSB_EMERGENCY_STATUS">
   <a href="#ENUM_UAVIONIX_ADSB_EMERGENCY_STATUS">UAVIONIX_ADSB_EMERGENCY_STATUS</a>
  </h3>
  <p class="description">Emergency status encoding</p>
  <table class="sortable">
   <thead>
    <tr>
     <th class="mavlink_field_header">CMD ID</th>
     <th class="mavlink_field_header">Field Name</th>
     <th class="mavlink_field_header">Description</th>
    </tr>
   </thead>
   <tbody>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_NO_EMERGENCY">
     <td class="mavlink_type" valign="top">0</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_NO_EMERGENCY">UAVIONIX_ADSB_OUT_NO_EMERGENCY</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_GENERAL_EMERGENCY">
     <td class="mavlink_type" valign="top">1</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_GENERAL_EMERGENCY">UAVIONIX_ADSB_OUT_GENERAL_EMERGENCY</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_LIFEGUARD_EMERGENCY">
     <td class="mavlink_type" valign="top">2</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_LIFEGUARD_EMERGENCY">UAVIONIX_ADSB_OUT_LIFEGUARD_EMERGENCY</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_MINIMUM_FUEL_EMERGENCY">
     <td class="mavlink_type" valign="top">3</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_MINIMUM_FUEL_EMERGENCY">UAVIONIX_ADSB_OUT_MINIMUM_FUEL_EMERGENCY</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_NO_COMM_EMERGENCY">
     <td class="mavlink_type" valign="top">4</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_NO_COMM_EMERGENCY">UAVIONIX_ADSB_OUT_NO_COMM_EMERGENCY</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_UNLAWFUL_INTERFERANCE_EMERGENCY">
     <td class="mavlink_type" valign="top">5</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_UNLAWFUL_INTERFERANCE_EMERGENCY">UAVIONIX_ADSB_OUT_UNLAWFUL_INTERFERANCE_EMERGENCY</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_DOWNED_AIRCRAFT_EMERGENCY">
     <td class="mavlink_type" valign="top">6</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_DOWNED_AIRCRAFT_EMERGENCY">UAVIONIX_ADSB_OUT_DOWNED_AIRCRAFT_EMERGENCY</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
    <tr class="mavlink_field" id="UAVIONIX_ADSB_OUT_RESERVED">
     <td class="mavlink_type" valign="top">7</td>
     <td class="mavlink_name" valign="top">
      <a href="#UAVIONIX_ADSB_OUT_RESERVED">UAVIONIX_ADSB_OUT_RESERVED</a>
     </td>
     <td class="mavlink_comment">
     </td>
    </tr>
   </tbody>
  </table>
  <h2>MAVLink Messages</h2>
  <h3 class="mavlink_message_name" id="UAVIONIX_ADSB_OUT_CFG">UAVIONIX_ADSB_OUT_CFG (<a href="#UAVIONIX_ADSB_OUT_CFG">
    #10001
   </a>
   )
  </h3>
  <p class="description">
   <strong>
    (MAVLink 2)
   </strong>Static data to configure the ADS-B transponder (send within 10 sec of a POR and every 10 sec thereafter)</p>
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
     <td class="mavlink_name" valign="top">ICAO</td>
     <td class="mavlink_type" valign="top">uint32_t</td>
     <td class="mavlink_comment">Vehicle address (24 bit)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">callsign</td>
     <td class="mavlink_type" valign="top">char[9]</td>
     <td class="mavlink_comment">Vehicle identifier (8 characters, null terminated, valid characters are A-Z, 0-9, " " only)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">emitterType</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Transmitting vehicle type. See ADSB_EMITTER_TYPE enum
     (Enum:<a href="#ENUM_ADSB_EMITTER_TYPE">ADSB_EMITTER_TYPE</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">aircraftSize</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Aircraft length and width encoding (table 2-35 of DO-282B)
     (Enum:<a href="#ENUM_UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">gpsOffsetLat</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">GPS antenna lateral offset (table 2-36 of DO-282B)
     (Enum:<a href="#ENUM_UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT">UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">gpsOffsetLon</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">GPS antenna longitudinal offset from nose [if non-zero, take position (in meters) divide by 2 and add one] (table 2-37 DO-282B)
     (Enum:<a href="#ENUM_UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON">UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">stallSpeed</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Aircraft stall speed in cm/s
     (Units: cm/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">rfSelect</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">ADS-B transponder reciever and transmit enable flags
     (Enum:<a href="#ENUM_UAVIONIX_ADSB_OUT_RF_SELECT">UAVIONIX_ADSB_OUT_RF_SELECT</a>
      )
     </td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="UAVIONIX_ADSB_OUT_DYNAMIC">UAVIONIX_ADSB_OUT_DYNAMIC (<a href="#UAVIONIX_ADSB_OUT_DYNAMIC">
    #10002
   </a>
   )
  </h3>
  <p class="description">
   <strong>
    (MAVLink 2)
   </strong>Dynamic data used to generate ADS-B out transponder data (send at 5Hz)</p>
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
     <td class="mavlink_name" valign="top">utcTime</td>
     <td class="mavlink_type" valign="top">uint32_t</td>
     <td class="mavlink_comment">UTC time in seconds since GPS epoch (Jan 6, 1980). If unknown set to UINT32_MAX
     (Units: s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">gpsLat</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">Latitude WGS84 (deg * 1E7). If unknown set to INT32_MAX
     (Units: degE7)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">gpsLon</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">Longitude WGS84 (deg * 1E7). If unknown set to INT32_MAX
     (Units: degE7)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">gpsAlt</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">Altitude in mm (m * 1E-3) UP +ve. WGS84 altitude. If unknown set to INT32_MAX
     (Units: mm)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">gpsFix</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">0-1: no fix, 2: 2D fix, 3: 3D fix, 4: DGPS, 5: RTK
     (Enum:<a href="#ENUM_UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX">UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">numSats</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Number of satellites visible. If unknown set to UINT8_MAX</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">baroAltMSL</td>
     <td class="mavlink_type" valign="top">int32_t</td>
     <td class="mavlink_comment">Barometric pressure altitude relative to a standard atmosphere of 1013.2 mBar and NOT bar corrected altitude (m * 1E-3). (up +ve). If unknown set to INT32_MAX
     (Units: mbar)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">accuracyHor</td>
     <td class="mavlink_type" valign="top">uint32_t</td>
     <td class="mavlink_comment">Horizontal accuracy in mm (m * 1E-3). If unknown set to UINT32_MAX
     (Units: mm)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">accuracyVert</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Vertical accuracy in cm. If unknown set to UINT16_MAX
     (Units: cm)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">accuracyVel</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Velocity accuracy in mm/s (m * 1E-3). If unknown set to UINT16_MAX
     (Units: mm/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">velVert</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">GPS vertical speed in cm/s. If unknown set to INT16_MAX
     (Units: cm/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">velNS</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">North-South velocity over ground in cm/s North +ve. If unknown set to INT16_MAX
     (Units: cm/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">VelEW</td>
     <td class="mavlink_type" valign="top">int16_t</td>
     <td class="mavlink_comment">East-West velocity over ground in cm/s East +ve. If unknown set to INT16_MAX
     (Units: cm/s)</td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">emergencyStatus</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">Emergency status
     (Enum:<a href="#ENUM_UAVIONIX_ADSB_EMERGENCY_STATUS">UAVIONIX_ADSB_EMERGENCY_STATUS</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">state</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">ADS-B transponder dynamic input state flags
     (Enum:<a href="#ENUM_UAVIONIX_ADSB_OUT_DYNAMIC_STATE">UAVIONIX_ADSB_OUT_DYNAMIC_STATE</a>
      )
     </td>
    </tr>
    <tr class="mavlink_field">
     #Conditionally format field name based on whether it is MAVLink 2 (to blue)
     <td class="mavlink_name" valign="top">squawk</td>
     <td class="mavlink_type" valign="top">uint16_t</td>
     <td class="mavlink_comment">Mode A code (typically 1200 [0x04B0] for VFR)</td>
    </tr>
   </tbody>
  </table>
  <h3 class="mavlink_message_name" id="UAVIONIX_ADSB_TRANSCEIVER_HEALTH_REPORT">UAVIONIX_ADSB_TRANSCEIVER_HEALTH_REPORT (<a href="#UAVIONIX_ADSB_TRANSCEIVER_HEALTH_REPORT">
    #10003
   </a>
   )
  </h3>
  <p class="description">
   <strong>
    (MAVLink 2)
   </strong>Transceiver heartbeat with health report (updated every 10s)</p>
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
     <td class="mavlink_name" valign="top">rfHealth</td>
     <td class="mavlink_type" valign="top">uint8_t</td>
     <td class="mavlink_comment">ADS-B transponder messages
     (Enum:<a href="#ENUM_UAVIONIX_ADSB_RF_HEALTH">UAVIONIX_ADSB_RF_HEALTH</a>
      )
     </td>
    </tr>
   </tbody>
  </table>
 </body>
</html>