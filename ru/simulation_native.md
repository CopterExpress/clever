# Сборка на собственной машине

Настройка среды для симуляции с нуля требует некоторых усилий, однако это приведет к улучшению производительности и к уменьшению вероятности появления проблем с драйверами.

Требования для сборки: установлены Ubuntu 18.04 и [ROS](ros-install.md).

## Создание рабочего пространства для симулятора

В этой статье мы будем использовать `catkin_ws` как имя рабочего пространства (вы можете поменять её). Мы создадим её в домашнем каталоге текущего пользователя (`~`).

Создайте рабочее пространство и загрузите исходный код Клевера:

```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
git clone https://github.com/CopterExpress/clover
git clone https://github.com/CopterExpress/ros_led
```

Установите все зависимости, используя `rosdep`:

```bash
cd ~/catkin_ws
rosdep update
rosdep install --from-paths src --ignore-src -y
```

## Загрузка исходного кода PX4

Сборка PX4 будет осуществлена вместе с другими пакетами в нашем рабочем пространстве. Вы можете загрузить его прямо в рабочее пространство или поместить куда-нибудь и создать симлинк к `~/catkin_ws/src`. Нам также нужно будет поместить его подмодуль `sitl_gazebo` в `~/catkin_ws/src`. Для упрощения мы загрузим прошивку прямо в рабочее пространство:

```bash
cd ~/catkin_ws/src
git clone --recursive https://github.com/CopterExpress/Firmware -b v1.10.1-clever
ln -s Firmware/Tools/sitl_gazebo ./sitl_gazebo
```

## Установка зависимостей PX4

PX4 имеет свой собственный скрипт для установки зависимостей. Воспользуемся им:

```bash
cd ~/catkin_ws/src/Firmware/Tools/setup
sudo ./ubuntu.sh
```

Он установит все, что нужно для сборки PX4 и SITL.

Также вы можете пропустить установку ARM тулчейна, если вы не планируете компилировать PX4 для вашего полетного контроллера. Для этого воспользуйтесь флагом `--no-nuttx`:

```
sudo ./ubuntu.sh --no-nuttx
```

## Патчинг плагинов Gazebo

Пакет `sitl_gazebo`, содержащий плагины нужно пропатчить, из-за недавних изменений в MAVLink. Эти патчи уже применены в [образе виртуальной машины](simulation_vm.md) и хранятся в репозитории CopterExpress/VM. Запустите следующие команды для загрузки и применения патчей:

```bash
cd ~/catkin_ws/src/Firmware/Tools/sitl_gazebo
wget https://raw.githubusercontent.com/CopterExpress/clover_vm/master/assets/patches/sitl_gazebo.patch
patch -p1 < sitl_gazebo.patch
rm sitl_gazebo.patch
```

## Установка датасетов geographiclib

Для `mavros` нужны датасеты geographiclib:

```bash
cd ~
wget https://raw.githubusercontent.com/mavlink/mavros/6f5bd5a1a67c19c2e605f33de296b1b1be9d02fc/mavros/scripts/install_geographiclib_datasets.sh
chmod +x ./install_geographiclib_datasets.sh
sudo ./install_geographiclib_datasets.sh
rm ./install_geographiclib_datasets.sh
```

## Сборка симулятора

После установки всех зависимостей можно начинать сборку рабочего пространства:

```bash
cd ~/catkin_ws
catkin_make
```

> **Note** Некоторые файлы, особенно плагины Gazebo, требуют большого объема оперативной памяти для сборки. Вы можете уменьшить количество параллельных процессов; количество параллельных процессов должно быть равно объёму RAM в гигабайтах, поделенному на 2. Например, для машины с 16Гб следует указывать не более 8 процессов. Вы можете указать количество процессов, используя флаг `-j` : ```catkin_make -j8```

## Запуск симулятора

Чтобы удостовериться в том, что все было собрано корректно, попробуйте запустить симулятор:

```bash
source ~/catkin_ws/devel/setup.bash
roslaunch clover_simulation simulator.launch
```
