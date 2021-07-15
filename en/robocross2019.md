# Robocross-2019

On July, 2019, for the fourth time in a row, the team Copter Express won the annual tests of unmanned vehicles "[Robocross](http://russianrobotics.ru/activities/robokross-2019/)". Tests are held at the GAZ test site near Nizhny Novgorod.

The main objective of the tests in the UAV category was to localize and destroy the target - the red balloon - autonomously.

## Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/zMh5THdHuX8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Implementation

The team used an F450 frame based quadcopter and [Clover software platform](https://github.com/CopterExpress/clover). The final source code is available [on GitHub](https://github.com/CopterExpress/robocross2019/).

`robocross2019` ROS package is divided into two parts: `red_dead_detection` ROS nodelet recognizes the red ball, `ball.py` implements high-level flight logic.

## red_dead_detection

The `red_dead_detection` nodelet recognizes the red ball on the image from the forward looking quadcopter camera (`/front_camera/image_raw` and `/front_camera/camera_info` topics). The simplest method of filtering the image by color is applied. Then the nodelet calculates the geometric center of the detected segments, and performs camera distortion compensation (`cv::undistortPoints`).

Using the known focal lengths of the camera (from `camera_info`), the nodelet calculates the vector directed towards the target. The resulting vector is published to the topic `/red_dead_detection/direction`; its coordinate system (`frame_id` is associated with the front camera `front_camera_optical`).

## balloon.py

To fly towards the ball, the direction vector `red_dead_detection/direction` is used, which is set as a setpoint for the velocity of the drone. The yaw angle is also set towards the ball. The target is considered destroyed when the total area of red pixels is less than the threshold for a certain amount of camera frames.
