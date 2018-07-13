# File Transfer Protocol (FTP)

> **Note** THIS IS WORK IN PROGRESS: The FTP protocol is pretty simple. Right now everything is exchanged inside [ENCAPSULATED_DATA](../messages/common.md#MAV_PROTOCOL_CAPABILITY_FTP) packets, and there are a few other things that could be tightened up, but the protocol should be brought up first before optimising bandwidth. 

The actual implementation is in this file:
* [src/modules/mavlink/mavlink_ftp.cpp](https://github.com/PX4/Firmware/blob/master/src/modules/mavlink/mavlink_ftp.cpp)
* [src/modules/mavlink/mavlink_ftp.h](https://github.com/PX4/Firmware/blob/master/src/modules/mavlink/mavlink_ftp.h)

The QGC side of the implementation is here:
* [src/uas/FileManager.cc](https://github.com/mavlink/qgroundcontrol/blob/master/src/uas/FileManager.cc)

And with the main protocol being implemented here (which has a few function calls for test purposes):
https://github.com/mavlink/qgroundcontrol/blob/mavlink-ftp/src/uas/QGCUASFileManager.cc

These function calls are triggered by this UI element:
https://github.com/mavlink/qgroundcontrol/blob/master/src/ui/QGCUASFileView.cc#L20

So only very basic C/C++ skills are needed at this point to complete the implementation.


Everything is run by the master (QGC in this case); the slave simply responds to packets in order as they arrive. There’s buffering in the server for a little overlap (two packets in the queue at a time) but it’s a tradeoff between memory and link latency so I didn’t want to get ahead of myself bumping it up.

The MAVLink receiver thread copies an incoming request verbatim from the MAVLink buffer into a request queue, and queues a low-priority work item to handle the packet. This avoids trying to do file I/O on the MAVLink receiver thread, as well as avoiding yet another worker thread. The worker is responsible for directly queueing replies, which are sent with the same sequence number as the request.

The opcodes defined/implemented in the server are:

Reset
- Clears all state held by the server; closes all open files, etc.
- Sends an Ack reply with no data.

List (path, offset)
- Opens the directory (path), seeks to (offset) and fills the result buffer with nul-separated filenames. Sends an Ack packet with the result buffer on success, or a Nak packet with an error code on error.
- The directory is closed after the operation, so this leaves no state on the server.

Open (path)
- Opens the file (path) and allocates a session number. The file must exist.
- Sends an Ack packet with the allocated session number on success, or a Nak packet with an error code on error.
- The file remains open after the operation, and must eventually be closed by Reset or Terminate.

Read (session, offset, size)
- Seeks to (offset) in the file opened in (session) and reads (size) bytes into the result buffer.
- Sends an Ack packet with the result buffer on success, or a Nak packet with an error code on error. For short reads or reads beyond the end of a file, the (size) field in the Ack packet will indicate the actual number of bytes read.
- Reads can be issued to any offset in the file for any number of bytes, so reconstructing portions of the file to deal with lost packets should be easy.
- For best download performance, try to keep two Read packets in flight.

Create (path)
- Creates the file (path) and allocates a session number. The file must not exist, but all parent directories must exist.
- Sends an Ack packet with the allocated session number on success, or a Nak packet with an error code on error.
- The file remains open after the operation, and must eventually be closed by Reset or Terminate.

Write (session, offset, size)
- Attempts to append (size) bytes from the request to the file opened in (session). The (offset) value must exactly match the current size of the file, i.e. writes can only append.
- Sends an Ack reply with no data on success, or a Nak packet with an error code on error.
- The kErrNotAppend error (7) indicates that the offset value does not match the size of the file. There are two likely causes of this - a lost Write request, and a lost Ack reply for a successful write.
- On detecting a missed Ack, rewind the upload to the first Ack lost and begin sending again; ignore any kErrNotAppend errors (since you may be overlapping Writes that were received but not acked) until you have received another ack.

Terminate (session)
- Closes the file associated with (session) and frees the session ID for re-use.

Remove (path)
- Currently not implemented; we will probably want to be careful about what we allow to be deleted…

I would expect that you can run all of the protocol from an asynchronous state machine; once you have 
initiated a process, you can kick the state machine from either packet reception or a timeout event.
