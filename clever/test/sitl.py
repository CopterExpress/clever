#!/usr/bin/env python

import math
import rospy
import pytest
from pytest import approx
from numpy import isfinite
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State
from sensor_msgs.msg import NavSatFix
from clever import srv
from std_srvs.srv import Trigger

import tf2_ros
import tf2_geometry_msgs

def roughly(expected):
    return approx(expected, abs=1e-1)

def very_roughly(expected):
    return approx(expected, abs=1)

@pytest.fixture()
def node():
    return rospy.init_node('clever_test', anonymous=True)

def wait_service(name, service_class):
    res = rospy.ServiceProxy(name, service_class)
    res.wait_for_service(5)
    return res

@pytest.fixture
def get_telemetry():
    return wait_service('get_telemetry', srv.GetTelemetry)

@pytest.fixture
def navigate():
    return wait_service('navigate', srv.Navigate)

@pytest.fixture
def navigate():
    res = rospy.ServiceProxy('navigate', srv.Navigate)
    res.wait_for_service(5)
    return res

@pytest.fixture
def land():
    return wait_service('land', Trigger)

@pytest.fixture
def tf_buffer():
    buf = tf2_ros.Buffer()
    tf2_ros.TransformListener(buf)
    return buf

def wait_connection():
    start = rospy.get_rostime()
    while rospy.get_rostime() - start <= rospy.Duration(15):
        state = rospy.wait_for_message('mavros/state', State, timeout=10)
        if state.connected:
            return True
    assert False, "no connection to SITL"

def minimal_rate(func, rate):
    start = rospy.get_rostime()
    i = 0
    while rospy.get_rostime() - start <= rospy.Duration(2):
        func()
        i += 1
    result_rate = i / 2
    assert result_rate >= rate, 'Rate too low: %s Hz' % result_rate

def test_state_initial(node):
    wait_connection()
    state = rospy.wait_for_message('mavros/state', State, timeout=10)
    assert state.connected == True
    assert state.armed == False

def test_telem_initial(node, get_telemetry):
    # wait for local position
    rospy.wait_for_message('mavros/local_position/pose', PoseStamped, timeout=15)
    rospy.wait_for_message('mavros/global_position/global', NavSatFix, timeout=30)

    telem = get_telemetry()
    assert telem.frame_id == 'map'
    assert telem.connected == True
    assert telem.armed == False
    assert telem.mode != ''
    assert telem.x == roughly(0.0)
    assert telem.y == roughly(0.0)
    assert telem.z == roughly(0.0)
    assert telem.lat == approx(47.397742)
    assert telem.lon == approx(8.545594)
    assert telem.vx == roughly(0.0)
    assert telem.vy == roughly(0.0)
    assert telem.vz == roughly(0.0)
    assert telem.pitch == roughly(0.0)
    assert telem.roll == roughly(0.0)
    assert telem.yaw == roughly(1.56)
    assert isfinite(telem.voltage)
    assert isfinite(telem.cell_voltage)

def test_telem_rate(node, get_telemetry):
    minimal_rate(lambda: get_telemetry(), 20)
    minimal_rate(lambda: get_telemetry(frame_id='body'), 20)
    minimal_rate(lambda: get_telemetry(frame_id='base_link'), 200)

def test_takeoff_without_auto_arm(node, navigate):
    res = navigate(z=2, frame_id='body')
    assert res.success == False
    assert res.message == 'Copter is not in OFFBOARD mode, use auto_arm?'

def test_takeoff(node, navigate, get_telemetry, tf_buffer):
    res = navigate(z=2, speed=1, frame_id='body', auto_arm=True)
    assert res.success == True, res.message
    rospy.sleep(5)
    telem = get_telemetry()
    assert telem.z == very_roughly(2.0)
    assert telem.x == very_roughly(0.0)
    assert telem.y == very_roughly(0.0)
    assert telem.pitch == roughly(0.0)
    assert telem.roll == roughly(0.0)
    assert telem.yaw == roughly(1.56)

def test_navigate_nans(node, navigate):
    res = navigate(x=float('nan'))
    assert res.success == False
    assert res.message == 'x argument cannot be NaN or Inf'
    res = navigate(y=float('nan'))
    assert res.success == False
    assert res.message == 'y argument cannot be NaN or Inf'
    res = navigate(z=float('nan'))
    assert res.success == False
    assert res.message == 'z argument cannot be NaN or Inf'
    res = navigate(x=float('inf'))
    assert res.success == False
    assert res.message == 'x argument cannot be NaN or Inf'
    res = navigate(y=float('inf'))
    assert res.success == False
    assert res.message == 'y argument cannot be NaN or Inf'
    res = navigate(z=float('inf'))
    assert res.success == False
    assert res.message == 'z argument cannot be NaN or Inf'
    res = navigate(x=float('-inf'))
    assert res.success == False
    assert res.message == 'x argument cannot be NaN or Inf'
    res = navigate(y=float('-inf'))
    assert res.success == False
    assert res.message == 'y argument cannot be NaN or Inf'
    res = navigate(z=float('-inf'))
    assert res.success == False
    assert res.message == 'z argument cannot be NaN or Inf'

def test_navigate(node, navigate, get_telemetry, tf_buffer):
    res = navigate(x=1, y=2, z=3, speed=1)
    assert res.success == True, res.message
    nav_target = tf_buffer.lookup_transform('map', 'navigate_target', rospy.get_rostime(), rospy.Duration(0.2))
    assert nav_target.transform.translation.x == approx(1)
    assert nav_target.transform.translation.y == approx(2)
    assert nav_target.transform.translation.z == approx(3)
    rospy.sleep(10)
    telem = get_telemetry()
    assert telem.x == very_roughly(1.0)
    assert telem.y == very_roughly(2.0)
    assert telem.z == very_roughly(3.0)
    assert telem.pitch == roughly(0.0)
    assert telem.roll == roughly(0.0)
    assert telem.yaw == roughly(0.0)

    res = navigate(x=-1, y=-2, z=-1, frame_id='body', speed=1)
    assert res.success == True, res.message
    nav_target = tf_buffer.lookup_transform('map', 'navigate_target', rospy.get_rostime(), rospy.Duration(0.2))
    assert nav_target.transform.translation.x == very_roughly(0)
    assert nav_target.transform.translation.y == very_roughly(0)
    assert nav_target.transform.translation.z == very_roughly(2)
    rospy.sleep(10)
    telem = get_telemetry()
    assert telem.x == very_roughly(0)
    assert telem.y == very_roughly(0)
    assert telem.z == very_roughly(2)
    assert telem.pitch == roughly(0)
    assert telem.roll == roughly(0)
    assert telem.yaw == roughly(0)

# TODO
# test navigate_global, set_velocity, set_attitude, set_rates

def test_land(node, get_telemetry, land):
    res = land()
    assert res.success, res.message
    telem = get_telemetry()
    assert telem.mode == 'AUTO.LAND'
    assert telem.armed == True, 'Drone unexpectedly disarmed while landing'
    rospy.sleep(12)
    telem = get_telemetry()
    assert telem.mode == 'AUTO.LAND'
    assert telem.armed == False, 'Drone is not disarmed after landing'
