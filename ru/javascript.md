# Работа с ROS из браузера

С помощью библиотеки [`roslibjs`](http://wiki.ros.org/roslibjs) возможна работа со всеми ресурсами ROS (топики, сервисы, параметры) из JavaScript-кода внутри браузера, что позволяет создавать различные интерактивные браузерные приложения для коптера.

Все необходимое для работы с `roslibjs` предустановлено и настроено на [образе для RPi для Клевера](image.md).

## Пример

Пример HTML-кода страницы, работающей с `roslib.js`:

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

[Взлет, посадка и все остальные операции](programming.md) могут быть осуществлены аналогичным образом.

Страница должна быть помещена в каталог `/home/pi/catkin_ws/src/clover/clover/www/`. После этого она станет доступна по адресу `http://192.168.11.1/clover/<имя_страницы>.html`. При открытии страницы браузер должен показать окно с телеметрией дрона, а также постоянно выводить состояние полетного контроллера в консоль.

<img src="../assets/js-ros.png" class="center zoom"/>

Более подробную информацию смотрите в [туториале по `roslibjs`](http://wiki.ros.org/roslibjs/Tutorials/BasicRosFunctionality).

## Браузерная GCS

Смотрите также пример реализации ([`gcs.html`](https://github.com/CopterExpress/clover/blob/master/clover/www/gcs.html), [`gcs.js`](https://github.com/CopterExpress/clover/blob/master/clover/www/js/gcs.js)) упрощенной браузерной наземной станции (GCS) на Клевере по адресу http://192.168.11.1/clover/gcs.html.

<img src="../assets/web-gcs.png" class="center zoom"/>
