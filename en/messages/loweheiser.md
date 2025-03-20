<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->

# Dialect: loweheiser

::: warning
This topic documents the version of the dialect file in the [mavlink/mavlink](https://github.com/mavlink/mavlink) Github repository, which may not be up to date with the file in the source repository (it is up to the dialect owner to push changes when needed).
The source repo should be listed in the comments at the top of the XML definition file listed below (but may not be).
:::

This topic is a human-readable form of the XML definition file: [loweheiser.xml](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/loweheiser.xml).

<span id="mav2_extension_field"></span>

::: info

- MAVLink 2 [extension fields](../guide/define_xml_element.md#message_extensions) are displayed in blue.
- Entities from dialects are displayed only as headings (with link to original)

:::

<style>
span.ext {
    color: blue;
  }
span.warning {
    color: red;
  }
</style>
## MAVLink Include Files

- [minimal.xml](../messages/minimal.md)

## Summary

Type | Defined | Included
--- | --- | ---
[Messages](#messages) | 1 | 2
[Enums](#enumerated-types) | 0 | 6
[Commands](#mav_commands) | 1 | 0

The following sections list all entities in the dialect (both included and defined in this file).

## Messages

### LOWEHEISER_GOV_EFI (10151) {#LOWEHEISER_GOV_EFI}

Composite EFI and Governor data from Loweheiser equipment.  This message is created by the EFI unit based on its own data and data received from a governor attached to that EFI unit.

Field Name | Type | Units | Description
--- | --- | --- | ---
volt_batt | `float` | V | Generator Battery voltage. 
curr_batt | `float` | A | Generator Battery current. 
curr_gen | `float` | A | Current being produced by generator. 
curr_rot | `float` | A | Load current being consumed by the UAV (sum of curr_gen and curr_batt) 
fuel_level | `float` | l | Generator fuel remaining in litres. 
throttle | `float` | % | Throttle Output. 
runtime | `uint32_t` | s | Seconds this generator has run since it was rebooted. 
until_maintenance | `int32_t` | s | Seconds until this generator requires maintenance.  A negative value indicates maintenance is past due. 
rectifier_temp | `float` | degC | The Temperature of the rectifier. 
generator_temp | `float` | degC | The temperature of the mechanical motor, fuel cell core or generator. 
efi_batt | `float` | V | EFI Supply Voltage. 
efi_rpm | `float` | rpm | Motor RPM. 
efi_pw | `float` | ms | Injector pulse-width in miliseconds. 
efi_fuel_flow | `float` | | Fuel flow rate in litres/hour. 
efi_fuel_consumed | `float` | l | Fuel consumed. 
efi_baro | `float` | kPa | Atmospheric pressure. 
efi_mat | `float` | degC | Manifold Air Temperature. 
efi_clt | `float` | degC | Cylinder Head Temperature. 
efi_tps | `float` | % | Throttle Position. 
efi_exhaust_gas_temperature | `float` | degC | Exhaust gas temperature. 
efi_index | `uint8_t` | | EFI index.<br>Messages with same value are from the same source (instance). 
generator_status | `uint16_t` | | Generator status. 
efi_status | `uint16_t` | | EFI status. 


## Enumerated Types

## Commands (MAV_CMD) {#mav_commands}

### MAV_CMD_LOWEHEISER_SET_STATE (10151) {#MAV_CMD_LOWEHEISER_SET_STATE}

Set Loweheiser desired states

Param (Label) | Description
--- | ---
1 | EFI Index 
2 | Desired Engine/EFI State (0: Power Off, 1:Running) 
3 | Desired Governor State (0:manual throttle, 1:Governed throttle) 
4 | Manual throttle level, 0% - 100% 
5 | Electronic Start up (0:Off, 1:On) 
6 | Empty 
7 | Empty 


