# Image Transmission Protocol

The image transmission protocol uses MAVLink as the communication channel to transport any kind of image (raw images, Kinect data, etc.) from one MAVLink node to another.
It basically takes a live camera image, splits it into small chunks and sends it over MAVLink.  

This topic describes how the image streaming functionality works and covers both the communication protocol and implementation details (for a vehicle and *QGroundControl*).

> **Note** At time of writing (2020) the protocol is mainly used to transfer images from a vehicle to *QGroundControl* (to show PX4 Flow images for focusing).
  The protocol could also be used to send any other file types.


## Communication

The image streaming component uses two MAVLink messages: a handshake message, [DATA_TRANSMISSION_HANDSHAKE](../messages/common.md#DATA_TRANSMISSION_HANDSHAKE), to initiate image streaming and describe the image to be sent, and a data container message, [ENCAPSULATED_DATA](../messages/common.md#ENCAPSULATED_DATA), to transport the image data.

[![](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgR0NTLT4-RHJvbmU6IFJlcXVlc3QgaW1hZ2UgKERBVEFfVFJBTlNNSVNTSU9OX0hBTkRTSEFLRSlcbiAgICBEcm9uZS0-PkRyb25lOiBXYWl0IGZvciBpbWFnZSBmcm9tIGNhbWVyYS4gXG4gICAgRHJvbmUtPj5Ecm9uZTogRW5jb2RlIGltYWdlIChKUEVHKS5cbiAgICBEcm9uZS0-PkdDUzogU2VuZCBpbWFnZSBtZXRhZGF0YSAoREFUQV9UUkFOU01JU1NJT05fSEFORFNIQUtFKVxuICAgIERyb25lLT4-RHJvbmU6IFNwbGl0IGltYWdlIGludG8gY2h1bmtzLlxuICAgIERyb25lLT4-R0NTOiBTZW5kIGltYWdlIGNodW5rcyAoRU5DQVBTVUxBVEVEX0RBVEEpXG4gICAgR0NTLT4-R0NTOiBSZWNlaXZlIGltYWdlIGNodW5rcy5cbiAgICBHQ1MtPj5HQ1M6IFJlLWFzc2VtYmxlIGltYWdlIGFuZCBkaXNwbGF5LlxuICAgIE5vdGUgb3ZlciBHQ1MsRHJvbmU6IE1BViB1c2VzIERBVEFfVFJBTlNNSVNTSU9OX0hBTkRTSEFLRSB0byBpbmRpY2F0ZSBzdGFydCBvZiBuZXcgaW1hZ2VcblxuXG4gICAgR0NTLT4-RHJvbmU6IFJlcXVlc3QgdG8gc3RvcCBpbWFnZSBzdHJlYW0gKERBVEFfVFJBTlNNSVNTSU9OX0hBTkRTSEFLRSlcbiAgICBEcm9uZS0-PkRyb25lOiBTdG9wIGltYWdlIHByZXBhcmF0aW9uXG4gICAgRHJvbmUtPj5HQ1M6IEFja25vd2xlZGdlIHRvIHN0b3AgaW1hZ2Ugc3RyZWFtICg_KSIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/#/edit/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtO1xuICAgIHBhcnRpY2lwYW50IEdDU1xuICAgIHBhcnRpY2lwYW50IERyb25lXG4gICAgR0NTLT4-RHJvbmU6IFJlcXVlc3QgaW1hZ2UgKERBVEFfVFJBTlNNSVNTSU9OX0hBTkRTSEFLRSlcbiAgICBEcm9uZS0-PkRyb25lOiBXYWl0IGZvciBpbWFnZSBmcm9tIGNhbWVyYS4gXG4gICAgRHJvbmUtPj5Ecm9uZTogRW5jb2RlIGltYWdlIChKUEVHKS5cbiAgICBEcm9uZS0-PkdDUzogU2VuZCBpbWFnZSBtZXRhZGF0YSAoREFUQV9UUkFOU01JU1NJT05fSEFORFNIQUtFKVxuICAgIERyb25lLT4-RHJvbmU6IFNwbGl0IGltYWdlIGludG8gY2h1bmtzLlxuICAgIERyb25lLT4-R0NTOiBTZW5kIGltYWdlIGNodW5rcyAoRU5DQVBTVUxBVEVEX0RBVEEpXG4gICAgR0NTLT4-R0NTOiBSZWNlaXZlIGltYWdlIGNodW5rcy5cbiAgICBHQ1MtPj5HQ1M6IFJlLWFzc2VtYmxlIGltYWdlIGFuZCBkaXNwbGF5LlxuICAgIE5vdGUgb3ZlciBHQ1MsRHJvbmU6IE1BViB1c2VzIERBVEFfVFJBTlNNSVNTSU9OX0hBTkRTSEFLRSB0byBpbmRpY2F0ZSBzdGFydCBvZiBuZXcgaW1hZ2VcblxuXG4gICAgR0NTLT4-RHJvbmU6IFJlcXVlc3QgdG8gc3RvcCBpbWFnZSBzdHJlYW0gKERBVEFfVFJBTlNNSVNTSU9OX0hBTkRTSEFLRSlcbiAgICBEcm9uZS0-PkRyb25lOiBTdG9wIGltYWdlIHByZXBhcmF0aW9uXG4gICAgRHJvbmUtPj5HQ1M6IEFja25vd2xlZGdlIHRvIHN0b3AgaW1hZ2Ugc3RyZWFtICg_KSIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)

<!-- Original diagram
sequenceDiagram;
    participant GCS
    participant Drone
    GCS->>Drone: Request image (DATA_TRANSMISSION_HANDSHAKE)
    Drone->>Drone: Wait for image from camera. 
    Drone->>Drone: Encode image (JPEG).
    Drone->>GCS: Send image metadata (DATA_TRANSMISSION_HANDSHAKE)
    Drone->>Drone: Split image into chunks.
    Drone->>GCS: Send image chunks (ENCAPSULATED_DATA)
    GCS->>GCS: Receive image chunks.
    GCS->>GCS: Re-assemble image and display.
    Note over GCS,Drone: MAV uses DATA_TRANSMISSION_HANDSHAKE to indicate start of new image
    GCS->>Drone: Request to stop image stream (DATA_TRANSMISSION_HANDSHAKE)
    Drone->>Drone: Stop image preparation
    Drone->>GCS: Acknowledge to stop image stream (?)
-->


1. The communication is initiated by the *QGroundControl* with a `DATA_TRANSMISSION_HANDSHAKE` request to start the stream.
   The messages should specify:
   * `type`: any of the types in the enum [MAVLINK_DATA_STREAM_TYPE](../messages/common.md#MAVLINK_DATA_STREAM_TYPE) in **mavlink.h**,
   * `jpg_quality`: Desired image quality (for lossy formats like JPEG).
   * All other fields must be zero in the initial request.

1. When the targeted MAV receives the handshake request, it sends back a `DATA_TRANSMISSION_HANDSHAKE`.
   This acts provides acknowledgment of the request and information about the image that is about to be streamed:
   * `type`: Type of image to be streamed (same as requested type)
   * `size`: Image size in bytes.
   * `width`: Image width in pixels.
   * `height`: Image height in pixels.
   * `packets`: number of MAVLink `ENCAPSULATED_DATA` packets to be sent
   * `payload`: Size of the payload of each data packet (normally 252 bytes)
   * `jpg_quality`: Image quality (same as requested)

1. The image data is then split into chunks to fit into `ENCAPSULATED_DATA` message and sent over MAVLink.
   Every packet contains a sequence number as well as the ID of the image stream it belongs to.
   
1. The image streamer periodically sends new images without further interaction.
   Every new image comes with a new `DATA_TRANSMISSION_HANDSHAKE` ACK packet with updated image `size`, `packets` and `payload` fields.
   After this ACK packet, the new image arrives as a series of `ENCAPSULATED_DATA` packets.
   > **Note** The sequence number starts at 0 for every new image of the stream.

1. To stop an image stream a GSC must send a new `DATA_TRANSMISSION_HANDSHAKE` request packet.
   The MAVLink node will acknowledge this by sending back an ACK packet containing the same data as in the request.


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