# Working with the camera

> **Note** In the image version **0.20** `clever` package was renamed to `clover`. See [previous version of the article](https://github.com/CopterExpress/clover/blob/v0.19/docs/en/camera.md) for older images.

Make sure the camera is enabled in the `~/catkin_ws/src/clover/clover/launch/clover.launch` file:

```xml
<arg name="main_camera" default="true"/>
```

Also make sure that [position and orientation of the camera](camera_setup.md) is correct.

The `clover` service must be restarted after the launch-file has been edited:

```(bash)
sudo systemctl restart clover
```

You may use rqt or [web_video_server](web_video_server.md) to view the camera stream.

## Troubleshooting

If the camera stream is missing, try using the [`raspistill`](https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md) utility to check whether the camera works.

First, stop the `clover` service:

```bash
sudo systemctl stop clover
```

Then use `raspistill` to capture an image from the camera:

```bash
raspistill -o test.jpg
```

If it doesn't work, check the camera cable connections and the cable itself. Replace the cable if it is damaged. Also, make sure the camera screws don't touch any components on the camera board.

## Camera parameters

Some camera parameters, such as image size, FPS cap, and exposure, may be configured in the `main_camera.launch` file. The list of supported parameters can be found [in the cv_camera repository](https://github.com/OTL/cv_camera#parameters).

Additionally you can specify an arbitrary capture parameter using its [OpenCV code](https://docs.opencv.org/3.3.1/d4/d15/group__videoio__flags__base.html). For example, add the following parameters to the camera node to set exposition manually:

```xml
<param name="property_0_code" value="21"/> <!-- property code 21 is CAP_PROP_AUTO_EXPOSURE -->
<param name="property_0_value" value="0.25"/> <!-- property values are normalized as per OpenCV specs, even for "menu" controls; 0.25 means "use manual exposure" -->
<param name="cv_cap_prop_exposure" value="0.3"/> <!-- set exposure to 30% of maximum value -->
```

## Computer vision

The [SD card image](image.md) comes with a preinstalled [OpenCV](https://opencv.org) library, which is commonly used for various computer vision-related tasks. Additional libraries for converting from ROS messages to OpenCV images and back are preinstalled as well.

### Python

Main article: http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython.

An example of creating a subscriber for a topic with an image from the main camera for processing with OpenCV:

```python
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

rospy.init_node('computer_vision_sample')
bridge = CvBridge()

def image_callback(data):
    cv_image = bridge.imgmsg_to_cv2(data, 'bgr8')  # OpenCV image
    # Do any image processing with cv2...

image_sub = rospy.Subscriber('main_camera/image_raw', Image, image_callback)

rospy.spin()
```

To debug image processing, you can publish a separate topic with the processed image:

```python
image_pub = rospy.Publisher('~debug', Image)
```

Publishing the processed image (at the end of the image_callback function):

```python
image_pub.publish(bridge.cv2_to_imgmsg(cv_image, 'bgr8'))
```

The obtained images can be viewed using [web_video_server](web_video_server.md).

#### Retrieving one frame

It's possibly to retrieve one camera frame at a time. This method works slower than normal topic subscribing and should not be used when it's necessary to process camera images continuously.

```python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

rospy.init_node('computer_vision_sample')
bridge = CvBridge()

# ...

# Retrieve a frame:
img = bridge.imgmsg_to_cv2(rospy.wait_for_message('main_camera/image_raw', Image), 'bgr8')
```

### Examples

#### Working with QR codes

> **Hint** For high-speed recognition and positioning, it is better to use [ArUco markers](aruco.md).

To program actions of the copter for the detection of [QR codes](https://en.wikipedia.org/wiki/QR_code) you can use the [pyZBar](https://pypi.org/project/pyzbar/). This lib is installed in the last image for Raspberry Pi.

QR codes recognition in Python:

```python
import rospy
from pyzbar import pyzbar
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

bridge = CvBridge()

rospy.init_node('barcode_test')

# Image subscriber callback function
def image_callback(data):
    cv_image = bridge.imgmsg_to_cv2(data, 'bgr8')  # OpenCV image
    barcodes = pyzbar.decode(cv_image)
    for barcode in barcodes:
        b_data = barcode.data.decode("utf-8")
        b_type = barcode.type
        (x, y, w, h) = barcode.rect
        xc = x + w/2
        yc = y + h/2
        print("Found {} with data {} with center at x={}, y={}".format(b_type, b_data, xc, yc))

image_sub = rospy.Subscriber('main_camera/image_raw', Image, image_callback, queue_size=1)

rospy.spin()
```

The script will take up to 100% CPU capacity. To slow down the script artificially, you can use [throttling](http://wiki.ros.org/topic_tools/throttle) of frames from the camera, for example, at 5 Hz (`main_camera.launch`):

```xml
<node pkg="topic_tools" name="cam_throttle" type="throttle"
    args="messages main_camera/image_raw 5.0 main_camera/image_raw_throttled"/>
```

The topic for the subscriber in this case should be changed for `main_camera/image_raw_throttled`.

## Video recording

To record a video you can use [`video_recorder`](http://wiki.ros.org/image_view#image_view.2Fdiamondback.video_recorder) node from `image_view` package:

```bash
rosrun image_view video_recorder image:=/main_camera/image_raw
```

The video file will be saved to a file `output.avi`. The `image` argument contains the name of the topic to record.
