# Переход на версию 0.22

## Переход на Python 3

Python 2 был признан [устаревшим](https://www.python.org/doc/sunset-python-2/), начиная с 1 января 2020 года. Платформа Клевера переходит на использование Python 3.

Для запуска полетных скриптов вместо команды `python`:

```bash
python flight.py
```

теперь следует использовать команду `python3`:

```bash
python3 flight.py
```

Синтаксис языка Python 3 имеет определенные изменения по сравнения со второй версией. Вместо *оператора* `print`:

```python
print 'Clover is the best'  # this won't work
```

теперь используется *функция* `print`:

```python
print('Clover is the best')
```

Оператор деления по умолчанию выполняет деление с плавающей точкой (вместо целочисленного). Python 2:

```python
>>> 10 / 4
2
```

Python 3:

```python
>>> 10 / 4
2.5
```

Для строк по умолчанию теперь используется тип `unicode` (вместо типа `str`).

Указание кодировки файла (`# coding: utf8`) перестало быть необходимым.

Полное описание всех изменений языка смотрите в [соответствующей статье](https://pythonworld.ru/osnovy/python2-vs-python3-razlichiya-sintaksisa.html).

## Переход на ROS Noetic

<img src="../assets/noetic.png" width=200>

Версия ROS Melodic обновлена до ROS Noetic. Смотрите полный список изменений в [официальной документации ROS](http://wiki.ros.org/noetic/Migration).

## Изменения в launch-файлах

Упрощено конфигурирование навигации с использованием ArUco-маркеров. Подробнее в статьях по [навигации по маркерам](aruco_marker.md) и [навигации по картам маркеров](aruco_map.md).
