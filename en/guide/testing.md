# Testing

## Changes to Mavgen

Changes to the mavgen generator (in [ArduPilot/pymavlink](https://github.com/ArduPilot/pymavlink)) are tested on every PR prior to acceptance into the master branch.

You can run the test code yourself in Ubuntu.
1. Install additional dependencies for gtest:
   ```sh
   sudo apt-get install cmake libgtest-dev
   ```
1. Run the test generator from the pymavlink directory:
   ```sh
   cd pymavlink
   ./test_generator.sh
   ```
   > **Tip** The tests require message definitions in **../message_definitions/** (i.e. at the level above the **pymavlink** directory).
     This is how things are set up when you're running the tests from the *mavlink* repo.
