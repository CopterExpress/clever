# Connecting Raspberry Pi to the flight controller

In order to program [autonomous flights](simple_offboard.md), [work with Pixhawk or Pixracer over Wi-Fi](gcs_bridge.md), use [controller app](rc.md) and access other functions you need to connect your Raspberry Pi to the flight controller.

## USB connection

USB connection is the preferred way to connect to the flight controller.

1. Connect your FCU to the Raspberry Pi using a microUSB to USB cable.
2. [Connect to the Raspberry Pi over SSH](ssh.md).
3. Make sure the connection is working by [running the following command on the Raspberry Pi](ssh.md):

    ```bash
    rostopic echo /mavros/state
    ```

    The `connected` field should have the `True` value.s

> **Hint** You need to set the `CBRK_USB_CHK` [parameter](px4_parameters.md) to 197848 for the USB connection to work.

## UART connection

> **Note** In the image version **0.20** `clever` package and service was renamed to `clover`. See [previous version of the article](https://github.com/CopterExpress/clover/blob/v0.19/docs/en/connection.md) for older images.

<!-- TODO: Connection scheme -->

UART connection is another way for the Raspberry Pi and FCU to communicate.

1. Connect Raspberry Pi to your FCU using a UART cable.
2. [Connect to the Raspberry Pi over SSH](ssh.md).
3. Change the connection type in `~/catkin_ws/src/clover/clover/launch/clover.launch` to UART:

    ```xml
    <arg name="fcu_conn" default="uart"/>
    ```

    Be sure to restart the `clover` service after editing the .launch file:

    ```bash
    sudo systemctl restart clover
    ```

> **Hint** Set the `SYS_COMPANION` PX4 parameter to 921600 to enable UART on the FCU.

## SITL connection

In order to connect to a local or a remote [SITL](sitl.md) instance set the `fcu_conn` parameter to `udp` and `fcu_ip` to the IP address of the SITL instance (`127.0.0.1` if you are running the instance locally):

```xml
<arg name="fcu_conn" default="udp"/>
<arg name="fcu_ip" default="127.0.0.1"/>
```

**Next**: [Using QGroundControl over Wi-Fi](gcs_bridge.md)
