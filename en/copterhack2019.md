# Copter Hack 2019

The [Copter Hack 2019](https://copterexpress.timepad.ru/event/1017592/) hackathon took place on the 11th to 13th of October in the "Moscow" Technopolis.

Event page: https://coex.tech/copterhack.

Hackathon chat: https://t.me/CopterHack.

Timepad event page: https://copterexpress.timepad.ru/event/1017592/.

## Information for participants

### COEX Pix specifics

Be sure to set the *Autopilot orientation* parameter to `ROTATION_ROLL_180_YAW_90` if you're using the *COEX Pix* flight controller. This parameter should be applied during calibration of each sensor.

<img src="../assets/autopilot_orientation.png" class="center" width="600">

This parameter is used for *IMU* orientation correction.

### Suggested image versions

Raspberry Pi versions 3B+ and lower: [v0.18](https://github.com/CopterExpress/clover/releases/tag/v0.18)

Raspberry Pi version 4: [v0.19-alpha.1](https://github.com/CopterExpress/clover/releases/tag/v0.19-alpha.1)

### Camera orientation

Some drones have the camera mounted with the cable going forward. You should set this orientation in the `main_camera.launch` file in the `clever` package.

Further reading: [Camera orientation](camera_setup.md)

### Using Optical Flow

In order to enable optical flow set `optical_flow` and `rangefinder_vl53l1x` parameters to `true` in `clever.launch`.

Enable `pub agl as lpos down` in `LPE_FUSION` parameter using QGroundControl.

Make sure the rangefinder is mounted correctly and is working (see [Interfacing with a laser rangefinder](laser.md)).

Further reading: [Optical Flow](optical_flow.md).

### Using ArUco map

Use the `cmit.txt` map. See [instructions](aruco_map.md).

### Drone batteries

**The battery indicator should be connected to the battery at all times. The organizers will not replace your damaged batteries!**

### Flight videos

Be sure to record **ALL** your flights on video! If your drone fails before your presentation, you'll be able to at least show your videos.

### Yaw problem

The v1.8.2-clever.7 FCU firmware has a potential bug that manifests during VPE (marker-based) flights. If your drone does not correct its yaw when using ArUco markers, try using an older firmware version (v1.8.2-clever.6, available from https://github.com/CopterExpress/Firmware/releases/tag/v1.8.2-clever.6). Download `px4fmu-v4_default.px4` for COEX Pix.

### `navigate` service problem

The 0.18 Raspberry Pi image has a potential bug that makes the drone fly through waypoints too fast. Try setting the `nav_from_sp` parameter to `false` in `~/catkin_ws/src/clever/clever/launch/clever.launch` if you are affected by it:

```xml
<!-- simplified offboard control -->
<node name="simple_offboard" pkg="clever" type="simple_offboard" output="screen" clear_params="true">
    <param name="reference_frames/body" value="map"/>
    <param name="reference_frames/base_link" value="map"/>
    <param name="reference_frames/navigate_target" value="map"/>
    <param name="reference_frames/navigate_target" value="map"/>
    <param name="nav_from_sp" value="false"/>
</node>
```

## Lectures (in Russian)

Lecture 1: Introduction – https://www.youtube.com/watch?v=cjtmZNuq7z0.

Lecture 2: FCU setup – https://www.youtube.com/watch?v=PJNDYFPZQms.

Lecture 3: PX4 architecture – https://www.youtube.com/watch?v=_jl7FImq3jk.

Lecture 4: Autonomous flights – https://www.youtube.com/watch?v=ThXiNG1IzvI.

Be sure to check out other videos on the COEX YouTube channel: https://www.youtube.com/channel/UCeCu93sLBkcgbIkIC7Jaauw/featured.

## Results

Winners:

1. Bulbolet – potato delivery using a smart hoist.
2. Copter don't hurt me – controlling drone using a neural interface.
3. import torch – active track using neural networks.
4. Autobot – freeze light through a VK bot.
5. Stardust Crusaders – AR drone simulation.
