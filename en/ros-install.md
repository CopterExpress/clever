# ROS Melodic package installation and setup

In order to use tools such as rqt, rviz and others as well as running the simulator (SITL), you will need to install and setup ROS package

> **Hint** For more details on installation refer to [the main article](http://wiki.ros.org/melodic/Installation/Ubuntu).

## ROS Melodic installation on Ubuntu

To find the correct package version, you will need to change the settings of your repositories. Go to "Software and updates" and enable `restricted`, `universe` and `multiverse`.

Set up your system so that software form `packages.ros.org` can be installed :

```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

Configure access keys in your system for correct download:

```bash
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
```

Make sure that your packages are up to date:

```bash
sudo apt-get update
```

Now you can install the ROS package itself.

+ If you plan to use ROS together with the simulator (also includes tools such as rqt, rviz and others):

    ```bash
    sudo apt-get install ros-melodic-desktop-full
    ```

+ If you plan to use ROS exclusively for tools rqt, rviz etc.:

    ```bash
    sudo apt-get install ros-melodic-desktop
    ```

After the package has installed, initialize `rosdep`.
Package `rosdep` will allow to easily install dependencies for the source files that you whish to compile. Running some essential components of ROS will as well require this package.

```bash
sudo rosdep init
rosdep update
```

If you are not comfortable with entering environment variables manually each time, you may configure it in a way that it add itself in your bash session on every new shell startup:

```bash
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

If you whish to install any additional packages for your ROS Melodic simply use:

```bash
sudo apt-get install ros-melodic-PACKAGE
```
