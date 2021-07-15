# RC setup

<img src="../assets/en/consistofTransmitter.jpg" class="zoom">

Before connecting and calibrating the RC, make sure that:

* There is no battery connected to the drone.
* The propellers are not mounted.

## Connecting the RC transmitter

1. Open the *Vehicle Setup* tab and select the *Radio* menu.
2. Power on the transmitter by sliding the **POWER** slider up.
3. Make sure the transmitter-receiver link is working.

    The transmitter LCD screen should display the connection:

    <img src="../assets/connectionOK.jpg" class="zoom">

    The LED on the receiver should glow steadily. Read the [radio troubleshooting article](radioerrors.md) if the link does not work.

## Transmitter calibration

1. Press the *Calibrate* button.
2. Set the *Throttle*, *Yaw*, *Pitch*, and *Roll* trims to 0
    * Trims are small constant offsets applied to a control in order to make your drone fly correctly.
    * Move the trimming slider to the center using trimming buttons until you hear a long beep. Do this for each axis.
3. Press *OK* in QGroundControl.

    <img src="../assets/qgc-radio.png" class="zoom">

4. Place the left stick (throttle) in the bottom position and press *Next*.
5. Place the sticks in positions requested by QGroundControl.
6. When you get the *"Move all transmitter switches and/or dials back and forth to their extreme positions"* instruction, move all switches and dials to their extreme positions.
7. Press *Next*.
8. When you get the *"All settings have been captured. Click Next to write the new parameters to your board"*, press *Next*.

Further reading: https://docs.qgroundcontrol.com/en/SetupView/Radio.html

**Next**: [Flight modes](modes.md).
