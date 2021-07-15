Copter Hack 2017
===

On July 28 – 30, 2017, Copter Express held a hackathon named "Copter Hack 2017", where the objective was to program a Clover to dance-fly autonomously to random music.

The team "Pangolins" became the winners.

<iframe width="560" height="315" src="https://www.youtube.com/embed/xgXheg3TTs4?rel=0" frameborder="0" allowfullscreen></iframe>

Video lectures are available at https://copterexpress.timepad.ru/event/510375/.

Modules
---

* Navigation in the marker field and simplified copter control: https://github.com/CopterExpress/marker_navigator (installed on the flash drive)

* ROS module for communication with the music server https://github.com/CopterExpress/copter_hack_music (installed on a flash drive)

* the source of the music server https://github.com/CopterExpress/copter_hack_music_server

Viewing video from the camera
---

To run on Raspberry:

```(bash)
rosrun web_video_server web_video_server
```

In the browser, open webpage ``http://<ip raspberry>:8080``.

**Attention**: Video stream distribution greatly reduces the performance of marker recognition for the flight.

SSID Wi-Fi
---

To change the SSID of distributed Wi-Fi you should change the SSID parameter in any way in file``/etc/hostapd/hostapd.conf``.

The list of recognized markers
---

```(bash)
rostopic echo /marker_data
```

Helpful articles
---

* [Copter setup](setup.md)

* [Flight modes](modes.md)

* [MAVRos package](mavros.md)

* A good introductory article: https://habrahabr.ru/post/227425/

* Signals used in drones: https://geektimes.ru/post/258186/

* A good article about PIDs: https://habrahabr.ru/company/technoworks/blog/216437/

* Video lectures are available at https://copterexpress.timepad.ru/event/510375/.

* [Aubio](https://aubio.org), a library for sound (music) analysis

* Packages for Python for working with music: https://wiki.python.org/moin/PythonInMusic
