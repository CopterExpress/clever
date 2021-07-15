# MAVROS

Main article is available in the official documentations: [http://wiki.ros.org/mavros](http://wiki.ros.org/mavros)

MAVROS \(MAVLink + ROS\) is a ROS package that allows controlling drones via the [MAVLink](mavlink.md) protocol. MAVROS supports PX4 and APM flight stacks. Communication may be established via UART, USB, TCP or UDP.

MAVROS subscribes to certain ROS topics that can be used to send commands, publishes telemetry to other topics, and provides services.

The MAVROS node is automatically started in the Clover launch-file. In order to [set the type of connection](connection.md), change the `fcu_conn` argument.

> **Hint** Simplified interaction with the drone is possible with the use of [`simple_offboard`] package (simple_offboard.md).

<!-- -->

> **Note** Some MAVROS plugins are disabled by default in the `clover` package in order to save resources. For more information, see the `plugin_blacklist` parameter in `/home/pi/catkin_ws/src/clover/clover/launch/mavros.launch`.

## Main services

`/mavros/set_mode` — set [flight mode](modes.md) of the controller. Most often used to set the OFFBOARD mode to accept commands from Raspberry Pi.

`/mavros/cmd/arming` — arm or disarm drone motors \(change arming status\).

## Main published topics

`/mavros/state` — status of connection to the flight controller and flight controller mode.

`/mavros/local_position/pose` — local position and orientation of the copter in the ENU coordinate system.

`/mavros/local_position/velocity` — current speed in local coordinates and angular velocities.

`/mavros/global_position/global` — current global position \(latitude, longitude, altitude\).

`/mavros/global_position/local` — the global position in the [UTM](https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system) coordinate system.

`/mavros/global_position/rel_alt` — relative altitude \(relative to the arming altitude\).

Messages published in the topics may be viewed with the `rostopic` utility, e.g., `rostopic echo /mavros/state`. See more in [working with ROS](ros.md).

## Main topics for publication

`/mavros/setpoint_position/local` — set target position and yaw of the drone \(in the ENU coordinate system\).

`/mavros/setpoint_position/cmd_vel` — set target linear velocity of the drone.

`/mavros/setpoint_attitude/attitude` and `/mavros/setpoint_attitude/att_throttle` — set target attitude and throttle level.

`/mavros/setpoint_attitude/cmd_vel` and `/mavros/setpoint_attitude/att_throttle` — set target angular velocity and throttle level.

### Topics for sending raw packets

`/mavros/setpoint_raw/local` — sends [SET\_POSITION\_TARGET\_LOCAL\_NED](https://mavlink.io/en/messages/common.html#SET_POSITION_TARGET_LOCAL_NED) message. Allows setting target position/target speed and target yaw/angular yaw velocity. The values to be set are selected using the `type_mask` field.

`/mavros/setpoint_raw/attitude` — sends [SET\_ATTITUDE\_TARGET](https://mavlink.io/en/messages/common.html#SET_ATTITUDE_TARGET) message. Allows setting the target attitude /angular velocity and throttle level. The values to be set are selected using the `type_mask` field

`/mavros/setpoint_raw/global` — sends [SET\_POSITION\_TARGET\_GLOBAL\_INT](https://mavlink.io/en/messages/common.html#SET_POSITION_TARGET_GLOBAL_INT). Allows setting the target attitude in global coordinates \(latitude, longitude, altitude\) and flight speed. **Not supported in PX4** \([issue](https://github.com/PX4/Firmware/issues/7552)\).
