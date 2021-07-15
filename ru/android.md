
# Пульт на Android

Все владельцы мобильных устройств фирмы *Apple* ещё морозным январем 2018го обзавелись приятным приложением под *iOS* для пилотирования квадрокоптеров с помощью **WiFi**. И вот, спустя год вышло такое же приложение но уже для другой операционной системы. Актуальную версию вы можете скачать [**тут**](https://vk.com/away.php?to=https%3A%2F%2Fplay.google.com%2Fstore%2Fapps%2Fdetails%3Fid%3Dexpress.copter.cleverrc&cc_key=) .

## Введение

В данной статье я расскажу вам о том, как можно написать свой или доработать уже имеющийся пульт для Андроид своими руками. Для работы будем использовать модный язык *Kotlin*, а в качестве среды разработки возьмем *Android Studio*. Для тех кто ни разу ей не пользовался рекомендую к ознакомлению следующие [*материалы*](https://www.google.com/search?ei=xQxDXMH0C8OOmgW4mYigDQ&q=%D0%A7%D1%82%D0%BE+%D0%B4%D0%B5%D0%BB%D0%B0%D1%82%D1%8C+%D0%B5%D1%81%D0%BB%D0%B8+%D1%8F+%D0%BD%D0%B5+%D1%83%D0%BC%D0%B5%D1%8E+%D0%BF%D0%B8%D1%81%D0%B0%D1%82%D1%8C+%D0%BF%D0%BE%D0%B4+%D0%B0%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D0%B4%3F&oq=%D0%A7%D1%82%D0%BE+%D0%B4%D0%B5%D0%BB%D0%B0%D1%82%D1%8C+%D0%B5%D1%81%D0%BB%D0%B8+%D1%8F+%D0%BD%D0%B5+%D1%83%D0%BC%D0%B5%D1%8E+%D0%BF%D0%B8%D1%81%D0%B0%D1%82%D1%8C+%D0%BF%D0%BE%D0%B4+%D0%B0%D0%BD%D0%B4%D1%80%D0%BE%D0%B8%D0%B4%3F&gs_l=psy-ab.3...4413.17423..17726...9.0..2.442.4577.45j5j1j0j1....2..0....1..gws-wiz.....6..0i71j35i39j0i131j0j0i67j0i131i67j0i22i30j33i22i29i30j33i21j33i160.0bZz-WGxoHY). Весь код приложения можно найти [**тут**](https://github.com/Tennessium/android). Если вы хотите сразу получить приложение с целью дальнейшей доработки, выполните следующую команду:

```Bash
git clone https://github.com/Tennessium/android
```

Однако чтобы вы смогли полностью понять устройство приложения, я расскажу вам о каждом этапе создания проекта, как если бы вы делали его с нуля.

## Обертка

Начнем с самого простого - внешнего вида нашего приложения. На [**гитхабе**](https://github.com/CopterExpress/clover/tree/master/apps/android/app/src/main/assets) вы можете найти *HTML*, *CSS* и *JavaScript* файлы, это и есть веб страница с которой будет происходить управление коптером. Чтобы эта страница отображалась у нас в приложении надо:

1. Создать папку **assets** в главной папке приложения **app**

2. Добавить в нее файлы все файлы [отсюда](https://github.com/CopterExpress/clover/tree/master/apps/android/app/src/main/assets)

Если вы дошли до этого этапа то у вас уже есть необходимая веб страница, поздравляю! Теперь нам надо её как-то отобразить в приложении. Для этого в классе вашего *activity* в методе **onCreate** необходимо написать следующий код:

```Kotlin
main_web.loadUrl("file:///android_asset/index.html")
```

Где *main_web* - id вашего *WebView*, который должен находится в *xml* файле выбранного вами *activity*.

К сожалению, пульт для управления коптером требует всего экрана устройства, а элементы интерфейса системы мешают полноценному использованию программы. Для этого надо в начале метода **onCreate** вызвать следующую функцию:

```Kotlin
private fun fullScreenCall() {
	window.setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN)
	if (Build.VERSION.SDK_INT < 19) {
		val v = this.window.decorView
		v.systemUiVisibility = View.GONE
	} else {
		//for higher api versions.
		val decorView = window.decorView
		val uiOptions = View.SYSTEM_UI_FLAG_HIDE_NAVIGATION or View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY
		decorView.systemUiVisibility = uiOptions
	}
}
```

Данная функция позволяет избавиться от элементов интерфейса системы. Идем дальше.

Вот так выглядит пульт на этом этапе:

<img src="../assets/IMG_4397.PNG" width="50%">

Если вы запустите приложение, то заметите что стики не работают. Это происходит по тому, что на нашей странице отключен *JavaScript*. чтобы его включить надо прописать следующее:

```Kotlin
	main_web.settings.apply {
	domStorageEnabled = true
	javaScriptEnabled = true
	loadWithOverviewMode = true
	useWideViewPort = true
	setSupportZoom(false)
}
```

Этим куском кода мы разрешаем странице использовать *JavaScript* и заодно готовимся к следующему этапу - **логике**.

## Прием данных с веб страницы

Чтобы телефон мог принимать данные с *HTML страницы*, надо создать класс для взаимодействия с веб интерфейсом

```Kotlin
class WebAppInterface(c: Context) {
	@JavascriptInterface
	public fun postMessage(message: String) {
		val data = JSONObject(message)
		send("255.255.255.255", 35602, pack(
		data.getInt("x").toShort(),
		data.getInt("y").toShort(),
		data.getInt("z").toShort(),
		data.getInt("r").toShort()))
	}
}
```

Данный класс будет получать сообщение с веб страницы отправленное методом *postMessage*, где аргумент *message* - сообщение от страницы.

Теперь надо связать классы **WebAppInterface** и **MainActivity**. Для этого надо всего лишь добавить одну строку в метод **onCreate**:

```Kotlin
main_web.addJavascriptInterface(WebAppInterface(this), "appInterface")
```

## Отправка данных на коптер

**Важно!**
Для любой работы с интернетом на платформе *Android* в файле **AndroidManifest.xml** внутри тега *manifest* необходимо добавить такую строку:

```XML
<uses-permission android:name="android.permission.INTERNET"/>
```

Она дает вашему приложению доступ в интернет и возможность передавать данные по средствам **WiFi**. А как это делать, мы с вами сейчас и узнаем. Идём дальше!

Вы наверное заметили функцию *send* в классе **WebAppInterface**. Именно она отправляет данные на коптер. Давайте объявим ее **вне классов**:

```Kotlin
fun send(host: String, port: Int, data: ByteArray, senderPort: Int = 0): Boolean {
	var ret = false
	var socket: DatagramSocket? = null
	try {
		socket = DatagramSocket(senderPort)
		val address = InetAddress.getByName(host)
		val packet = DatagramPacket(data, data.size, address, port)
		socket.send(packet)
		ret = true
	} catch (e: Exception) {
		e.printStackTrace()
	} finally {
		socket?.close()
	}
	return ret
}
```

Данная функция отправляет данные при помощи [*протокола пользовательских датаграмм*](https://www.google.com/search?q=udp+%D0%BF%D1%80%D0%BE%D1%82%D0%BE%D0%BA%D0%BE%D0%BB&oq=udp+&aqs=chrome.0.69i59j69i57j35i39j0l3.1434j1j7&sourceid=chrome&ie=UTF-8) на коптер. Программа отправляет **байты**, поэтому неплохо бы было объявить функцию для создания массива **байтов** из четырех переменных:

```Kotlin
fun pack(x: Short, y: Short, z: Short, r: Short): ByteArray {
	val pump_on_buf: ByteBuffer = ByteBuffer.allocate(8)
	pump_on_buf.putShort(r)
	pump_on_buf.putShort(z)
	pump_on_buf.putShort(y)
	pump_on_buf.putShort(x)
	return pump_on_buf.array().reversedArray()
}
```

## Итог

Теперь ваше приложение имеет полный функционал аналога под **iOS**. Можете кастомизировать его как пожелаете. По любым вопросам о приложении можете обращаться в Телеграм @Tenessinum.
