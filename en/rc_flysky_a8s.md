# Using Flysky FS-A8S

The Flysky FS-A8S receiver is compatible with the Flysky FS-i6 and FS-i6x transmitters. The receiver can output both analog PPM and digital S.Bus/i-Bus signals to the flight controller.

S.Bus is the preferred protocol for the receiver.

## Making a cable

> **Note** You don't need to follow these steps if you already have the right cable; read on to learn [how to bind your transmitter](#rc_bind).

1. Gently remove the yellow wire from the receiver connector. Use sharp tweezers to lift up the plastic wire lock:

    <div class="image-group">
        <img src="../assets/flysky_a8s/01_remove_cable_fs.png" width=300 class="zoom border" alt="a8s wire removal 1">
        <img src="../assets/flysky_a8s/02_remove_cable_fs.png" width=300 class="zoom border" alt="a8s wire removal 2">
    </div>

2. [Pixracer only] Remove the green and brown wires from the 5-pin connector:

    <div class="image-group">
        <img src="../assets/flysky_a8s/03_remove_cable_pixracer.png" width=300 class="zoom border" alt="pixracer wire removal 1">
        <img src="../assets/flysky_a8s/04_remove_cable_pixracer.png" width=300 class="zoom border" alt="pixracer wire removal 2">
    </div>

3. [COEX Pix only] Remove the green wire (or blue if the green one is not present) from the 4-pin connector:

    <div class="image-group">
        <img src="../assets/flysky_a8s/05_remove_cable_coexpix.png" width=300 class="zoom border" alt="coexpix wire removal 1">
        <img src="../assets/flysky_a8s/06_remove_cable_coexpix.png" width=300 class="zoom border" alt="coexpix wire removal 2">
    </div>

4. Use side cutters to cut the Dupont connectors:

    <div class="image-group">
        <img src="../assets/flysky_a8s/07_wirecuts_1.png" width=300 class="zoom border" alt="wire cutting">
        <img src="../assets/flysky_a8s/08_wirecuts_2.png" width=300 class="zoom border" alt="wire cuts">
    </div>

5. Strip and tin 5-7 mm of wire from each side:

    <img src="../assets/flysky_a8s/09_wirecuts_stripped.png" width=300 class="zoom border center" alt="tinning prep">

6. Put heat shrinking tubes on the wires:

    <img src="../assets/flysky_a8s/10_heatshrink.png" width=300 class="zoom border center" alt="shrink tubing">

7. Solder the following wires:
    * black wire from the receiver connector to the black wire from the flight controller connector;
    * red wire from the receiver connector to the red wire from the flight controller connector;
    * white wire from the receiver connector to the white (if you're using Pixracer) or yellow (if you're using COEX Pix) wire from the flight controller connector:

    <img src="../assets/flysky_a8s/11_solder_scheme.png" width=300 class="zoom border center" alt="wire soldering">

8. Put the heat shrinking tubes on the solder joints and heat them:

    <img src="../assets/flysky_a8s/12_heatshrink_heat.png" width=300 class="zoom border center" alt="shrink tube heating">

9. Twist your new cable:

    <img src="../assets/flysky_a8s/13_cable_twist.png" width=300 class="zoom border center" alt="twisted cables">

Connect your receiver to the RC IN port on your flight controller:

<div class="image-group">
    <img src="../assets/flysky_a8s/14_pixracer_rcin.png" width=300 class="zoom border center" alt="pixracer connection">
    <img src="../assets/flysky_a8s/14_coexpix_rcin.png" width=300 class="zoom border center" alt="coex pix connection">
</div>

> **Hint** Double check that you're using the RC IN port on the COEX Pix:
<img src="../assets/coexpix-bottom.jpg" width=300 class="zoom border center" alt="coex pix pinout">

## Binding your transmitter {#rc_bind}

Do the following to bind your transmitter to the FS-A8S receiver:

1. Make sure your flight controller is powered off.
2. Hold the **BIND** button on the receiver:

    <img src="../assets/flysky_a8s/15_bind_key.png" width=300 class="zoom border center" alt="bind key">

3. Turn on the flight controller. The LED light on the receiver should blink fast, about 3 times per second.

    <img src="../assets/flysky_a8s/16_blink_fast.gif" width=300 class="zoom border center" alt="fast blink">

4. Hold the **BIND KEY** on your transmitter and power it on. You should see a message saying **RX Binding...**

    <img src="../assets/flysky_a8s/17_controller_rxbind.png" width=300 class="zoom border center" alt="rx binding">

5. The LED light on the receiver should start blinking slowly, about once per second.

    <img src="../assets/flysky_a8s/16_blink_slow.gif" width=300 class="zoom border center" alt="slow blink">

6. Turn your transmitter off and on again. The LED light on the receiver should glow steadily.

    <img src="../assets/flysky_a8s/16_bind_indicator.png" width=300 class="zoom border center" alt="steady glow">

> **Note** This receiver does not send any telemetry data back to the transmitter. Your transmitter will not display any data like RSSI and drone battery level on its screen. In fact, there will be no indication that the transmitter is connected to the receiver. This is not a malfunction, the controls will still work.

## Changing the receiver mode (S.Bus/i-Bus)

Connect your flight controller to your computer and open QGroundControl. In it, open the Radio tab:

![qgc radio pane](../assets/flysky_a8s/18_qgc_radio.png)

If it shows zero channels under the transmitter image, hold the **BIND** key on the receiver for 2 seconds. You should then see 18 channels appear under the image:

![qgc radio with channels](../assets/flysky_a8s/19_qgc_channels.png)
