# Clover 4 assembly

<img src="../assets/assembling_clever4/clover_assembly.png" width=900 class="zoom center">

## Frame base assembly

> **Info** To increase the strength of the frame, you can print on a 3D printer or cut on a laser cutter reinforcing pads.

1. Mount the reinforcement pads on the stiffening ribs if you have them. Proceed without them if you don't.

    <img src="../assets/assembling_clever4/frame_assembly_1.png" width=300 class="zoom border center">

2. Align two carbon stiffening ribs using the center notch.

    <div class="image-group">
        <img src="../assets/assembling_clever4/frame_assembly_2.png" width=300 class="zoom border">
        <img src="../assets/assembling_clever4/frame_assembly_3.png" width=300 class="zoom border">
    </div>

3. Install the top carbon deck using notches as guides.

    <div class="image-group">
        <img src="../assets/assembling_clever4/frame_assembly_4.png" width=300 class="zoom border">
        <img src="../assets/assembling_clever4/frame_assembly_5.png" width=300 class="zoom border">
    </div>

4. Place self-locking steel nuts into the slots in reinforcement plates and tighten the assembly with M3x8 screws.

## Installing motors

1. Unbox the motors.
2. Shorten the motor wires using wire strippers or side cutters:

    * Cut wires to 30 mm.
    * Strip 5 mm of insulation while taking care to not damage the cores

    <img src="../assets/assembling_clever4/motor_1.png" width=300 class="zoom border center">

    * Twist the cores.
    * [Tin the wires](tinning.md). You may want to use tweezers to hold the wire.

3. Place the motor on the support arm.
4. Use hexagonal M3x5 screws to attach the motor to its arm.

    <img src="../assets/assembling_clever4/motor_2.png" width=300 class="zoom border center">

Perform these actions for each motor.

## Frame assembly

1. Install the support arms on the frame base according to their rotation direction. Use notches as guides.

    <img src="../assets/assembling_clever4/motor_3.png" width=300 class="zoom border center">

    > **Hint** Note the motor nut colors when installing the arms. Motors with red nuts should be placed on the front right and back left arms, with black ones - on the front left and back right arms.

2. Attach the arms to the frame base using 8 M3x8 screws, 6 steel nuts, and 2 15 mm spacers.

    <div class="image-group">
        <img src="../assets/assembling_clever4/motor_4.png" width=300 class="zoom border">
        <img src="../assets/assembling_clever4/motor_5.png" width=300 class="zoom border">
    </div>

## Preparing the power distribution board

1. [Tin](tinning.md) the pads on the power distribution board.
2. Check the board for shorts using a multimeter:
    * Set your multimeter to the Continuity Test mode.
    * Ensure your multimeter works by connecting the probes to each other. The multimeter should beep.
    * Connect one of the probes to the **«+»** pad and the other to **«-»/GND**. If there is a short circuit, the multimeter will beep.

## Mounting the PDB

1. Attach four 6 mm standoffs on the top carbon deck using M3x6 screws.

    <div class="image-group">
        <img src="../assets/assembling_clever4/pdb_1.png" width=300 class="zoom border">
        <img src="../assets/assembling_clever4/pdb_2.png" width=300 class="zoom border">
    </div>

2. Place the PDB on the standoffs.

    <img src="../assets/assembling_clever4/pdb_3.png" width=300 class="zoom border center">

3. Make sure the arrow on the PDB is pointing in the same direction as the arrow on the top carbon deck.

## Soldering the speed controllers and the BEC

1. Solder the motor wires to the electronic speed controllers (ESCs).
2. Solder the ESC power wires to the power distribution board (**<font color=red>red</font>** to **«+»**, **black** to **«-»**).

    <div class="image-group">
        <img src="../assets/assembling_clever4/esc_bec_1.png" width=300 class="zoom border">
        <img src="../assets/assembling_clever4/esc_bec_2.png" width=300 class="zoom border">
    </div>

3. Solder power wires of the battery elimination circuit in parallel to one of the ESC power wires (**<font color=red>red</font>** to **«+»**, **black** to **«-»**).

    <div class="image-group">
        <img src="../assets/assembling_clever4/esc_bec_3.png" width=300 class="zoom border">
        <img src="../assets/assembling_clever4/esc_bec_4.png" width=300 class="zoom border">
    </div>

4. Check the board for shorts using a multimeter.

### Setting up PWM mode on RC

