# Image Transmission Protocol

The image transmission protocol uses MAVLink as the communication channel to transport any kind of image (raw images, Kinect data, etc.) from one MAVLink node to another.
It basically takes a live camera image, splits it into small chunks and sends it over MAVLink.  

This topic describes how the image streaming functionality works and covers both the communication protocol and implementation details (for a vehicle and *QGroundControl*).

> **Note** At time of writing (March 2018) the protocol is mainly used to transfer images from a vehicle to *QGroundControl* (to show PX4 Flow images for focusing). The protocol could also be used to send any other file types.


## Communication

The image streaming component uses two MAVLink messages: A handshake message, [DATA_TRANSMISSION_HANDSHAKE](../messages/common.md#DATA_TRANSMISSION_HANDSHAKE), to initiate, control and stop the image streaming; and a data container message, [ENCAPSULATED_DATA](../messages/common.md#ENCAPSULATED_DATA), to transport the image data.

[![Mermaid Diagram](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgR0NTLT4-RHJvbmU6IFJlcXVlc3QgdG8gc3RhcnQgaW1hZ2Ugc3RyZWFtXG4gICAgRHJvbmUtPj5Ecm9uZTogV2FpdCBmb3IgaW1hZ2UgZnJvbSBjYW1lcmEuIFxuICAgIERyb25lLT4-RHJvbmU6IEVuY29kZSBpbWFnZSAoSlBFRykuXG4gICAgRHJvbmUtPj5HQ1M6IFNlbmQgaW1hZ2UgbWV0YSBkYXRhXG4gICAgRHJvbmUtPj5Ecm9uZTogU3BsaXQgaW1hZ2UgaW50byBjaHVua3MuXG4gICAgRHJvbmUtPj5HQ1M6IFNlbmQgaW1hZ2UgY2h1bmtzLlxuICAgIEdDUy0-PkdDUzogUmVjZWl2ZSBpbWFnZSBjaHVua3MuXG4gICAgR0NTLT4-R0NTOiBSZS1hc3NlbWJsZSBpbWFnZSBhbmQgZGlzcGxheS5cbiAgICBHQ1MtPj5Ecm9uZTogUmVxdWVzdCB0byBzdG9wIGltYWdlIHN0cmVhbVxuICAgIERyb25lLT4-RHJvbmU6IFN0b3AgaW1hZ2UgcHJlcGFyYXRpb25cbiAgICBEcm9uZS0-PkdDUzogQWNrbm93bGVkZ2UgdG8gc3RvcCBpbWFnZSBzdHJlYW0iLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgR0NTLT4-RHJvbmU6IFJlcXVlc3QgdG8gc3RhcnQgaW1hZ2Ugc3RyZWFtXG4gICAgRHJvbmUtPj5Ecm9uZTogV2FpdCBmb3IgaW1hZ2UgZnJvbSBjYW1lcmEuIFxuICAgIERyb25lLT4-RHJvbmU6IEVuY29kZSBpbWFnZSAoSlBFRykuXG4gICAgRHJvbmUtPj5HQ1M6IFNlbmQgaW1hZ2UgbWV0YSBkYXRhXG4gICAgRHJvbmUtPj5Ecm9uZTogU3BsaXQgaW1hZ2UgaW50byBjaHVua3MuXG4gICAgRHJvbmUtPj5HQ1M6IFNlbmQgaW1hZ2UgY2h1bmtzLlxuICAgIEdDUy0-PkdDUzogUmVjZWl2ZSBpbWFnZSBjaHVua3MuXG4gICAgR0NTLT4-R0NTOiBSZS1hc3NlbWJsZSBpbWFnZSBhbmQgZGlzcGxheS5cbiAgICBHQ1MtPj5Ecm9uZTogUmVxdWVzdCB0byBzdG9wIGltYWdlIHN0cmVhbVxuICAgIERyb25lLT4-RHJvbmU6IFN0b3AgaW1hZ2UgcHJlcGFyYXRpb25cbiAgICBEcm9uZS0-PkdDUzogQWNrbm93bGVkZ2UgdG8gc3RvcCBpbWFnZSBzdHJlYW0iLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlfQ)

<!-- Original diagram
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: Request to start image stream
    Drone->>Drone: Wait for image from camera. 
    Drone->>Drone: Encode image (JPEG).
    Drone->>GCS: Send image meta data
    Drone->>Drone: Split image into chunks.
    Drone->>GCS: Send image chunks.
    GCS->>GCS: Receive image chunks.
    GCS->>GCS: Re-assemble image and display.
    GCS->>Drone: Request to stop image stream
    Drone->>Drone: Stop image preparation
    Drone->>GCS: Acknowledge to stop image stream
-->


1. The communication is initiated by the *QGroundControl* with a request to start the stream. To do so, one must set the following fields in the MAVLink message:
  * `target`: to the ID of the targeted MAV,
  * `state`: to 0 for a request,
  * `id`: an ID for the image stream, 
    > **Note** For the moment, the image streamer only supports one stream per image type and therefore requires you to set the `id` to the same integer as the `type` field.
  * `type`: any of the types in the enum [MAVLINK_DATA_STREAM_TYPE](../messages/common.md#MAVLINK_DATA_STREAM_TYPE) in **mavlink.h**,
  * `freq`: bigger than 0 for "frames per seconds", lower than 0 for "seconds per frame"

It is possible to request for a specific image quality. To do so, you must set the ''quality'' field. All other fields should be zero in the initial request.

1. When the targeted MAV receives the handshake request, it sends back an acknowledgment and starts the image stream at the requested framerate. The handshake ACK packet normally contains the same values as requested by the GCS (`state` set to 1, because it's an ACK), and adds data about the size of the next sent image:
  * The field `packets` contains the number of MAVLink `ENCAPSULATED_DATA` packets,
  * the field `payload` specifies the size of the payload of each data packet (normally 252 bytes),
  * and the `size` field specifies the image size in bytes.

1. The image data is then split into chunks to fit into normal MAVLink messages. They are then packed into `ENCAPSULATED_DATA` packets and sent over MAVLink. Every packet contains a sequence number as well as the ID of the image stream it belongs to. The image streamer now sends periodically new images, there is no further interaction needed. Every new image comes with a new `DATA_TRANSMISSION_HANDSHAKE` ACK packet with updated image `size`, `packets` and `payload` fields. After this ACK packet, the new image arrives as a series of `ENCAPSULATED_DATA` packets.
   > **Note** The sequence number starts at 0 for every new image of the stream.

1. To stop an image stream you must send a new `DATA_TRANSMISSION_HANDSHAKE` request packet with the frequency set to 0. The MAVLink node will acknowledge this by sending back an ACK packet containing the same data as in the request.



## Usage / Configuration

To use the two modules on your MAV, you have to do the following steps:

- Compile the `mavconn` middleware for your MAV: [Guide](https://www.pixhawk.org/wiki/software/mavconn/start), [Github](https://github.com/pixhawk/mavconn).
- Start at least these components on the MAV: 
  ```
  px_mavlink_bridge_udp &
  px_system_control --heartbeat &
  px_camera -o lcm &
  ```
- Compile and start *QGroundControl*.
- Start the image streaming component (you can add the `-v` flag to see some more output): `px_imagestreamer`.
- Initiate the image stream: Open the HUD widget, right-click into the widget and choose **Enable live Image Streaming**.

You should now be able to see the live video feed with one image per second (default, hardcoded at the moment).


## Developer 

Out-of-the-box, the image streaming component only implements JPEG streaming of the camera image. To implement your own image stream, you have to do the following:

* Write a MAVLink handler, which handles requests to start image streams of your type of choice.
* Write a data handler, which takes your desired data (i.e. a stereo camera image), encodes it into the format of your choice (i.e. rawimage, JPEG, BMP) and splits/sends the data over MAVLink.
* Extend the data/message handler in the UAS component of *QGroundControl* to correctly handle your data (i.e. unpacking of the chosen format).
* Write or extend a widget to display your data according to your wishes.