# Flight modes

PX4 **mode** determines how the vehicle should react to commands and RC signals. Mode changing is usually mapped to one of the RC transmitter sticks.

In order to configure flight modes:

1. Open the *Vehicle Setup* tab in QGroundControl.
2. Select the *Flight Modes* menu.
3. Choose SwC (Channel 6) as mode selection switch.
4. Set desired flight modes.

    The following flight modes are recommended:

    * Flight Mode 1: *Stabilized*.
    * Flight Mode 4: *Altitude*.
    * Flight Mode 6: *Position*.

5. Check mode switching by changing the switch position.
6. Choose SwA (Channel 5) as emergency motor stop (*Kill switch*).

<img src="../assets/qgc-modes.png" class="zoom" alt="QGroundControl modes">

## Flight modes description

### Manual control

In manual mode the pilot controls the drone directly. GPS, computer vision data, and barometer are not used. Flying in these modes requires good drone piloting skills.

* **STABILIZED**/**MANUAL** — the mode with stabilized horizontal orientation. Allows control of the throttle, the copter pitch and roll, and the yaw rate.
* **ACRO** — control of throttle and the copter's pitch rate, roll rate, and yaw rate. Used by drone racers and in 3D piloting stunt shows.
* **RATTITUDE** — in the center, the right stick is similar to STABILIZED, at the edges, it passes to the ACRO mode.

### Assisted flight modes

* **ALTCTL** (ALTITUDE) — control of the altitude rate, pitch, roll and yaw angular velocity. Requires a barometer or another altitude source.
* **POSCTL** (POSITION) — control of the altitude rate, forward/backward and right/left speed, and yaw angular velocity. It is the easiest flying mode. The barometer, GPS, computer vision, and other sensors are used.

### Auto flight modes {#auto}

In autonomous flight modes the quadcopter ignores the control signals from the transmitter and uses a program to fly.

* **OFFBOARD** mode uses an external computer (like a [Raspberry Pi](raspberry.md)). This mode is used in Clover for [autonomous flights](simple_offboard.md).
* **AUTO.MISSION** – PX4 uses the mission pre-loaded into the drone (the mission is uploaded using ground control station over [MAVLink](mavlink.md)). This mode is commonly used to move in a pre-planned path using GPS as a position source, for example, in photogrammetry.
* **AUTO.RTL** – the copter automatically returns to the takeoff (launch) point.
* **AUTO.LAND** – the copter lands at the current position.

Additional information: https://dev.px4.io/en/concept/flight_modes.html.

**Next**: [Power setup](power.md).