Turn on your transmitter using the **POWER** slider. If the RC transmitter is locked, place all controls in their neutral position:

1. Left stick should be in the **lower center position**.
2. Right stick should be **centered**.
3. The switches (A, B, C, D) should be in the **top position**.

    <img src="../assets/assembling_clever4/base.png" alt="Neutral control state" class="zoom center" width=500>

Make sure the transmitter operates in the PWM mode:

1. Power down the receiver.
2. Hold down the "OK" button to enter the menu.
3. Select the "System setup" option, press "OK" to enter the submenu.
4. Select "RX Setup" option.
5. Select "Output mode".
6. Make sure the "PWM" option is selected.
7. Save settings by holding the "Cancel" button.

### Binding the RC transmitter and receiver

1. Turn off the RC transmitter with the **POWER** slider.
2. Connect the RC receiver to the 5 V BEC output. Connect the black wire into one of the bottom pins and the red wire to one of the central pins.
3. Place the binding jumper on the B/VCC output.
4. Connect the battery pack.
5. The LED on the RC receiver should start to blink.

    <div class="image-group">
        <img src="../assets/assembling_clever4/rc_binding_1.png" width=300 class="zoom border">
        <img src="../assets/assembling_clever4/rc_binding_2.png" width=300 class="zoom border">
    </div>

6. Hold down the **BIND KEY** on the RC transmitter.
7. Turn on the RC transmitter while holding the **BIND KEY**

    <img src="../assets/assembling_clever4/binding.png" class="zoom border center" width=500>

8. Wait for the **RXBind ok** message on the RC transmitter
9. Disconnect the binding jumper.
10. The LED on the RC receiver should be lit continuously.

### Checking the motor rotation direction

Motors with **<font color=red>red</font>** nuts should rotate **counterclockwise**, the ones with **black** nuts should rotate **clockwise**. Correct rotation direction should also be printed on the motors. You can use a servo tester or your RC transmitter and receiver to check rotation direction.

<img src="../assets/assembling_clever4/props_rotation.png" width=400 class="zoom border center">

1. Disconnect the battery pack and power down the transmitter.
2. Connect the signal wires from the ESC to CH3 pins on the output. The white wire should go to the top pin, the black one should go to the bottom one.
3. Power on the transmitter. Make sure the left stick is in the bottom position.
4. Connect the battery pack.
5. Slowly move the left stick up until the motor starts to spin.

If the motor rotation direction is wrong, switch any two motor wires.

> **Info** You can also change motor direction by reprogramming the speed controllers. The process is described [in the ESC firmware flashing article](esc_firmware.md).

Do this for each motor.

### Switching the transmitter back to PPM mode

The flight controller expects PPM signal from your RC gear. Switch your transmitter back to PPM before flight.

1. Make sure the receiver is not powered.
2. Hold down the "OK" button to enter the menu.
3. Select the "System setup" option, press "OK" to enter the submenu.
4. Select "RX Setup" option.
5. Select "Output mode".
6. Make sure the "PPM" option is selected.
7. Save settings by holding the "Cancel" button.

## Mounting the flight controller plate

1. Attach four 6 mm standoffs on top of PDB.

    <img src="../assets/assembling_clever4/fcu_1.png" width=300 class="zoom border center">

2. Connect the flight controller power cable to the PDB.

    <img src="../assets/assembling_clever4/fcu_2.png" width=300 class="zoom border center">

3. Place the polycarbonate plate on the standoffs and fix them with plastic nuts.

    <img src="../assets/assembling_clever4/fcu_3.png" width=300 class="zoom border center">

## Mounting the flight controller

1. Insert the microSD card into your flight controller.

    <img src="../assets/assembling_clever4/pixracer_sdcard.png" width=300 class="zoom border center">

2. Align the flight controller so that the arrows on the controller and on the top carbon deck point in the same direction.

    <img src="../assets/assembling_clever4/fcu_4.png" width=300 class="zoom border center">

3. Attach the flight controller to the flight controller plate using 3M double-sided adhesive pads.
4. Connect the power cable to the **"POWER"** input of the flight controller.

    <div class="image-group">
        <img src="../assets/assembling_clever4/fcu_5.png" width=300 class="zoom border">
        <img src="../assets/assembling_clever4/fcu_6.png" width=300 class="zoom border">
    </div>

