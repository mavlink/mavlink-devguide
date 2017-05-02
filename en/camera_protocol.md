# Camera Protocol

The camera protocol allows to configure camera payloads and request their status. It supports photo and video cameras and includes messages to query and configure the onboard camera storage.



## Geotagging and Trigger Feedback

The [CAMERA\_IMAGE\_CAPTURED](http://mavlink.org/messages/common#CAMERA_IMAGE_CAPTURED) message is intended for geo-tagging. It should be sent by the camera when an image has been taken.

