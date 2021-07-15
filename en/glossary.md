# Glossary

## Drone

An unmanned aircraft. Typical examples are: quadrotors, hexacopters, model airplanes, fixed wings, VTOLs, model helicopters.

## Quadcopter

An unmanned aerial vehicle with 4 propellers and an electronic stabilization system.

## Multicopter

An unmanned aerial vehicle with an electronic stabilization system and the number of propellers equal to 3 (tricopter), 4 (quadcopter), 6 (hexacopter), 8 (octocopter), or more.

## Flight controller / autopilot

**1\.** A specialized circuit-board designed for controlling a multicopter, a plane or another vehicle. Examples:
Pixhawk, ArduPilot, Naze32, CC3D.

**2\.** Software for the multicopter control circuit-board. Examples: PX4, APM, CleanFlight, BetaFlight.

## Firmware

Software primarily for embedded systems, for example, a flight controller or an ESC.

## Motor

An electric motor that rotates propellers of the multicopter. Brushless motors are commonly used. These motors require an ESC.

## ESC / motor controller

An Electronic Speed Controller. A specialized circuit-board that controls the speed of the brushless motor. It is controlled by a flight controller using pulse width modulation (PWM).

ESC has the firmware that determines the characteristics of its operation.

## Battery

A rechargeable power source for the drone. Quadrotors typically use LiPo (lithium-ion polymer) batteries.

## Battery cell

Single element of the battery pack. Typical drone batteries contain several (2 to 6) cells connected in series. Maximum LiPo cell voltage is 4.2 v; battery voltage is a sum of each cell's voltage (if they are connected in series). The number of cells connected in series is marked by the letter *S*, as in *2S* (two cells in series), *3S*, *4S*.

Clover kits typically use *3S* batteries.

## Remote control / radio control equipment

A radio-operated quadcopter remote control. Operation of the remote control requires connecting a receiver to the flight controller.

Clover may also be [controlled from a smartphone](rc.md).

## Telemetry

**1\.** Transmitting the data about the state of a quadcopter or another aircraft over a distance.

**2\.** The data about the aircraft state (height, orientation, global coordinates, etc.).

**3\.** A system for transmitting the data about the  aircraft state or commands to it over the air. Examples: radio modems (RFD900, 3DR Radio Modem), Wi-Fi modules (ESP-07). Raspberry Pi may also be used in Clover as a telemetry module: [the use of QGroundControl via Wi-Fi](gcs_bridge.md).

## Arming

Armed is the state of copter readiness for the flight. When the gas stick is lifted, or when an external command with the target point is sent, the copter will fly. Usually, a copter starts rotating its propellers when it is switched to the "armed" state, even if the gas stick is down.

The opposite state is Disarmed.

## PX4

A popular open source flight controller software that works with the Pixhawk series of flight controllers, Pixracer, and others. PX4 is recommended to be used with Clover.

## Raspberry Pi

[A popular single-board computer](raspberry.md) that is used in the Clover kit.

## SD card image

A complete digital copy of SD card contents stored in a single file. This file may be written to an SD card using special software like Etcher. A Raspberry Pi's SD card is the only long-term memory of the single-board computer.

The Clover kit includes a [recommended SD card image](image.md)

## APM / ArduPilot

An open source flight controller originally created for the Arduino boards. It was later ported to Pixhawk, Pixracer and other boards.

## MAVLink

A communication protocol for drones, ground stations and other devices over radio channels. This protocol is widely used for telemetry.

## ROS

A popular framework for writing complex robotics applications.

## MAVROS

A library that is a link between the aircraft operating using the MAVLink protocol, and ROS.

## UART

A serial asynchronous data transfer interface used in many devices. For example, GPS antennas, Wi-Fi routers, or Pixhawk.

## IMU

Inertial measurement unit. A set of inertial sensors (a gyroscope and an accelerometer; a magnetometer is typically added as well) that allow the drone to compute its orientation (and, to a lesser extent, position) in space.

## Estimation

A process of current state (position, rotation, velocity, angular rates, etc.) estimation performed by the flight controller software. A [Kalman Filter](https://en.wikipedia.org/wiki/Kalman_filter) is typically used for sensor fusion; other filters are typically applied to raw sensor data.

PX4 has two estimation modules: LPE and [ECL EKF](https://dev.px4.io/en/tutorials/tuning_the_ecl_ekf.html) (EKF2).

APM utilizes its [EKF2](http://ardupilot.org/dev/docs/ekf2-estimation-system.html) subsystem.
