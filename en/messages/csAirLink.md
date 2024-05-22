<!-- THIS FILE IS AUTO-GENERATED: https://github.com/mavlink/mavlink/blob/master/doc/mavlink_xml_to_markdown.py -->


# Dialect: csAirLink

*This is a human-readable form of the XML definition file: [csAirLink](https://github.com/mavlink/mavlink/blob/master/message_definitions/v1.0/csAirLink).*

<span id="mav2_extension_field"></span>

> **Note**
> - MAVLink 2 [extension fields](../guide/define_xml_element.md#message_extensions) are displayed in blue.
> - Entities from dialects are displayed only as headings (with link to original)

<style>
span.ext {
    color: blue;
  }
span.warning {
    color: red;
  }
</style>
**Protocol version:** 3

## MAVLink Include Files

 None

## Summary

Type | Defined | Included
--- | --- | ---
[Messages](#messages) | 6 | 0
[Enums](#enumerated-types) | 5 | 0
Commands | 0 | 0

The following sections list all entities in the dialect (both included and defined in this file).

## Messages

### AIRLINK_AUTH (52000) {#AIRLINK_AUTH}

Authorization package

Field Name | Type | Description
--- | --- | ---
login | `char[50]` | Login 
password | `char[50]` | Password 


### AIRLINK_AUTH_RESPONSE (52001) {#AIRLINK_AUTH_RESPONSE}

Response to the authorization request

Field Name | Type | Values | Description
--- | --- | --- | ---
resp_type | `uint8_t` | [AIRLINK_AUTH_RESPONSE_TYPE](#AIRLINK_AUTH_RESPONSE_TYPE) | Response type 


### AIRLINK_EYE_GS_HOLE_PUSH_REQUEST (52002) {#AIRLINK_EYE_GS_HOLE_PUSH_REQUEST}

Request to hole punching

Field Name | Type | Values | Description
--- | --- | --- | ---
resp_type | `uint8_t` | [AIRLINK_EYE_GS_HOLE_PUSH_RESP_TYPE](#AIRLINK_EYE_GS_HOLE_PUSH_RESP_TYPE) | Hole push response type 


### AIRLINK_EYE_GS_HOLE_PUSH_RESPONSE (52003) {#AIRLINK_EYE_GS_HOLE_PUSH_RESPONSE}

Response information about the connected device

Field Name | Type | Values | Description
--- | --- | --- | ---
resp_type | `uint8_t` | [AIRLINK_EYE_GS_HOLE_PUSH_RESP_TYPE](#AIRLINK_EYE_GS_HOLE_PUSH_RESP_TYPE) | Hole push response type 
ip_version | `uint8_t` | [AIRLINK_EYE_IP_VERSION](#AIRLINK_EYE_IP_VERSION) | ip version 
ip_address_4 | `uint8_t[4]` | | ip 4 address 
ip_address_6 | `uint8_t[16]` | | ip 6 address 
ip_port | `uint32_t` | | port 


### AIRLINK_EYE_HP (52004) {#AIRLINK_EYE_HP}

A package with information about the hole punching status. It is used for constant sending to avoid NAT closing timeout.

Field Name | Type | Values | Description
--- | --- | --- | ---
resp_type | `uint8_t` | [AIRLINK_EYE_HOLE_PUSH_TYPE](#AIRLINK_EYE_HOLE_PUSH_TYPE) | Hole push response type 


### AIRLINK_EYE_TURN_INIT (52005) {#AIRLINK_EYE_TURN_INIT}

Initializing the TURN protocol

Field Name | Type | Values | Description
--- | --- | --- | ---
resp_type | `uint8_t` | [AIRLINK_EYE_TURN_INIT_TYPE](#AIRLINK_EYE_TURN_INIT_TYPE) | Turn init type 


## Enumerated Types

### AIRLINK_AUTH_RESPONSE_TYPE {#AIRLINK_AUTH_RESPONSE_TYPE}

Value | Name | Description
--- | --- | ---
<a id='AIRLINK_ERROR_LOGIN_OR_PASS'></a>0 | [AIRLINK_ERROR_LOGIN_OR_PASS](#AIRLINK_ERROR_LOGIN_OR_PASS) | Login or password error 
<a id='AIRLINK_AUTH_OK'></a>1 | [AIRLINK_AUTH_OK](#AIRLINK_AUTH_OK) | Auth successful 

### AIRLINK_EYE_GS_HOLE_PUSH_RESP_TYPE {#AIRLINK_EYE_GS_HOLE_PUSH_RESP_TYPE}

Value | Name | Description
--- | --- | ---
<a id='AIRLINK_HPR_PARTNER_NOT_READY'></a>0 | [AIRLINK_HPR_PARTNER_NOT_READY](#AIRLINK_HPR_PARTNER_NOT_READY) |  
<a id='AIRLINK_HPR_PARTNER_READY'></a>1 | [AIRLINK_HPR_PARTNER_READY](#AIRLINK_HPR_PARTNER_READY) |  

### AIRLINK_EYE_IP_VERSION {#AIRLINK_EYE_IP_VERSION}

Value | Name | Description
--- | --- | ---
<a id='AIRLINK_IP_V4'></a>0 | [AIRLINK_IP_V4](#AIRLINK_IP_V4) |  
<a id='AIRLINK_IP_V6'></a>1 | [AIRLINK_IP_V6](#AIRLINK_IP_V6) |  

### AIRLINK_EYE_HOLE_PUSH_TYPE {#AIRLINK_EYE_HOLE_PUSH_TYPE}

Value | Name | Description
--- | --- | ---
<a id='AIRLINK_HP_NOT_PENETRATED'></a>0 | [AIRLINK_HP_NOT_PENETRATED](#AIRLINK_HP_NOT_PENETRATED) |  
<a id='AIRLINK_HP_BROKEN'></a>1 | [AIRLINK_HP_BROKEN](#AIRLINK_HP_BROKEN) |  

### AIRLINK_EYE_TURN_INIT_TYPE {#AIRLINK_EYE_TURN_INIT_TYPE}

Value | Name | Description
--- | --- | ---
<a id='AIRLINK_TURN_INIT_START'></a>0 | [AIRLINK_TURN_INIT_START](#AIRLINK_TURN_INIT_START) |  
<a id='AIRLINK_TURN_INIT_OK'></a>1 | [AIRLINK_TURN_INIT_OK](#AIRLINK_TURN_INIT_OK) |  
<a id='AIRLINK_TURN_INIT_BAD'></a>2 | [AIRLINK_TURN_INIT_BAD](#AIRLINK_TURN_INIT_BAD) |  

