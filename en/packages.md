# COEX packages repository

COEX provides an open [Debian-repository](https://wiki.debian.org/DebianRepository) with ROS Noetic related prebuilt binary pacakges for `armhf` architecture.

> **Info** Repository URL: http://packages.coex.tech.

The repository is already addedd in [RPi image](image.md) and may be used for simple installation of additional ROS packages.

## Packages publishing

You can make a Pull Request in a [git repository with packages](https://github.com/CopterExpress/packages), adding or updating your package (a file with `.deb` extension), that relates to Clover or ROS. After merging your package will be available for installation with `apt` utility:

```bash
sudo apt install ros-noetic-clover-some-feature
```

Packages, that extend Clover functionality are recommended to be named with `clover_` prefix, e. g. `clover_some_feature`.

## Using on a normal Raspberry Pi OS

On a normal Raspberry Pi OS, the repository may be added to the sources list, this way:

```bash
wget -O - 'http://packages.coex.tech/key.asc' | apt-key add - 
echo 'deb http://packages.coex.tech buster main' >> /etc/apt/sources.list
sudo apt update
```
