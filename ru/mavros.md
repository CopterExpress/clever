# MAVROS

Основная документация: [http://wiki.ros.org/mavros](http://wiki.ros.org/mavros)

MAVROS \(MAVLink + ROS\) — это пакет для ROS, предоставляющий возможность управлять беспилотниками по протоколу [MAVLink](mavlink.md). MAVROS поддерживает полетные стеки PX4 и APM. Связь организовывается по UART, USB, TCP или UDP.

MAVROS подписывается на определенные ROS-топики в ожидании команд, публикует в другие топики телеметрию, и предоставляет сервисы.

Нода MAVROS автоматически запускается в launch-файле Клевера. Для [настройки типа подключения](connection.md) см. аргумент `fcu_conn`.

> **Hint** Упрощенное взаимодействие с коптером возможно с использованием пакета [`simple_offboard`](simple_offboard.md).

<!-- -->

> **Note** В пакете `clover` некоторые плагины MAVROS отключены (в целях сохранения ресурсов). Подробнее см. параметр `plugin_blacklist` в файле `/home/pi/catkin_ws/src/clover/clover/launch/mavros.launch`.

## Основные сервисы

`/mavros/set_mode` — установить [полетный режим](modes.md) контроллера. Обычно устанавливается режим OFFBOARD \(для управления с Raspberry Pi\).

`/mavros/cmd/arming` — включить или выключить моторы беспилотника \(изменить armed-статус\).

## Основные публикуемые топики

`/mavros/state` — статус подключения к полетному контроллеру. Режим полетного контроллера.

`/mavros/local_position/pose` — локальная позиция коптера в системе координат ENU и его ориентация.

`/mavros/local_position/velocity` — текущая скорость в локальных координатах. Угловые скорости.

`/mavros/global_position/global` — текущая глобальная позиция \(широта, долгота, высота\).

`/mavros/global_position/local` — глобальная позиция в системе координат [UTM](https://ru.wikipedia.org/wiki/Система_координат_UTM).

`/mavros/global_position/rel_alt` — относительная высота \(относительно высоты включения моторов\).

Просмотр сообщений, публикуемых в топики возможен с помощью утилиты `rostopic`, например `rostopic echo /mavros/state`. Подробнее см. [работа с ROS](ros.md).

## Основные топики для публикации

`/mavros/setpoint_position/local` — установить целевую позицию  и рысканье \(yaw\) беспилотника \(в системе координат ENU\).

`/mavros/setpoint_velocity/cmd_vel` — установить целевую линейную скорость беспилотника.

`/mavros/setpoint_attitude/attitude` и `/mavros/setpoint_attitude/att_throttle` — установить целевую ориентацию \(Attitude\) и уровень газа.

`/mavros/setpoint_attitude/cmd_vel` и `/mavros/setpoint_attitude/att_throttle` — установить целевые угловые скорости и уровень газа.

### Топики для посылки raw-пакетов

`/mavros/setpoint_raw/local` — отправка пакета [SET\_POSITION\_TARGET\_LOCAL\_NED](https://mavlink.io/en/messages/common.html#SET_POSITION_TARGET_LOCAL_NED). Позволяет установить целевую позицию /целевую скорость и целевое рысканье/угловую скорость по рысканью. Выбор устанавливаемых величин осуществляется с помощью поля `type_mask`.

`/mavros/setpoint_raw/attitude` — отправка пакета [SET\_ATTITUDE\_TARGET](https://mavlink.io/en/messages/common.html#SET_ATTITUDE_TARGET). Позволяет установить целевую ориентацию / угловые скорости и уровень газа. Выбор устанавливаемых величин осуществляется с помощью поля `type_mask`

`/mavros/setpoint_raw/global` — отправка пакета [SET\_POSITION\_TARGET\_GLOBAL\_INT](https://mavlink.io/en/messages/common.html#SET_POSITION_TARGET_GLOBAL_INT). Позволяет установить целевую позицию в глобальных координатах \(ширина, долгота, высота\), а также скорости полета. **Не поддерживается в PX4** \([issue](https://github.com/PX4/Firmware/issues/7552)\).
