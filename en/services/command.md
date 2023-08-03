# Command Protocol

The MAVLink command protocol allows guaranteed delivery of MAVLink commands.

Commands are values of [MAV_CMD](#MAV_CMD) that define the values of up to 7 parameters.
These parameters and the command id are encoded in [COMMAND_INT](#COMMAND_INT) or [COMMAND_LONG](#COMMAND_LONG) for sending.

The protocol provides reliable delivery by expecting a matching acknowledgement (`COMMAND_ACK`) from commands to indicate command arrival, and result.
If no acknowledgement is received the command must be automatically re-sent.

## Message/Enum Summary

Message | Description
-- | --
<a id="COMMAND_INT"></a>[COMMAND_INT](../messages/common.md#COMMAND_INT) | Message for encoding a command ([MAV_CMD](#MAV_CMD)). The message encodes commands into up to 7 parameters: parameters 1-4, 7 are floats, and parameters 5,6 are scaled integers. The scaled integers are used for positional information (scaling depends on the actual command value). The coordinate frame of positional parameters is explicitly specified in a frame field. Commands that require float-only properties in parameters 5, 6 cannot be sent in this message (e.g. commands where NaN has an explicit meaning).
<a id="COMMAND_LONG"></a>[COMMAND_LONG](../messages/common.md#COMMAND_LONG) | Message for encoding a command ([MAV_CMD](#MAV_CMD)). The mesage encodes commands into up to 7 float parameters. The coordinate frame used for positional co-ordinates is implementation dependent. Any command may be packaged in this message, but there may be some loss of precision for positional co-ordinates (latitude, longitude).
<a id="COMMAND_ACK"></a>[COMMAND_ACK](../messages/common.md#COMMAND_ACK) | Command acknowledgement. Includes result (success, failure, still in progress) and may include progress information and additional detail about failure reasons.
<a id="COMMAND_CANCEL"></a>[COMMAND_CANCEL](../messages/common.md#COMMAND_CANCEL) | Cancel a long running command.


Enum | Description
-- | --
<a id="MAV_CMD"></a>[MAV_CMD](../messages/common.md#mav_commands) | Commands to be executed/sent in the command messages.
<a id="MAV_FRAME"></a>[MAV_FRAME](../messages/common.md#MAV_FRAME) | Coordinate frame. Used in `COMMAND_INT` to specify the co-ordinate frame of any positional parameters.
<a id="MAV_RESULT"></a>[MAV_RESULT](../messages/common.md#MAV_RESULT) | Result of command, included in [COMMAND_ACK.result](#COMMAND_ACK).

## Use COMMAND_INT or COMMAND_LONG?

`COMMAND_INT` should be used when sending commands that contain positional or navigation information, if supported by the flight stack for the particular command.
This is because it allows the co-ordinate frame to be specified for location and altitude values, which may otherwise be "unspecified".
In addition latitudes/longitudes can be sent with greater precision in a `COMMAND_INT` as scaled integers in params 5 and 6 (than when sent in float values in `COMMAND_LONG`).

`COMMAND_LONG` must be used for sending `MAV_CMD` commands that send float properties in parameters 5 and 6, as these values would be truncated to integers if sent in `COMMAND_INT`.

Commands that are not positional or that specify integers in params 5 and 6 can be used in either message, if supported by the flight stack.

Flight stacks may support commands in either message `COMMAND_INT` or `COMMAND_LONG` or both, albeit with a loss of precision, rounding errors, and/or undefined frames of reference.
However they are encouraged to only support positional commands in `COMMAND_INT`, and commands that have float values in param 5 and 6 in `COMMAND_LONG`.
The flight stack can reject commands sent in the "wrong" message type using the [COMMAND_ACK.result](#COMMAND_ACK) of `MAV_RESULT_COMMAND_LONG_ONLY` or `MAV_RESULT_COMMAND_INT_ONLY`, as appropriate. 
Flight stacks that only support a particular command in a particular message type can more generally use these result values to indicate the correct message type for a command.

## Sequences

### COMMAND_INT sequence

[![Mermaid Sequence: Command INT](https://mermaid.ink/img/pako:eNplj90KwjAMhV-l5EphvkAFQTYREfViXhYktJkW1nZ26YWMvbv1ZyCYixDO-XJIBtDBEEjo6Z7Ia6osXiO6pfIiV4eRrbYdehbbsv4Xqxg8feTsL1artyBFeToc1sfqsjueZ03Oo-K1hq6f_8K5S1FzzhNsHYXEH_cdMvlT1LrcQwGOokNr8sXDi1XAN3KkQObRUIOpZQXKjxlNnUGmjbEcIsgG254KwMShfngNkmOiCfp-_aXGJ9ehWtc?type=png)](https://mermaid-js.github.io/mermaid-live-editor/edit#pako:eNplj90KwjAMhV-l5EphvkAFQTYREfViXhYktJkW1nZ26YWMvbv1ZyCYixDO-XJIBtDBEEjo6Z7Ia6osXiO6pfIiV4eRrbYdehbbsv4Xqxg8feTsL1artyBFeToc1sfqsjueZ03Oo-K1hq6f_8K5S1FzzhNsHYXEH_cdMvlT1LrcQwGOokNr8sXDi1XAN3KkQObRUIOpZQXKjxlNnUGmjbEcIsgG254KwMShfngNkmOiCfp-_aXGJ9ehWtc)

The request is sent by the ground station encoded within a [COMMAND_INT](#COMMAND_INT).
The drone processes the request and responds quickly with a [COMMAND_ACK](#COMMAND_ACK) indicating the result.
The result is that the command has been accepted (`COMMAND_ACK.result=MAV_RESULT_ACCEPTED`), has been accepted and is in progress (MAV_RESULT_IN_PROGRESS) or it has been rejected with some reason code.
Note that "accepted" means that the command is valid and the flight stack will attempt to act on it, not that the command has completed.
Most commands just return "accepted" (they are not implemented as long running commands).

`COMMAND_ACK.result_param2` may also include additional information about the reason for command rejection in a command-specific enum.

If no ACK is received the GCS will resend `COMMAND_INT` for a flight-specific number of times before giving up.

### COMMAND_LONG sequence

[![Mermaid Sequence: Command Long](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgR0NTLT4-RHJvbmU6IENPTU1BTkRfTE9ORyhjb25maXJtYXRpb249MClcbiAgICBHQ1MtPj5HQ1M6IFN0YXJ0IHRpbWVvdXRcbiAgICBEcm9uZS0-PkdDUzogQ09NTUFORF9BQ0siLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgR0NTLT4-RHJvbmU6IENPTU1BTkRfTE9ORyhjb25maXJtYXRpb249MClcbiAgICBHQ1MtPj5HQ1M6IFN0YXJ0IHRpbWVvdXRcbiAgICBEcm9uZS0-PkdDUzogQ09NTUFORF9BQ0siLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)

<!-- Original sequence
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: COMMAND_LONG(confirmation=0)
    GCS->>GCS: Start timeout
    Drone->>GCS: COMMAND_ACK
-->

If the command drops the sender should increase the confirmation field:

[![Mermaid Sequence: increase confirmation field](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgR0NTLT4-RHJvbmU6IENPTU1BTkRfTE9ORyhjb25maXJtYXRpb249MClcbiAgICBHQ1MtPj5HQ1M6IFN0YXJ0IHRpbWVvdXRcbiAgICBHQ1MtPj5Ecm9uZTogQ09NTUFORF9MT05HKGNvbmZpcm1hdGlvbj0xKVxuICAgIEdDUy0-PkdDUzogU3RhcnQgdGltZW91dFxuICAgIERyb25lLT4-R0NTOiBDT01NQU5EX0FDSyIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgR0NTLT4-RHJvbmU6IENPTU1BTkRfTE9ORyhjb25maXJtYXRpb249MClcbiAgICBHQ1MtPj5HQ1M6IFN0YXJ0IHRpbWVvdXRcbiAgICBHQ1MtPj5Ecm9uZTogQ09NTUFORF9MT05HKGNvbmZpcm1hdGlvbj0xKVxuICAgIEdDUy0-PkdDUzogU3RhcnQgdGltZW91dFxuICAgIERyb25lLT4-R0NTOiBDT01NQU5EX0FDSyIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)

<!-- Original sequence
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: COMMAND_LONG(confirmation=0)
    GCS->>GCS: Start timeout
    GCS->>Drone: COMMAND_LONG(confirmation=1)
    GCS->>GCS: Start timeout
    Drone->>GCS: COMMAND_ACK
-->

### Long Running Commands {#long_running_commands}

Some commands are *long running*, and cannot complete immediately. 
The drone reports its progress by sending `COMMMAND_ACK` messages with [COMMAND_ACK.result=MAV_RESULT_IN_PROGRESS](../messages/common.md#MAV_RESULT_IN_PROGRESS) and the progress as a percentage in `COMMMAND_ACK.progress` ([0-100] percent complete, 255 if progress not supplied). 
When the operation completes, the drone must terminate with a `COMMMAND_ACK` containing the final [result](#MAV_RESULT) of the operation: `MAV_RESULT_ACCEPTED`, `MAV_RESULT_FAILED`, `MAV_RESULT_CANCELLED`).

[![Mermaid Sequence: MAV_RESULT_IN_PROGRESS](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgR0NTLT4-RHJvbmU6IENPTU1BTkRfTE9ORygpXG4gICAgR0NTLT4-R0NTOiBTdGFydCB0aW1lb3V0XG4gICAgRHJvbmUtPj5HQ1M6IENPTU1BTkRfQUNLKHJlc3VsdD1NQVZfUkVTVUxUX0lOX1BST0dSRVNTLHByb2dyZXNzPT8pXG4gICAgR0NTLT4-R0NTOiBTdGFydCAobG9uZ2VyKSB0aW1lb3V0XG4gICAgRHJvbmUtPj5HQ1M6IENPTU1BTkRfQUNLKHJlc3VsdD1NQVZfUkVTVUxUX0lOX1BST0dSRVNTLHByb2dyZXNzPT8pXG4gICAgR0NTLT4-R0NTOiBTdGFydCAobG9uZ2VyKSB0aW1lb3V0XG4gICAgTm90ZSByaWdodCBvZiBHQ1M6IC4uLlxuICAgIERyb25lLT4-R0NTOiBDT01NQU5EX0FDSyhyZXN1bHQ9TUFWX1JFU1VMVF9BQ0NFUFRFRCkiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgR0NTLT4-RHJvbmU6IENPTU1BTkRfTE9ORygpXG4gICAgR0NTLT4-R0NTOiBTdGFydCB0aW1lb3V0XG4gICAgRHJvbmUtPj5HQ1M6IENPTU1BTkRfQUNLKHJlc3VsdD1NQVZfUkVTVUxUX0lOX1BST0dSRVNTLHByb2dyZXNzPT8pXG4gICAgR0NTLT4-R0NTOiBTdGFydCAobG9uZ2VyKSB0aW1lb3V0XG4gICAgRHJvbmUtPj5HQ1M6IENPTU1BTkRfQUNLKHJlc3VsdD1NQVZfUkVTVUxUX0lOX1BST0dSRVNTLHByb2dyZXNzPT8pXG4gICAgR0NTLT4-R0NTOiBTdGFydCAobG9uZ2VyKSB0aW1lb3V0XG4gICAgTm90ZSByaWdodCBvZiBHQ1M6IC4uLlxuICAgIERyb25lLT4-R0NTOiBDT01NQU5EX0FDSyhyZXN1bHQ9TUFWX1JFU1VMVF9BQ0NFUFRFRCkiLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)


<!-- Original sequence
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: COMMAND_LONG()
    GCS->>GCS: Start timeout
    Drone->>GCS: COMMAND_ACK(result=MAV_RESULT_IN_PROGRESS,progress=?)
    GCS->>GCS: Start (longer) timeout
    Drone->>GCS: COMMAND_ACK(result=MAV_RESULT_IN_PROGRESS,progress=?)
    GCS->>GCS: Start (longer) timeout
    Note right of GCS: ...
    Drone->>GCS: COMMAND_ACK(result=MAV_RESULT_ACCEPTED)
-->

Long running operations may be cancelled by sending the [COMMAND_CANCEL](#COMMAND_CANCEL) message.
The drone should cancel the operation and complete the sequence by sending `COMMAND_ACK` with `COMMAND_ACK.result=MAV_RESULT_CANCELLED`
- If cancellation is not supported the drone can just continue to send progress updates until completion.
- If the sequence has already completed (or is idle) the cancel command should be ignored.
 
The rate at which progress messages are emitted is system-dependent.
Generally though, the GCS should have a much increased timeout after receiving an ACK with `MAV_RESULT_IN_PROGRESS`.
  
If a timeout is triggered when waiting for a progress or completion update, the GCS should terminate the sequence (return to the idle state) and notify the user if appropriate.

Only one instance of a _particular_ long running command can execute at a time; to restart a long running operation (i.e. with new parameters) it must first be cancelled!
If the same command is recieved while the operation is in progress the new command should be ACKed with `MAV_RESULT_TEMPORARILY_REJECTED` (to indicate that the target is busy).

The protocol allows for _different_ long running commands to run in parallel, if supported by the state machine of the recieving flight stack.
If a flight stack does not support multiple commands running in parallel it should ACK new commands with `MAV_RESULT_TEMPORARILY_REJECTED` (with the possible exception of the [COMMAND_CANCEL](#COMMAND_CANCEL), which might be used to cancel the first request).

## Location Commands and Frame Types

Commands that contain a location or altitude should be sent in [COMMAND_INT](#COMMAND_INT) so that the frame can be specified in the `COMMAND_INT.frame` field (as outlined [above](#use-commandint-or-commandlong)).
If sent in [COMMAND_LONG](#COMMAND_LONG) the frame is arbitrary, and cannot be predicted.

A flight stack that does not support the frame specified in a command (if required by command) should reject it with the [MAV_RESULT](#MAV_RESULT) of `MAV_RESULT_COMMAND_UNSUPPORTED_MAV_FRAME`.
This allows consumers to attempt the same command with other frames.
Flight stacks that return `MAV_RESULT_COMMAND_UNSUPPORTED` for this case should be updated to use `MAV_RESULT_COMMAND_UNSUPPORTED_MAV_FRAME`.

Note that it is an error to ignore the specified frame and use some other arbitrary frame.

## Designing Commands

Guidance for designing commands can be found in [Defining XML Elements > Command values](../guide/define_xml_element.md#command_values).

At high level:

- Commands that include location information should specify latitude in Param 5, Longitude in param 6, and Altitude in param 7.
  This allows them to be sent in [COMMAND_INT](#COMMAND_INT) with higher precision.
- Otherwise it is desirable to be able to send commands in either command message.
  Therefore use param 5 and 6 for integers rather than floats if possible.
  If reserving values, then consider choosing to reserve params 5 and 6, and reserve them with a default value of `0`.
