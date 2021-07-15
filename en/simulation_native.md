# Native setup

Setting up the simulation environment from scratch requires some effort, but results in the most performant setup, with less chance of driver issues.

Prerequisites: Ubuntu 18.04, [native ROS installation](ros-install.md).

## Create a workspace for the simulation

Throughout this guide we will be using the `catkin_ws` as the workspace name. Feel free to change it in your setup. We will be creating it in the home directory of the current user (`~`).

Create the workspace and clone Clover sources:

```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
git clone https://github.com/CopterExpress/clover
git clone https://github.com/CopterExpress/ros_led
```

Install all prerequisites using `rosdep`:

```bash
cd ~/catkin_ws
rosdep update
rosdep install --from-paths src --ignore-src -y
```

## Get PX4 sources

PX4 will be built along with the other packages in our workspace. You may clone it directly into the workspace or put it somewhere and symlink to `~/catkin_ws/src`. We will need to put its `sitl_gazebo` submodule in `~/catkin_ws/src` as well. For simplicity's sake we will clone the firmware directly to the workspace:

```bash
cd ~/catkin_ws/src
git clone --recursive https://github.com/CopterExpress/Firmware -b v1.10.1-clever
ln -s Firmware/Tools/sitl_gazebo ./sitl_gazebo
```

## Install PX4 prerequisites

PX4 comes with its own script for dependency installation. We may as well leverage it:

```bash
cd ~/catkin_ws/src/Firmware/Tools/setup
sudo ./ubuntu.sh
```

This will install everything required to build PX4 and its SITL environment.

You may want to skip installing the ARM toolchain if you're not planning on compiling PX4 for your flight controller. To do this, use the `--no-nuttx` flag:

```
sudo ./ubuntu.sh --no-nuttx
```

## Patch Gazebo plugins

The `sitl_gazebo` package containing required Gazebo plugins needs patching due to recent changes in MAVLink. These patches are already preapplied in the [virtual machine image](simulation_vm.md) and are stored in the VM repository. Run the following commands to download and apply the patches:

```bash
cd ~/catkin_ws/src/Firmware/Tools/sitl_gazebo
wget https://raw.githubusercontent.com/CopterExpress/clover_vm/master/assets/patches/sitl_gazebo.patch
patch -p1 < sitl_gazebo.patch
rm sitl_gazebo.patch
```

## Install geographiclib datasets

`mavros` requires geographiclib datasets to be present:

```bash
cd ~
wget https://raw.githubusercontent.com/mavlink/mavros/6f5bd5a1a67c19c2e605f33de296b1b1be9d02fc/mavros/scripts/install_geographiclib_datasets.sh
chmod +x ./install_geographiclib_datasets.sh
sudo ./install_geographiclib_datasets.sh
rm ./install_geographiclib_datasets.sh
```

## Build the simulator

With all dependencies installed, you can build your workspace:

```bash
cd ~/catkin_ws
catkin_make
```

> **Note** Some of the files - particularly Gazebo plugins - require large amounts of RAM to be built. You may wish to reduce the number of parallel jobs; the number of parallel jobs should be equal to the amount of RAM in gigabytes divided by 2 - so a 16GB machine should use no more than 8 jobs. You can specify the number of jobs using the `-j` flag: `catkin_make -j8`

## Run the simulator

In order to be sure that everything was built correctly, try running the simulator for the first time:

```bash
source ~/catkin_ws/devel/setup.bash
roslaunch clover_simulation simulator.launch
```
