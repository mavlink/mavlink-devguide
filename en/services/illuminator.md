# Illuminator Protocol

The illuminator protocol allows MAVLink control over the behaviour of lights, LEDs, and/or emitters mounted or integrated on the drone.
The protocol currently allows for the following control: brightness, on/off, and a strobe feature.

Along with this, the illuminator protocol also publishes status information for developers or users.
The status messaging encompasses the current configuration of the illuminator and the health of the illuminator device.

## MAVLink Illuminator Implementations

These illuminators have built-in MAVLink support:

- Skydio Spotlight for X10

## Message/Command/Enum Summary

| Message                                                                                       | Description                                                                                                                                    |
| --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| <a id="COMPONENT_INFORMATION_BASIC"></a>[COMPONENT_INFORMATION_BASIC][CMPNT_INFO_BSC]         | Basic illuminator information data. Should be requested using [MAV_CMD_REQUEST_MESSAGE][MAV_CMD_REQUEST_MESSAGE] on startup, or when required. |
| <a id="ILLUMINATOR_STATUS"></a>[ILLUMINATOR_STATUS](../messages/common.md#ILLUMINATOR_STATUS) | Current status of the illuminator. Recommended to publish this at a regular rate.                                                              |

| Command                                                                                       | Description                      |
| --------------------------------------------------------------------------------------------- | -------------------------------- |
| <a id="MAV_CMD_ILLUMINATOR_ON_OFF"></a>[MAV_CMD_ILLUMINATOR_ON_OFF][ILLUM_ON_OFF]             | Turns illuminators ON/OFF.       |
| <a id="MAV_CMD_DO_ILLUMINATOR_CONFIGURE"></a>[MAV_CMD_DO_ILLUMINATOR_CONFIGURE][DO_ILLM_CNFG] | Configures illuminator settings. |

<!-- reference links to make table above easier to edit -->

[DO_ILLM_CNFG]: ../messages/common.md#MAV_CMD_DO_ILLUMINATOR_CONFIGURE
[MAV_CMD_REQUEST_MESSAGE]: ../messages/common.md#MAV_CMD_REQUEST_MESSAGE
[CMPNT_INFO_BSC]: ../messages/common.md#COMPONENT_INFORMATION_BASIC
[ILLUM_ON_OFF]: ../messages/common.md#MAV_CMD_ILLUMINATOR_ON_OFF

| Enum Values                                                                                                   | Description                          |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| <a id="MAV_TYPE_ILLUMINATOR"></a>[MAV_TYPE_ILLUMINATOR](../messages/minimal.md#MAV_TYPE_ILLUMINATOR)          | Type of the component (illuminator). |
| <a id="MAV_COMP_ID_ILLUMINATOR"></a>[MAV_COMP_ID_ILLUMINATOR](../messages/minimal.md#MAV_COMP_ID_ILLUMINATOR) | ID of the component (illuminator).   |

| Enum                                                                                                         | Description               |
| ------------------------------------------------------------------------------------------------------------ | ------------------------- |
| <a id="ILLUMINATOR_MODE"></a>[ILLUMINATOR_MODE](../messages/common.md#ILLUMINATOR_MODE)                      | Illuminator modes.        |
| <a id="ILLUMINATOR_ERROR_FLAGS"></a>[ILLUMINATOR_ERROR_FLAGS](../messages/common.md#ILLUMINATOR_ERROR_FLAGS) | Fault/health indications. |

## Implementation and Messages

### Illuminator Connection

Illuminators are expected to follow the [Heartbeat/Connection Protocol](../services/heartbeat.md) and send a constant flow of heartbeats (nominally at 1Hz).
Illuminators are identified via their type [MAV_TYPE_ILLUMINATOR](#MAV_TYPE_ILLUMINATOR).
Individual illuminators are distinguished via their unique component ID, which by default should be [MAV_COMP_ID_ILLUMINATOR](#MAV_COMP_ID_ILLUMINATOR) (though this is not mandated and any ID may be used).
Once a heartbeat is received, the drone can then send a [MAV_CMD_REQUEST_MESSAGE ][MAV_CMD_REQUEST_MESSAGE] command to the illuminator to receive information, set settings, or control the illuminator.
An example below illustrates how a drone can request the status of the illuminator.

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

### COMPONENT_INFORMATION_BASIC

While the `MAV_TYPE` and Component ID help identify the system and component, the [COMPONENT_INFORMATION_BASIC](#COMPONENT_INFORMATION_BASIC) command can be requested to retrieve component information data, which can help further identify the component being communicated with. This data includes `time_boot_ms`, `MAV_PROTOCOL_CAPABILITY`, `vendor_name`, `model_name`, `software_version`, `hardware_version`, and `serial_number`.

| Parameter                 | Description                                                                                                                                    |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `time_boot_ms`            | Time since system boot up in milliseconds.                                                                                                     |
| `MAV_PROTOCOL_CAPABILITY` | Bitmask detailing the component capability flags.                                                                                              |
| `vendor_name`             | Name of the component vendor (optional).                                                                                                       |
| `model_name`              | Name of the component's model (optional).                                                                                                      |
| `software_version`        | Software version on the module, recommended format is SEMVER: 'major.minor.patch' but any format can be used (24-character string) (optional). |
| `hardware_version`        | Hardware version on the module, recommended format is SEMVER: 'major.minor.patch' but any format can be used (24-character string) (optional). |
| `serial_number`           | Hardware's serial number (optional).                                                                                                           |

Optional parameters can be left empty or set to zero.

### ON/OFF

The [MAV_CMD_ILLUMINATOR_ON_OFF](#MAV_CMD_ILLUMINATOR_ON_OFF) command is used to enable/disable the illuminator.
It's usage can be seen below:

<!-- Mermaid graph:
sequenceDiagram;
    participant Drone
    participant Illuminator
    Drone->>Illuminator: MAV_CMD_ILLUMINATOR_ON_OFF (param1 = 1)
    Drone->>Drone: Start timeout
    Illuminator->>Drone: MAV_RESULT_ACCEPTED
-->

[![](https://mermaid.ink/img/pako:eNplkMFqwzAMhl_F6LRCd-jVZYWQpBBImtGkOxmMSLTNLLYzVz6M0nef2zLWMV0kpE__j3SCwY8EEo70GckNVBh8C2jXyokUMwY2g5nRsSiCd_S_XU1TtMYh-3AbXrnHzeZuIEWTvei8KXRV14em2mV9u9ftTrfbrXhIamhX4kmsFn8VrlmKjpOdYGPJR74Rd9q_3MVjX3aHutdZnpfPfVnAEiwFi2ZMJ54uuwr4nSwpkKkcMXwoUO6cOIzsuy83gOQQaQlxHpF_3gHyFacjnb8BIBNkuQ?type=png)](https://mermaid.live/edit#pako:eNplkMFqwzAMhl_F6LRCd-jVZYWQpBBImtGkOxmMSLTNLLYzVz6M0nef2zLWMV0kpE__j3SCwY8EEo70GckNVBh8C2jXyokUMwY2g5nRsSiCd_S_XU1TtMYh-3AbXrnHzeZuIEWTvei8KXRV14em2mV9u9ftTrfbrXhIamhX4kmsFn8VrlmKjpOdYGPJR74Rd9q_3MVjX3aHutdZnpfPfVnAEiwFi2ZMJ54uuwr4nSwpkKkcMXwoUO6cOIzsuy83gOQQaQlxHpF_3gHyFacjnb8BIBNkuQ)

### CONFIGURE

The [MAV_CMD_DO_ILLUMINATOR_CONFIGURE](#MAV_CMD_DO_ILLUMINATOR_CONFIGURE) command controls the illuminator's settings. This will adjust how the illuminator behaves when enabled.
The operation follows the normal [Command Protocol](../services/command.md) rules for command/acknowledgment. The four parameters for this command are: Mode, Brightness, Strobe Period, Strobe Duty.

Illuminators can be set in different modes which can change the behavior of the illuminator (described in a separate section, [Modes](#MODES)).
The brightness can be set via "Brightness" as a percentage value (0-100%).
Illuminators may also have the functionality to strobe the light source.
This behavior is configured via "Strobe Period" and "Strobe Duty".
These parameters can be set to `0` when not used.
"Strobe Period" is in seconds and "Strobe Duty" is a percentage value (indicating the % of time in the "Strobe Period" the illuminator is enabled).

#### MODES

If the mode is unknown, the mode parameter value will be set to 0.

A mode value of 1 is `ILLUMINATOR_MODE_INTERNAL_CONTROL`, where the illuminator behavior is controlled by [MAV_CMD_DO_ILLUMINATOR_CONFIGURE](#MAV_CMD_DO_ILLUMINATOR_CONFIGURE) settings.

When the value is set to 2, it indicates that the illuminator mode is `ILLUMINATOR_MODE_EXTERNAL_SYNC`. This mode is for instances where the illuminator behavior is controlled by external factors: e.g. an external hardware signal.

### STATUS

The [ILLUMINATOR_STATUS](#ILLUMINATOR_STATUS) message can be requested to receive information about the status of the illuminator. This includes information such as uptime, errors, whether the illuminator is enabled via [MAV_CMD_ILLUMINATOR_ON_OFF](#MAV_CMD_ILLUMINATOR_ON_OFF), current settings from the [MAV_CMD_DO_ILLUMINATOR_CONFIGURE](#MAV_CMD_DO_ILLUMINATOR_CONFIGURE) command, and the temperature of the illuminator.

#### ILLUMINATOR_ERROR_FLAGS

The [ILLUMINATOR_ERROR_FLAGS](#ILLUMINATOR_ERROR_FLAGS) can be used to indicate if there is any issue with the illuminator. At this time, there are three flags. If there is no error and the illuminator is behaving as normal, the [ILLUMINATOR_ERROR_FLAGS](#ILLUMINATOR_ERROR_FLAGS) bitmap will be 0.
If [ILLUMINATOR_ERROR_FLAGS](#ILLUMINATOR_ERROR_FLAGS) is set to 1 or 2, this indicates an error related to the temperature of the illuminator.

`1` indicates `ILLUMINATOR_ERROR_FLAGS_THERMAL_THROTTLING` as in the illuminator is throttling its output due to a thermal issue.
`2` indicates `ILLUMINATOR_ERROR_FLAGS_OVER_TEMPERATURE_SHUTDOWN` which means that the illuminator is shutting off due to passing some temperature threshold.

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

## Test Script

### Description

The test suite included in [assets/services/illuminators](https://github.com/mavlink/mavlink-devguide/blob/master/assets/services/illuminators/) allows for testing both sides of the illuminator interaction.

- [illuminator.py](https://github.com/mavlink/mavlink-devguide/blob/master/assets/services/illuminators/illuminator.py) emulates a standard illuminator module.
- [test_illuminator.py](https://github.com/mavlink/mavlink-devguide/blob/master/assets/services/illuminators/test_illuminator.py) runs a standard test suite against the emulator, testing all commands listed in this document.

### Instructions

1. Run simple illuminator emulator `python3 illuminator.py`
2. Run test `python3 -m unittest -v test_illuminator.py`
