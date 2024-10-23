# Multi GCS protocol
## Introduction
A controlled vehicle should only accept MAVLink commands (or command-like messages) that are sent by the controlling GCS, or from other components with the same system id. Commands from other system should be rejected with [MAV_RESULT_PERMISSION_DENIED](../messages/common.md#MAV_RESULT_PERMISSION_DENIED) (except for this command, which may be acknowledged with [MAV_RESULT_ACCEPTED](../messages/common.md#MAV_RESULT_ACCEPTED) if control is granted).

The command is sent by a GCS to the autopilot component to request or release control of a system, specifying whether subsequent takeover requests from another GCS are automatically granted, or require permission.
The autopilot should grant control to the GCS if the system does not require takeover permission (or is uncontrolled) and ACK the request with MAV_RESULT_ACCEPTED.

The autopilot should stream CONTROL_STATUS indicating its controlling system: all other components with the same system id should monitor this message and set their own owner to match that of the autopilot.
If the autopilot cannot grant control (because takeover requires permission), the request should be rejected with MAV_RESULT_PERMISSION_DENIED.

The autopilot should then send this same command to the current owning GCS in order to notify of the request.
The owning GCS would ACK with MAV_RESULT_ACCEPTED, and might choose to release ownership of the vehicle, or re-request ownership with the takeover bit set to allow permission. 

Note that the pilots of both GCS should co-ordinate safe handover offline.
It is also possible for a GCS to request control of a specific component rather than the whole system (though this is not recommended).
In this case the command should be sent to the specific component, which should also emit CONTROL_STATUS to indicate its owner (this component would ignore the CONTROL_STATUS set by the autopilot).
The flow is otherwise the same.

### Multi GCS protocol messages

This is the set of messages and commands used on this protocol.

| Message                                                                                                                                    | Description                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <a id="CONTROL_STATUS"></a>[CONTROL_STATUS](../messages/development.md#CONTROL_STATUS)                      | Information about GCS in control of this MAV. This should be broadcast at low rate (nominally 1 Hz) and emitted when ownership or takeover status change. Control over MAV is requested using MAV_CMD_REQUEST_OPERATOR_CONTROL.                                                                                                                                           |

| Command                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <a id="MAV_CMD_REQUEST_OPERATOR_CONTROL"></a>[MAV_CMD_REQUEST_OPERATOR_CONTROL](../messages/development.md#MAV_CMD_REQUEST_OPERATOR_CONTROL)                                                       | Request control of a system.                                                                                                            

### Workflow diagrams
Diagram 1 - 2 GCS, one of them asks for control without enforcing being asked before other GCS takes over (MAV_CMD_REQUEST_OPERATOR_CONTROL param 3 = 1)

<!-- Mermaid graph:
sequenceDiagram;
    participant GCS - 253
    participant Vehicle - 1
    participant GCS - 250
    note over Vehicle - 1: Broadcast CONTROL_STATUS: Nobody in control <br> - Sysid In control: 0
    Vehicle - 1->>GCS - 253: CONTROL_STATUS <br> - sysid_in_control: 0
    Vehicle - 1->>GCS - 250: CONTROL_STATUS <br> - sysid_in_control: 0 
    Note over GCS - 253: GCS 253 wants to request control <br> not enforcing asking for takeover
    GCS - 253->>Vehicle - 1: MAV_CMD_REQUEST_OPERATOR_CONTROL: <br> - param 1: 0 (Sysid requesting control not needed, can be deducted from sender) <br> - param 2: 1 (request control) <br> - param 3: 1 (allow automatic takeover)
    Vehicle - 1->>GCS - 253: COMMAND_ACK
    Note over Vehicle - 1: Control is transfered to GCS 253
    Vehicle - 1->>GCS - 250: CONTROL_STATUS <br> - sysid_in_control: 253 <br> - takeover_allowed: 1 (takeover allowed automatically)
    Vehicle - 1->>GCS - 253: CONTROL_STATUS <br> - sysid_in_control: 253 <br> - takeover_allowed: 1 (takeover allowed automatically)
    Note over GCS - 253: It is now in control of vehicle 1
    Note over GCS - 250: Now GCS 250 wants to request control. <br> As GCS 253 didn't enforce being asked, <br> it will be granted automatically.
    GCS - 250->>Vehicle - 1: MAV_CMD_REQUEST_OPERATOR_CONTROL: <br> - param 1: 0 (Sysid requesting control not needed, can be deducted from sender) <br> - param 2: 1 (request control) <br> - param 3: 1 (allow automatic takeover, although irrelevant right now)
    Vehicle - 1->>GCS - 250: COMMAND_ACK
    Note over Vehicle - 1: As asking for takeover wasn't enforced by GCS 253, <br> control is granted automatically.
    Vehicle - 1->>GCS - 253: CONTROL_STATUS <br> - sysid_in_control: 250 <br> - takeover_allowed: 1 (takeover allowed automatically)
    Vehicle - 1->>GCS - 250: CONTROL_STATUS <br> - sysid_in_control: 250 <br> - takeover_allowed: 1 (takeover allowed automatically)
-->

[![](https://mermaid.ink/img/pako:eNrdVV9v2jAQ_yqnvKxItAqt9pJNSBmgqdqAjdA-IUUmvoDVxGaOA0JVv_vO4KSQlbWT2B7GC87Zd_n9uXMevURx9AKvwB8lygT7gi00yz_MJNBvxbQRiVgxaeBzL4JLuH5_8-vWPS5FkiFtd07n-fstqQyCWqM-zArgk1aMJ6ww0BuPppPx1ziahtO7KICRmiu-BSEhUdJolcHHue5SVrQtBIfbOh6Ae8VB4ctut8YdNEpXdQpbJxYyflsd_w_qwL7QqOZ8AMYuaQEbEqkAo0BbC0iAI5okF6BMlU6EXAArHuwfPYJhD2hL7t9Q1yWgR7oOw_u4N-zHk8H3u0E0jcffBpNwOp7EjkNQoSfLWG4zfLjYK-vw2BdWkCwaiciRtyFhEuYItC4TgxxSrXIoUHLUreOi1wF04KJBr3HmZneGZZnaACuNyhk1UE2y9aqxw2E46sdh70tT8SM1eo6HIME1k0WKmpCT9s6MM_lubXWbFYN4Rw35jmYVBBd8ZkyBbetMXXwWFC-27q2xCkqy6mAqVQprB7lzKte347xxavsnW_9qjzss6iHhgst31SQg9Z2bBtuIu7PCwEZkme1Iur-kadK5Op4T__-ckzZ5aZaqXCxBaI0Zru0NrMViaaxdrVf7-21jRMa8cBORncWBSRzm28o_Z1LyPH6_M-kMne__rfnz_xkKr-3lqHMmOH2eHy2mmWeWmOPMC2jJMWVlZmbeTD7RUZsbbWXiBUaX2Pa0bQIvSFlW0FO54sxU3_ZGdMCFUdoFn34CXbSSUw?type=png)](https://mermaid-js.github.io/mermaid-live-editor/edit#pako:eNrdVV9v2jAQ_yqnvKxItAqt9pJNSBmgqdqAjdA-IUUmvoDVxGaOA0JVv_vO4KSQlbWT2B7GC87Zd_n9uXMevURx9AKvwB8lygT7gi00yz_MJNBvxbQRiVgxaeBzL4JLuH5_8-vWPS5FkiFtd07n-fstqQyCWqM-zArgk1aMJ6ww0BuPppPx1ziahtO7KICRmiu-BSEhUdJolcHHue5SVrQtBIfbOh6Ae8VB4ctut8YdNEpXdQpbJxYyflsd_w_qwL7QqOZ8AMYuaQEbEqkAo0BbC0iAI5okF6BMlU6EXAArHuwfPYJhD2hL7t9Q1yWgR7oOw_u4N-zHk8H3u0E0jcffBpNwOp7EjkNQoSfLWG4zfLjYK-vw2BdWkCwaiciRtyFhEuYItC4TgxxSrXIoUHLUreOi1wF04KJBr3HmZneGZZnaACuNyhk1UE2y9aqxw2E46sdh70tT8SM1eo6HIME1k0WKmpCT9s6MM_lubXWbFYN4Rw35jmYVBBd8ZkyBbetMXXwWFC-27q2xCkqy6mAqVQprB7lzKte347xxavsnW_9qjzss6iHhgst31SQg9Z2bBtuIu7PCwEZkme1Iur-kadK5Op4T__-ckzZ5aZaqXCxBaI0Zru0NrMViaaxdrVf7-21jRMa8cBORncWBSRzm28o_Z1LyPH6_M-kMne__rfnz_xkKr-3lqHMmOH2eHy2mmWeWmOPMC2jJMWVlZmbeTD7RUZsbbWXiBUaX2Pa0bQIvSFlW0FO54sxU3_ZGdMCFUdoFn34CXbSSUw)

Diagram 2 - Now one of them asks for control enforcing being asked before other GCS takes over. When the other GCS takes over, the original GCS in control just requests again control without enforcing being asked before. This situation is interesting so the vehicle is never with no GCS in control. An alternative approach is in diagram 3.

<!-- mermaid graph:
sequenceDiagram;
    participant GCS - 253
    participant Vehicle - 1
    participant GCS - 250
    Vehicle - 1->>GCS - 253: CONTROL_STATUS <br> - sysid_in_control: 0
    Vehicle - 1->>GCS - 250: CONTROL_STATUS <br> - sysid_in_control: 0 
    Note over GCS - 253: GCS 253 wants to request control <br> ENFORCING asking for takeover first
    GCS - 253->>Vehicle - 1: MAV_CMD_REQUEST_OPERATOR_CONTROL: <br> - param 1: 0 (Sysid requesting control not needed, can be deducted from sender) <br> - param 2: 1 (request control) <br> - param 3: 0 (Do not allow automatic takeover, ask first)
    Vehicle - 1->>GCS - 253: COMMAND_ACK
    Note over Vehicle - 1: Control is transfered to GCS 253
    Vehicle - 1->>GCS - 250: CONTROL_STATUS <br> - sysid_in_control: 253 <br> - takeover_allowed: 0 (automatic takeover not allowed, ask first)
    Vehicle - 1->>GCS - 253: CONTROL_STATUS <br> - sysid_in_control: 253 <br> - takeover_allowed: 0 (automatic takeover not allowed, ask first)
    Note over GCS - 253: It is now in control of vehicle 1
    Note over GCS - 250: Now GCS 250 wants to request control
    GCS - 250->>Vehicle - 1: MAV_CMD_REQUEST_OPERATOR_CONTROL: <br> - param 1: 0 (Sysid requesting control not needed, can be deducted from sender) <br> - param 2: 1 (request control) <br> - param 3: 1 (allow automatic takeover, although irrelevant at this point)
    Vehicle - 1->>GCS - 250: COMMAND_ACK
    Vehicle - 1->>GCS - 253: MAV_CMD_REQUEST_OPERATOR_CONTROL: <br> - param 1: 250 (Sysid requesting control) <br> - param 2: 1 (request control) <br> - param 3: 1 (allow automatic takeover, although irrelevant at this point)
    Note over GCS - 253: Popup appears in GCS comunicating the request from GCS 250. <br>User accepts. Requesting control again without enforcint being asked for takeover
    GCS - 253->>Vehicle - 1: MAV_CMD_REQUEST_OPERATOR_CONTROL: <br> - param 1: 0 (Sysid requesting control not needed, can be deducted from sender) <br> - param 2: 1 (request control) <br> - param 3: 1 (allow automatic takeover)
    Vehicle - 1->>GCS - 253: COMMAND_ACK
    Vehicle - 1->>GCS - 250: CONTROL_STATUS <br> - sysid_in_control: 253 <br> - takeover_allowed: 1 (automatic takeover allowed)
    Vehicle - 1->>GCS - 253: CONTROL_STATUS <br> - sysid_in_control: 253 <br> - takeover_allowed: 1 (automatic takeover allowed)
    Note over GCS - 250: As vehicle is reporting now automatic takeover <br> is allowed, we are free to request control  
    GCS - 250->>Vehicle - 1: MAV_CMD_REQUEST_OPERATOR_CONTROL: <br> - param 1: 0 (Sysid requesting control not needed, can be deducted from sender) <br> - param 2: 1 (request control) <br> - param 3: 0 (do not allow automatic takeover, although irrelevant at this point)
    Vehicle - 1->>GCS - 250: COMMAND_ACK
    Note over Vehicle - 1: Control will be granted automatically now
    Vehicle - 1->>GCS - 253: CONTROL_STATUS <br> - sysid_in_control: 250 <br> - takeover_allowed: 1 (allow automatic takeover)
    Vehicle - 1->>GCS - 250: CONTROL_STATUS <br> - sysid_in_control: 250 <br> - takeover_allowed: 1 (allow automatic takeover)
-->

[![](https://mermaid.ink/img/pako:eNrdV9FO2zAU_ZWrPIFUUAraSzYhVW2H0NaWtYWnSpFxblqLxM5shwoh_n3XSZqVkpZ1YqDRJze2r8-55-TIefC4itALPIM_c5Qce4LNNUs_zyTQL2PaCi4yJi2cdydwBCefTp9PXeNC8ARpur19n19Ora09OjuriwbQHQ2n49H3cDLtTK8m8OVGn9GUuTciCoUMuZJWqySAnXX8PepAWWioLIK6Qw1rYNyQBrAkBgasAu36YyxU28uy_eHX0bh7MTwHZm6FnEOsNFh2i0W5WGhjyzPqygR1DXgAg8512B30wnH_x1V_Mg1Hl_1xZzoahxWLYIWfOspSt8OHg4njskLkjl2BksqCRIwwagFnEm4QaJxzixHEWqVgUEaoD58WPQmgDQcbBDfWnBYH91RxBEsStQSWW5Uykrlm3HJtKGkfvij2YNAZ9sJO99umCk_6062YCRJBM2li1MSF9KgEeiUvOKmryRWZsGCJUUH8OdffjXDN3oP3-wBqNPmFdX2VpKWQtYdUDHcV-va2vdTZIe0qNfC3viRPve__x96nNTtMn9iFyucLEFpjgncu9JgFu6DmZkrI3abwG16GrfbZv2VOn61Ne8dmNBryUmV5BizLkGnjTOnmuEpzKTgrgNsF1i4rVK08eFygvDJUj3GOmTXHMH5uEjZnVHUpHEYLKCmvOWEis7hV9NI4s6xl-MdJ7x2i7Z3V_zZu243pVk2_Sb7-CYLGUOyYOjvJ7hozpQuFZWPfSwC0sE7tJQLTSGIjNt054OMEKh0cvXiZePVcfeGSsRRJ4mjSBVg6ljUownjvRHw18_m7zfc3L6r_Bud7LS9FnTIR0RfDg0Mz8yiRU5x5AQ0jjFme2Jk3k4-01BWY3EvuBVbn2PK0E9MLYpYY-pdnEbOrz42Np_1IWKWrh4-_AIxLByI?type=png)](https://mermaid-js.github.io/mermaid-live-editor/edit#pako:eNrdV9FO2zAU_ZWrPIFUUAraSzYhVW2H0NaWtYWnSpFxblqLxM5shwoh_n3XSZqVkpZ1YqDRJze2r8-55-TIefC4itALPIM_c5Qce4LNNUs_zyTQL2PaCi4yJi2cdydwBCefTp9PXeNC8ARpur19n19Ora09OjuriwbQHQ2n49H3cDLtTK8m8OVGn9GUuTciCoUMuZJWqySAnXX8PepAWWioLIK6Qw1rYNyQBrAkBgasAu36YyxU28uy_eHX0bh7MTwHZm6FnEOsNFh2i0W5WGhjyzPqygR1DXgAg8512B30wnH_x1V_Mg1Hl_1xZzoahxWLYIWfOspSt8OHg4njskLkjl2BksqCRIwwagFnEm4QaJxzixHEWqVgUEaoD58WPQmgDQcbBDfWnBYH91RxBEsStQSWW5Uykrlm3HJtKGkfvij2YNAZ9sJO99umCk_6062YCRJBM2li1MSF9KgEeiUvOKmryRWZsGCJUUH8OdffjXDN3oP3-wBqNPmFdX2VpKWQtYdUDHcV-va2vdTZIe0qNfC3viRPve__x96nNTtMn9iFyucLEFpjgncu9JgFu6DmZkrI3abwG16GrfbZv2VOn61Ne8dmNBryUmV5BizLkGnjTOnmuEpzKTgrgNsF1i4rVK08eFygvDJUj3GOmTXHMH5uEjZnVHUpHEYLKCmvOWEis7hV9NI4s6xl-MdJ7x2i7Z3V_zZu243pVk2_Sb7-CYLGUOyYOjvJ7hozpQuFZWPfSwC0sE7tJQLTSGIjNt054OMEKh0cvXiZePVcfeGSsRRJ4mjSBVg6ljUownjvRHw18_m7zfc3L6r_Bud7LS9FnTIR0RfDg0Mz8yiRU5x5AQ0jjFme2Jk3k4-01BWY3EvuBVbn2PK0E9MLYpYY-pdnEbOrz42Np_1IWKWrh4-_AIxLByI)

Diagram 3 - Now one of them asks for control enforcing being asked before other GCS takes over. When the other GCS takes over, the original GCS in control just releases control. This might be desirable in some situations, but leaves the vehicle with no owner until the second GCS requests control:

<!-- mermaid graph:
sequenceDiagram;
    participant GCS - 253
    participant Vehicle - 1
    participant GCS - 250
    Vehicle - 1->>GCS - 253: CONTROL_STATUS <br> - sysid_in_control: 0
    Vehicle - 1->>GCS - 250: CONTROL_STATUS <br> - sysid_in_control: 0 
    Note over GCS - 253: GCS 253 wants to request control <br> ENFORCING asking for takeover first
    GCS - 253->>Vehicle - 1: MAV_CMD_REQUEST_OPERATOR_CONTROL: <br> - param 1: 0 (Sysid requesting control not needed, can be deducted from sender) <br> - param 2: 1 (request control) <br> - param 3: 0 (Do not allow automatic takeover, ask first)
    Vehicle - 1->>GCS - 253: COMMAND_ACK
    Note over Vehicle - 1: Control is transfered to GCS 253
    Vehicle - 1->>GCS - 250: CONTROL_STATUS <br> - sysid_in_control: 253 <br> - takeover_allowed: 0 (automatic takeover not allowed, ask first)
    Vehicle - 1->>GCS - 253: CONTROL_STATUS <br> - sysid_in_control: 253 <br> - takeover_allowed: 0 (automatic takeover not allowed, ask first)
    Note over GCS - 253: It is now in control of vehicle 1
    Note over GCS - 250: Now GCS 250 wants to request control
    GCS - 250->>Vehicle - 1: MAV_CMD_REQUEST_OPERATOR_CONTROL: <br> - param 1: 0 (Sysid requesting control not needed, can be deducted from sender) <br> - param 2: 1 (request control) <br> - param 3: 1 (allow automatic takeover, although irrelevant at this point)
    Vehicle - 1->>GCS - 250: COMMAND_ACK
    Vehicle - 1->>GCS - 253: MAV_CMD_REQUEST_OPERATOR_CONTROL: <br> - param 1: 250 (Sysid requesting control) <br> - param 2: 1 (request control) <br> - param 3: 1 (allow automatic takeover, although irrelevant at this point)
    Note over GCS - 253: Popup appears in GCS comunicating the request from GCS 250. <br>User accepts. Releasing control
    GCS - 253->>Vehicle - 1: MAV_CMD_REQUEST_OPERATOR_CONTROL: <br> - param 1: 0 (Sysid requesting control not needed, can be deducted from sender) <br> - param 2: 0 (release control) <br> - param 3: 1 (allow automatic takeover, although it doesn't apply as we drop control)
    Vehicle - 1->>GCS - 253: COMMAND_ACK
    Note over Vehicle - 1: Nobody in control now
    Vehicle - 1->>GCS - 250: CONTROL_STATUS <br> - sysid_in_control: 0 <br> - takeover_allowed: 1 (automatic takeover allowed)
    Vehicle - 1->>GCS - 253: CONTROL_STATUS <br> - sysid_in_control: 0 <br> - takeover_allowed: 1 (automatic takeover allowed)
    Note over GCS - 250: As vehicle is reporting now nobody in control <br> We are free to request control  
    GCS - 250->>Vehicle - 1: MAV_CMD_REQUEST_OPERATOR_CONTROL: <br> - param 1: 0 (Sysid requesting control not needed, can be deducted from sender) <br> - param 2: 1 (request control) <br> - param 3: 0 (do not allow automatic takeover, although irrelevant at this point)
    Vehicle - 1->>GCS - 250: COMMAND_ACK
    Note over Vehicle - 1: Control will be granted automatically now, as <br> nobody is in control
    Vehicle - 1->>GCS - 253: CONTROL_STATUS <br> - sysid_in_control: 250 <br> - takeover_allowed: 1 (allow automatic takeover)
    Vehicle - 1->>GCS - 250: CONTROL_STATUS <br> - sysid_in_control: 250 <br> - takeover_allowed: 1 (allow automatic takeover)
-->

[![](https://mermaid.ink/img/pako:eNrdV1FP2zAQ_iunvAykglLQXrIJqWo7hLamrC3spVJkkgu1SOzMdqgqxH_fOUmzUhoqRiTE-uTG9t333Xf-4jw4oYzQ8RyNv3MUIQ44u1Us_TIXQL-MKcNDnjFh4Lw_hSM4-Xz6fOoaFzxMkKa7zfvccmpj7dHZWR3Ug_7Yn03GP4LprDe7msLXG3VGU3qleRRwEYRSGCUTD16M474iDpSBfGkQ5D0q2ABjhzSAJTHQYCQoWx9toNpehh3638aT_oV_DkzfcXELsVRg2B0W4WKutClz1JEJ6gZwD0a966A_GgST4c-r4XQWjC-Hk95sPAkqFt4aP1WUpXaHCwdTy2WNyKZdgxLSgECMMOpAyATcINA4Dw1GECuZgkYRoTp8GvTEgy4cbBHcWnNaJB7IIgVLErkElhuZMpK5ZtyxZShpH-4VezTq-YOg1_--rcKT-vQrZpxEUEzoGBVxIT0qgVrqBSt1NbkmExQsMSqIP-f6txC22K_g_T6Adjb5hbF1FaQlF3UPyRjuK_Tdpr1UWZ92lRq4jYfkae-7H7j3ac0LTZ-YhcxvF8CVwgTvrekxA2ZBxc0kFy83hbvjMDS2z-tLZvVpLNo7FmNnQ17KLM-AZRkypW1T2rlQprngISuAmwXWXVaoWvXgcYHySlM8FoaYGX0ME8rP9Abdj-HFrpXAIsc3S2AgkqjFJ2NrmqzIFWBJMJTM6tAt-bQvb2S02vQRspXWXtSNTtjd6YTVdFte_Mb8O-2zp2uXpYOhMJOq6B5rxuJZLYv8vxCYQuodxF0XEvh_3JYSR3tvGq2b7p4byJIniaVJt2NhWdagCOPK6mZfuiWVtYB6Q8PW7gV7urGhYIetXZT-Mb_TcVJUKeMRfWw8WDRzh8w8xbnj0TDCmOWJmTtz8UhLbYDpSoSOZ1SOHUdZqR0vZommf3kWMbP-Utl6Ooy4kap6-PgHUpIZrw?type=png)](https://mermaid-js.github.io/mermaid-live-editor/edit#pako:eNrdV1FP2zAQ_iunvAykglLQXrIJqWo7hLamrC3spVJkkgu1SOzMdqgqxH_fOUmzUhoqRiTE-uTG9t333Xf-4jw4oYzQ8RyNv3MUIQ44u1Us_TIXQL-MKcNDnjFh4Lw_hSM4-Xz6fOoaFzxMkKa7zfvccmpj7dHZWR3Ug_7Yn03GP4LprDe7msLXG3VGU3qleRRwEYRSGCUTD16M474iDpSBfGkQ5D0q2ABjhzSAJTHQYCQoWx9toNpehh3638aT_oV_DkzfcXELsVRg2B0W4WKutClz1JEJ6gZwD0a966A_GgST4c-r4XQWjC-Hk95sPAkqFt4aP1WUpXaHCwdTy2WNyKZdgxLSgECMMOpAyATcINA4Dw1GECuZgkYRoTp8GvTEgy4cbBHcWnNaJB7IIgVLErkElhuZMpK5ZtyxZShpH-4VezTq-YOg1_--rcKT-vQrZpxEUEzoGBVxIT0qgVrqBSt1NbkmExQsMSqIP-f6txC22K_g_T6Adjb5hbF1FaQlF3UPyRjuK_Tdpr1UWZ92lRq4jYfkae-7H7j3ac0LTZ-YhcxvF8CVwgTvrekxA2ZBxc0kFy83hbvjMDS2z-tLZvVpLNo7FmNnQ17KLM-AZRkypW1T2rlQprngISuAmwXWXVaoWvXgcYHySlM8FoaYGX0ME8rP9Abdj-HFrpXAIsc3S2AgkqjFJ2NrmqzIFWBJMJTM6tAt-bQvb2S02vQRspXWXtSNTtjd6YTVdFte_Mb8O-2zp2uXpYOhMJOq6B5rxuJZLYv8vxCYQuodxF0XEvh_3JYSR3tvGq2b7p4byJIniaVJt2NhWdagCOPK6mZfuiWVtYB6Q8PW7gV7urGhYIetXZT-Mb_TcVJUKeMRfWw8WDRzh8w8xbnj0TDCmOWJmTtz8UhLbYDpSoSOZ1SOHUdZqR0vZommf3kWMbP-Utl6Ooy4kap6-PgHUpIZrw)