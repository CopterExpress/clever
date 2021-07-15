# Образ для Raspberry Pi

**Образ RPi для Клевера** включает в себя все необходимое ПО для удобной работы с Клевером и [программирования автономных полетов](simple_offboard.md). Платформа Клевера основана на операционной системе [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) и популярном робототехническом фреймворке [ROS](ros.md). Исходный код сборщика образа и всех дополнительных пакетов доступен [на GitHub](https://github.com/CopterExpress/clover).

## Использование

> **Info** Начиная с версии v0.22, образ основан на ROS Noetic и использует Python 3. Если вы хотите использовать ROS Melodic и Python 2, используйте версию [v0.21.2](https://github.com/CopterExpress/clover/releases/download/v0.21.2/clover_v0.21.2.img.zip).

1. Скачайте последний стабильный релиз образа — **<a class="latest-image" href="https://github.com/CopterExpress/clover/releases">скачать</a>**.
2. Скачайте и установите [программу для записи образов Etcher](https://www.balena.io/etcher/) (доступна для Windows/Linux/macOS).
3. Установите MicroSD-карту в компьютер (используйте адаптер при необходимости).
4. Запишите скачанный образ на карту, используя Etcher.
5. Установите карту в Raspberry Pi.

<img src="../assets/etcher.png" class="zoom">

После записи образа на SD-карту, вы можете подключаться к [Клеверу по Wi-Fi](wifi.md), использовать [беспроводное соединение в QGroundControl](gcs_bridge.md), получать [доступ по SSH](ssh.md) и использовать остальные функции. При необходимости узнать версию записанного на карту образа используйте [утилиту selfcheck.py](selfcheck.md).

**Далее:** [Подключение по Wi-Fi](wifi.md).
