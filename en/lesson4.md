Lesson # 4 "Aerodynamics of the flight. Propeller"
========================================

Aerodynamics of the propeller
-----------------------

 A propeller is a blade unit rotated by the motor and used for converting the torque of the motor into the thrust.

The screw (propeller) rotates in place. With that, the air flows vertically downwards. This is one of the modes of the so-called axial screw airflow. On one of the blades, two small sections are marked: one (A) — closer to the rotation axis, the other (B) — at the end of the blade. During screw rotation, both sections will circumscribe concentric circles. It is clear that the length of the circle circumscribed by the element "B", and hence its speed relative to the air are greater than those of element "A". In other words, the speed of the blade element relative to the air depends on the distance to the rotation axis. The longer the distance, the greater the speed of the element. It is clear that at the axis of rotation, the speed will be zero, and at the end of the blade, it will be the maximum.

![rotation](../assets/7_1.png)

The blade cross section in this area has the shape of a streamlined profile. When air flows past this profile at the angle of incidence, the lifting force Y and the drag force X appear, which are calculated using special formulas. By breaking the blade into many small sections, one can determine their lifting forces and the drag forces, and by adding the appropriate forces of all sections, one can determine the lifting force and the drag force of one blade. (From the mathematical point of view, this operation is called integrating along the span of the blade). The lifting force (or the thrust) of the entire screw is obtained by multiplying the lifting force of one blade by the number of blades.
The edge effect. The magnitude of the screw thrust is calculated by the method described above with a certain error, which is determined by several reasons. One of them is not considering the so-called edge effect. The edge effect is manifested in the fact that the air tends to equalize the pressure above the blade and under the blade by flowing over the edge of the blade.

![rotation](../assets/7_2.png)

In this case, flowing over occurs on both on outer and inner edges of the blade. And since the lifting force occurs due to the pressure difference on the top and the bottom surfaces of the blade, any equalization of these pressures causes the loss of the lifting force.

Parameters of propellers
---------------------

There are many types of airscrews which may be used with varying degree of success.
One should consider the following parameters:

1. **Propeller diameter.** Larger propellers require more power of the motor for spinning. Make sure that the motor can develop the required power. Large and heavy propeller cells to have more inertia, therefore they cannot accelerate instantly, which will affect the copter's maneuverability.
2. **Prop pitch.** It is indicated by the second digit after "x" in the propeller brand; it may also be indicated by the third and the fourth digits of the brand - e.g., 1260 are propellers with the pitch of 6.0 inches. Physically, it is the air column that the propeller moves downwards in one revolution. The larger the pitch, the greater the lifting force. Naturally, there are reasonable limits: for example, 14х7 propellers have greater lifting force than 14х5 propellers. By the way, for the ideal case, the pitch of the propeller multiplied by the number of revolutions per second gives the speed of the air flow from the propeller.
3. **The number of blades.** In the classic case, there are two blades. However, propellers with three blades have greater lifting force - roughly equivalent to that of a two-blade propeller with the diameter 1 inch larger and the pitch 1 inch greater.
4. **Propeller constant**, the so-called Prop-Const, strongly affects the lifting force and the power of the motor required to spin the propeller, because physically this constant indicates the magnitude of the losses for air resistance during propeller rotation: the thinner the material the propeller is made of, the smaller this constant, and the smaller the power of the motor required for spinning the prop.

### Screws layout

Building a quadcopter requires two pairs of bidirectional screws, building a hexacopter requires 3 pairs, etc.

![rotation](../assets/7_3.png)

5\. **Direction of screws rotation** - classic - two screws counterclockwise, the other two screws clockwise in quadcopters.
6\. **Propellers workmanship quality** is also important. In the practice, it means that you should always balance the propellers to minimize vibration, which gradually destructs mechanical parts and drives periscopes crazy, deteriorating the flight properties of the quadcopter.

Building a quadcopter requires two pairs of bidirectional screws, building a hexacopter requires 3 pairs, etc.

Choosing the propeller
----------------

It is hard to imagine a propulsion source that would be more versatile than the propeller.
However, not everybody clearly understands how to correctly calculate the parameters of the propeller. Using the -and-see method, we sometimes lose a lot of time and effort on picking up dozens of various propellers in the hope of finding the one that would provide optimal thrust with specific motor and vehicle.

Calculating and choosing an air screw for the motor and a specific copter is a complex and a delicate task.
The source data for choosing the screws for DIY drone kits are usually the power of the motor Nmot (W), the airscrew rotation speed NS (rpm), and the maximum (flight) speed Vmax (m/s).

One should face the fact that no calculation will let you immediately and accurately determine all parameters of a fixed-pitch propeller. Exact calculation of such screws is a very difficult task. Even the most careful calculations do not allow getting an ideal propulsion unit for a specific vehicle. It is only during testing that it becomes clear how the crew should be modified, whether the pitch should be increased or decreased. The methods provided here allow choosing the initial screw if one can say so, a first approximation screw. And it is only the testing that will show, whether further modification of the screw will be required to fit your vehicle.

If the screw diameter should be decreased, it is sometimes recommended increasing the pitch or the width of the blades. Indeed, this helps take all the power from the motor, however efficiency of the propulsion unit inevitably drops.
it is very important to remember that a high-speed copter or requires a small-diameter high-speed propeller, and a low-speed one requires a large-diameter low-speed one.
The following method of choosing a screw for an amateur copter would seem to be reasonable: First, in accordance with the layout, choose the maximum possible diameter of the screw: consider all permissible gaps between the ends of the blades and the structure and other parameters. Then choose the motors according to the requirements of the model. There are also situations where the propeller is chosen for the motor.

So, we have to choose a motor and a propeller. How can one do it without using cumbersome formulas and complex calculations? Below, the choice of propellers is shown based on the motors chosen. However, this method is also suitable for choosing a motor for a propeller, if performed in reverse order.

For example, let's take motor X2204S 2300kv from the SunnySky company. Go to the manufacturer's website, and find the motor. The description contains a table for choosing the propeller (prop).

![rotation](../assets/7_4.png)

### Reference questions

1. How is thrust formed in a propeller?
2. How can one determine the prop pitch from the name of its brand?
3. What is propeller constant?
4. What is the purpose of using propellers rotating clockwise and counterclockwise in a copter?
5. What are the source data for choosing a screw for a copter?
6. What characteristics of the propeller are required for a high-speed and a low-speed copter?
7. Using a table for motor X2204S 2300kv, find the propeller that would develop the maximum speed.
