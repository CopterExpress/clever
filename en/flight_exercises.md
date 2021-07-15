# Drone control exercises

The following are the recommended exercises for novice pilots. Repeat each exercise as many times as necessary until you feel confident in it.

> **Hint** In case there is a person nearby who can control a copter, use [trainer mode](trainer_mode.md).

<!---->

> **Hint** The first flights are strongly recommended to be performed behind a protective grid. In the absence of such, the flight area must be at least 6x6&nbsp;m.

## Turning on/off motors, changing flight modes

> **Hint** For convenience, connect to the aircraft using [QGC over Wi-Fi](gcs_bridge.md) and turn on the sound. This will allow you to monitor the change in flight modes. If you cannot connect via Wi-Fi, connect via USB to check flight modes.

Be sure to set the flight mode to one of the toggle switches. To do this, switch the toggle to different positions and make sure that the mode change.

It is recommended to configure *Kill Switch*. To check it, follow these steps:

* Turn on *Kill Switch*, make sure QGC has a notification.
* Put the aircraft in *Armed* state and then enable *Kill Switch*. Make sure the motors stop. Then switch the *Kill Switch* to its original position. If the aircraft haven't automatically entered the *Disarmed* state due to inactivity, the motors will start rotating again.

> **Caution** Set the aircraft to *Armed* state on the flight zone only.

Make sure modes switching is assigned to toggle switch that is convenient for you. Otherwise, change it according to the [article on setting flight modes](modes.md). Repeat the above steps several times in order to remember which toggle switches are responsible for what.

## Working with throttle

The first step is to feel the responsiveness of the copter to the movement of the throttle stick and learn how to control it. Each drone has slightly different power reserves and therefore lifts off the ground at different stick positions.

For this exercise, only the throttle stick should be used. It is recommended not to use the rest of the sticks during the exercise.

The main tasks of the exercise:

1. Drift of the copter on the ground without taking off the ground.

### Preflight checks

Do the following before takeoff:

1. Check the integrity of the aircraft and the propellers are clear to rotate.
2. Make sure the aircraft is with its back toward you.
3. Turn on the aircraft by connecting the battery.
4. Move back to a safe distance. It is recommended to maintain a minimum distance of 4-5 m to the aircraft.
5. Make sure the aircraft is in *Stabilized* mode.

Do not try to lift the copter off the ground right away, find the lowest possible stick position for the copter to start drifting on the ground. Failure to do so may result in damage or injury.

> **Caution** If you lose control of the aircraft, you must immediately turn on *Kill Switch*.

**Exercise №1**. Slowly lift the throttle stick up until the aircraft starts to move. At this point, it will begin to slowly drift on the ground. Leave the throttle stick in this position and wait a couple of seconds, then move the throttle stick to its original position to land the aircraft. After landing the aircraft, turn off the motors by switching to *Disarmed* state. Repeat the exercise 5–10 times to get better feel for the copter's throttle stick response.

**Exercise №2**. Slowly lift the throttle stick up until the aircraft starts to lift slightly off the ground. Leave the throttle stick in this position and wait a couple of seconds, then land the aircraft as in Exercise №1. Repeat the exercise 5–10 times.

**Exercise №3**. Raise the throttle stick until the aircraft starts to drift on the ground, wait a second and continue increasing the throttle until the aircraft starts to lift off the ground, wait a second and land the aircraft. To consolidate, repeat the exercises 5–10 times, increasing the number of repetitions if necessary.

## Working with roll and pitch

After mastering the throttle control of the copter, it is necessary to learn how to control its horizontal position. The right stick on the remote control is responsible for this.

Manipulating these axes is intuitive:

* Stick tilted forward (up) - aircraft moves forward.
* Stick tilted back (down) - aircraft moves backward.
* Stick tilted to the right - aircraft moves to the right.
* Stick tilted to the left - aircraft moves to the left.

The more the stick is tilted to the side, the more the aircraft will tilt to the side and the faster it moves.

The main tasks of the exercise:

1. Flying along the X axis, forward / backward.
2. Flying along the Y axis, left / right.
3. Stabilization of the copter in one place.
4. Flying in a square clockwise and counterclockwise.

> **Hint** Always stay behind the aircraft with the rear facing towards you, otherwise you may lose control over it by mixing sides.

