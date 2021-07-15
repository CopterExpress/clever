# Hostname

> **Note** The following applies to [image version](image.md) **0.20** and up. See [previous version of the article](https://github.com/CopterExpress/clover/blob/v0.19/docs/en/hostname.md) for older images.

[By default](image.md) the hostname of the Clover drone is set to `clover-xxxx`, where `xxxx` are random numbers. These numbers are the same as in the [Wi-Fi SSID](wifi.md).

Thus, Clover is accessible on machines that support mDNS as `clover-xxxx.local`. You can use this name to access Clover over SSH:

```bash
ssh pi@clover-xxxx.local
```

Also, this name can be used in place of IP-address to open Clover web pages in browser, accessing ROS master, etc.

## Changing hostname

In some situations it is necessary to change Clover's hostname. You can use the `hostnamectl` utility for that:

```bash
sudo hostnamectl set-hostname newname
```

Where `newname` is the new name of the machine. `hostnamectl` utility will change the name in `/etc/hostname` file.

You should also put the new name to `/etc/hosts` file:

```txt
127.0.1.1	newname newname.local
```

Setting `newname.local` is necessary to allow ROS to resolve this name in situations where all the network interfaces are down (when Wi-Fi is turned off or disconnected).

> **Note** Changing the hostname does not affect the Wi-Fi SSID (and vice versa, changing the Wi-Fi SSID won't affect the hostname).
