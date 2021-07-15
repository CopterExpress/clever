# Controlling the copter from Arduino

For interaction with ROS topics and services on a Raspberry Pi, you can use the [rosserial_arduino](http://wiki.ros.org/rosserial_arduino) library. This library is pre-installed on [a Raspberry Pi image](image.md).

The main tutorial for rosserial: http://wiki.ros.org/rosserial_arduino/Tutorials

Arduino is to be installed on Clover and connected via a USB port.

## Configuring Arduino IDE

To work with ROS and Arduino, you should understand the format of installed packages' messages. For this purpose [on Raspberry Pi](ssh.md), build the ROS messages library:

```(bash)
rosrun rosserial_arduino make_libraries.py.
```

The obtained folder `ros_lib` is to be copied to `<sketches folder>/libraries` on a computer with Arduino IDE.

## Configuring Raspberry Pi

To run the program on Arduino once, you can use command:

```(bash)
roslaunch clover arduino.launch
```

To start the link with Arduino at the startup automatically, set argument `arduino` in the Clover launch file (`~/catkin_ws/src/clover/clover/launch/clover.launch`):

```xml
<arg name="arduino" default="true"/>
```

After the launch file is edited, restart the `clover` service:

```(bash)
sudo systemctl restart clover
```

## Delays

When `rosserial_arduino` is used, the Arduino microcontroller should not be blocked for more than a few seconds (for example, using the `delay` function); otherwise communication between Raspberry Pi and Arduino will be broken.

During implementation of long `while` cycles, ensure periodic calling the `hn.spinOnce` function:

```cpp
while(/* condition */) {
  // ... Perform required actions
  nh.spinOnce();
}
```

To organize long delays, use the delays in a loop with periodic calling of the `hn.spinOnce()` function:

```cpp
// 8 second delay
for(int i=0; i<8; i++) {
  delay(1000);
  nh.spinOnce();
}
```

## Working with Clover

The set of services and topics is similar to the regular set in [simple_offboard](simple_offboard.md) and [mavros](mavros.md).

An example of a program that controls the copter by position using the `navigate` and `set_mode` services:

```cpp
// Connecting libraries for working with rosserial
#include <ros.h>

// Connecting Clover and MAVROS package message header files
#include <clover/Navigate.h>
#include <mavros_msgs/SetMode.h>

using namespace clover;
using namespace mavros_msgs;

ros::NodeHandle nh;

// Declaring services
ros::ServiceClient<Navigate::Request, Navigate::Response> navigate("/navigate");
ros::ServiceClient<SetMode::Request, SetMode::Response> setMode("/mavros/set_mode");

void setup()
{
  // Initializing rosserial
  nh.initNode();

  // Initializing services
  nh.serviceClient(navigate);
  nh.serviceClient(setMode);

  // Waiting for connection to Raspberry Pi
  while(!nh.connected()) nh.spinOnce();
  nh.loginfo("Startup complete");

  // Custom settings
  // <...>

  // Test program
  Navigate::Request nav_req;
  Navigate::Response nav_res;
  SetMode::Request sm_req;
  SetMode::Response sm_res;

  // Ascending to 2 meters:
  nh.loginfo("Take off");
  nav_req.auto_arm = false;
  nav_req.x = 0;
  nav_req.y = 0;
  nav_req.z = 2;
  nav_req.frame_id = "body";
  nav_req.speed = 0.5;
  navigate.call(nav_req, nav_res);

  // Waiting for 5 seconds
  for(int i=0; i<5; i++) {
  	delay(1000);
  	nh.spinOnce();
  }

  nav_req.auto_arm = false;

  // Flying forward 3 meters:
  nh.loginfo("Fly forward");
  nav_req.auto_arm = true;
  nav_req.x = 3;
  nav_req.y = 0;
  nav_req.z = 0;
  nav_req.frame_id = "body";
  nav_req.speed = 0.8;
  navigate.call(nav_req, nav_res);

  // Waiting for 5 seconds
  for(int i=0; i<5; i++) {
    delay(1000);
    nh.spinOnce();
  }

  // Flying to point 1:0:2 in the marker field
  nh.loginfo("Fly on point");
  nav_req.auto_arm = false;
  nav_req.x = 1;
  nav_req.y = 0;
  nav_req.z = 2;
  nav_req.frame_id = "aruco_map";
  nav_req.speed = 0.8;
  navigate.call(nav_req, nav_res);

  // Waiting for 5 seconds
  for(int i=0; i<5; i++) {
    delay(1000);
    nh.spinOnce();
  }

  // Landing
  nh.loginfo("Land");
  sm_req.custom_mode = "AUTO.LAND";
  setMode.call(sm_req, sm_res);
}

void loop()
{
}
```

## Getting telemetry

With Arduino, you can use the [`get_telemetry` service](simple_offboard.md). To do so, declare it similar to the `navigate` and `set_mode` services:

```cpp
#include <ros.h>

// ...

#include <clover/GetTelemetry.h>

// ...

ros::ServiceClient<GetTelemetry::Request, GetTelemetry::Response> getTelemetry("/get_telemetry");

// ...

nh.serviceClient(getTelemetry);

// ...

GetTelemetry::Request gt_req;
GetTelemetry::Response gt_res;


// ...

gt_req.frame_id = "aruco_map"; // frame id for x, y, z
getTelemetry.call(gt_req, gt_res);

// gt_res.x is copter position on the x axis
// gt_res.y is copter position on the y axis
// gt_res.z is copter position on the z axis
```

## Problem

When using Arduino Nano, RAM may be insufficient. In this case, messages will appear in the Arduino IDE like:

```
Global variables use 1837 bytes (89%) of the dynamic memory, leaving 211 bytes for local variables. The maximum is 2048 bytes.
Not enough memory, the program may be unstable.
```

You can reduce RAM usage by reducing the size of the buffers allocated for sending and receiving messages. To do this, place the following line **at the beginning** the program:

```cpp
#define __AVR_ATmega168__ 1
```

You can reduce the amount of used memory even more, if you manually configure the number publishers and subscribers, as well as the size of memory buffers allocated for messages, for example:

```cpp
#include <ros.h>

// ...

typedef ros::NodeHandle_<ArduinoHardware, 3, 3, 100, 100> NodeHandle;

// ...
NodeHandle nh;
```
