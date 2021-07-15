# MAVLink

Basic documentation: https://mavlink.io/en/.

MAVLink is a communication protocol between autonomous aircraft and vehicle systems (drones, planes, vehicles). The MAVLink protocol lies at the base of interaction between Pixhawk and Raspberry Pi.

Clover contains two wrappers for this protocol: [MAVROS](mavros.md) and [simple_offboard](simple_offboard.md).

The code for sending an arbitrary MAVLink message may be found in [the examples](snippets.md#mavlink).

## The main concerts

### Communication channel

The MAVLink protocol may be used on top of the following communication channels:

* connection in series (UART, USB, etc.);
* UDP (Wi-Fi, Ethernet, 3G, LTE);
* TCP (Wi-Fi, Ethernet, 3G, LTE).

### Message

A MAVLink message is an individual "portion" of data transmitted between devices. An individual MAVLink message contains information about the state of the drone (or another device) or a command for the drone.

Examples of MAVLink messages:

* `ATTITUDE`, `ATTITUDE_QUATERNION` – the quadcopter orientation in the space;
* `LOCAL_POSITION_NED` – local position of the quadcopter;
* `GLOBAL_POSITION_INT` – global position of the quadcopter (latitude/longitude/altitude);
* `COMMAND_LONG` – a command to the quadcopter (take off, land, toggle modes, etc).

A complete list of MAVLink messages is available in [MAVLink documentation] (http://mavlink.org/messages/common).

### System, system component

Each device (a drone, a base station, etc.) has an ID in the MAVLink network. In PX4 MAVLink, ID is changed using parameter `MAV_SYS_ID`. Each MAVLink message contains a field with the ID of the originating system. Besides, some messages (for example, `COMMAND_LONG`) also contain the ID of the target system.

In addition to IDs of the systems, the messages may contain IDs of the originating component and the target component. Examples of the system components: a flight controller, an external camera, a controlling onboard computer (Raspberry Pi in case of Clover), etc.

### An example of a package

An example of a MAVLink package structure with message `COMMAND_LONG`:

<table>
    <tr>
        <th></th>
        <th>Field</th>
        <th>Length</th>
        <th>Name</th>
        <th>Comment</th>
    </tr>
    <tr>
        <td rowspan="8"><div style="transform: rotate(-90deg)">Header</div></td>
        <td><code>magic</code></td>
        <td>1 byte</td>
        <td>Start tag</td>
        <td>0xFD for MAVLink 2.0</td>
    </tr>
    <tr>
        <td><code>len</code></td>
        <td>1 byte</td>
        <td>Data size</td>
        <td></td>
    </tr>
    <tr>
        <td><code>incompat_flags</code></td>
        <td>1 byte</td>
        <td>Reversely incompatible flags</td>
        <td>Currently unused</td>
    </tr>
    <tr>
        <td><code>compat_flags</code></td>
        <td>1 byte</td>
        <td>Reversely compatible flags</td>
        <td>Currently unused</td>
    </tr>
    <tr>
        <td><code>seq</code></td>
        <td>1 byte</td>
        <td>Message sequence number</td>
        <td></td>
    </tr>
    <tr>
        <td><code>sysid</code></td>
        <td>1 byte</td>
        <td>Originating system ID</td>
        <td></td>
    </tr>
    <tr>
        <td><code>compid</code></td>
        <td>1 byte</td>
        <td>Originating component ID</td>
        <td></td>
    </tr>
    <tr>
        <td><code>msgid</code></td>
        <td>3 bytes</td>
        <td>Message ID</td>
        <td></td>
    </tr>
    <tr style="background: #fffee6">
        <td rowspan="11"><div style="transform: rotate(-90deg)">Data (example)</div></td>
        <td><code>target_system</code></td>
        <td>1 byte</td>
        <td>Target system ID</td>
        <td></td>
    </tr>
    <tr style="background: #fffee6">
        <td><code>target_component</code></td>
        <td>1 byte</td>
        <td>Target component ID</td>
        <td></td>
    </tr>
    <tr style="background: #fffee6">
        <td><code>command</code></td>
        <td>2 bytes</td>
        <td>Command ID</td>
        <td></td>
    </tr>
    <tr style="background: #fffee6">
        <td><code>confirmation</code></td>
        <td>1 byte</td>
        <td>Number for confirmation</td>
        <td></td>
    </tr>
    <tr style="background: #fffee6">
        <td><code>param1</code></td>
        <td>4 bytes</td>
        <td>Parameter 1</td>
        <td rowspan="7">A single-precision floating point number</td>
    </tr>
    <tr style="background: #fffee6">
        <td><code>param2</code></td>
        <td>4 bytes</td>
        <td>Parameter 2</td>
    </tr>
    <tr style="background: #fffee6">
        <td><code>param3</code></td>
        <td>4 bytes</td>
        <td>Parameter 3</td>
    </tr>
    <tr style="background: #fffee6">
        <td><code>param4</code></td>
        <td>4 bytes</td>
        <td>Parameter 4</td>
    </tr>
    <tr style="background: #fffee6">
        <td><code>param5</code></td>
        <td>4 bytes</td>
        <td>Parameter 5</td>
    </tr>
    <tr style="background: #fffee6">
        <td><code>param6</code></td>
        <td>4 bytes</td>
        <td>Parameter 6</td>
    </tr>
    <tr style="background: #fffee6">
        <td><code>param7</code></td>
        <td>4 bytes</td>
        <td>Parameter 7</td>
    </tr>
    <tr>
        <td></td>
        <td><code>checksum</code></td>
        <td>2 bytes</td>
        <td>Checksum</td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td><code>signature</code></td>
        <td>13 bytes</td>
        <td>Signature (optional)</td>
        <td>Allows checking that the package has not been compromised.
Usually unused.</td>
    </tr>
</table>

<span style="background: #fffee6">Yellow</span> is used for highlighting the data fields(payload). An individual set of such fields exists for every message type.
