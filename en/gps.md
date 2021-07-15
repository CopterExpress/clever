Connecting GPS
==

Upon connecting GPS, the following possibilities appear:

* The copter can remain at the same point when flying outside
* Autonomous missions may be programmed in the QGroundControl application
* Flying may be performed by global points in standalone mode using the [simple_offboard](simple_offboard.md) module.

Useful links:

* https://docs.px4.io/en/assembly/quick_start_pixhawk.html
* http://ardupilot.org/copter/docs/common-pixhawk-wiring-and-quick-start.html
* http://ardupilot.org/copter/docs/common-installing-3dr-ublox-gps-compass-module.html

Connection
---

The GPS module is connected to "GPS" and "I2C" (compass) connectors of the flight controller.

If GPS is connected, magnetometers are to be re-calibrated in the QGroundControl application via a [Wi-Fi](wifi.md) or USB connection.

Next, GPS is to be enabled in parameter `EKF2_AID_MASK` (when EKF2 is used) or `LPE_FUSION` (when LPE is used). When using LPE the weight of the magnetometer should be more 0 (`ATT_W_MAG` = 0.1).
