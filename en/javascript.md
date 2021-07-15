# Work with ROS from browser

Using the [`roslibjs`](http://wiki.ros.org/roslibjs) library it's possible to work with all the ROS resources (topics, services, parameters) from JavaScript code within the browser, which allows creating various interactive web applications for drone.

All the required software is preinstalled in [RPi image](image.md) for Clover.

## Example

An example of a web page, working with `roslib.js`:

```html
<html>
	<script src="js/roslib.js"></script>
	<script type="text/javascript">
		// Establish roslibjs connection
		var ros = new ROSLIB.Ros({ url: 'ws://' + location.hostname + ':9090' });

		ros.on('connection', function () {
			// Connection callback
			alert('Connected');
		});
		
		// Declare get_telemetry service client
		var getTelemetry = new ROSLIB.Service({ ros: ros, name : '/get_telemetry', serviceType : 'clover/GetTelemetry' });

		// Call get_telemetry
		getTelemetry.callService(new ROSLIB.ServiceRequest({ frame_id: 'map' }), function(result) {
			// Service respond callback
			alert('Telemetry: ' + JSON.stringify(result));
		});

		// Subscribe to `/mavros/state` topic
		var stateSub = new ROSLIB.Topic({ ros : ros, name : '/mavros/state', messageType : 'mavros_msgs/State' });
		stateSub.subscribe(function(msg) {
			// Topic message callback
			console.log('State: ', msg);
		});
	</script>
</html>
```

[Taking off, landing and all the rest operations](programming.md) can be implemented in a similar way.

The page should be placed in the `/home/pi/catkin_ws/src/clover/clover/www/` directory. After that, it will be available at `http://192.168.11.1/clover/<page_name>.html`. When the page is opened, browser should show an alert with the drone telemetry and constantly print the state of the flight controller to the console.

<img src="../assets/js-ros.png" class="center zoom"/>

See additional information in [`roslibjs` tutorial](http://wiki.ros.org/roslibjs/Tutorials/BasicRosFunctionality).

## Web GCS

See an example of simplified web ground control station on Clover at http://192.168.11.1/clover/gcs.html.

<img src="../assets/web-gcs.png" class="center zoom"/>
