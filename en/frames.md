Coordinate systems (frames)
===

![TF2 Clover frames](../assets/frames.png)

Main frames in the `clover` package:

* `map` has its origin at the flight controller initialization point and may be considered stationary. It is shown as a white grid on the image above;
* `base_link` is rigidly bound to the drone. It is shown by the simplified drone model on the image above;
* `body` is bound to the drone, but its Z axis points up regardless of the drone's pitch and roll. It is shown by the red, blue and green lines in the illustration;
* <a name="navigate_target"></a>`navigate_target` is bound to the current navigation target (as set by the [navigate](simple_offboard.md#navigate) service);
* `setpoint` is current position setpoint.

Additional frames become available when [ArUco positioning system](aruco.md) is active:

* `aruco_map` is bound to the currently active [ArUco map](aruco_map.md);
* `aruco_N` is bound to the [marker](aruco_marker.md) with ID=N.

> **Hint** Frames that are bound to the drone are oriented according to [the ROS convention](http://www.ros.org/reps/rep-0103.html): the X axis points forward, Y to the left, and Z up.

3D visualization of the coordinate systems can be viewed using [rviz](rviz.md).

tf2
--

Read more at http://wiki.ros.org/tf2

tf2 ROS package is used extensively in the Clover platform. tf2 is a set of libraries for C++, Python and other programming languages that are used to work with the frames. Internally, ROS nodes publish `TransformStamped` messages to `/tf` topic with transforms between frames at certain points in time.

The [`simple_offboard`](simple_offboard.md) node can be used to request the drone position in an arbitrary frame by setting the `frame_id` argument appropriately in a call to `get_telemetry` service.

tf2 can be used from Python to transform coordinates (for objects like PoseStamped and PointStamped) from one frame to another
