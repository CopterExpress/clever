Simple offboard
===

> **Warning** Это описание API версии 0.5. См. [описание API предыдущих версий](https://github.com/CopterExpress/clever/blob/67051b21a05b12e2e9e519cb640565bccb80fbe3/docs/simple_offboard.md).

Модуль `simple_offboard` пакета `clever` предназначен для упрощенного программирования автономного дрона (режим `OFFBOARD`). Он позволяет устанавливать желаемые полетные  задачи и автоматически трансформирует [систему координат](frames.md).

`simple_offboard` является высокоуровневым способом взаимодействия с полетным контроллером. Для более низкоуровневой работы см. [mavros](mavros.md).

Основные сервисы – `get_telemetry` (получение всей телеметрии), `navigate` (полет в заданную точку по прямой), `navigate_global` (полет в глобальную точку по прямой), `land` (переход в режим посадки).

Общие для сервисов параметры:

* `auto_arm` = `true`/`false` – перевести коптер в `OFFBOARD` и заармить автоматически (**коптер взлетит, если находится на полу!**)
* `frame_id` — система координат в TF2, в которой заданы координаты и рысканье (yaw), [описание систем координат](frames.md);
* `update_frame` — считать ли систему координат изменяющейся (например, `false` для `local_origin`, `fcu`, `fcu_horiz`, `true` для `marker_map`);
* `x`, `y` – горизонтальные координаты в системе координат `frame_id`;
* `z` — высота в системе координат `frame_id`;
* `lat`, `lon` – широта и долгота (в градусах);
* `yaw` — рысканье в радианах в системе координат `frame_id` (0 – коптер смотрит по оси X);
* `yaw_rate` — угловая скорость по рысканью в радианах в секунду (против часовой), `yaw` должен быть установлен в NaN;
* `thrust` — уровень газа от 0 (нет газа) до 1 (полный газ).

> **Warning** API модуля `simple_offboard` на данный момент нестабилен и может измениться.

Использование из языка Python
---

Для использования сервисов, необходимо создать объекты-прокси к ним. Пример программы, объявляющей прокси ко всем сервисам `simple_offboard`:

```python
import rospy
from clever import srv
from std_srvs.srv import Trigger

rospy.init_node('foo')   # название вашей ROS-ноды

# Создаем прокси ко всем сервисам:

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)
release = rospy.ServiceProxy('release', Trigger)
```

Неиспользуемые фукнции-прокси можно удалить из кода.

Описание API
---

> **Note** Незаполненные числовые параметры устанавливаются в значение 0.

### get_telemetry

Получить полную телеметрию коптера.

Параметры:

* `frame_id` – [фрейм](frames.md) для значений `x`, `y`, `z`, `vx`, `vy`, `vz`. Пример: `local_origin`, `fcu_horiz`, `aruco_map`.

Формат ответа:

* `frame_id` – фрейм;
* `connected` – есть ли подключение к <abbr title="Flight Control Unit, полетный контроллер">FCU</abbr>;
* `armed` – состояние `armed` винтов (винты включены, если true);
* `mode` - текущий [полетный режим](modes.md);
* `x, y, z` – локальная позиция коптера;
* `lat, lon` – широта, долгота (при наличии [gps](gps.md));
* `vx, vy, vz` – скорость коптера;
* `pitch` – угол по тангажу (радианы);
* `roll` – угол по крену (радианы);
* `yaw` – угол по рысканью в фрейме `frame_id`;
* `pitch_rate` – угловая скорость по тангажу (*work in progress*);
* `roll_rate` – угловая скорость по крену (*work in progress*);
* `yaw_rate` – угловая скорость по рысканью (*work in progress*);
* `voltage` – общее напряжение аккумулятора;
* `cell_voltage` – напряжение аккумулятора на ячейку.

> **Note** Недоступные по каким-то причинам поля будут содержать в себе значения `NaN`.

Вывод координат `x`, `y` и `z` коптера в локальной системе координат:

```python
telemetry = get_telemetry()
print telemetry.x, telemetry.y, telemetry.z
```

Вывод высоты коптера относительно [карты ArUco-меток](aruco.md):

```python
telemetry = get_telemetry(frame_id='aruco_map')
print telemetry.z
```

Проверка доступности глобальной позиции:

```python
import math
if not math.isnan(get_telemetry().lat):
    print 'Global position presents'
else:
    print 'No global position'
```

Вывод текущей телеметрии (командная строка):

```bash
rosservice call /get_telemetry "{frame_id: ''}"
```

### navigate

Прилететь в обозначенную точку по прямой.

Параметры:

* `x`, `y`, `z` – координаты в системе `frame_id`;
* `yaw` – угол по рысканью;
* `yaw_rate` – угловая скорость по рысканью (при установке yaw в `NaN`);
* `speed` – скорость полета (скорость движения setpoint);
* `auto_arm` – перевести коптер в `OFFBOARD` и заармить автоматически (**коптер взлетит, если находится на полу!**);
* `frame_id`, `update_frame`.

Взлет на высоту 1.5 м со скоростью взлета 0.5 м/с:

```python
navigate(x=0, y=0, z=1.5, speed=0.5, frame_id='fcu_horiz', auto_arm=True)
```

Полет по прямой в точку 5:0 (высота 2) в локальной системе координат со скоростью 0.8 м/с (рысканье установится в 0):

```python
navigate(x=5, y=0, z=3, speed=0.8)
```

Полет в точку 5:0 без изменения угла по рысканью (`yaw` = `NaN`, `yaw_rate` = 0):

```python
navigate(x=5, y=0, z=3, speed=0.8, yaw=float('nan'))
```

Полет вправо относительно коптера на 3 м:

```python
navigate(x=0, y=-3, z=0, speed=1, frame_id='fcu_horiz')
```

Полет в точку 3:2 (высота 2) в системе координат [маркерного поля](aruco.md) со скоростью 1 м/с:

```python
navigate(x=3, y=2, z=2, speed=1, frame_id='aruco_map', update_frame=True)
```

Вращение на месте со скоростью 0.5 рад/c (против часовой):

```python
navigate(x=0, y=0, z=0, speed=1, yaw=float('nan'), yaw_rate=0.5, frame_id='fcu_horiz')
```

Полет вперед 3 метра со скоростью 0.5 м/с, вращаясь по рысканью со скоростью 0.2 рад/с:

```python
navigate(x=3, y=0, z=0, speed=0.5, yaw=float('nan'), yaw_rate=0.2, frame_id='fcu_horiz')
```

Взлет на высоту 2 м (командная строка):

```bash
rosservice call /navigate "{x: 0.0, y: 0.0, z: 2, yaw: 0.0, yaw_rate: 0.0, speed: 0.5, frame_id: 'fcu_horiz', update_frame: false, auto_arm: true}"
```

### navigate_global

Полет по прямой в точку в глобальной системе координат (широта/долгота).

Параметры:

* `lat`, `lon` – широта и долгота;
* `z` – высота в системе координат `frame_id`;
* `yaw` – угол по рысканью;
* `yaw_rate` – угловая скорость по рысканью (при установке yaw в `NaN`);
* `speed` – скорость полета (скорость движения setpoint);
* `auto_arm` – перевести коптер в `OFFBOARD` и заармить автоматически (**коптер взлетит, если находится на полу!**);
* `frame_id`, `update_frame`.

Полет в глобальную точку со скоростью 5 м/с, оставаясь на текущей высоте (`yaw` установится в 0, коптер сориентируется передом на восток):

```python
navigate_global(lat=55.707033, lon=37.725010, z=0, speed=5, frame_id='fcu_horiz')
```

Полет в глобальную точку без изменения угла по рысканью (`yaw` = `NaN`, `yaw_rate` = 0):

```python
navigate_global(lat=55.707033, lon=37.725010, z=0, speed=5, yaw=float('nan'), frame_id='fcu_horiz')
```

Полет в глобальную точку (командная строка):

```bash
rosservice call /navigate_global "{lat: 55.707033, lon: 37.725010, z: 0.0, yaw: 0.0, yaw_rate: 0.0, speed: 5.0, frame_id: 'fcu_horiz', update_frame: false, auto_arm: false}"
```

### set_position

Установить цель по позиции и рысканью. Данный сервис следует использовать при необходимости задания продолжающегося потока целевых точек, например, для полета по сложным траекториям (круговой, дугообразной и т. д.).

> **Hint** Для полета на точку по прямой или взлета используйте более высокоуровневый сервис `navigate`.

Параметры:

* `x`, `y`, `z` – координаты точки в системе координат `frame_id`;
* `yaw` – угол по рысканью;
* `yaw_rate` – угловая скорость по рысканью (при установке yaw в NaN);
* `speed` – скорость полета (скорость движения setpoint);
* `auto_arm` – перевести коптер в `OFFBOARD` и заармить автоматически (**коптер взлетит, если находится на полу!**);
* `frame_id`, `update_frame`.

Зависнуть на месте:

```python
set_position(frame_id='fcu_horiz')
```

Назначить целевую точку на 3 м выше текущей позиции:

```python
set_position(x=0, y=0, z=3, frame_id='fcu_horiz')
```

Назначить целевую точку на 1 м впереди текущей позиции:

```python
set_position(x=1, y=0, z=0, frame_id='fcu_horiz')
```

Вращение на месте со скоростью 0.5 рад/c:

```python
set_position(x=0, y=0, z=0, frame_id='fcu_horiz', yaw=float('nan'), yaw_rate=0.5)
```

### set_velocity

Установить скорости и рысканье.

* `vx`, `vy`, `vz` – требуемая скорость полета;
* `yaw` – угол по рысканью;
* `yaw_rate` – угловая скорость по рысканью (при установке yaw в NaN);
* `auto_arm` – перевести коптер в `OFFBOARD` и заармить автоматически (**коптер взлетит, если находится на полу!**);
* `frame_id`, `update_frame`.

> **Note** Параметр `frame_id` определяет только ориентацию результирующего вектора скорости, но не его длину.

Полет вперед (относительно коптера) со скоростью 1 м/с:

```python
set_velocity(vx=1, vy=0.0, vz=0, frame_id='fcu_horiz')
```

Один из вариантов полета по кругу:

```python
set_velocity(vx=0.4, vy=0.0, vz=0, yaw=float('nan'), yaw_rate=0.4, frame_id='fcu_horiz', update_frame=True)
```

### set_attitude

Установить тангаж, крен, рысканье и уровень газа (примерный аналог управления в [режиме `STABILIZED`](modes.md)). Данный сервис может быть использован для более низкоуровнего контроля поведения коптера либо для управления коптером при отсутствии источника достоверных данных о его позиции.

> **Note** Параметр `frame_id` определяет только систему координат, в которой задается рысканье (`yaw`).

Параметры:

* `pitch`, `roll`, `yaw` – необходимый угол по тангажу, крену и рысканью (рад.);
* `thrust` – уровень газа от 0 (нет газа) до 1 (полный газ);
* `auto_arm` – перевести коптер в `OFFBOARD` и заармить автоматически (**коптер взлетит, если находится на полу!**);
* `frame_id`, `update_frame`.

### set_rates

Установить угловые скорости по тагажу, крену и рысканью и уровень газа (примерный аналог управления в [режиме `ACRO`](modes.md)). Это самый низкий уровень управления коптером (исключая непосредственный контроль оборотов моторов). Данный сервис может быть использован для автоматического выполнения акробатических трюков (например, флипа).

Параметры:

* `pitch_rate`, `roll_rate`, `yaw_rate` – угловая скорость по танажу, крену и рыканью (рад/с);
* `thrust` – уровень газа от 0 (нет газа) до 1 (полный газ).
* `auto_arm` – перевести коптер в `OFFBOARD` и заармить автоматически (**коптер взлетит, если находится на полу!**);

### land

Перевести коптер в [режим](modes.md) посадки (`AUTO.LAND` или аналогичный).

> **Note** Для автоматического отключения винтов после посадки PX4-параметр `COM_DISARM_LAND` должен быть установлен в значение > 0.

Посадка коптера:

```python
res = land()

if res.success:
    print 'Copter is landing'
```

Посадка коптера (командная строка):

```bash
rosservice call /land "{}"
```

### release

Перестать публиковать setpoint'ы коптеру (отпустить управление). Необходим для продолжения контроля средствами [MAVROS](mavros.md).

Дополнительные материалы
------------------------

* [Полеты в поле ArUco-макеров](aruco.md).
* [Примеры программ и сниппеты](snippets.md).
