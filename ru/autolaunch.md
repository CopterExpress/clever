Автозапуск ПО
===

> **Note** В версии образа **0.20** пакет и сервис `clever` был переименован в `clover`. Для более ранних версий см. документацию для версии [**0.19**](https://github.com/CopterExpress/clover/blob/v0.19/docs/ru/autolaunch.md).

systemd
---

Основная документация: [https://wiki.archlinux.org/index.php/Systemd_(Русский)](https://wiki.archlinux.org/index.php/Systemd_(Русский)).

Все автоматически стартуемое ПО Клевера запускается в виде systemd-сервиса `clover.service`.

Сервис может быть перезапущен командой `systemctl`:

```bash
sudo systemctl restart clover
```

Текстовый вывод ПО можно просмотреть с помощью команды `journalctl`:

```bash
journalctl -u clover
```

Для того, запустить ПО Клевера непосредственно в текущей консольной сессии, вы можете использовать `roslaunch`:

```bash
sudo systemctl stop clover
roslaunch clover clover.launch
```

Вы можете выключить автозапуск ПО Клевера с помощью команды `disable`:

```bash
sudo systemctl disable clover
```

roslaunch
---

Основная документация: http://wiki.ros.org/roslaunch.

Список объявленных для запуска нод / программ указывается в файле `/home/pi/catkin_ws/src/clover/clover/launch/clover.launch`.

Вы можете добавить собственную ноду в список автозапускаемых. Для этого разместите ваш запускаемый файл (например, `my_program.py`) в каталог `/home/pi/catkin_ws/src/clover/clover/src`. Затем добавьте запуск вашей ноды в `clover.launch`, например:

```xml
<node name="my_program" pkg="clover" type="my_program.py" output="screen"/>
```

Запускаемый файл должен иметь *permission* на запуск:

```bash
chmod +x my_program.py
```

При использовании скриптовых языков вначале файла должен стоять [shebang](https://ru.wikipedia.org/wiki/Шебанг_(Unix)), например:

```bash
#!/usr/bin/env python
```
