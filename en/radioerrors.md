Possible radio failures
==========================================

The remote is blocked
--------------

If the remote is blocked, the LCD will read:
"Warning. Place all switches in their up position and lower the throttle".

To unlock the controller, place all sticks and switches to the initial position, namely:

1. The left stick (1) to the central bottom position.
2. Switches A, B, C, D (2) to the position “away from yourself”.
3. The right stick (3) to the center.

![Blocked remote](../assets/lockradio.jpg)

No communication with the receiver
--------------

To test the remote connection with the receiver, turn on the remote and watch the readouts on the LCD Screen.

1. Communication with the receiver is absent:

    ![No communication with the receiver](../assets/connectionLost.jpg)

2. Communication with the receiver established:

    ![Communication with the receiver OK](../assets/connectionOK.jpg)

If there is no communication:

1. Make sure the receiver is enabled (the red LED is blinking). If the LED remains constantly ON, it means that communication is established with another remote.
2. Pair the remote and the receiver.

No communication with the flight controller
--------------

If there is no communication with the flight controller, the screen of the computer monitor in the Channel Monitor window will not display changes in the position of the sliders when the sticks of your remote are shifted.

![No communication with the flight controller](../assets/notmoveslider.jpg)

1. Go to MENU (by holding down the “OK” button)
2. Select menu “System setup” (Up/Down Button to navigate, OK button - to confirms the choice).
3. Select “RX setup” > “PPM OUTPUT” > “On”
4. Save changes (hold pressed the “CANCEL” button).
