# Flight

> **Info** See also official PX4 flying guide: https://docs.px4.io/v1.9.0/en/flying/.

This section explains the basics of manual controlling the quadcopter in different modes using radio remote control (for autonomous flying see "[Programming](programming.md)") section.

## Main features of radio remote control

Before you can launch your drone, you need to understand how the radio remote control works.

The drone is controlled using two sticks on the remote control. By default, the left stick controls throttle and yaw, and the right stick controls roll and pitch. These terms are used for all aircraft, from airplanes to quadcopters.

<img src="../assets/flight/rc_basic_commands.svg" width=400 class="zoom center">

* Throttle – is responsible for rotation speed of the motors.
* Yaw – is responsible for rotation around the vertical axis (Z), clockwise (when tilted to the right) and counterclockwise (when tilted to the left).
* Pitch – is responsible for tilting or moving forward / backward.
* Roll – is responsible for tilting or moving left / right.

These descriptions assume the aircraft is turned with its back to the pilot.

<img src="../assets/flight/basic_movements_multicopter.svg" width=400 class="zoom center">

## Flight Modes

Manual flight using the PX4 flight controller can be performed in different flight modes. They determine the radio controller stick assignments and other flight characteristics. For the complete list of flight modes, see the article "[Flight modes](modes.md)".

The main manual modes are described below.

**STABILIZED** - horizontal angle stabilization mode. In this mode, the aircraft will hold the horizon if not controlled. Functions of sticks:

* Throttle – the average speed of rotation of the motors.
* Yaw – angular velocity around the vertical axis.
* Pitch – the angle of inclination around the transverse axis (forward / backward).
* Roll – the angle of inclination around the longitudinal axis (left / right).

**POSCTL** - position holding mode (requires positioning system enabled). Functions of sticks:

* Throttle – vertical flight speed.
* Yaw – angular velocity around the vertical axis.
* Pitch – linear speed of the drone (forward / backward).
* Roll – linear speed of the drone (left / right).

**ACRO** - controlling the average rotational speed of the motors and angular speeds of the drone. This mode is the most difficult to fly and is most often used by drone racers and 3D piloting shows to perform tricks. Functions of sticks:

* Throttle – the average speed of rotation of the motors.
* Yaw – angular velocity around the vertical axis.
* Pitch – angular velocity around the transverse axis (forward / backward).
* Roll – angular velocity around the longitudinal axis (left / right).

> **Info** Other flight controllers may have different names for similar flight modes.

## Preparing to fly

### Installing propellers and batteries

1. Install the battery strap.

    <img src="../assets/assembling_clever4_2/final_1.png" width=300 class="zoom border center">

2. Set the propellers according to the [motor direction pattern](#prop_rotation).

    <img src="../assets/assembling_clever4_2/final_3.png" width=300 class="zoom border center">

3. Attach the buzzer and install the battery.

    <div class="image-group">
        <img src="../assets/flight/buzzer_acb.jpg" width=200 class="zoom border">
        <img src="../assets/assembling_clever4_2/final_4.png" width=300 class="zoom border">
    </div>

### Setting the buzzer

In order not to over-discharge or damage the battery, it is recommended to use a voltage indicator (*buzzer*).

To configure the buzzer, connect it to the balance connector of your battery. By pressing the button, change the minimum voltage on the cells. The optimal value for the minimum voltage is *3.5-3.6 V*.

<div class="image-group">
    <img src="../assets/flight/buzzer_connection.jpg" width=300 class="zoom border">
    <img src="../assets/flight/buzzer.jpg" width=300 class="zoom border">
</div>

### Flight readiness states

Before starting the flight, the aircraft must be in the *Armed* state.

* *Armed* state – motors rotate according to throttle stick position, copter is ready to fly.
* *Disarmed* state – motors do not rotate, copter does not respond to throttle stick.

By default, the aircraft is in the *Disarmed* state and switches to it automatically if you do not take off for a long time.

There are several ways to change the copter's state to *Armed*:

* Using the stick – move the left stick down to the right and wait a couple of seconds.

  <img src="../assets/flight/controller_arm.jpg" width=300 class="zoom center">

* Using the toggle switch – the Armed / Disarmed states can be set to one of the toggle switches. For more information on setting up, see the article on [flight modes](modes.md).
* With QGC – you can arm your drone programmatically. To do this, click on the *Disarmed* label in the header and select another state.
* In the [user program](programming.md) – the copter can switch to *Armed* state if the `auto_arm=True` argument is specified in the navigation command, such as `navigate`, `set_position`, etc.

### Kill switch

When the *Kill Switch* is activated, no control signals are sent to the motors and the motors stop rotating. This function is used in extreme cases, for example, if you lose control of the aircraft.

> **Caution** Be careful, *Kill Switch* does not put the copter into *Disarmed* state!

Before disabling the *Kill Switch*, make sure the throttle stick is its down position and the aircraft is in *Disarmed* state. If the throttle stick is not in the lower position, when the *Kill Switch* is turned off, a signal corresponding to the stick position will be sent to the motors, which will lead your copter to jerk.

**Next**: [Drone control exercises](flight_exercises.md).
