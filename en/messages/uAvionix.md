<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_gitbook.py -->
# MAVLINK Message Set: uAvionix.xml

*This is a human-readable form of the XML definition file: [uAvionix.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/uAvionix.xml).*

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
  <h2>MAVLink Type Enumerations</h2>
  <h3 id="UAVIONIX_ADSB_OUT_DYNAMIC_STATE">
   <a href="#UAVIONIX_ADSB_OUT_DYNAMIC_STATE">UAVIONIX_ADSB_OUT_DYNAMIC_STATE</a>
  </h3>
  <p>State flags for ADS-B transponder dynamic report</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Value</th>
     <th>Field Name</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr id="UAVIONIX_ADSB_OUT_DYNAMIC_STATE_INTENT_CHANGE">
     <td>1</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_DYNAMIC_STATE_INTENT_CHANGE">UAVIONIX_ADSB_OUT_DYNAMIC_STATE_INTENT_CHANGE</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_DYNAMIC_STATE_AUTOPILOT_ENABLED">
     <td>2</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_DYNAMIC_STATE_AUTOPILOT_ENABLED">UAVIONIX_ADSB_OUT_DYNAMIC_STATE_AUTOPILOT_ENABLED</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_DYNAMIC_STATE_NICBARO_CROSSCHECKED">
     <td>4</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_DYNAMIC_STATE_NICBARO_CROSSCHECKED">UAVIONIX_ADSB_OUT_DYNAMIC_STATE_NICBARO_CROSSCHECKED</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_DYNAMIC_STATE_ON_GROUND">
     <td>8</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_DYNAMIC_STATE_ON_GROUND">UAVIONIX_ADSB_OUT_DYNAMIC_STATE_ON_GROUND</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_DYNAMIC_STATE_IDENT">
     <td>16</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_DYNAMIC_STATE_IDENT">UAVIONIX_ADSB_OUT_DYNAMIC_STATE_IDENT</a>
     </td>
     <td>
     </td>
    </tr>
   </tbody>
  </table>
  <h3 id="UAVIONIX_ADSB_OUT_RF_SELECT">
   <a href="#UAVIONIX_ADSB_OUT_RF_SELECT">UAVIONIX_ADSB_OUT_RF_SELECT</a>
  </h3>
  <p>Transceiver RF control flags for ADS-B transponder dynamic reports</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Value</th>
     <th>Field Name</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr id="UAVIONIX_ADSB_OUT_RF_SELECT_STANDBY">
     <td>0</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_RF_SELECT_STANDBY">UAVIONIX_ADSB_OUT_RF_SELECT_STANDBY</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_RF_SELECT_RX_ENABLED">
     <td>1</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_RF_SELECT_RX_ENABLED">UAVIONIX_ADSB_OUT_RF_SELECT_RX_ENABLED</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_RF_SELECT_TX_ENABLED">
     <td>2</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_RF_SELECT_TX_ENABLED">UAVIONIX_ADSB_OUT_RF_SELECT_TX_ENABLED</a>
     </td>
     <td>
     </td>
    </tr>
   </tbody>
  </table>
  <h3 id="UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX">
   <a href="#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX">UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX</a>
  </h3>
  <p>Status for ADS-B transponder dynamic input</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Value</th>
     <th>Field Name</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr id="UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_NONE_0">
     <td>0</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_NONE_0">UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_NONE_0</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_NONE_1">
     <td>1</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_NONE_1">UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_NONE_1</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_2D">
     <td>2</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_2D">UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_2D</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_3D">
     <td>3</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_3D">UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_3D</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_DGPS">
     <td>4</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_DGPS">UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_DGPS</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_RTK">
     <td>5</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_RTK">UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX_RTK</a>
     </td>
     <td>
     </td>
    </tr>
   </tbody>
  </table>
  <h3 id="UAVIONIX_ADSB_RF_HEALTH">
   <a href="#UAVIONIX_ADSB_RF_HEALTH">UAVIONIX_ADSB_RF_HEALTH</a>
  </h3>
  <p>Status flags for ADS-B transponder dynamic output</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Value</th>
     <th>Field Name</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr id="UAVIONIX_ADSB_RF_HEALTH_INITIALIZING">
     <td>0</td>
     <td>
      <a href="#UAVIONIX_ADSB_RF_HEALTH_INITIALIZING">UAVIONIX_ADSB_RF_HEALTH_INITIALIZING</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_RF_HEALTH_OK">
     <td>1</td>
     <td>
      <a href="#UAVIONIX_ADSB_RF_HEALTH_OK">UAVIONIX_ADSB_RF_HEALTH_OK</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_RF_HEALTH_FAIL_TX">
     <td>2</td>
     <td>
      <a href="#UAVIONIX_ADSB_RF_HEALTH_FAIL_TX">UAVIONIX_ADSB_RF_HEALTH_FAIL_TX</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_RF_HEALTH_FAIL_RX">
     <td>16</td>
     <td>
      <a href="#UAVIONIX_ADSB_RF_HEALTH_FAIL_RX">UAVIONIX_ADSB_RF_HEALTH_FAIL_RX</a>
     </td>
     <td>
     </td>
    </tr>
   </tbody>
  </table>
  <h3 id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE">
   <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE</a>
  </h3>
  <p>Definitions for aircraft size</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Value</th>
     <th>Field Name</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_NO_DATA">
     <td>0</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_NO_DATA">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_NO_DATA</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L15M_W23M">
     <td>1</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L15M_W23M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L15M_W23M</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L25M_W28P5M">
     <td>2</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L25M_W28P5M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L25M_W28P5M</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L25_34M">
     <td>3</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L25_34M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L25_34M</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L35_33M">
     <td>4</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L35_33M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L35_33M</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L35_38M">
     <td>5</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L35_38M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L35_38M</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L45_39P5M">
     <td>6</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L45_39P5M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L45_39P5M</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L45_45M">
     <td>7</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L45_45M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L45_45M</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L55_45M">
     <td>8</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L55_45M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L55_45M</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L55_52M">
     <td>9</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L55_52M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L55_52M</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L65_59P5M">
     <td>10</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L65_59P5M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L65_59P5M</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L65_67M">
     <td>11</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L65_67M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L65_67M</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L75_W72P5M">
     <td>12</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L75_W72P5M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L75_W72P5M</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L75_W80M">
     <td>13</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L75_W80M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L75_W80M</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L85_W80M">
     <td>14</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L85_W80M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L85_W80M</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L85_W90M">
     <td>15</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L85_W90M">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE_L85_W90M</a>
     </td>
     <td>
     </td>
    </tr>
   </tbody>
  </table>
  <h3 id="UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT">
   <a href="#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT">UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT</a>
  </h3>
  <p>GPS lataral offset encoding</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Value</th>
     <th>Field Name</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr id="UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_NO_DATA">
     <td>0</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_NO_DATA">UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_NO_DATA</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_2M">
     <td>1</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_2M">UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_2M</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_4M">
     <td>2</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_4M">UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_4M</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_6M">
     <td>3</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_6M">UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_LEFT_6M</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_0M">
     <td>4</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_0M">UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_0M</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_2M">
     <td>5</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_2M">UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_2M</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_4M">
     <td>6</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_4M">UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_4M</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_6M">
     <td>7</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_6M">UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT_RIGHT_6M</a>
     </td>
     <td>
     </td>
    </tr>
   </tbody>
  </table>
  <h3 id="UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON">
   <a href="#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON">UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON</a>
  </h3>
  <p>GPS longitudinal offset encoding</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Value</th>
     <th>Field Name</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr id="UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON_NO_DATA">
     <td>0</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON_NO_DATA">UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON_NO_DATA</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON_APPLIED_BY_SENSOR">
     <td>1</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON_APPLIED_BY_SENSOR">UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON_APPLIED_BY_SENSOR</a>
     </td>
     <td>
     </td>
    </tr>
   </tbody>
  </table>
  <h3 id="UAVIONIX_ADSB_EMERGENCY_STATUS">
   <a href="#UAVIONIX_ADSB_EMERGENCY_STATUS">UAVIONIX_ADSB_EMERGENCY_STATUS</a>
  </h3>
  <p>Emergency status encoding</p>
  <table class="sortable">
   <thead>
    <tr>
     <th>Value</th>
     <th>Field Name</th>
     <th>Description</th>
    </tr>
   </thead>
   <tbody>
    <tr id="UAVIONIX_ADSB_OUT_NO_EMERGENCY">
     <td>0</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_NO_EMERGENCY">UAVIONIX_ADSB_OUT_NO_EMERGENCY</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_GENERAL_EMERGENCY">
     <td>1</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_GENERAL_EMERGENCY">UAVIONIX_ADSB_OUT_GENERAL_EMERGENCY</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_LIFEGUARD_EMERGENCY">
     <td>2</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_LIFEGUARD_EMERGENCY">UAVIONIX_ADSB_OUT_LIFEGUARD_EMERGENCY</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_MINIMUM_FUEL_EMERGENCY">
     <td>3</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_MINIMUM_FUEL_EMERGENCY">UAVIONIX_ADSB_OUT_MINIMUM_FUEL_EMERGENCY</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_NO_COMM_EMERGENCY">
     <td>4</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_NO_COMM_EMERGENCY">UAVIONIX_ADSB_OUT_NO_COMM_EMERGENCY</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_UNLAWFUL_INTERFERANCE_EMERGENCY">
     <td>5</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_UNLAWFUL_INTERFERANCE_EMERGENCY">UAVIONIX_ADSB_OUT_UNLAWFUL_INTERFERANCE_EMERGENCY</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_DOWNED_AIRCRAFT_EMERGENCY">
     <td>6</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_DOWNED_AIRCRAFT_EMERGENCY">UAVIONIX_ADSB_OUT_DOWNED_AIRCRAFT_EMERGENCY</a>
     </td>
     <td>
     </td>
    </tr>
    <tr id="UAVIONIX_ADSB_OUT_RESERVED">
     <td>7</td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_RESERVED">UAVIONIX_ADSB_OUT_RESERVED</a>
     </td>
     <td>
     </td>
    </tr>
   </tbody>
  </table>
  <h2>MAVLink Messages</h2>
  <h3 id="UAVIONIX_ADSB_OUT_CFG">UAVIONIX_ADSB_OUT_CFG (<a href="#UAVIONIX_ADSB_OUT_CFG">
    #10001
   </a>
   )
  </h3>
  <p>
   <strong>
    (MAVLink 2)
   </strong>Static data to configure the ADS-B transponder (send within 10 sec of a POR and every 10 sec thereafter)</p>
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
     <td>ICAO</td>
     <td>uint32_t</td>
     <td>
     </td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>Vehicle address (24 bit)</td>
    </tr>
    <tr>
     <td>callsign</td>
     <td>char[9]</td>
     <td>
     </td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>Vehicle identifier (8 characters, null terminated, valid characters are A-Z, 0-9, " " only)</td>
    </tr>
    <tr>
     <td>emitterType</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>
      <a href="#ADSB_EMITTER_TYPE">ADSB_EMITTER_TYPE</a>
     </td>
     <td>Transmitting vehicle type. See ADSB_EMITTER_TYPE enum</td>
    </tr>
    <tr>
     <td>aircraftSize</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE">UAVIONIX_ADSB_OUT_CFG_AIRCRAFT_SIZE</a>
     </td>
     <td>Aircraft length and width encoding (table 2-35 of DO-282B)</td>
    </tr>
    <tr>
     <td>gpsOffsetLat</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT">UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LAT</a>
     </td>
     <td>GPS antenna lateral offset (table 2-36 of DO-282B)</td>
    </tr>
    <tr>
     <td>gpsOffsetLon</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON">UAVIONIX_ADSB_OUT_CFG_GPS_OFFSET_LON</a>
     </td>
     <td>GPS antenna longitudinal offset from nose [if non-zero, take position (in meters) divide by 2 and add one] (table 2-37 DO-282B)</td>
    </tr>
    <tr>
     <td>stallSpeed</td>
     <td>uint16_t</td>
     <td>cm/s</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>Aircraft stall speed in cm/s</td>
    </tr>
    <tr>
     <td>rfSelect</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_RF_SELECT">UAVIONIX_ADSB_OUT_RF_SELECT</a>
     </td>
     <td>ADS-B transponder reciever and transmit enable flags</td>
    </tr>
   </tbody>
  </table>
  <h3 id="UAVIONIX_ADSB_OUT_DYNAMIC">UAVIONIX_ADSB_OUT_DYNAMIC (<a href="#UAVIONIX_ADSB_OUT_DYNAMIC">
    #10002
   </a>
   )
  </h3>
  <p>
   <strong>
    (MAVLink 2)
   </strong>Dynamic data used to generate ADS-B out transponder data (send at 5Hz)</p>
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
     <td>utcTime</td>
     <td>uint32_t</td>
     <td>s</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>UTC time in seconds since GPS epoch (Jan 6, 1980). If unknown set to UINT32_MAX</td>
    </tr>
    <tr>
     <td>gpsLat</td>
     <td>int32_t</td>
     <td>degE7</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>Latitude WGS84 (deg * 1E7). If unknown set to INT32_MAX</td>
    </tr>
    <tr>
     <td>gpsLon</td>
     <td>int32_t</td>
     <td>degE7</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>Longitude WGS84 (deg * 1E7). If unknown set to INT32_MAX</td>
    </tr>
    <tr>
     <td>gpsAlt</td>
     <td>int32_t</td>
     <td>mm</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>Altitude (WGS84). UP +ve. If unknown set to INT32_MAX</td>
    </tr>
    <tr>
     <td>gpsFix</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX">UAVIONIX_ADSB_OUT_DYNAMIC_GPS_FIX</a>
     </td>
     <td>0-1: no fix, 2: 2D fix, 3: 3D fix, 4: DGPS, 5: RTK</td>
    </tr>
    <tr>
     <td>numSats</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>Number of satellites visible. If unknown set to UINT8_MAX</td>
    </tr>
    <tr>
     <td>baroAltMSL</td>
     <td>int32_t</td>
     <td>mbar</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>Barometric pressure altitude (MSL) relative to a standard atmosphere of 1013.2 mBar and NOT bar corrected altitude (m * 1E-3). (up +ve). If unknown set to INT32_MAX</td>
    </tr>
    <tr>
     <td>accuracyHor</td>
     <td>uint32_t</td>
     <td>mm</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>Horizontal accuracy in mm (m * 1E-3). If unknown set to UINT32_MAX</td>
    </tr>
    <tr>
     <td>accuracyVert</td>
     <td>uint16_t</td>
     <td>cm</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>Vertical accuracy in cm. If unknown set to UINT16_MAX</td>
    </tr>
    <tr>
     <td>accuracyVel</td>
     <td>uint16_t</td>
     <td>mm/s</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>Velocity accuracy in mm/s (m * 1E-3). If unknown set to UINT16_MAX</td>
    </tr>
    <tr>
     <td>velVert</td>
     <td>int16_t</td>
     <td>cm/s</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>GPS vertical speed in cm/s. If unknown set to INT16_MAX</td>
    </tr>
    <tr>
     <td>velNS</td>
     <td>int16_t</td>
     <td>cm/s</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>North-South velocity over ground in cm/s North +ve. If unknown set to INT16_MAX</td>
    </tr>
    <tr>
     <td>VelEW</td>
     <td>int16_t</td>
     <td>cm/s</td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>East-West velocity over ground in cm/s East +ve. If unknown set to INT16_MAX</td>
    </tr>
    <tr>
     <td>emergencyStatus</td>
     <td>uint8_t</td>
     <td>
     </td>
     <td>
      <a href="#UAVIONIX_ADSB_EMERGENCY_STATUS">UAVIONIX_ADSB_EMERGENCY_STATUS</a>
     </td>
     <td>Emergency status</td>
    </tr>
    <tr>
     <td>state</td>
     <td>uint16_t</td>
     <td>
     </td>
     <td>
      <a href="#UAVIONIX_ADSB_OUT_DYNAMIC_STATE">UAVIONIX_ADSB_OUT_DYNAMIC_STATE</a>
     </td>
     <td>ADS-B transponder dynamic input state flags</td>
    </tr>
    <tr>
     <td>squawk</td>
     <td>uint16_t</td>
     <td>
     </td>
     <td>
      <a href="#">
      </a>
     </td>
     <td>Mode A code (typically 1200 [0x04B0] for VFR)</td>
    </tr>
   </tbody>
  </table>
  <h3 id="UAVIONIX_ADSB_TRANSCEIVER_HEALTH_REPORT">UAVIONIX_ADSB_TRANSCEIVER_HEALTH_REPORT (<a href="#UAVIONIX_ADSB_TRANSCEIVER_HEALTH_REPORT">
    #10003
   </a>
   )
  </h3>
  <p>
   <strong>
    (MAVLink 2)
   </strong>Transceiver heartbeat with health report (updated every 10s)</p>
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
     <td>rfHealth</td>
     <td>uint8_t</td>
     <td>
      <a href="#UAVIONIX_ADSB_RF_HEALTH">UAVIONIX_ADSB_RF_HEALTH</a>
     </td>
     <td>ADS-B transponder messages</td>
    </tr>
   </tbody>
  </table>
 </body>
</html>