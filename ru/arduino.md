# Управление коптером с Arduino

Для взаимодействия с ROS-топиками и сервисами на Raspberry Pi можно использовать библиотеку [rosserial_arduino](http://wiki.ros.org/rosserial_arduino). Эта библиотека предустановлена на [образе для Raspberry Pi](image.md).

Основной туториал по rosserial: http://wiki.ros.org/rosserial_arduino/Tutorials

Arduino необходимо установить на Клевер и подключить по USB-порту.

## Настройка Arduino IDE

Для работы с ROS Arduino необходимо понимать формат сообщений установленных пакетов. Для этого [на Raspberry Pi](ssh.md) необходимо собрать библиотеку ROS-сообщений:

```bash
rosrun rosserial_arduino make_libraries.py .
```

Полученный каталог `ros_lib` необходимо скопировать в `<папку скетчей>/libraries` на компьютере с Arduino IDE.

## Настройка Raspberry Pi

Для запуска `rosserial` создайте файл `arduino.launch` в каталоге `~/catkin_ws/src/clover/clover/launch/` со следующим содержимым:

```xml
<launch>
    <node pkg="rosserial_python" type="serial_node.py" name="serial_node" output="screen" if="$(arg arduino)">
        <param name="port" value="/dev/serial/by-id/usb-1a86_USB2.0-Serial-if00-port0"/>
    </node>
</launch>
```

Чтобы единоразово запустить программу на Arduino, можно будет воспользоваться командой:

```bash
roslaunch clover arduino.launch
```

Чтобы запускать связку с Arduino при старте системы автоматически, необходимо добавить запуск созданного launch-файла в основной launch-файл Клевера (`~/catkin_ws/src/clover/clover/launch/clover.launch`). Добавьте в конец этого файла строку:

```xml
<include file="$(find clover)/launch/arduino.launch"/>
```

При изменении launch-файла необходимо перезапустить пакет `clover`:

```bash
sudo systemctl restart clover
```

## Задержки

При использовании `rosserial_arduino` микроконтроллер Arduino не должен быть заблокирован больше чем на несколько секунд (например, с использованием функции `delay`); иначе связь между Raspberry Pi и Arduino будет разорвана.

При реализации долгих циклов `while` обеспечьте периодический вызов функции `hn.spinOnce`:

```cpp
while(/* условие */) {
  // ... Произвести необходимые действия
  nh.spinOnce();
}
```

Для организации долгих задержек используйте задержки в цикле с периодическим вызовом функции `hn.spinOnce()`:

```cpp
// Задержка на 8 секунд
for(int i=0; i<8; i++) {
  delay(1000);
  nh.spinOnce();
}
```

## Работа с Клевером

Набор сервисов и топиков аналогичен обычному набору в [simple_offboard](simple_offboard.md) и [mavros](mavros.md).

Пример программы, контролирующей коптер по позиции, с использованием сервисов `navigate` и `set_mode`:

```cpp
// Подключение библиотек для работы с rosserial
#include <ros.h>

// Подключение заголовочных файлов сообщений пакета clover и MAVROS
#include <clover/Navigate.h>
#include <mavros_msgs/SetMode.h>

using namespace clover;
using namespace mavros_msgs;

ros::NodeHandle nh;

// Объявление сервисов
ros::ServiceClient<Navigate::Request, Navigate::Response> navigate("/navigate");
ros::ServiceClient<SetMode::Request, SetMode::Response> setMode("/mavros/set_mode");

void setup()
{
  // Инициализация rosserial
  nh.initNode();

  // Инициализация сервисов
  nh.serviceClient(navigate);
  nh.serviceClient(setMode);

  // Ожидание подключение к Raspberry Pi
  while(!nh.connected()) nh.spinOnce();
  nh.loginfo("Startup complete");

  // Пользовательская настройка
  // <...>

  // Тестовая программа
  Navigate::Request nav_req;
  Navigate::Response nav_res;
  SetMode::Request sm_req;
  SetMode::Response sm_res;

  // Взлет на 2 метра:
  nh.loginfo("Take off");
  nav_req.auto_arm = false;
  nav_req.x = 0;
  nav_req.y = 0;
  nav_req.z = 2;
  nav_req.frame_id = "body";
  nav_req.speed = 0.5;
  navigate.call(nav_req, nav_res);

  // Ждем 5 секунд
  for(int i=0; i<5; i++) {
  	delay(1000);
  	nh.spinOnce();
  }

  nav_req.auto_arm = false;

  // Пролет вперед на 3 метра:
  nh.loginfo("Fly forward");
  nav_req.auto_arm = true;
  nav_req.x = 3;
  nav_req.y = 0;
  nav_req.z = 0;
  nav_req.frame_id = "body";
  nav_req.speed = 0.8;
  navigate.call(nav_req, nav_res);

  // Ждем 5 секунд
  for(int i=0; i<5; i++) {
    delay(1000);
    nh.spinOnce();
  }

  // Полет в точку 1:0:2 по маркерному полю
  nh.loginfo("Fly on point");
  nav_req.auto_arm = false;
  nav_req.x = 1;
  nav_req.y = 0;
  nav_req.z = 2;
  nav_req.frame_id = "aruco_map";
  nav_req.speed = 0.8;
  navigate.call(nav_req, nav_res);

  // Ждем 5 секунд
  for(int i=0; i<5; i++) {
    delay(1000);
    nh.spinOnce();
  }

  // Посадка
  nh.loginfo("Land");
  sm_req.custom_mode = "AUTO.LAND";
  setMode.call(sm_req, sm_res);
}

void loop()
{
}
```

## Получение телеметрии

С Arduino можно использовать [сервис](simple_offboard.md) `get_telemetry`. Для этого надо объявить его по аналогии с сервисами `navigate` и `set_mode`:

```cpp
#include <ros.h>

// ...

#include <clover/GetTelemetry.h>

// ...

ros::ServiceClient<GetTelemetry::Request, GetTelemetry::Response> getTelemetry("/get_telemetry");

// ...

nh.serviceClient(getTelemetry);

// ...

GetTelemetry::Request gt_req;
GetTelemetry::Response gt_res;


// ...

gt_req.frame_id = "aruco_map"; // фрейм для значений x, y, z
getTelemetry.call(gt_req, gt_res);

// gt_res.x - положение коптера по x
// gt_res.y - положение коптера по y
// gt_res.z - положение коптера по z
```

## Проблемы

При использовании Arduino Nano может не хватать оперативной памяти (RAM). В таком случае в Arduino IDE будут появляться сообщения, типа:

```
Глобальные переменные используют 1837 байт (89%) динамической памяти, оставляя 211 байт для локальных переменных. Максимум: 2048 байт.
Недостаточно памяти, программа может работать нестабильно.
```

Можно сократить использование оперативной памяти уменьшив размер выделяемых буферов для передачи и приема сообщений. Для этого **в самое начало** программы следует поместить строку:

```cpp
#define __AVR_ATmega168__ 1
```

Можно уменьшить количество занятой памяти еще сильнее, если вручную настроить количество publisher'ов и subscriber'ов, а также размеры буферов памяти, выделяемой для сообщений, например:

```cpp
#include <ros.h>

// ...

typedef ros::NodeHandle_<ArduinoHardware, 3, 3, 100, 100> NodeHandle;

// ...
NodeHandle nh;
```