5. Attach four 40 mm aluminum spacers to the top carbon deck using M3x10 screws.

    <div class="image-group">
        <img src="../assets/assembling_clever4/fcu_7.png" width=300 class="zoom border">
        <img src="../assets/assembling_clever4/fcu_8.png" width=300 class="zoom border">
    </div>

6. Connect signal wires to the flight controller as shown in these pictures:

    <div class="image-group">
        <img src="../assets/assembling_clever4/motor_conenction.png" width=300 class="zoom border">
        <img src="../assets/assembling_clever4/fcu_9.png" width=300 class="zoom border">
    </div>

7. Attach two 15 mm spacers to the top carbon deck using M3x8 screws.

    <div class="image-group">
        <img src="../assets/assembling_clever4/fcu_10.png" width=300 class="zoom border">
        <img src="../assets/assembling_clever4/raspberry_1.png" width=300 class="zoom border">
    </div>

8. Attach two 15 mm spacers to the top carbon deck and the front arms using M3x10 screws (this was already described in the "Frame Assembly" section, p. 2).

## Mounting the LED strip ring

1. Bend the polycarbonate strip into a ring and use the locks to fix it in this shape.
2. Fix the ring on the frame using appropriate notches.

    <div class="image-group">
        <img src="../assets/assembling_clever4/led_1.png" width=300 class="zoom border">
        <img src="../assets/assembling_clever4/led_2.png" width=300 class="zoom border">
    </div>

## Installing the Raspberry Pi

1. Insert your microSD card [with our image](image.md) into the Raspberry Pi

    <img src="../assets/assembling_clever4/rpi_sdcard.png" width=300 class="zoom border center">

2. Attach the Raspberry Pi using four standoffs.

    <img src="../assets/assembling_clever4/raspberry_2.png" width=300 class="zoom border center">

3. Route the BEC wires through the channel in the top carbon deck.

    <img src="../assets/assembling_clever4/raspberry_3.png" width=300 class="zoom border center">

4. Connect the BEC outputs according to the following image:

    <img src="../assets/assembling_clever4/raspberry_4.png" width=300 class="zoom border center">

## Installing the LED strip on the LED strip ring

