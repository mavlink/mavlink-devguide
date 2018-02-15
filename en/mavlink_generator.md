# MAVLink Generator (C/C++, Python)

MAVLink is distributed with a common set of messages. Custom messages can be generated and included as a replacement for the common message set or as extension to it. See the minimal.xml for a minimal example and pixhawk.xml for an example of using the common message set with some project-specific extensions.

Download the generator from here: https://github.com/mavlink/mavlink

Then run:

```sh
python mavgenerate.py
```
 
To obtain the generator GUI.

Generator Steps
1. Load XML file, from mavlink/message_definitions
1. Select output directory, e.g. mavlink/include
1. Click “Generate”
1. Use the new headers in your project