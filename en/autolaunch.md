Software autorun
===

> **Note** In the image version **0.20** `clever` package and service was renamed to `clover`. See [previous version of the article](https://github.com/CopterExpress/clover/blob/v0.19/docs/en/autolaunch.md) for older images.

systemd
---

Main documentation: [https://wiki.archlinux.org/index.php/Systemd_(Russian)](https://wiki.archlinux.org/index.php/Systemd_(Russian)).

All automatically started Clover software is launched as a `clover.service` systemd service.

The service may be restarted by the `systemctl` command:

```(bash)
sudo systemctl restart clover
```

Text output of the software can be viewed using the `journalctl` command:

```(bash)
journalctl -u clover
```

To run Clover software directly in the current console session, you can use the `roslaunch` command:

```(bash)
sudo systemctl restart clover
roslaunch clover clover.launch
```

You can disable Clover software autolaunch using the `disable` command:

```(bash)
sudo systemctl disable clover
```

roslaunch
---

Main documentation: http://wiki.ros.org/roslaunch.

The list of nodes / programs declared for running is specified in file `/home/pi/catkin_ws/src/clover/clover/launch/clover.launch`.

You can add your own node to the list of automatically launched ones. To do this, place your executable file (e.g. `my_program.py`) into folder `/home/pi/catkin_ws/src/clover/clover/src`. Then add the start of your node to `clover.launch`, for example:

```xml
<node name="my_program" pkg="clover" type="my_program.py" output="screen"/>
```

The started file must have *permission* to run:

```(bash)
chmod +x my_program.py
```

When scripting languages are used, [shebang] should be placed at the beginning of the file (https://ru.wikipedia.org/wiki/Shebang_(Unix)), for example:

```(bash)
#!/usr/bin/env python
```
