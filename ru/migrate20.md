# Переход на версию 0.20

[Образ для RPi](image.md) версии 0.20 содержит в себе значительные изменения по сравнению с версией 0.19. При переходе на новую версию обратите внимание на разъяснения, приведенные ниже.

## Пакет `clever` переименован в `clover`

Необходимо заменить все импорты модуля в Python-скриптах.

Было:

```python
# coding: utf8

import rospy
from clever import srv
from std_srvs.srv import Trigger

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)

# Взлет на высоту 1 м
navigate(x=0, y=0, z=1, frame_id='body', auto_arm=True)
```

Стало:

```python
import rospy
from clover import srv
from std_srvs.srv import Trigger

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)

# Взлет на высоту 1 м
navigate(x=0, y=0, z=1, frame_id='body', auto_arm=True)
```

## systemd-сервис `clever` переименован в `clover`

Для перезапуска платформы теперь вместо команды:

```bash
sudo systemctl restart clever
```

используется команда:

```bash
sudo systemctl restart clover
```

## Путь к файлам платформы изменен

Каталог `~/catkin_ws/src/clever/` переименован в `~/catkin_ws/src/clover`. Таким образом, файлы конфигурации (`.launch`) необходимо редактировать по новому пути.

Например, файл `~/catkin_ws/src/clever/clever/launch/clever.launch` теперь называется `~/catkin_ws/src/clover/clover/launch/clover.launch`.

## Настройки Wi-Fi сети

SSID Wi-Fi сети изменен на `clover-XXXX` (где X – случайная цифра), пароль изменен на `cloverwifi`.

## Способ настройки ориентации камеры изменен

Подробнее читайте в статье про [настройку камеры](camera_setup.md#frame).
