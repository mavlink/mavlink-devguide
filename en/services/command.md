# Command Protocol

The MAVLink command protocol allows guaranteed delivery of MAVLink commands.

Commands are values of [MAV_CMD](#MAV_CMD) that define the values of up to 7 parameters.
These parameters and the command id are encoded in [COMMAND_INT](#COMMAND_INT) or [COMMAND_LONG](#COMMAND_LONG) for sending.

The protocol provides reliable delivery by expecting a matching acknowledgement (`COMMAND_ACK`) from commands to indicate command arrival, and result.
If not acknowledgement is received the command must be automatically re-sent.

> **Note** `COMMAND_INT` is generally recommended when sending positional information as it allows greater precision, and is explicit about the co-ordinate frame.
  Commands that require float-only properties in parameters 5, 6 must be sent in `COMMAND_LONG` (e.g. commands where NaN has an explicit meaning).  

## Message/Enum Summary

Message | Description
-- | --
<span id="COMMAND_INT"></span>[COMMAND_INT](../messages/common.md#COMMAND_INT) | Message for encoding a command ([MAV_CMD](#MAV_CMD)). The message encodes commands into up to 7 parameters: parameters 1-4, 7 are floats, and parameters 5,6 are scaled integers. The scaled integers are used for positional information (scaling depends on the actual command value). The coordinate frame of positional parameters is explicitly specified in a frame field. Commands that require float-only properties in parameters 5, 6 cannot be sent in this message (e.g. commands where NaN has an explicit meaning).
<span id="COMMAND_LONG"></span>[COMMAND_LONG](../messages/common.md#COMMAND_LONG) | Message for encoding a command ([MAV_CMD](#MAV_CMD)). The mesage encodes commands into up to 7 float parameters. The coordinate frame used for positional co-ordinates is implementation dependent. Any command may be packaged in this message, but there may be some loss of precision for positional co-ordinates (latitude, longitude).
<span id="COMMAND_ACK"></span>[COMMAND_ACK](../messages/common.md#COMMAND_ACK) | Command acknowledgement. Includes result (success, failure, still in progress) and may include progress information and additional detail about failure reasons.
<span id="COMMAND_CANCEL"></span>[COMMAND_CANCEL](../messages/common.md#COMMAND_CANCEL) | Cancel a long running command.


Enum | Description
-- | --
<span id="MAV_CMD"></span>[MAV_CMD](../messages/common.md#mav_commands) | Commands to be executed/sent in the command messages.
<span id="MAV_FRAME"></span>[MAV_FRAME](../messages/common.md#MAV_FRAME) | Coordinate frame. Used `COMMAND_INT` to specify co-ordinate frame of an positional parameters.
<span id="MAV_RESULT"></span>[MAV_RESULT](../messages/common.md#MAV_RESULT) | Result of command, included in [COMMAND_ACK.result](#COMMAND_ACK).


## Sequences

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

> **Note** If another command is received while handling a command (long running or otherwise) the new command should be rejected with `MAV_RESULT_TEMPORARILY_REJECTED`.
  What this means is that to restart an operation (i.e. with new parameters) it must first be cancelled.
  
The rate at which progress messages are emitted is system-dependent.
Generally though, the GCS should have a much increased timeout after receiving an ACK with `MAV_RESULT_IN_PROGRESS`.
  
If a timeout is triggered when waiting for a progress or completion update, the GCS should terminate the sequence (return to the idle state) and notify the user if appropriate.
