# Image Transmission Protocol

> **Caution** This content has not been reviewed since being ported from the old website (and may be out of date). Updates/re-validation welcome!

<span></span>
> **Note** At time of writing (March 2018) the *QGroundControl* only uses the *Image Transmission Protocol* to show PX4 Flow images for focusing.

This topic describes how the image streaming functionality works and covers both the implementation details (on MAV and QGroundControl) as well as the communication between the MAV and *QGroundControl*.

The image transmission protocol consists of two modules: An image streaming and a video streaming component:
* The **image streaming** component uses MAVLink as communication channel and can be used to transport any kind of image (raw images, Kinect data, ...) from the MAV to *QGroundControl*. It basically takes a live camera image, splits it into small chunks and sends it over MAVLink. This module is mainly used to transfer images directly into *QGroundControl* (i.e. the HUD component as shown below).
  > **Note** This component could also be used to send large data chunks other than images to *QGroundControl*.
* The **video streaming** component streams "real" video in MPEG2 format. It uses the live camera image and [FFMpeg](http://ffmpeg.org/) to encode a video stream. The main use case for this module is to watch a live camera feed on almost any mobile device (Laptops, Smartphones, ...) without the need of using *QGroundControl* or a MAVLink client.

The main advantage of the image streaming component over the video streaming is the better integration into *QGroundControl*. The main disadvantage is its need for MAVLink support (hence not as cross-platform as the video streaming component).

## Communication

### Image streaming

The image streaming component uses two mavlink messages: A handshake message, [DATA_TRANSMISSION_HANDSHAKE](../messages/common.md#DATA_TRANSMISSION_HANDSHAKE), to initiate, control and stop the image streaming; and a data container message, [ENCAPSULATED_DATA](../messages/common.md#ENCAPSULATED_DATA), to transport the image data.

{% mermaid %}
sequenceDiagram;
    participant QGroundControl
    participant MAV Component
    QGroundControl->>MAV Component: Request to start image stream
    MAV Component->>MAV Component: Wait for image from camera. 
    MAV Component->>MAV Component: Encode image (JPEG).
    MAV Component->>QGroundControl: Send image meta data
    MAV Component->>MAV Component: Split image into chunks.
    MAV Component->>QGroundControl: Send image chunks.
    QGroundControl->>QGroundControl: Receive image chunks.
    QGroundControl->>QGroundControl: Re-assemble image and display.
    QGroundControl->>MAV Component: Request to stop image stream
    MAV Component->>MAV Component: Stop image preparation
    MAV Component->>QGroundControl: Acknowledge to stop image stream
{% endmermaid %}


1. The communication is initiated by the *QGroundControl* with a request to start the stream. To do so, one must set the following fields in the MAVLink message:
  * `target`: to the ID of the targeted MAV,
  * `state`: to 0 for a request,
  * `id`: an ID for the image stream, 
    > **Note** For the moment, the image streamer only supports one stream per image type and therefore requires you to set the ''id'' to the same integer as the ''type'' field.
  * `type`: any of the types in the ENUM ''MAVLINK_DATA_STREAM_TYPES'' in **mavlink.h**,
  * `freq`: bigger than 0 for "frames per seconds", lower than 0 for "seconds per frame"

It is possible to request for a specific image quality. To do so, you must set the ''quality'' field. All other fields should be zero in the initial request.

1. When the targeted MAV receives the handshake request, it sends back an acknowledgment and starts the image stream at the requested framerate. The handshake ACK packet normally contains the same values as requested by the QGroundStation (`state` set to 1, because it's an ACK), and adds data about the size of the next sent image:
  * The field ''packets'' contains the number of MAVLink `ENCAPSULATED_DATA` packets,
  * the field ''payload'' specifies the size of the payload of each data packet (normally 252 bytes),
  * and the ''size'' field specifies the image size in bytes.

1. The image data is then split into chunks to fit into normal MAVLink messages. They are then packed into `ENCAPSULATED_DATA` packets and sent over MAVLink. Every packet contains a sequence number as well as the ID of the image stream it belongs to. The image streamer now sends periodically new images, there is no further interaction needed. Every new image comes with a new `DATA_TRANSMISSION_HANDSHAKE` ACK packet with updated image `size`, `packets` and `payload` fields. After this ACK packet, the new image arrives as a series of `ENCAPSULATED_DATA` packets.
   > **Note** The sequence number starts at 0 for every new image of the stream.

1. To stop an image stream you must send a new ''DATA_TRANSMISSION_HANDSHAKE'' request packet with the frequency set to 0. The MAV will acknowledge this by sending back an ACK packet containing the same data as in the request.

### Video streaming

The video transmission communication protocol is much simpler than the image streaming one: It consists of just one MAVLink message, `VIDEO_STREAM`, which is used to start and stop the video stream.

{% mermaid %}
sequenceDiagram;
    participant QGroundControl
    participant MAV Component
    QGroundControl->>MAV Component: Request to start video stream
    MAV Component->>MAV Component: Acknowledge to start video stream 
    MAV Component->>MAV Component: Get camera image
    MAV Component->>MAV Component: Add (Y)UV channels
    MAV Component->>MAV Component: Feed into FFmpeg
    MAV Component->>MAV Component: Output to network
    MAV Component->>QGroundControl: Deliver video stream 
    QGroundControl->>QGroundControl: Display video
    QGroundControl->>QGroundControl: Listen to streaming requests
    QGroundControl->>MAV Component: Request to stop video stream
    MAV Component->>QGroundControl: Acknowledge to stop image stream
    MAV Component->>MAV Component: Stop video output
{% endmermaid %}



The message has two fields to set:
* `target`: The targeted MAV
* `start_stop`: 1 to start the stream, 0 to stop it.

The video stream is generated by FFMpeg on the MAV side. A small MAVLink wrapper grabs the camera image, adds (Y)UV channels for the [YUV420 rawimage](https://secure.wikimedia.org/wikipedia/en/wiki/YUV#Y.27UV420p_.28and_Y.27V12_or_YV12.29) format and feeds that image into FFMpeg. The output is then sent to the ground station (at the moment this requires a fixed IP for the ground station as well as one initial configuration step when setting up the MAV). 

Upon receiving the video stream, *QGroundControl* opens up a VLC window to redistribute the video stream: It takes the stream from the MAV, and offers this stream as RTP stream (on a multicast address) and as HTTP stream (for direct unicast streaming) to the network. This is done without transcoding of the original stream, to keep the performance impact as low as possible.

Other mobile devices can now connect to the stream on the multicast address `239.255.12.45`, or to the HTTP stream on `%%http://[QGC-HOST]/MAVLive.mpg%%`. The multicast stream is announced via SAP under the name "MAVLive".

## Usage / Configuration
To use the two modules on your MAV, you have to do the following steps.

### Image streaming

- Compile the `mavconn` middleware for your MAV: [Guide](https://www.pixhawk.org/wiki/software/mavconn/start), [Github](https://github.com/pixhawk/mavconn).
- Start at least these components on the MAV: 
  ```
  px_mavlink_bridge_udp &
  px_system_control --heartbeat &
  px_camera -o lcm &
  ```
- Compile and start *QGroundControl*.
- Start the image streaming component (you can add the -v flag to see some more output): `px_imagestreamer`.
- Initiate the image stream: Open the HUD widget, right-click into the widget and chose "Enable live Image Streaming".

You should now be able to see the live video feed with one image per second (default, hardcoded at the moment).

### Video streaming

- Perform steps 1 to 3 as in the image streaming part above
- Create a symlink in your home directory: 
  ```sh
  cd ~
  ln -s mavconn/src/comm/video/px_videostreamer.sh px_videostreamer.sh
  ```
  > **Note** You could also copy the file, though that is not recommended.
- Start the video streaming component on the MAV: `px_videostreamer`
- Initiate the video stream: Open the HUD widget, right-click into the widget and choose **Enable Video Live feed**.

A VLC window should now open. Don't close that window as long as you want to stream the video to others! If you want to watch the current stream, just open the stream in another VLC window.

## Developer 

Out-of-the-box, the image streaming component only implements JPEG streaming of the camera image. To implement your own image stream, you have to do the following:

* Write a MAVLink handler, which handles requests to start image streams of your type of choice.
* Write a data handler, which takes your desired data (i.e. a stereo camera image), encodes it into the format of your choice (i.e. rawimage, JPEG, BMP) and splits/sends the data over MAVLink.
* Extend the data/message handler in the UAS component of *QGroundControl* to correctly handle your data (i.e. unpacking of the chosen format)
* Write or extend a widget to display your data according to your wishes.