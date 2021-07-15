# Подключение Raspberry Pi к полетному контроллеру

Для программирования [автономных полетов](simple_offboard.md), [работы с Pixhawk (Pixracer) по Wi-Fi](gcs_bridge.md), использования [телефонного пульта](rc.md) и других функций необходимо соединение Raspberry Pi и полетного контроллера.

## Подключение по USB

Основным способом подключения является подключение по интерфейсу USB.

1. Соедините Raspberry Pi и полетный контроллер micro-USB to USB кабелем.
2. [Подключитесь в Raspberry Pi по SSH](ssh.md).
3. Убедитесь в работоспособности подключения, [выполнив на Raspberry Pi](ssh.md):

    ```bash
    rostopic echo /mavros/state
    ```

    Поле `connected` должно содержать значение `True`.

> **Hint** Для корректной работы подключения Raspberry Pi и Pixhawk по USB необходимо установить значение [параметра](px4_parameters.md) `CBRK_USB_CHK` на 197848.

## Подключение по UART

> **Note** В версии образа **0.20** пакет и сервис `clever` был переименован в `clover`. Для более ранних версий см. документацию для версии [**0.19**](https://github.com/CopterExpress/clover/blob/v0.19/docs/ru/connection.md).

<!-- TODO схема подключения -->

Дополнительным способом подключения является подключение подключение по интерфейсу UART.

1. Подключите Raspberry Pi к полетному контроллеру по UART.
2. [Подключитесь в Raspberry Pi по SSH](ssh.md).
3. Поменяйте в launch-файле Клевера (`~/catkin_ws/src/clover/clover/launch/clover.launch`) тип подключения на UART:

    ```xml
    <arg name="fcu_conn" default="uart"/>
    ```

    При изменении launch-файла необходимо перезапустить сервис `clover`:

    ```bash
    sudo systemctl restart clover
    ```

> **Hint** Для корректной работы подключения Raspberry Pi и полетного контроллера по UART необходимо установить значение параметра `SYS_COMPANION` на 921600.

## Подключение к SITL

Для того, чтобы подсоединиться к локально/удаленно запущенному [SITL](sitl.md), необходимо установить аргумент `fcu_conn` в `udp`, и `fcu_ip` в IP-адрес машины, где запущен SITL (`127.0.0.1` для локального):

```xml
<arg name="fcu_conn" default="udp"/>
<arg name="fcu_ip" default="127.0.0.1"/>
```

**Далее**: [Подключение QGroundControl по Wi-Fi](gcs_bridge.md).
