# Step-by-step guide on autonomous flight with Clover 4

> **Note** The following applies to [image version](image.md) **0.20** and up. See [previous version of the article](https://github.com/CopterExpress/clover/blob/v0.19/docs/en/auto_setup.md) for older images.

This manual contains links to other articles in which each of the topics addressed is discussed in more detail. If you encounter difficulties while reading one of these articles, it is recommended that you return to this manual, since many operations here are described step by step and some unnecessary steps are skipped.

## Raspberry Pi initial setup

- Install Raspberry Pi and a camera on the drone according to the [manual](assemble_4_2.md#installing-the-raspberry-pi).
- Download the system image [here](image.md).
- Burn the image to the microSD card.
- Insert the card into Raspberry Pi.
- Connect power to Raspberry Pi and wait for the Wi-Fi network to appear. To do this, connect the Raspberry Pi to the computer via the microUSB cable.
   On Raspberry Pi, the green LED should flash blink. It shows that Raspberry Pi works properly.

  > **Warning** Before connecting the Raspberry Pi to the computer via USB, you need to remove the 5V power cable from Raspberry Pi. Otherwise, there may be problems with power.

- Connect to Wi-Fi and open the web interface ([this article](wifi.md)).

   After the first power-up, the network appears with a delay. You need to wait until the system is fully loaded. If the Clover network does not appear in the list of networks for a long time, reopen the window with the network selection. Then the list of networks will be updated.

> **Hint** Now if you have connected to the Clover's Wi-Fi network, it is recommended to open the [local version of this guide](http://192.168.11.1/docs/ru/auto_setup.html), otherwise the links will not work.

- Connect to Raspberry Pi via SSH.

   Web access is the easiest way. Follow the instructions in the article [SSH Access](ssh.md).

- You can change the name and password of the network if you want to. See the article "[Network Settings] (network.md # change-password-or-ssid-network-name)". The remaining operations with the network are unnecessary.

- Use the nano editor to edit files. [Instructions for working with nano](cli.md#editing).

  > **Hint** In nano, you can only move the cursor with the arrow keys on the keyboard.

- Reboot Raspberry Pi:

  ```bash
  sudo reboot
  ```

  The connection will temporary close, a new network will be created and you will need to reconnect to it.

- Make sure that the camera is working correctly. Follow the link http://192.168.11.1:8080 and click `image_raw`.

  For more information read "[Viewing images from cameras](web_video_server.md)".

  If the image is blurry, you need to focus the lens. To do this, twist the lens in one or the other direction. Continue to twist until the image becomes clear.

  > **Hint** The red LED on the camera should be lit: it means that the camera is currently capturing image. If the LED does not light: either the camera is connected incorrectly, or the operating system did not boot yet, or there is an error in settings.

## Basic commands

You will need the basic Linux commands, as well as special Clover commands, to work efficiently in the system.

Show list of files and folders:

```bash
ls
```

Go to certain directory by entering the path too it (catkin_ws/src/clover/clover/launch/):

```bash
cd catkin_ws/src/clover/clover/launch/
```

Go to home directory:

```bash
cd
```

Open the file `file.py`:

```bash
nano file.py
```

Open the file clover.launch by entering the full path to it (it works even if you're in a different directory):

```bash
nano ~/catkin_ws/src/clover/clover/launch/clover.launch
```

Save file (press sequentially):

```bash
Ctrl+X; Y; Enter
```

Delete a file or folder called `name` (WARNING: the operation will not request confirmation. Be careful!):

```bash
rm -rf name
```

Make a new directory called `myfolder`:

```bash
mkdir myfolder
```

Raspberry Pi complete reboot:

```bash
sudo reboot
```

Reboot only the `clover` service:

```bash
sudo systemctl restart clover
```

Perform selfcheck:

```bash
rosrun clover selfcheck.py
```

Stop a program:

```bash
Ctrl+C
```

Start a program `myprogram.py` using Python:

```bash
python3 myprogram.py
```

Journal of the events related to `clover` package. Scroll the list by pressing Enter or Ctrl+V (scrolls faster):

```bash
journalctl -u clover
```

Open the sudoers file with super user rights (this particular file doesn't open without sudo. You can use sudo to open other locked files or run programs that require super user rights):

```bash
sudo nano /etc/sudoers
```

## Setting Raspberry Pi for autonomous flight

Most of the parameters for autonomous flight are located in the following directory: `~/catkin_ws/src/clover/clover/launch/`.

- Enter the directory:

  ```bash
  cd ~/catkin_ws/src/clover/clover/launch/
  ```

  The `~` symbol stands for home directory of your user. If you are already in the directory, you can go with just the command:

  ```bash
  cd catkin_ws/src/clover/clover/launch/
  ```

  > **Hint** Tab can automatically complete the names of files, folders or commands. You need to start entering the desired name and press Tab. If there are no conflicts, the name will be auto completed. For example, to quickly enter the path to the `catkin_ws/src/clover/clover/launch/` directory, after entering `cd`, you can start typing the following key combination:`c-Tab-s-Tab-c-Tab-c-Tab-l-Tab`. This way you can save a lot of time when writing a long command, and also avoid possible mistakes in writing the path.

- In this folder you need to configure three files:

  - `clover.launch`
  - `aruco.launch`
  - `main_camera.launch`

- Open the file `clover.launch`:

  ```bash
  nano clover.launch
  ```

  You must be in the directory in which the file is located. If you are in other directory, you can open the file by writing the full path to it:

  ```bash
  nano ~/catkin_ws/src/clover/clover/launch/clover.launch
  ```

  If two users are editing a file at the same time, or if previously the file was closed incorrectly, nano will not display the file contents, it will ask for permission to display the file. To grant permission, press Y.

  If the content of a file is still empty, you may have entered the file name incorrectly. You need to pay attention to the extension. If you entered a wrong name or extension, nano will create a new empty file named this way, which is undesirable. Such file should be deleted.

- Find the following line in clover.launch file:

  ```xml
  <arg name="aruco" default="false"/>
  ```

  Replace `false` with `true`:

  ```xml
  <arg name="aruco" default="true"/>.
  ```

  This will activate the ArUco marker detection module.
- Open the file `aruco.launch`:

  ```bash
   nano aruco.launch
  ```

- Here you need to activate some parameters. Go to the [article](aruco_map.md) for more detail.

  Here is what you should get:

  ```xml
  <arg name="aruco_detect" default="true"/>
  <arg name="aruco_map" default="true"/>
  <arg name="aruco_vpe" default="true"/>`
  ```

- Generate the ArUco markers field. See the article [Map-based navigation with ArUco markers] (aruco_map.md # marker map settings) for details. To generate markers, you need to enter a command with specific values.

  Here is the example generating command where:

  - marker length = 0.335 m (`length`)
  - 10 columns (x)
  - 10 rows (y)
  - distance between markers on the x axis = 1 m (`dist_x`)
  - distance between markers on the y axis = 1 m (`dist_y`)
  - the first marker's ID = 0 (`first`)
  - the marker map name is default: map.txt
  - the marker map numbering is from the top left corner (key `--top-left`)

  ```bash
  rosrun aruco_pose genmap.py 0.335 10 10 1 1 0 > ~/catkin_ws/src/clover/aruco_pose/map/map.txt --top-left
  ```

  In most maps, numbering starts with a zero marker. Also, in most cases, numbering starts from the upper left corner, so when generating, it is very important to enter the key `--top-left`.

  > **Hint** If you choose a different name for your ArUco map, you also need to  change it in the `aruco.launch`. Find the line
`<param name="map" value="$(find aruco_pose)/map/map.txt"/>`
and replace map.txt with your map name.

- Edit the `main_camera.launch` for setting up the camera:

  Read more in the article. "[Camera orientation](camera_setup.md)".

  In this file, you need to edit the line with the camera location parameters. The line looks like this:

  ```xml
  <node pkg="tf2_ros" type="static_transform_publisher" name="main_camera_frame" args="0.05 0 -0.07 -1.5707963 0 3.1415926 base_link main_camera_optical"/>
  ```

  In the file you will find many lines similar to this, but most of them are commented out (i.e. not readable) and only one is uncommented. These are pre-configured settings from which you can choose the one you need.

  Comment in XML is `<!--` at the beginning of a line and   `-->` at the end of a line. An example of a commented line:

  ```xml
  <!--<node pkg="tf2_ros" type="static_transform_publisher" name="main_camera_frame" args="0.05 0 -0.07 -1.5707963 0 3.1415926 base_link main_camera_optical"/>-->
  ```

  An example of an uncommented line (the line will be read by the program):

  ```xml
  <node pkg="tf2_ros" type="static_transform_publisher" name="main_camera_frame" args="0.05 0 -0.07 -1.5707963 0 3.1415926 base_link main_camera_optical"/>
  ```

  The writing above each of these lines indicates which camera position the line corresponds to. If the camera cable goes forward relative to the drone, and the camera is pointing down, you need to select the following setting:

  ```xml
  <!-- camera is oriented downward, camera cable goes forward  [option 2] -->
  ```

  To select the desired setting, you need to uncomment the corresponding line, and comment out another similar line so that there are no conflicts.

- Save changes. Press sequentially:

  ```
  Ctrl+x; y; Enter
  ```

- Restart the `clover` service:

  ```bash
  sudo systemctl restart clover
  ```

## Setting the flight controller

- Flash the flight controller with modified firmware. You can download it [here](setup.md) in the section "Flashing the flight controller".

- Instructions for flashing and calibrating the flight controller are in the same article.

> **Warning** Don't forget to choose the downloaded firmware when you flash the flight controller.

## Connecting the flight controller with Raspberry Pi

- Connect the Raspberry Pi and the Pixracer via the microUSB cable. The cable should be tightly fastened and passed through the bottom of the drone to not get into the propellers.

- Connect remotely to the flight controller through QGroundControl.

  All the necessary settings for that are already set in Clover. Now you need to create a new connection in QGroundControl. Use the settings from [this article](gcs_bridge.md).

## Remote controller setup

- Flight modes setup is described in the article "[Flight modes](modes.md)".

  Set channel 5 to SwC switch; channel 5 to SwA switch. Or you can use any other switches you like.

## Clover selfcheck

Perform selfcheck when you have set up your drone or when you have faced problems. The selfcheck process is described in the article "[Automated self checks](selfcheck.md)"

- Run the command:

  ```bash
  rosrun clover selfcheck.py
  ```

## Writing a program

The article "[Simple OFFBOARD](simple_offboard.md)" describes working with `simple_offboard` module that helps to easily program a drone. All the basic flight functions are described in this article, as well as code snippets.

- Copy the Python code example from "The use of Python language" section and paste in code editor (e.g. Visual Studio Code, PyCharm, Sublime Text, Notepad++)
- Save the document with .py extension for highlighting the code.
- Add flight logic. The examples of such functions are given in the article. You need to call functions for taking off, flying to point and landing.
- Taking off.

  Use `navigate` function to take off. Add this line at the bottom of the program.

  ```python
  navigate(x=0, y=0, z=1.5, speed=0.5, frame_id='body', auto_arm=True)
  ```

  Add this line to add delay to the program. It gives you time for doing previously called operation.

  ```python
  rospy.sleep(3)
  ```

> **Hint** It is important to allocate time to execute the `navigate` function, otherwise the drone, without waiting for the previous command to execute, will immediately proceed to the next. For allocating time, use the `rospy.sleep ()` command. The time in seconds is indicated in parentheses. The function `rospy.sleep ()` refers to the previous `navigate` command, and not to the next. This is the time we give to fly to the point indicated in previous `navigate` (the one that is just above the `rospy.sleep ()` ).

- Set the drone's position in the marker field coordinate system.

  For doing that you need to call a `navigate`, set the coordinates and coordinate system (`frame_id`):

  ```python
  navigate(x=1, y=1, z=1.5, speed=1, frame_id='aruco_map')
  ```

- As the result you get:

  ```python
  navigate(x=0, y=0, z=1.5, speed=0.5, frame_id='body', auto_arm=True)
  rospy.sleep(3)
  navigate(x=1, y=1, z=1.5, speed=1, frame_id='aruco_map')
  rospy.sleep(5)
  ```

  > **Warning** Note that the parameter `auto_arm=True` is only set once on the first takeoff. In other cases it should not be set True because it prevents overtaking the control.

- If you want to add other points for the drone's mission, add another `navigate` and `rospy.sleep()`. Calculate time individually for each point, depending on the speed of flight and the distance between two points.

  If you want to add the points with coordinates (3, 3, 1.5):

  ```python
  navigate(x=3, y=3, z=1.5, speed=1, frame_id=‘aruco_map’)
  rospy.sleep(3)
  ```

  > **Warning** Coordinates should not exceed the size of your field. If the field is 4x4 meters in size, the maximum coordinate value is 4.

- After reaching all of the points you need to land. The following line is placed at the end of the program:

  ```
  land()
  ```

## Writing the program to the drone

The easiest way to send the program is to copy the content of the program, create a new file in the command line and paste the program text into the file.

- To create the file `myprogram.py`, run the command:

  ```bash
  nano myprogram.py
  ```

  You can select any name you want, but it is not recommended to use spaces and special characters. In addition, the program extension should always end with `.py`

- Paste text in the input field. If you use Butterfly web access on Windows or Linux:

  ```
  Ctrl+Shift+V
  ```

  On Mac you can click `Cmd+v`.

- Save the file:

  ```
  Ctrl+x; Y; Enter
  ```

## Starting the program

- It is necessary to carefully prepare the drone, remote control and program before you fly autonomously. Run `selfcheck.py`. Make sure the drone flies well in manual mode.
- Turn on the drone and wait for the system to boot. A red light on the camera means that the system has booted.
- Check drone's flight in POSCTL mode.
- To do this, take off above the markers in STABILIZED mode and turn the SwC switch (or the one you have set) to the lower position - POSCTL mode.

  > **Warning** You need to be ready to immediately switch back to STABILIZED mode if the drone gets out of control!

  Set the left stick (throttle) to the middle position. The drone has to hover in place. If so, you can land the drone and proceed to the next step. If not, you need to find the reason for the problem.

- Before you start your program, set the SwC switch to the middle position. It will help you to take control of the drone. For taking control, switch your mode switch (SwC by default) to any other flight mode.
- Set the left stick (throttle) to the middle position so that in case of taking control the drone won't fall down.

- Run the program:

  ```bash
  python3 my_program.py
  ```

  > **Warning** After completion of the program , the drone can land incorrectly and continue to fly over the floor. In this case, you need to intercept control.

- If you want to stop the program before it ends, press `Ctrl+C`. If didn't work, press `Ctrl+Z`, but it is not recommended.
