# Migration to version 0.22

## Python 3 transition

Python 2 is [deprecated](https://www.python.org/doc/sunset-python-2/) since January 1st, 2020. The Clover platform moves to Python 3.

For running flight script instead of `python` command:

```bash
python flight.py
```

use `python3` command:

```bash
python3 flight.py
```

Python 3 has certain syntax differences in comparison with the old version. Instead of `print` *operator*:

```python
print 'Clover is the best'  # this won't work
```

use `print` *function*:

```python
print('Clover is the best')
```

The division operator operates floating points by default (instead of integer). Python 2:

```python
>>> 10 / 4
2
```

Python 3:

```python
>>> 10 / 4
2.5
```

For strings `unicode` type is used by default (instead of `str` type).

Encoding specification (`# coding: utf8`) is not necessary any more.

More details on all the language changes see in [appropriate article](https://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html).

## Move to ROS Noetic

<img src="../assets/noetic.png" width=200>

ROS Melodic version was updated to ROS Noetic. See the full list of changes in the [ROS official documentation](http://wiki.ros.org/noetic/Migration).

## Changes in launch-files

Configuration of ArUco-markers navigation is simplified. See details in [markers navigation](aruco_marker.md) and [markers map navigation](aruco_map.md) articles.
