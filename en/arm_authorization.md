# Arm authorization

When enabled by setting a parameter on flight stack, the drone will only arm the motors if authorized by a external entity.
This external entity is reposible to request any information that it need from the drone and from other souces(example: weather) and authorize or not the arm procedure.

This will be useful to comply to NASA UTM (https://utm.arc.nasa.gov/) but can also be useful for private companies.

## Authorization flow

{% mermaid %}
sequenceDiagram;
    participant Drone
    participant Remote control/QCS
    participant Arm authorizer
    participant Internet

    Remote control/QCS->>Drone: Request arm
    Drone->>Arm authorizer: COMMAND_LONG command=MAV_CMD_ARM_AUTHORIZATION_REQUEST
    Arm authorizer->>Drone: COMMAND_ACK result=MAV_RESULT_IN_PROGRESS
    Arm authorizer->>Drone: (optional)Request information about mission, battery level and etc.
    Arm authorizer->>Internet: (optional)Request information about weather, aerospace trafic and etc.
    Arm authorizer->>Drone: COMMAND_ACK command=MAV_CMD_ARM_AUTHORIZATION_REQUEST result=ACCEPTED, TEMPORARILY_REJECTED or DENIED
    Drone->>Remote control/QCS: QCS COMMAND_ACK command=MAV_CMD_COMPONENT_ARM_DISARM result=ACCEPTED, TEMPORARILY_REJECTED or DENIED
{% endmermaid %}

In case the authorizer need a lot of time to get and process the information is better have another authorization flow to avoid arm the drone at unexpected time.
{% mermaid %}
sequenceDiagram;
    participant Drone
    participant Remote control/QCS
    participant Arm authorizer
    participant Internet

    Remote control/QCS->>Drone: Request arm1
    Drone->>Remote control/QCS: QCS COMMAND_ACK result=TEMPORARILY_REJECTED
    Drone->>Arm authorizer: COMMAND_LONG command=MAV_CMD_ARM_AUTHORIZATION_REQUEST
    Arm authorizer->>Drone: COMMAND_ACK result=MAV_RESULT_IN_PROGRESS
    Arm authorizer->>Drone: (optional)Request information about mission, battery level and etc.
    Arm authorizer->>Internet: (optional)Request information about weather, aerospace trafic and etc.
    Arm authorizer->>Drone: COMMAND_ACK command=MAV_CMD_ARM_AUTHORIZATION_REQUEST result=ACCEPTED, TEMPORARILY_REJECTED or DENIED
    Drone->>Remote control/QCS: QCS STATUSTEXT text=Arm authorization was approved or denied

    Remote control/QCS->>Drone: Request arm2
    Drone->>Remote control/QCS: QCS COMMAND_ACK command=MAV_CMD_COMPONENT_ARM_DISARM result=ACCEPTED, TEMPORARILY_REJECTED or DENIED
{% endmermaid %}

## Message parameters:

COMMAND_LONG
```
	command=MAV_CMD_ARM_AUTHORIZATION_REQUEST
	target_system=system id of arm authorizer
	target_component=component id of arm authorizer
```

COMMAND_ACK
```
	command=MAV_CMD_ARM_AUTHORIZATION_REQUEST
	result=ACCEPTED, TEMPORARILY_REJECTED or DENIED
	progress/result_param1=if result is TEMPORARILY_REJECTED or DENIED the reason should be set MAV_ARM_AUTH_DENIED_REASON otherwise it should be set as 0
	result_param2=if result is ACCEPTED the it should be set with the time in seconds that this authorization is valid otherwise an aditional information about why it was denied should be set. example: for result_param1=MAV_ARM_AUTH_DENIED_REASON_INVALID_WAYPOINT or MAV_ARM_AUTH_DENIED_REASON_AIRSPACE_IN_USE it may have the index of the waypoint that caused it to be denied.
	target_system=system id of the drone
	target_component=component id of the drone
```







