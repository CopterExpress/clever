# Assembling and setting up the electromagnetic gripper

The magnetic gripper can be assembled in various ways according to the wiring diagram.

<img src="../assets/magnet_grip/scheme.jpg" width=300 class="zoom border center">

The following is an example of assembling an electromagnetic capture circuit on a breadboard.

> **Info** It is recommended to lay the wiring between the elements on the back side of the board (in the following images, the wiring is done over the diagram for illustrative purpose).

1. Place the Schottky diode, 10K resistor, and transistor on the soldering board.

    <img src="../assets/magnet_grip/magnet1.png" width=300 class="zoom border center">

2. Solder the contacts on the other side of the board and bite off the remaining element legs.
3. Connect the pins of the resistor and the two outer legs of the transistor.

    <img src="../assets/magnet_grip/magnet2.png" width=300 class="zoom border center">

4. Connect the center leg of the transistor and the leg of the Schottky diode (opposite to the gray marking strip).

    <img src="../assets/magnet_grip/magnet3.png" width=300 class="zoom border center">

5. Cut the required amount of magnetic grab wire and solder it to the pins of the Schottky diode.

    <img src="../assets/magnet_grip/magnet4.png" width=300 class="zoom border center">

6. Solder the *Dupont* - male wires to the transistor and diode leg (red, black wires), and the *Dupont* - fmale wire to the opposite transistor leg (white wire).

    <img src="../assets/magnet_grip/magnet5.png" width=300 class="zoom border center">

## Checking the operation of the electromagnetic gripper

In order to check the operation of the gripper, apply a voltage of 5V to the signal wire. You can use the *Dupont* dad-dad wire for that.

<img src="../assets/magnet_grip/magnet_check.png" width=300 class="zoom border center">

After applying voltage, the magnet should turn on.

## Connecting to Raspberry Pi

Connect the magnetic gripper to a Raspberry Pi for software activation.

<img src="../assets/magnet_grip/magnet_raspberry.png" width=300 class="zoom border center">

An example of the code activating the magnetic gripper can be found [here](gpio.md#connecting-an-electromagnet).

## Connecting to Arduino

Connect the gripper to the Arduino Nano board in order to control it manually.

It is convenient to place it on the same soldering board — insert it into the appropriate holes and solder it from the back to the board.

<img src="../assets/magnet_grip/magnet_arduino1.png" width=300 class="zoom border center">

Then connect the signal output of the circuit to the selected port and solder the *Dupont* female wire to the selected signal port on the board.

<img src="../assets/magnet_grip/magnet_arduino2.png" width=300 class="zoom border center">

## Installation of electromagnetic gripper

1. Install an electromagnet into the center hole on the gripper deck.
2. Use a zip tie to pull the assembled circuit to the back of the deck.
3. Plug the Arduino *D11* signal pin into one of the *AUX* pins on the flight controller.
4. Plug the power wire of the electromagnetic gripper to JST 5V.
