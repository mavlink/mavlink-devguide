# Examples (Pymavlink)

Other examples:

- [ArduPilot/pymavlink/examples](https://github.com/ArduPilot/pymavlink/tree/master/examples) - The Pymavlink submodule contains a number of simple examples.
- [ArduSub Pymavlink Docs](https://www.ardusub.com/developers/pymavlink.html) - A number of useful examples, which use ArduSub and MAVProxy

Complex examples:

- [MAVProxy](http://ardupilot.github.io/MAVProxy/html/development/index.html) is a command line, console based UAV ground station software package for MAVLink based systems built on Pymavlink.
  - It demonstrates most of the features of using the MAVLink module.
  - The source code can be found here: https://github.com/ArduPilot/MAVProxy


## Multi-Vehicle SYSID Disambiguation

The [multi_vehicle_sysid.py](https://github.com/mavlink/mavlink/blob/master/examples/python/multi_vehicle_sysid.py) example demonstrates how to receive MAVLink messages from multiple vehicles on a single connection and route them by `(sysid, compid)` pairs.

The example shows how to:
- Disambiguate vehicles by keying each component as `(sysid, compid)`
- Filter out GCS self-messages (sysid 255)
- Discover new components dynamically via heartbeats
- Monitor vehicle liveness and drop stale components
- Send `COMMAND_LONG` to a specific vehicle and wait for `COMMAND_ACK`
- 
