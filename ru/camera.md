# Работа с камерой

> **Note** В версии образа **0.20** пакет и сервис `clever` был переименован в `clover`. Для более ранних версий см. документацию для версии [**0.19**](https://github.com/CopterExpress/clover/blob/v0.19/docs/ru/camera.md).

<!-- TODO: физическое подключение -->

Для работы с основной камерой необходимо убедиться что она включена в файле `~/catkin_ws/src/clover/clover/launch/clover.launch`:

```xml
<arg name="main_camera" default="true"/>
```

Также нужно убедиться, что камера [сфокусирована и для нее указано корректное расположение и ориентация](camera_setup.md).

При изменении launch-файла необходимо перезапустить пакет `clover`:

```bash
sudo systemctl restart clover
```

Для мониторинга изображения с камеры можно использовать [rqt](rviz.md) или [web_video_server](web_video_server.md).

## Неисправности

Если изображение с камеры отсутствует, попробуйте проверить ее с помощью утилиты [`raspistill`](https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md).

Остановите сервисы Клевера:

```bash
sudo systemctl stop clover
```

Получите картинку с камеры утилитой `raspistill`:

```bash
raspistill -o test.jpg
```

Если команда завершается с ошибкой, проверьте качество подключения шлейфа камеры к Raspberry Pi или замените его.

## Настройки камеры

Ряд параметров камеры - размер изображения, максимальную частоту кадров, экспозицию - можно настроить в файле `main_camera.launch`. Список настраиваемых параметров можно [посмотреть в репозитории cv_camera](https://github.com/OTL/cv_camera#parameters).

Параметры, не указанные в этом списке, можно указывать через [код параметра OpenCV](https://docs.opencv.org/3.3.1/d4/d15/group__videoio__flags__base.html). Например, для установки фиксированной экспозиции добавьте следующие параметры в ноду камеры:

```xml
<param name="property_0_code" value="21"/> <!-- property code 21 is CAP_PROP_AUTO_EXPOSURE -->
<param name="property_0_value" value="0.25"/> <!-- property values are normalized as per OpenCV specs, even for "menu" controls; 0.25 means "use manual exposure" -->
<param name="cv_cap_prop_exposure" value="0.3"/> <!-- set exposure to 30% of maximum value -->
```

## Компьютерное зрение

Для реализации алгоритмов компьютерного зрения рекомендуется использовать предустановленную на [образ SD-карты](image.md) библиотеку [OpenCV](https://opencv.org).

### Python

Основная статья: http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython.

Пример создания подписчика на топик с изображением с основной камеры для обработки с использованием OpenCV:

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

Для отладки обработки изображения можно публиковать отдельный топик с обработанным изображением:

```python
image_pub = rospy.Publisher('~debug', Image)
```

Публикация обработанного изображения (в конце функции image_callback):

```python
image_pub.publish(bridge.cv2_to_imgmsg(cv_image, 'bgr8'))
```

Получаемые изображения можно просматривать используя [web_video_server](web_video_server.md).

#### Получение одного кадра

Существует возможность единоразового получения кадра с камеры. Этот способ работает медленнее, чем подписка на топик; его не следует применять в случае необходимости постоянной обработки изображений.

```python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

rospy.init_node('computer_vision_sample')
bridge = CvBridge()

# ...

# Получение кадра:
img = bridge.imgmsg_to_cv2(rospy.wait_for_message('main_camera/image_raw', Image), 'bgr8')
```

### Примеры

#### Работа с QR-кодами

> **Hint** Для высокоскоростного распознавания и позиционирования лучше использовать [ArUco-маркеры](aruco.md).

Для программирования различных действий коптера при детектировании нужных [QR-кодов](https://ru.wikipedia.org/wiki/QR-код) можно использовать библиотеку [pyZBar](https://pypi.org/project/pyzbar/). Она уже установлена в последнем образе для Raspberry Pi.

Распознавание QR-кодов на Python:

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

Скрипт будет занимать 100% процессора. Для искусственного замедления работы скрипта можно запустить [throttling](http://wiki.ros.org/topic_tools/throttle) кадров с камеры, например, в 5 Гц (`main_camera.launch`):

```xml
<node pkg="topic_tools" name="cam_throttle" type="throttle"
    args="messages main_camera/image_raw 5.0 main_camera/image_raw_throttled"/>
```

Топик для подписчика в этом случае необходимо поменять на `main_camera/image_raw_throttled`.

## Запись видео

Для записи видео может использована нода [`video_recorder`](http://wiki.ros.org/image_view#image_view.2Fdiamondback.video_recorder) из пакета `image_view`:

```bash
rosrun image_view video_recorder image:=/main_camera/image_raw
```

Видео будет сохранено в файл `output.avi`. В аргументе `image` указывается название топика для записи видео.
