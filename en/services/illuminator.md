# Illuminator Protocol


## Introduction

The illuminator protocol allows MAVLink control over the behavior of lights, LEDs, and/or emitters mounted or integrated on the drone. 
The protocol currently allows for the following control: brightness, on/off, and a strobe feature.

Along with this, the illuminator protocol also publishes status information for developers or users. The status messaging encompasses the current configuration of the illuminator and the health of the illuminator device.
   

## Concepts

### MAVLink Illuminator Implementations

These illuminators have built-in MAVLink support:
- Skydio Spotlight

### Message/Enum Summary
| Message                                                                                 | Description                                                                                                                         |
| --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| <span id="COMPONENT_INFORMATION_BASIC"></span>[COMPONENT_INFORMATION_BASIC](../messages/common.md#COMPONENT_INFORMATION_BASIC) | Basic illuminator information data. Should be requested using MAV_CMD_REQUEST_MESSAGE on startup, or when required.|
| <span id="MAV_CMD_ILLUMINATOR_ON_OFF"></span>[MAV_CMD_ILLUMINATOR_ON_OFF](../messages/common.md#MAV_CMD_ILLUMINATOR_ON_OFF) | Turns illuminators ON/OFF. |
| <span id="MAV_CMD_DO_ILLUMINATOR_CONFIGURE"></span>[MAV_CMD_DO_ILLUMINATOR_CONFIGURE](../messages/common.md#MAV_CMD_DO_ILLUMINATOR_CONFIGURE) | Configures illuminator settings. |
| <span id="ILLUMINATOR_STATUS"></span>[ILLUMINATOR_STATUS](../messages/common.md#ILLUMINATOR_STATUS) | Current status of the illuminator. Recommended to publish this at a regular rate. |
| <span id="MAV_TYPE_ILLUMINATOR"></span>[MAV_TYPE_ILLUMINATOR](../messages/minimal.md#MAV_TYPE_ILLUMINATOR) | Type of the component (illuminator). |
| <span id="MAV_COMP_ID_ILLUMINATOR"></span>[MAV_COMP_ID_ILLUMINATOR](../messages/minimal.md#MAV_COMP_ID_ILLUMINATOR) | ID of the component (illuminator).  |

| Enum                                                                                             | Description               |
| ------------------------------------------------------------------------------------------------ | ------------------------- |
| <span id="ILLUMINATOR_MODE"></span>[ILLUMINATOR_MODE](../messages/common.md#ILLUMINATOR_MODE)    | Illuminator modes. |
| <span id="ILLUMINATOR_ERROR_FLAGS"></span>[ILLUMINATOR_ERROR_FLAGS](../messages/common.md#ILLUMINATOR_ERROR_FLAGS)    | Fault/health indications.             |


### Illuminator Connection

Illuminators are expected to follow the [Heartbeat/Connection Protocol](https://github.com/mavlink/mavlink-devguide/blob/master/en/services/heartbeat.md) and send a constant flow of heartbeats (nominally at 1Hz). Illuminators are distinguished via their unique component ID: [MAV_COMP_ID_ILLUMINATOR](#MAV_COMP_ID_ILLUMINATOR). Once a heartbeat is received, the drone can then send a REQUEST_MESSAGE command to the illuminator to receive information, set settings, or control the illuminator. An example below illustrates how a drone can request the status of the illuminator. 

<!-- Mermaid graph:
sequenceDiagram;
    participant Drone
    participant Illuminator
    Illuminator->>Drone: HEARTBEAT [cmp id: MAV_TYPE_ILLUMINATOR] (first) 
    Drone->>Illuminator: MAV_CMD_REQUEST_MESSAGE(param1=ILLUMINATOR_STATUS)
    Drone->>Drone: Start timeout
    Illuminator->>Drone: COMMAND_ACK
    Note over Illuminator,Drone: If MAV_RESULT_ACCEPTED send info.
    Illuminator->>Drone: ILLUMINATOR_STATUS [cmp id: MAV_COMP_ID_ILLUMINATOR]
-->
[![](https://mermaid.ink/img/pako:eNp9UWFLwzAQ_SshnxxMwa8VB7ENWly32aSCrBJCe9XgktQ0FcbYfzeuEzoGu0_Hy3sv7-52uLI14Ah38N2DqSBR8sNJfVcaFKqVzqtKtdJ4lDhr4BxON5teKyO9dcPjCLiezQ6qCD1RkvMHSjhaZ-QV-W0bwNAJ_raiIp3PiyxdEL7M39FVo1znJ2hwO-iDz8h1EMZZInL6UlDGRUYZI4_0KuSS-vZ-ZCcYJ7xgk1OzYyjmwxzIKw229xfCx8ssI4tEkPh5YC2sB2R_wI350yM7bQ75csqKOQ-amK44TVAHpkbKNPbmwk_nydG60i1S9XHoZbYSaXKysMEOT7EGp6WqwzF3f1iJ_SdoKHEU2lq6rxKXZh94sveWbU2FI-96mOK-raX_PzyOGrnpYP8LFgqu1A?type=png)](https://mermaid.live/edit#pako:eNp9UWFLwzAQ_SshnxxMwa8VB7ENWly32aSCrBJCe9XgktQ0FcbYfzeuEzoGu0_Hy3sv7-52uLI14Ah38N2DqSBR8sNJfVcaFKqVzqtKtdJ4lDhr4BxON5teKyO9dcPjCLiezQ6qCD1RkvMHSjhaZ-QV-W0bwNAJ_raiIp3PiyxdEL7M39FVo1znJ2hwO-iDz8h1EMZZInL6UlDGRUYZI4_0KuSS-vZ-ZCcYJ7xgk1OzYyjmwxzIKw229xfCx8ssI4tEkPh5YC2sB2R_wI350yM7bQ75csqKOQ-amK44TVAHpkbKNPbmwk_nydG60i1S9XHoZbYSaXKysMEOT7EGp6WqwzF3f1iJ_SdoKHEU2lq6rxKXZh94sveWbU2FI-96mOK-raX_PzyOGrnpYP8LFgqu1A)


## Implementation and Messages

#### COMPONENT\_INFORMATION\_BASIC
While the MAV\_TYPE and Component ID help identify the system and component, the [COMPONENT_INFORMATION_BASIC](#COMPONENT_INFORMATION_BASIC) command can be requested to retrieve component information data, which can help further identify the component being communicated with. This data includes time\_boot\_ms, MAV\_PROTOCOL\_CAPABILITY, vendor\_name, model\_name, software\_version, hardware\_version, and serial\_number.

| Parameter                     | Description                                                                                                    |
|-------------------------------|----------------------------------------------------------------------------------------------------------------|
| `time_boot_ms`                | Time since system boot up in milliseconds.                                                                     |
| `MAV_PROTOCOL_CAPABILITY`     | Bitmask detailing the component capability flags.                                                              |
| `vendor_name`                 | Name of the component vendor (optional).                                                                       |
| `model_name`                  | Name of the component's model (optional).                                                                      |
| `software_version`            | Software version on the module, recommended format is SEMVER: 'major.minor.patch' but any format can be used (24-character string) (optional).        |
| `hardware_version`            | Hardware version on the module, recommended format is SEMVER: 'major.minor.patch' but any format can be used (24-character string) (optional).              |
| `serial_number`               | Hardware's serial number (optional).                                                                           |


Optional parameters can be left empty or set to zero.
<!-- This blank line provides visual separation in the document -->
<!-- This blank line provides visual separation in the document -->
#### ON/OFF
The [MAV_CMD_ILLUMINATOR_ON_OFF](#MAV_CMD_ILLUMINATOR_ON_OFF) command is used to enable/disable the illuminator. It's usage can be seen below:
<!-- Mermaid graph:
sequenceDiagram;
    participant Drone
    participant Illuminator
    Drone->>Illuminator: MAV_CMD_ILLUMINATOR_ON_OFF (param1 = 1)
    Drone->>Drone: Start timeout
    Illuminator->>Drone: MAV_RESULT_ACCEPTED
-->
[![](https://mermaid.ink/img/pako:eNplkMFqwzAMhl_F6LRCd-jVZYWQpBBImtGkOxmMSLTNLLYzVz6M0nef2zLWMV0kpE__j3SCwY8EEo70GckNVBh8C2jXyokUMwY2g5nRsSiCd_S_XU1TtMYh-3AbXrnHzeZuIEWTvei8KXRV14em2mV9u9ftTrfbrXhIamhX4kmsFn8VrlmKjpOdYGPJR74Rd9q_3MVjX3aHutdZnpfPfVnAEiwFi2ZMJ54uuwr4nSwpkKkcMXwoUO6cOIzsuy83gOQQaQlxHpF_3gHyFacjnb8BIBNkuQ?type=png)](https://mermaid.live/edit#pako:eNplkMFqwzAMhl_F6LRCd-jVZYWQpBBImtGkOxmMSLTNLLYzVz6M0nef2zLWMV0kpE__j3SCwY8EEo70GckNVBh8C2jXyokUMwY2g5nRsSiCd_S_XU1TtMYh-3AbXrnHzeZuIEWTvei8KXRV14em2mV9u9ftTrfbrXhIamhX4kmsFn8VrlmKjpOdYGPJR74Rd9q_3MVjX3aHutdZnpfPfVnAEiwFi2ZMJ54uuwr4nSwpkKkcMXwoUO6cOIzsuy83gOQQaQlxHpF_3gHyFacjnb8BIBNkuQ)
<!-- This blank line provides visual separation in the document -->
<!-- This blank line provides visual separation in the document -->
#### CONFIGURE
The [MAV_CMD_DO_ILLUMINATOR_CONFIGURE](#MAV_CMD_DO_ILLUMINATOR_CONFIGURE) command controls the illuminator's settings. This will adjust how the illuminator behaves when enabled. The operation follows the normal [Command Protocol](https://github.com/mavlink/mavlink-devguide/blob/master/en/services/command.md) rules for command/acknowledgment. The four parameters for this command are: Mode, Brightness, Strobe Period, Strobe Duty. 

Illuminators can be set in different modes which can change the behavior of the illuminator (described in a separate section, [Modes](#MODES) section. The brightness can be set via "Brightness" as a percentage value (0-100%). Illuminators may also have the functionality to strobe the light source. This behavior is configured via "Strobe Period" and "Strobe Duty". These parameters can be set to 0 when not used. "Strobe Period" is in seconds and "Strobe Duty" is a percentage value (indicating the % of time in the "Strobe Period" the illuminator is enabled).
<!-- This blank line provides visual separation in the document -->
<!-- This blank line provides visual separation in the document -->
##### MODES
Illuminator modes can help the drone configure the interaction behavior of the illuminator. 

If the mode is unknown, the mode parameter value will be set to 0. 

The mode value as 1 indicates ILLUMINATOR\_MODE\_INTERNAL\_CONTROL where the illuminator behavior is controlled by [MAV_CMD_DO_ILLUMINATOR_CONFIGURE](#MAV_CMD_DO_ILLUMINATOR_CONFIGURE) settings. 

When the value is set to 2, it indicates that the illuminator mode is ILLUMINATOR\_MODE\_EXTERNAL\_SYNC. This mode is for instances where the illuminator behavior is controlled by external factors: e.g. an external hardware signal.
<!-- This blank line provides visual separation in the document -->
<!-- This blank line provides visual separation in the document -->
##### STATUS
The [ILLUMINATOR_STATUS](#ILLUMINATOR_STATUS) message can be requested to receive information about the status of the illuminator. This includes information such as uptime, errors, whether the illuminator is enabled via [MAV_CMD_ILLUMINATOR_ON_OFF](#MAV_CMD_ILLUMINATOR_ON_OFF), current settings from the [MAV_CMD_DO_ILLUMINATOR_CONFIGURE](#MAV_CMD_DO_ILLUMINATOR_CONFIGURE) command, and temperature of the illuminator. 
<!-- This blank line provides visual separation in the document -->
<!-- This blank line provides visual separation in the document -->
##### ILLUMINATOR\_ERROR\_FLAGS
The [ILLUMINATOR_ERROR_FLAGS](#ILLUMINATOR_ERROR_FLAGS) can be used to indicate if there is any issue with the illuminator. At this time, there are three flags. If there is no error and the illuminator is behaving as normal, the ILLUMINATOR\_ERROR\_FLAGS bitmap will be 0. If ILLUMINATOR\_ERROR\_FLAGS is set to 1 or 2, this indicates an error related to the temperature of the illuminator. 

"1" indicates ILLUMINATOR\_ERROR\_FLAGS\_THERMAL\_THROTTLING as in the illuminator is throttling its output due to a thermal issue. "2" indicates ILLUMINATOR\_ERROR\_FLAGS\_OVER\_TEMPERATURE\_SHUTDOWN which means that the illuminator is shutting off due to passing some temperature threshold. 

The status message utilization can be seen below:

<!-- Mermaid graph:
    sequenceDiagram;
        participant Drone
        participant Illuminator
        Drone->>Illuminator: MAV_CMD_REQUEST_MESSAGE(param1=ILLUMINATOR_STATUS)
        Drone->>Drone: Start timeout
        Illuminator->>Drone: MAV_RESULT_ACCEPTED
        Illuminator->>Drone: ILLUMINATOR_STATUS [(50000.0, 1, 1, 1, 1, 80.0, 0.0, 0.0, 95.0, 0.0, 10.0)]
        Note over Illuminator, Drone: Illuminator Status published as: <br> uptime_ms = 50000.0, enable = 1, mode_bitmask = 1 <br> error_status = 1, mode = 1, brightness = 80% <br> strobe_period = 0.0, strobe_duty_cycle = 0.0, temp_c = 95.0 <br>min_strobe_period = 0.0, max_strobe_period = 10.0
        
-->
[![](https://mermaid.ink/img/pako:eNqFUm1rwjAQ_ishMHDghn4Qtm4KRcsQdC-27ss6QtreZrBJuuQyJmP_fWmdVlDYEdLLPc_dc5fmm-a6ABpQ4s3ChwOVw0Twd8PlTarIn1XcoMhFxRWSidEKTkPTsnRSKI7atISGfzEaHYABmYfPbDyfsEX0tIzihM2jOA7voo6vxmV_OJ3NlvPpfZg8LFichMkyPj8u2HwDEqPvgKCQoB22rAO5llvLLqJ4OUtYOB5Hj0k0-SfjuBPy0hn0vF32uqR_sK6aSLtdD_Zu3-_nr63SvUYg-hPMoWaX7CTbWD0cOksql5XCrqAg3AbkNjMj4qp6ZCYtGZJ9P6B4VoKP-H6k_7EsEyi5XdeRbRoYow2z27J73tbLjHhfoQJbI1e9s22GRaMzYBUYoQsPNEJ_wcLhhuWbvNFsAARZsdyf6vGbAn4UdrKG5F9HQH1TtEslGMlF4d_ld31rKcUVSEhp4N2Cm3VKU_XjedyhjjcqpwEaB13qqoLj7v3S4I2XFn5-AbUw5Hc?type=png)](https://mermaid.live/edit#pako:eNqFUm1rwjAQ_ishMHDghn4Qtm4KRcsQdC-27ss6QtreZrBJuuQyJmP_fWmdVlDYEdLLPc_dc5fmm-a6ABpQ4s3ChwOVw0Twd8PlTarIn1XcoMhFxRWSidEKTkPTsnRSKI7atISGfzEaHYABmYfPbDyfsEX0tIzihM2jOA7voo6vxmV_OJ3NlvPpfZg8LFichMkyPj8u2HwDEqPvgKCQoB22rAO5llvLLqJ4OUtYOB5Hj0k0-SfjuBPy0hn0vF32uqR_sK6aSLtdD_Zu3-_nr63SvUYg-hPMoWaX7CTbWD0cOksql5XCrqAg3AbkNjMj4qp6ZCYtGZJ9P6B4VoKP-H6k_7EsEyi5XdeRbRoYow2z27J73tbLjHhfoQJbI1e9s22GRaMzYBUYoQsPNEJ_wcLhhuWbvNFsAARZsdyf6vGbAn4UdrKG5F9HQH1TtEslGMlF4d_ld31rKcUVSEhp4N2Cm3VKU_XjedyhjjcqpwEaB13qqoLj7v3S4I2XFn5-AbUw5Hc)
<!-- This blank line provides visual separation in the document -->
<!-- This blank line provides visual separation in the document -->
## Test Script

#### Description
The test suite included in illuminator.py allows for testing both sides of the illuminator interaction. The first script `illuminator.py` will emulate a standard illuminator module. The second script will run a standard test suite against the emulator, testing all commands listed in this document.


##### Instructions
1. Run simple illuminator emulator `python3 illuminator.py`
2. Run test `python3 -m unittest -v test_illuminator.py`