1. Check wires on the strip (and solder them on if they're missing)

    <div class="image-group">
        <img src="../assets/assembling_clever4/led_3.png" width=300 class="zoom border">
        <img src="../assets/assembling_clever4/led_4.png" width=300 class="zoom border">
    </div>

2. Attach the LED strip to the ring using the adhesive layer on the strip. Use zip ties to fix it in place.

    <img src="../assets/assembling_clever4/led_5.png" width=300 class="zoom border center">

## Connecting the LED strip to Raspberry Pi

1. Power the LED strip from a separate BEC. Connect the **«+»** and **«-»** leads to **5v** and **Ground** respectively.

    <div class="image-group">
        <img src="../assets/assembling_clever4/led_6.png" width=300 class="zoom border">
        <img src="../assets/assembling_clever4/led_7.png" width=300 class="zoom border">
    </div>

2. Connect the **D** lead to GPIO21 (consult the [relevant article](leds.md) for more information).

    <img src="../assets/assembling_clever4/led_8.png" width=300 class="zoom border center">

## Installing the camera cable

1. Open the slot connector by lifting the T-clip.
2. Insert the ribbon cable.
3. Press the T-clip down to secure the cable.

<img src="../assets/assembling_clever4/raspberry_5.png" width=300 class="zoom border center">

## Mounting the lower deck periphery

1. Prepare the laser rangefinder by soldering leads to it.
2. Use four 2x5 self-tapping screws to secure the camera.

    > **Warning** Make sure the screws don't touch any components on the camera PCB! Otherwise the camera may not function properly.

3. Mount the laser rangefinder on the lower deck using two M3x8 screws and steel nuts.

    <div class="image-group">
        <img src="../assets/assembling_clever4/lower_deck_1.png" width=300 class="zoom border">
        <img src="../assets/assembling_clever4/lower_deck_2.png" width=300 class="zoom border">
    </div>

4. Attach RC receiver to the lower deck using 3M double-sided adhesive pads.

    <img src="../assets/assembling_clever4/lower_deck_3.png" width=300 class="zoom border center">

5. Mount the lower deck assembly using four M3x10 screws.

    <img src="../assets/assembling_clever4/lower_deck_4.png" width=300 class="zoom border center">

6. Connect the camera ribbon cable to the camera.
7. Connect the laser rangefinder to the Raspberry Pi using the following pinout:
    * Connect **VCC** to pin 1 (**3v3**)
    * Connect **GND** to pin 9 (**Ground**)
    * Connect **SDA** to pin 3 (**GPIO2**)
    * Connect **SCL** to pin 5 (**GPIO3**)

    <img src="../assets/assembling_clever4/lower_deck_5.png" width=300 class="zoom border center">

## Mounting the landing gear

1. Attach 8 landing gear pieces using M3x10 screws and steel nuts.

    <div class="image-group">
        <img src="../assets/assembling_clever4/landing_gear_1.png" width=300 class="zoom border">
        <img src="../assets/assembling_clever4/landing_gear_2.png" width=300 class="zoom border">
    </div>

2. Attach dampening pads to the landing gear pieces using M3x10 screws and steel nuts.

    <img src="../assets/assembling_clever4/landing_gear_3.png" width=300 class="zoom border center">

## Connecting the cables

1. Connect RC cable to the **RCIN** port on the flight controller.

    <img src="../assets/assembling_clever4/radio_2.png" width=300 class="zoom border center">

2. Connect RC cable to RC receiver.

    <div class="image-group">
        <img src="../assets/assembling_clever4/radio_1.png" width=300 class="zoom border">
        <img src="../assets/assembling_clever4/radio_3.png" width=300 class="zoom border">
    </div>

## Mounting the propeller guards

1. Assemble the lower part of the guards using twelve M3x10 screws and twelve 40 mm plastic spacers.

    <img src="../assets/assembling_clever4/propeller_guards_1.png" width=300 class="zoom border center">

2. Assemble the top part using twelve M3x10 screws.

    <img src="../assets/assembling_clever4/propeller_guards_2.png" width=300 class="zoom border center">

3. Attach the assembly to the drone using four M3x10 screws and steel nuts.

    <div class="image-group">
        <img src="../assets/assembling_clever4/propeller_guards_3.png" width=300 class="zoom border">
        <img src="../assets/assembling_clever4/propeller_guards_4.png" width=300 class="zoom border">
    </div>

## Mounting the top deck

1. Attach the battery holder to the top deck with four M3x8 screws and steel nuts.
2. Thread the battery strap through the slots in the deck.
3. Attach the top deck using four M3x10 screws.

    <img src="../assets/assembling_clever4/upper_deck_1.png" width=300 class="zoom border center">

4. Connect the flight controller to the Raspberry Pi using retractable USB cable.

    <div class="image-group">
        <img src="../assets/assembling_clever4/usb_connection_2.png" width=300 class="zoom border">
        <img src="../assets/assembling_clever4/usb_connection_3.png" width=300 class="zoom border">
    </div>

5. Attach the USB cable reel where convenient using 3M double-sided adhesive pads while making sure the cable does not interfere with the propellers.

    <img src="../assets/assembling_clever4/usb_connection_1.png" width=300 class="zoom border center">

## Mounting the propellers and preparing for flight

Perform the quadrotor components setup according to [the "Configuration" section](setup.md).

> **Warning** Be sure to **not** mount the propellers **until the setup is complete**. Do it only when you are ready to fly.

Attach the propellers according to their rotation direction. The battery should be disconnected during propeller installation.

<div class="image-group">
    <img src="../assets/assembling_clever4/final_2.png" width=300 class="zoom border">
    <img src="../assets/assembling_clever4/final_3.png" width=300 class="zoom border">
</div>

## Installing the battery

> **Warning** Make sure all cables are secured and nothing interferes with the propellers!

Check the quadrotor assembly:

* The balance connector should be fixed under the battery strap.
* The ESCs should be zip tied to the frame.
* All wires from the PDB and flight controller should be tucked under a velcro strap wound around aluminum spacers.

<img src="../assets/assembling_clever4/final_1.png" width=300 class="zoom border center">

Be sure to install and setup the voltage indicator before flying, so as not to overdischarge the battery. To configure the indicator, use the button located at its base. The displayed numbers during setup indicate the minimum possible voltage in each [cell](glossary.md#battery-cell) of the battery, the recommended value is **3.5**.

> **Info** Sound indication means that your battery is low and needs to be charged.

<img src="../assets/assembling_clever4/pishalka.png" width=300 class="zoom border center">

> **Success** The drone is ready to fly!
