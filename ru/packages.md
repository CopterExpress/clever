# Репозиторий пакетов COEX

COEX предоставляет открытый [Debian-репозиторий](https://wiki.debian.org/ru/SourcesList) с предсобранными пакетами, относящимися к ROS Noetic, для архитектуры `armhf`.

> **Info** Адрес репозитория: http://packages.coex.tech.

Репозиторий подключен в [образе для RPi](image.md) и может быть использован для легкой установки дополнительных ROS-пакетов.

## Публикация пакетов

Вы можете прислать Pull Request в [git-репозиторий с пакетами](https://github.com/CopterExpress/packages), добавляющий или обновляющий ваш пакет (файл с расширением `.deb`), относящийся с Клеверу или ROS. После принятия ваш пакет будет доступен для установки с помощью утилиты `apt`:

```bash
sudo apt install ros-noetic-clover-some-feature
```

Пакеты, расширяющие функциональность Клевера, рекомендуется называть с префиксом `clover_`, например `clover_some_feature`.

## Использование на обычной Raspberry Pi OS

На обычной Raspberry Pi OS репозиторий может быть добавлен в список источников пакетов следующими командами:

```bash
wget -O - 'http://packages.coex.tech/key.asc' | apt-key add - 
echo 'deb http://packages.coex.tech buster main' >> /etc/apt/sources.list
sudo apt update
```
