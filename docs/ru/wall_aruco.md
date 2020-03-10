# Навигация по вертикальным ArUco-маркерам

Алгоритм навигации по визуальным ArUco-маркерам, реализованный в образе Клевера поддерживает гибкую настройку положения маркеров в пространстве, что позволяет располагать их на любой поверхности, под любым углом.

## Установка вертикального крепления камеры

Для более точного распознавания маркеров необходимо установить камеру вертикально, таким образом, чтобы объектив был направлен параллельно горизонту.

> **Note** Конфигурационный файл позволяет настраивать расположение камеры в пространстве относительно коптера любым образом. Для удобства, далее будет рассматриваться вариант установки камеры под 90° к горизонту, по направлению носа коптера.

### Крепление камеры, 3D печать

Распечатайте [крепление камеры](models.html#клевер-3).

Установите крепление в удобное место, таким образом, чтобы в камере было минимальное количество лишних объектов(защита, ножки, пропеллеры, лучи), все эти части будут негативно сказываться на распознавании маркеров.

## Настройка расположения камеры

Чтобы установить расположение камеры под необходимым вам углом, откройте файл `main_camera.launch`, расположенный в *~/catkin_ws/src/clever/clever/launch/*.

```bash
nano ~/catkin_ws/src/clever/clever/launch/main_camera.launch
```

Необходимо или отредактировать одну из конфигурационных строк или добавить строку представленную ниже:

```
<node pkg="tf2_ros" type="static_transform_publisher" name="main_camera_frame" args="0.05 0 0.05 -1.5707963 0 -1.5707963 base_link main_camera_optical"/>
```

> **Note** Единовременно может использоваться только одна конфигурация камеры, если вы вставляете представленную выше строку, не забудьте закомментировать активную на данный момент. Для определения этого, вам поможет подсветка синтаксиса, используемая строка будет подсвечена другим цветом, нежели комментарии. Для комментирования в начало и конец строки добавьте символы *<!-- и -->* соответственно.

Если используемая вами карта маркеров имеет равномерные расстояния между ними, можете воспользоваться [утилитой для создания карт *gen_map.py*](aruco_map.html#настройка-карты-маркеров). В случае если ваши маркеры расположены в случайном порядке вам потребуется задать их вручную, для этого перейдите в директорию *~/catkin_ws/src/clever/aruco_map/map* и создайте файл карты *map_name.txt*. Заполните вашу карту в соответствии с [синтаксисом карт](aruco_map.html#настройка-карты-маркеров). Пример карты маркеров со случайным расположением маркеров:

> **Hint** При введении карты, выберите один из маркеров, как начало координат, и относительно него отмеряйте расстояние до всех остальных маркеров. Вы можете не указывать все 8 параметром, в случае если все ваши маркеры ориентированны одинаково, можно указывать только первые 5: индекс маркера, размера и его расположения в пространстве по осям x, y, z соответственно.

```
106 0.33    0   0   0
103 0.33    1.53    0.23    0
153 0.40    -0.56   1.36    0
```

После того, как карта введена, необходимо применить ее, для этого отредактируйте файл `aruco.launch`, расположенный в *~/catkin_ws/src/clever/clever/launch/*. Измените в нем строку `<param name="map" value="$(find aruco_pose)/map/map_name.txt"/>`, где `map_name.txt` название вашего файла с картой.

При использовании маркеров не привязанных к горизонтальным плоскостям(пол, потолок), необходимо отключить параметр `known_tilt`, как в модуле `aruco_detect`, так и в модуле `aruco_map` в том же файле. Для того, чтобы сделать это автоматически, введите:

```bash
sed -i "/known_tilt/s/value=\".*\"/value=\"\"/" /home/pi/catkin_ws/src/clever/clever/launch/aruco.launch
```

После всех настроек вызовите `sudo systemctl restart clover`, для перезагрузки сервиса *clover*.