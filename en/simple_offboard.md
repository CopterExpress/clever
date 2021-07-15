Autonomous flight (OFFBOARD)
===

> **Note** In the image version **0.20** `clever` package was renamed to `clover`. See [previous version of the article](https://github.com/CopterExpress/clover/blob/v0.19/docs/en/simple_offboard.md) for older images.

<!-- -->

> **Hint** We recommend using our [custom PX4 firmware for Clover](firmware.md#modified-firmware-for-clover) for autonomous flights.

The `simple_offboard` module of the `clover` package is intended for simplified programming of the autonomous drone flight (`OFFBOARD` [flight mode](modes.md)). It allows setting the desired flight tasks, and automatically transforms [coordinates between frames](frames.md).

`simple_offboard` is a high level system for interacting with the flight controller. For a more low level system, see [mavros](mavros.md).

Main services are [`get_telemetry`](#gettelemetry) (receive telemetry data), [`navigate`](#navigate) (fly to a given point along a straight line), [`navigate_global`](#navigateglobal) (fly to a point specified as latitude and longitude along a straight line), [`land`](#land) (switch to landing mode).

Python examples
---

You need to create proxies for services before calling them. Use the following template for your programs:

```python
import rospy
from clover import srv
from std_srvs.srv import Trigger

rospy.init_node('flight') # 'flight' is name of your ROS node

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)
```

Unused proxy functions may be removed from the code.

API description
---

> **Note** Omitted numeric parameters are set to 0.

### get_telemetry

Obtains complete telemetry of the drone.

Parameters:

* `frame_id` – [frame](frames.md) for values `x`, `y`, `z`, `vx`, `vy`, `vz`. Example: `map`, `body`, `aruco_map`. Default value: `map`.

Response format:

* `frame_id` — frame;
* `connected` – whether there is a connection to <abbr title="Flight Control Unit flight controller">FCU</abbr>;
* `armed` - drone arming state (armed if true);
* `mode` – current [flight mode](modes.md);
* `x, y, z` — local position of the drone *(m)*;
* `lat, lon` – drone latitude and longitude *(degrees)*, requires [GPS](gps.md) module;
* `alt` – altitude in the global coordinate system (according to [WGS-84](https://ru.wikipedia.org/wiki/WGS_84) standard, not <abbr title="Above Mean Sea Level">AMSL</abbr>!), requires [GPS](gps.md) module;
* `vx, vy, vz` – drone velocity *(m/s)*;
* `pitch` – pitch angle *(radians)*;
* `roll` – roll angle *(radians)*;
* `yaw` — yaw angle *(radians)*;
* `pitch_rate` — angular pitch velocity *(rad/s)*;
* `roll_rate` – angular roll velocity *(rad/s)*;
* `yaw_rate` – angular yaw velocity *(rad/s)*;
* `voltage` – total battery voltage *(V)*;
* `cell_voltage` – battery cell voltage *(V)*.

> **Note** Fields that are unavailable for any reason will contain the `NaN` value.

Displaying drone coordinates `x`, `y` and `z` in the local system of coordinates:

```python
telemetry = get_telemetry()
print(telemetry.x, telemetry.y, telemetry.z)
```

Displaying drone altitude relative to [the ArUco map](aruco.md):

```python
telemetry = get_telemetry(frame_id='aruco_map')
print(telemetry.z)
```

Checking global position availability:

```python
import math
if not math.isnan(get_telemetry().lat):
    print('Global position is available')
else:
    print('No global position')
```

Output of current telemetry (command line):

```bash
rosservice call /get_telemetry "{frame_id: ''}"
```

### navigate

Fly to the designated point in a straight line.

Parameters:

* `x`, `y`, `z` — coordinates *(m)*;
* `yaw` — yaw angle *(radians)*;
* `yaw_rate` – angular yaw velocity (will be used if yaw is set to `NaN`) *(rad/s)*;
* `speed` – flight speed (setpoint speed) *(m/s)*;
* `auto_arm` – switch the drone to `OFFBOARD` mode and arm automatically (**the drone will take off**);
* `frame_id` – [coordinate system](frames.md) for values `x`, `y`, `z`, `vx`, `vy`, `vz`. Example: `map`, `body`, `aruco_map`. Default value: `map`.

> **Note** If you don't want to change your current yaw set the `yaw` parameter to `NaN` (angular velocity by default is 0).

Ascending to the altitude of 1.5 m with the climb rate of 0.5 m/s:

```python
navigate(x=0, y=0, z=1.5, speed=0.5, frame_id='body', auto_arm=True)
```

Flying in a straight line to point 5:0 (altitude 2) in the local system of coordinates at the speed of 0.8 m/s (yaw is set to 0):

```python
navigate(x=5, y=0, z=3, speed=0.8)
```

Flying to point 5:0 without changing the yaw angle (`yaw` = `NaN`, `yaw_rate` = 0):

```python
navigate(x=5, y=0, z=3, speed=0.8, yaw=float('nan'))
```

Flying 3 m to the right from the drone:

```python
navigate(x=0, y=-3, z=0, speed=1, frame_id='body')
```

Flying 2 m to the left from the last navigation target:

```python
navigate(x=0, y=2, z=0, speed=1, frame_id='navigate_target')
```

Turn 90 degrees clockwise:

```python
navigate(yaw=math.radians(-90), frame_id='body')
```

Flying to point 3:2 (with the altitude of 2 m) in the [ArUco map](aruco.md) coordinate system with the speed of 1 m/s:

```python
navigate(x=3, y=2, z=2, speed=1, frame_id='aruco_map')
```

Rotating on the spot at the speed of 0.5 rad/s (counterclockwise):

```python
navigate(x=0, y=0, z=0, yaw=float('nan'), yaw_rate=0.5, frame_id='body')
```

Flying 3 meters forwards at the speed of 0.5 m/s, yaw-rotating at the speed of 0.2 rad/s:

```python
navigate(x=3, y=0, z=0, speed=0.5, yaw=float('nan'), yaw_rate=0.2, frame_id='body')
```

Ascending to the altitude of 2 m (command line):

```(bash)
rosservice call /navigate "{x: 0.0, y: 0.0, z: 2, yaw: 0.0, yaw_rate: 0.0, speed: 0.5, frame_id: 'body', auto_arm: true}"
```

> **Note** Consider using the `navigate_target` frame instead of `body` for missions that primarily use relative movements forward/back/left/right. This negates inaccuracies in relative point calculations.

### navigate_global

Flying in a straight line to a point in the global coordinate system (latitude/longitude).

Parameters:

* `lat`, `lon` — latitude and longitude *(degrees)*;
* `z` — altitude *(m)*;
* `yaw` — yaw angle *(radians)*;
* `yaw_rate` – angular yaw velocity (used for setting the yaw to `NaN`) *(rad/s)*;
* `speed` – flight speed (setpoint speed) *(m/s)*;
* `auto_arm` – switch the drone to `OFFBOARD` and arm automatically (**the drone will take off**);
* `frame_id` – [coordinate system](frames.md) for `z` and `yaw` (Default value: `map`).

> **Note** If you don't want to change your current yaw set the `yaw` parameter to `NaN` (angular velocity by default is 0).

Flying to a global point at the speed of 5 m/s, while maintaining current altitude (`yaw` will be set to 0, the drone will face East):

```python
navigate_global(lat=55.707033, lon=37.725010, z=0, speed=5, frame_id='body')
```

Flying to a global point without changing the yaw angle (`yaw` = `NaN`, `yaw_rate` = 0):

```python
navigate_global(lat=55.707033, lon=37.725010, z=0, speed=5, yaw=float('nan'), frame_id='body')
```

Flying to a global point (command line):

```bash
rosservice call /navigate_global "{lat: 55.707033, lon: 37.725010, z: 0.0, yaw: 0.0, yaw_rate: 0.0, speed: 5.0, frame_id: 'body', auto_arm: false}"
```

### set_position

Set the setpoint for position and yaw. This service may be used to specify the continuous flow of target points, for example, for flying along complex trajectories (circular, arcuate, etc.).

> **Hint** Use the [`navigate`](#navigate) higher-level service to fly to a point in a straight line or to perform takeoff.

Parameters:

* `x`, `y`, `z` — point coordinates *(m)*;
* `yaw` — yaw angle *(radians)*;
* `yaw_rate` – angular yaw velocity (used for setting the yaw to NaN) *(rad/s)*;
* `auto_arm` – switch the drone to `OFFBOARD` and arm automatically (**the drone will take off**);
* `frame_id` – [coordinate system](frames.md) for `x`, `y`, `z` and `yaw` parameters (Default value: `map`).

Hovering on the spot:

```python
set_position(frame_id='body')
```

Assigning the target point 3 m above the current position:

```python
set_position(x=0, y=0, z=3, frame_id='body')
```

Assigning the target point 1 m ahead of the current position:

```python
set_position(x=1, y=0, z=0, frame_id='body')
```

Rotating on the spot at the speed of 0.5 rad/s:

```python
set_position(x=0, y=0, z=0, frame_id='body', yaw=float('nan'), yaw_rate=0.5)
```

### set_velocity

Set speed and yaw setpoints.

* `vx`, `vy`, `vz` – flight speed *(m/s)*;
* `yaw` — yaw angle *(radians)*;
* `yaw_rate` – angular yaw velocity (used for setting the yaw to NaN) *(rad/s)*;
* `auto_arm` – switch the drone to `OFFBOARD` and arm automatically (**the drone will take off**);
* `frame_id` – [coordinate system](frames.md) for `vx`, `vy`, `vz` and `yaw` (Default value: `map`).

> **Note** Parameter `frame_id` specifies only the orientation of the resulting velocity vector, but not its length.

Flying forward (relative to the drone) at the speed of 1 m/s:

```python
set_velocity(vx=1, vy=0.0, vz=0, frame_id='body')
```

### set_attitude

Set pitch, roll, yaw and throttle level (similar to [the `STABILIZED` mode](modes.md)). This service may be used for lower level control of the drone behavior, or controlling the drone when no reliable data on its position is available.

Parameters:

* `pitch`, `roll`, `yaw` – requested pitch, roll, and yaw angle *(radians)*;
* `thrust` — throttle level, ranges from 0 (no throttle, propellers are stopped) to 1 (full throttle).
* `auto_arm` – switch the drone to `OFFBOARD` mode and arm automatically (**the drone will take off**);
* `frame_id` – [coordinate system](frames.md) for `yaw` (Default value: `map`).

### set_rates

Set pitch, roll, and yaw rates and the throttle level (similar to [the `ACRO` mode](modes.md)). This is the lowest drone control level (excluding direct control of motor rotation speed). This service may be used to automatically perform aerobatic tricks (e.g., flips).

Parameters:

* `pitch_rate`, `roll_rate`, `yaw_rate` – pitch, roll, and yaw rates *(rad/s)*;
* `thrust` — throttle level, ranges from 0 (no throttle, propellers are stopped) to 1 (full throttle).
* `auto_arm` – switch the drone to `OFFBOARD` and arm automatically (**the drone will take off**);

The positive direction of `yaw_rate` rotation (when viewed from the top) is counterclockwise,`pitch_rate` rotation is forward, `roll_rate` rotation is to the left.

### land

Switch the drone to landing [mode](modes.md) (`AUTO.LAND` or similar).

> **Note** Set the `COM_DISARM_LAND` [PX4 parameter](px4_parameters.md) to a value greater than 0 to enable automatic disarm after landing.

Landing the drone:

```python
res = land()

if res.success:
    print('drone is landing')
```

Landing the drone (command line):

```bash
rosservice call /land "{}"
```

<!--
### release

Stop publishing setpoints to the drone (release control). Required to continue monitoring by means of [MAVROS](mavros.md).
-->

Additional materials
------------------------

* [ArUco-based position estimation and navigation](aruco.md).
* [Program samples and snippets](snippets.md).
