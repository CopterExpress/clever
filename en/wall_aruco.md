# Navigation using vertical ArUco-markers

The algorithm of the navigation through visual ArUco-markers, that was implemented in the Clever image, supports the flexible configuration of the markers in area. It allows you to place them on any surface, at any angle.

## Installing the vertical camera mount

For a better recognition of the markers, you need to set the camera vertically so that the lens is pointed parallel to the horizon.

> **Note** The configuration file allows you to configure the location of the camera in area relative to the copter in any way. For your convenience, we will review the option of installing the camera at an angle of 90 degrees to the horizon in the direction of the copter's nose.

### Camera mount, 3D printing

Print the [camera mount](models.md#clover-3).

Install the mount in a convenient location, so that the camera has a minimum number of unnecessary objects (protection, legs, propellers, beams) — all of it will negatively affect the recognition of the markers.

## Setting the camera transform

To set the camera position at the desired angle, open the file `main_camera.launch`, located in `~/catkin_ws/src/clover/clover/launch/`.

```bash
nano ~/catkin_ws/src/clover/clover/launch/main_camera.launch
```

In the parameters `direction_x`, `direction_y`, set empty values manually or enter the following lines:

```bash
sed -i "/direction_z/s/default=\".*\"/default=\"\"/" /home/pi/catkin_ws/src/clover/clover/launch/main_camera.launch
sed -i "/direction_y/s/default=\".*\"/default=\"\"/" /home/pi/catkin_ws/src/clover/clover/launch/main_camera.launch
```

Edit one of the configuration lines or add the line shown bellow:

```xml
<node pkg="tf2_ros" type="static_transform_publisher" name="main_camera_frame" args="0.05 0 0.05 -1.5707963 0 -1.5707963 base_link main_camera_optical"/>
```

> **Note**. Only one camera configuration can be used at a time. If you insert the line above, don't forget to comment the currently active one. The syntax highlighting system will help you determine that — the active line will be highlighted in a different color than the comments. To comment, add the `<!--` and `-->` symbols at the beginning and the end respectively.

If you are using the marker map, where the markers have equal distances along the x and y axes, you can use [script for creating markers map `gen_map.py`](aruco_map.md#marker-map-definition). Otherwise, you will need to set them manually. To do this, go to the directory `map_name.txt` and create a map file. Fill out your map according to the [map syntax](aruco_map.md#marker-map-definition). Here is an example of a marker map with a random marker location:

>**Hint**. When filling out the map, select one of the markers as the origin, and measure the distance to all other markers relative to it. If all your parameters are oriented same way, you can choose not to specify all 8 parameters, but only the first 5: the marker index, size, and its location in space along the x, y, and z axes, respectively.

```
106 0.33    0   0   0
103 0.33    1.53    0.23    0
153 0.40    -0.56   1.36    0
```

After you fill out the map, you need to apply it. To do it, edit the file `aruco.launch`, located in `~/catkin_ws/src/clover/clover/launch/`. Change the line `<param name="map" value="$(find aruco_pose)/map/map_name.txt"/>`, where `map_name.txt` is the name of your map file.

If you are using markers that are not linked to horizontal surfaces (floor, ceiling), you must disable the parameter `known_tilt` both in the module `aruco_detect` and `aruco_map` in the same file. To do it automatically, enter:

```bash
sed -i "/known_tilt/s/value=\".*\"/value=\"\"/" /home/pi/catkin_ws/src/clover/clover/launch/aruco.launch
```

After all the settings, call `sudo systemctl restart clover` to restart the `clover` service.
