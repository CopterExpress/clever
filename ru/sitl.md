# Симуляция PX4

> **Hint** Мы также предоставляем [конфигурации для Gazebo](simulation.md) и [образ виртуальной машины](simulation_vm.md) со всем необходимым для запуска симуляции Клевера.

Основная статья: https://dev.px4.io/en/simulation/

Симуляция PX4 возможна в ОС GNU/Linux и macOS с использованием систем симуляции физической среды [jMAVSim](https://pixhawk.org/dev/hil/jmavsim) и [Gazebo](http://gazebosim.org).

jMAVSim является легковесной средой, предназначенной только для тестирование мультироторных летательных систем; Gazebo – универсальная среда для любых типов роботов.

## Запуск PX4 SITL

1. Склонировать репозиторий с PX4.

```bash
git clone https://github.com/PX4/Firmware.git
cd Firmware
```

## jMAVSim

Основная статья: https://dev.px4.io/en/simulation/jmavsim.html

Для симуляции с использованием легковесной среды jMAVSim используйте команду:

```bash
make posix_sitl_default jmavsim
```

Для использования модуля расчета позиции LPE вместо EKF2, используйте:

```bash
make posix_sitl_lpe jmavsim
```

## Gazebo

Основная статья: https://dev.px4.io/en/simulation/gazebo.html

Для начала установите Gazebo 7. На Mac:

```bash
brew install gazebo7
```

На Linux (Debian):

```bash
sudo apt-get install gazebo7 libgazebo7-dev
```

Запустите симуляцию, находясь в папке Firmware:

```bash
make posix_sitl_default gazebo
```

Можно запустить симуляцию в headless режиме (без оконного клиента). Для этого используйте команду:

```bash
HEADLESS=1 make posix_sitl_default gazebo
```

## Подключение

QGroundControl автоматически подключится к запущенной симуляции при запуске. Работа будет осуществляться также, как и с настоящим полетным контроллером.

Для подключение MAVROS к симуляции необходимо использовать протокол UDP, локальный IP-адрес и порт 14557, например:

```bash
roslaunch mavros px4.launch fcu_url:=udp://@127.0.0.1:14557
```

## Запуск SITL своими руками на чистой Ubuntu

### Настройка среды для запуска Gazebo

Для того, чтобы запустить симулятор полета дрона, Gazebo или jMAVSim вам потребуется сделать соответственные настройки вашей среды.

> **Caution** Среда `ROS Melodic` изначально ориентированна для Ubuntu версии 18.04 (Bionic), поэтому актуальность данной инструкции гарантируется только для данной версии операционной системы.

В первую очередь вам потребуется установить полный пакет ROS Melodic desktop-full, инструкцию по установке вы можете найти в [статье по установке ROS](ros-install.md).

После того, как вы выполнили указанные выше инструкции, вам нужно проверить, есть ли в вашем пакете `ROS` все нужные пакеты.

```bash
sudo apt-get install ros-melodic-gazebo-ros \
					 ros-melodic-gazebo-dev \
					 ros-melodic-gazebo-plugins \
					 ros-melodic-gazebo-ros-pkgs \
					 ros-melodic-gazebo-msgs \
					 ros-melodic-geographic-msgs
```

Чтобы избежать ошибок во время запуска симулятора, вам нужно будет установить Gazebo v9.11, для этого подключите необходимый репозиторий и добавьте соответствующие ключи:

```bash
sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
```

Вам нужно установить пакеты которые потребуются во время запуска симуляции:

```bash
sudo apt-get update && sudo apt-get -y --quiet --no-install-recommends install bzip2 ca-certificates ccache cmake cppcheck curl dirmngr doxygen file g++ gcc gdb git gnupg gosu lcov libfreetype6-dev libgtest-dev libpng-dev lsb-release make ninja-build openjdk-8-jdk openjdk-8-jre openssh-client pkg-config python-pip python-pygments python-setuptools rsync shellcheck tzdata unzip wget xsltproc zip ant gazebo7 gstreamer1.0-plugins-bad gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly libeigen3-dev libgazebo7-dev libgstreamer-plugins-base1.0-dev libimage-exiftool-perl libopencv-dev libxml2-utils pkg-config protobuf-compiler libgeographic-dev geographiclib-tools libignition-math2-dev

```

Для того, чтобы установить актуальные Python-модули, вам потребуется новая версия системы управления пакетами pip:

```bash
wget -qO- http://bootstrap.pypa.io/get-pip.py | sudo python
```

Теперь установите необходимые модули:

```bash
pip install --user setuptools pkgconfig wheel && pip install --user argparse argcomplete coverage jinja2 empy numpy requests serial toml pyyaml cerberus
```

Вам необходимо установить спецификацию для библиотеки `geographiclib`:

```bash
wget -qO- https://raw.githubusercontent.com/mavlink/mavros/master/mavros/scripts/install_geographiclib_datasets.sh | sudo bash
```

Склонируйте себе папку содержащую программное обеспечение PX4 и верните ее к стабильной версии v1.8.2:

```bash
git clone https://github.com/PX4/Firmware.git
cd Firmware/
git checkout v1.8.2
```

Если вы все настройки были произведены правильно, вы можете произвести сборку пакета Gazebo, чтобы в дальнейшем быстрее его запустить. Для этого вы должны находиться в директории `Firmware`:

```bash
make posix_sitl_default sitl_gazebo
```

Теперь все готово к запуску самого симулятора, для этого пропишите в переменных окружения, где искать собранные библиотеки и запустите симулятор. Обратите внимание, что если вы хотите вызвать симулятор в другом окне терминала, вам повторно потребуется прописать переменные окружения (первая строка последующей команды):

```bash
. Tools/setup_gazebo.bash $(pwd) $(pwd)/build/posix_sitl_default
roslaunch gazebo_ros empty_world.launch world_name:=$(pwd)/Tools/sitl_gazebo/worlds/iris_fpv_cam.world
```

#### Запуск PX4 для Gazebo

> **Hint** Для того, чтобы открыть окно PX4 параллельно с симулятором, откройте дополнительное окно терминала.

Чтобы запустить PX4 и подключить его к Gazebo, в директории `Firmware` соберите сам пакет симулятора:

```bash
make posix_sitl_default
```

Теперь при запущенном симуляторе, вы можете вызвать окно `PX4`. Для этого в той же директории вызовите команду:

```bash
./build/posix_sitl_default/px4 . posix-configs/SITL/init/ekf2/iris
```

После загрузки консоли, вы можете проверить то что соединение с симулятором установлено, вызвав команду `commander takeoff` для взлета и `commander land` для посадки.

#### Сборка образа Клевера в симуляторе

Для того, чтобы пользоваться командами, предоставляемыми образом Клевера, вам потребуется его скачать и настроить. Создайте директорию, в которой вы будете собирать образ, перейдите в созданную директорию и воспользуйтесь системой сборки, предоставляемой ROS, для инициализации рабочей среды.

```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws
catkin_make
```

Подтяните зависимости, прописанные в файле `setup` и склонируйте образ `Clover` в директорию `src`:

```bash
./devel/setup.bash
cd src
git clone https://github.com/copterexpress/clover
```

Перейдите в корневую папку и обновите зависимости ROS:

```bash
cd ..
rosdep install -y --from-paths src --ignore-src -r
```

Повторите сборку среды, но теперь с добавленным пакетом `Clover`:

```bash
catkin_make
```

Если сборка прошла успешно то вы можете запустить ноду Клевера и пользоваться пакетом `clover` точно так же, как и на реальном коптере:

```bash
. devel/setup.bash
roslaunch clover_simulation simulator.launch type:=none
```

Для того, чтобы воспользоваться функциями предоставляемыми нашим пакетом, в новом окне терминала подтяните зависимости из файла `setup`:

```bash
source ~/catkin_ws/devel/setup.bash
```

Теперь вы можете воспользоваться всеми возможностями пакета `clover` в вашем симуляторе.