As with throttle control, perform [the following steps](#preflight-checks) before flying.

> **Hint** If the aircraft is spinning strongly around its axis, land it and recalibrate the magnetometer and gyroscope.

**Exercise №1**. Similar to throttle exercises, raise the throttle stick until the aircraft starts to drift on the ground or bounce a little, then release the throttle stick, leaving it in that position, and raise the pitch stick, first up for a second, then down. The copter will gradually move away from you and then towards you. Repeat the exercise 5–10 times until you feel the copter's responsiveness to the stick movement.

**Exercise №2**. Raise the throttle stick until the aircraft starts to drift, then leave it and move the roll stick first to the right for a second, then to the left. The aircraft will gradually move first to the right and then to the left. Repeat the exercise 5–10 times until you feel the copter's responsiveness to the stick movement.

**Exercise №3**. Raise the throttle stick until the aircraft starts to drift, then leave it. Combine the first and second exercises and try to stabilize the aircraft at one point, compensating for its drift with the stick. Hold the aircraft for 50–60 seconds.

**Exercise №4**. Raise the throttle stick until the aircraft starts to drift, then leave it. When you feel the copter's responsiveness to stick changes, make a "square" shape with a side of 1 m, first clockwise and then counterclockwise. Perform the figures 2–3 times.

## Air cushion and control in it

The concept of *air cushion* is very important for all flying vehicles. The air cushion itself is a zone of increased pressure created by the air being forced through the propellers. This area is characterized by turbulence and air currents affecting the flight of the copter.

Pilots try to avoid flying in an air cushion, but there is a stable area at the boundary where the aircraft can hover at minimum throttle. In this case, it feels like the copter has "sat down" on an air cushion.

The main feature and advantage of such a flight is that the copter will not change altitude with one throttle value.

Main tasks:

1. Stabilization of the copter in one place.
2. Flying in a square.
3. Flying in a circle.

Similarly to the previous exercises, perform [the following steps](#pre-flight-checks) before take off.

**Exercise №1**. Raise the throttle stick until the copter flies over the air cushion and is above it (height from floor ~ 25-30 cm, for Clover 4 copter). The aircraft should not climb up or fall down, the flight altitude should stabilize. As in the previous exercise, adjust the X and Y position of the aircraft using the roll and pitch sticks. As a result, the copter should hover at one point with slight wiggle to the sides. Hold the aircraft for 30–40 seconds.

**Exercise №2**. Raise the aircraft on the air cushion and stabilize it at one point. Next, fly over a square with a side of 1 m, first clockwise, then counterclockwise. Repeat the path 2–3 times in each direction.

**Exercise №3**. Raise the aircraft on the air cushion and stabilize it at one point. Try to fly a circle with the copter around 1 m in diameter, clockwise and counterclockwise. Repeat the path 2–3 times in each direction.

## Working with yaw

In the visual control of multicopter devices, yaw does not play as important role as with fixed wing vehicles, since the copter can move in any direction regardless of where it is directed.

> **Info** The term *yaw* refers to the rotation of the aircraft around the vertical axis.

Main tasks:

1. Rotate the copter, orienting the rear of the copter towards you.
2. Turning around the copter, orienting the rear part towards you.

It is recommended that you find plenty of free space for the exercises presented.

Similarly to previous exercises, perform [preflight checks](#preflight-checks) before takeoff.

**Exercise №1**. Raise the aircraft on the air cushion and stabilize it at one point. Fly a circle around you with the copter, at a distance of 2–3 m, while rotating it so that the back of the copter is always directed towards you. Do the exercise clockwise and counterclockwise. Repeat the exercise 4–5 times.

**Exercise №2**. Raise the aircraft on the air cushion and stabilize it at one point. Walk around the aircraft while turning it so that the rear is facing you. Walk around the aircraft clockwise and counterclockwise. Repeat the exercise 4–5 times.

> **Caution** Additional exercises are much more difficult than usual and are not required. Only proceed with them if you are already confidently flying the copter.

**Additional exercise №1**. Raise the aircraft on the air cushion and stabilize it at one point. Face the aircraft with its front facing you and try to fly it backwards.

**Additional exercise №2**. Raise the aircraft on the air cushion and stabilize it at one point. Fly so that the front of the aircraft is always facing the direction of the aircraft.

## Free flight

If you can complete each of the exercises described above, chances are you already know how to freely take off and fly the aircraft. Some exercises will be presented below to consolidate the acquired skills.

Exercises:

* Flying in a vertical square.
* Flying along the sides of the cube.
* Flying in a vertical circle.
* Flight of the eight.
* Ascent of the copter in a spiral.

Strengthen the acquired skills as many times as necessary for you.
