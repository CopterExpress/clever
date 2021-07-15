# Simulation overview

The Clover simulation environment allows users to run and debug their code within a simulator while using most of the features available on the real drone. The simulation utilizes [PX4 SITL mode](sitl.md) and uses the same ROS code as the real drone. Most hardware is simulated as well.

<img src="../assets/simulator.jpg" width=600 class=center>

## Features

Basic, user-installable environment includes:

* high-quality Clover 4 visual model;
* Gazebo plugins for Clover-specific hardware (e.g. LED strip);
* modification-friendly [`xacro`](https://wiki.ros.org/xacro) drone descriptions;
* sample models and worlds;
* [`roslaunch`](https://wiki.ros.org/roslaunch) files for quick simulation launching and configuration.

Additionally, a [virtual machine image](simulation_vm.md) that mimics the real drone as closely as possible is provided with the following features:

* easy access to the simulation environment;
* Visual Studio Code editor, preconfigured to work with ROS packages;
* Monkey web server for web-based Clover plugins;
* always-running `roscore` service;
* ROS GUI tools (`rviz`, `rqt`).

## Architecture

The simulation environment is based on the following components:

* [Gazebo](http://gazebosim.org/), a state-of-the-art robotics simulator;
* [PX4](https://px4.io/), specifically its SITL (software-in-the-loop) components;
* [`sitl_gazebo`](https://github.com/PX4/sitl_gazebo) package containing Gazebo plugins for PX4;
* ROS packages and Gazebo plugins.

<!-- TODO: Write more, add a diagram, etc -->

## Video

Short video review of the simulator:

<iframe width="560" height="315" src="https://www.youtube.com/embed/8HYXREMDfzQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
