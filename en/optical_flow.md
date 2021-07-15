# Use of Optical Flow

Running the technology "Optical Flow" offers the possibility of POSCTL flight mode, and autonomous flight operating on a camera pointed downwards that detects changes of ground texture.

## Enabling

> **Hint** It is recommended to use [special PX4 firmware for Clover](firmware.md).

The use of a rangefinder is essential. [Connect and setup laser-ranging sensor VL53L1X](laser.md), according to the manual.

Enable Optical Flow in the file `~/catkin_ws/src/clover/clover/launch/clover.launch`:

```xml
<arg name="optical_flow" default="true"/>
```

Optical Flow publishes data in `mavros/px4flow/raw/send` topic. In the topic `optical_flow/debug` is also published a visualization, that can be viewed with [web_video_server](web_video_server.md).

> **Info** Correct connection and [setup](camera.md) of the camera module is needed for proper functioning.

## Setup of the flight controller

> **Hint** Suggested parameters are applied automatically in [our custom PX4 firmware](firmware.md#modified-firmware-for-clover).

When using **EKF2** (parameter `SYS_MC_EST_GROUP` = `ekf2`):

* `EKF2_AID_MASK` – flag 'use optical flow' is on.
* `EKF2_OF_DELAY` – 0.
* `EKF2_OF_QMIN` – 10.
* `EKF2_OF_N_MIN` – 0.05.
* `EKF2_OF_N_MAX` - 0.2.
* `SENS_FLOW_ROT` – No rotation.
* `SENS_FLOW_MAXHGT` – 4.0 (for the rangefinder VL53L1X)
* `SENS_FLOW_MINHGT` – 0.01 (for the rangefinder VL53L1X)
* Optional: `EKF2_HGT_MODE` – range sensor (cf. [rangefinder setup](laser.md)).

When using **LPE** (parameter `SYS_MC_EST_GROUP` = `local_position_estimator, attitude_estimator_q`):

* `LPE_FUSION` – flags 'fuse optical flow' and 'flow gyro compensation' are on.
* `LPE_FLW_QMIN` – 10.
* `LPE_FLW_SCALE` – 1.0.
* `LPE_FLW_R` – 0.2.
* `LPE_FLW_RR` – 0.0.
* `SENS_FLOW_ROT` – No rotation.
* `SENS_FLOW_MAXHGT` – 4.0 (for the rangefinder VL53L1X)
* `SENS_FLOW_MINHGT` – 0.01 (for the rangefinder VL53L1X)
* Optional: `LPE_FUSION` – flag 'pub agl as lpos down' is on (see [rangefinder setup](laser.md).

[The `selfcheck.py` utility](selfcheck.md) will help you verify that all settings are correctly set.

## POSCTL flight

Setup POSCTL to be one of PX4 flight modes and then select POSCTL.

## Autonomous flight

The module [simple_offboard](simple_offboard.md) enables autonomous flight.

Example of take off and leveling at 1.5m above the ground:

```python
navigate(z=1.5, frame_id='body', auto_arm=True)
```

Flying forward for 1m:

```python
navigate(x=1.5, frame_id='body')
```

[Navigation using ArUco-markers](aruco_marker.md) and [using VPE] are available when using Optical Flow.

## Additional settings

<!-- TODO: статья по пидам -->

If the copter has an unstable position, try to increase the *P* coefficient of speed PID controller - parameters are `MPC_XY_VEL_P` and `MPC_Z_VEL_P`.

If the copter has an unstable height, try increasing `MPC_Z_VEL_P` coefficient or getting better hover throttle - `MPC_THR_HOVER`.

If the copter is consistently yawing, try:

* recalibrate gyroscopes;
* recalibrate magnetometer;
* different values for `EKF2_MAG_TYPE` parameter, that indicates how data from the magnetometer is used in EKF2;
* changing values of `EKF2_MAG_NOISE`, `EKF2_GYR_NOISE`, `EKF2_GYR_B_NOISE` parameters.

> **Note** For better results perform gyro calibration directly before taking off, using [appropriate snippet](snippets.md#calibrate-gyro).

If the copter's height is deviating, try:

* increasing the value of `MPC_Z_VEL_P` coefficient;
* change the value of `MPC_THR_HOVER` parameter;
* add `MPC_ALT_MODE` = 2 (Terrain following).

When using Optical Flow, the maximal horizontal speed is further limited. This is an indirect influence of the parameter `SENS_FLOW_MAXR` (maximal reliable "angular speed" of the optical flow). In normal flight mode, control loops will be adjusted so that Optical Flow values do not exceed 50% of this parameter.

## Errors

If errors like `EKF INTERNAL CHECKS` occur, try to restart EKF2. To do so, enter in the MAVLink-console:

```nsh
ekf2 stop
ekf2 start
```
