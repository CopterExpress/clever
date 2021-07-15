# MAVLink

Основная документация: https://mavlink.io/en/.

MAVLink – это протокол для организации связи между автономными летательными и транспортными системами (дронами, самолетами, автомобилями). Протокол MAVLink лежит в основе взаимодействия между Pixhawk и Raspberry Pi.

В Клевер включено 2 обертки над этим протоколом: [MAVROS](mavros.md) и [simple_offboard](simple_offboard.md).

Код для отправки произвольного MAVLink сообщения можно найти в [примерах](snippets.md#mavlink).

## Основные концепции

### Канал связи

Протокол MAVLink может быть использован поверх следующих каналов связи:

* последовательное соединение (UART, USB и др.);
* UDP (Wi-Fi, Ethernet, 3G, LTE);
* TCP (Wi-Fi, Ethernet, 3G, LTE).

### Сообщение

MAVLink-сообщение это отдельная "порция" данных, передаваемая между устройствами. Отдельное MAVLink-сообщение содержит информацию о состоянии дрона (или другого устройства) или команду для дрона.

Примеры MAVLink-сообщений:

* `ATTITUDE`, `ATTITUDE_QUATERNION` – ориентация квадрокоптера в пространстве;
* `LOCAL_POSITION_NED` – локальная позиция квадрокоптера;
* `GLOBAL_POSITION_INT` – глобальная позиция квадрокоптера (широта/долгота/высота);
* `COMMAND_LONG` – команда для квадрокоптера (взлететь, сесть, переключить режим и т. д.).

Полный список MAVLink-сообщений можно посмотреть в [документации MAVLink](http://mavlink.org/messages/common).

### Система, компонент системы

Каждое устройство (дрон, базовая станция и т. д.) имеет ID в сети MAVLink. В PX4 MAVLink ID меняется с помощью параметра `MAV_SYS_ID`. Каждое MAVLink сообщение содержит поле с ID системы-отправителя. Кроме того, некоторые сообщения (например, `COMMAND_LONG`) содержат также ID системы-получателя.

Помимо ID систем, сообщения могут содержать ID компонента-отправителя и компонента-получателя. Примеры компонентов системы: полетный контроллер, внешняя камера, управляющий бортовой компьютер (Raspberry Pi в случае Клевера) и т. д.

### Пример пакета

Пример структуры MAVLink-пакета с сообщением `COMMAND_LONG`:

<table>
    <tr>
        <th></th>
        <th>Поле</th>
        <th>Длина</th>
        <th>Имя</th>
        <th>Комментарий</th>
    </tr>
    <tr>
        <td rowspan="8"><div style="transform: rotate(-90deg)">Заголовок</div></td>
        <td><code>magic</code></td>
        <td>1 байт</td>
        <td>Метка начала</td>
        <td>0xFD для MAVLink 2.0</td>
    </tr>
    <tr>
        <td><code>len</code></td>
        <td>1 байт</td>
        <td>Размер данных</td>
        <td></td>
    </tr>
    <tr>
        <td><code>incompat_flags</code></td>
        <td>1 байт</td>
        <td>Обратно несовместимые флаги</td>
        <td>На данный момент не используется</td>
    </tr>
    <tr>
        <td><code>compat_flags</code></td>
        <td>1 байт</td>
        <td>Обратно совместимые флаги</td>
        <td>На данный момент не используется</td>
    </tr>
    <tr>
        <td><code>seq</code></td>
        <td>1 байт</td>
        <td>Порядковый номер сообщения</td>
        <td></td>
    </tr>
    <tr>
        <td><code>sysid</code></td>
        <td>1 байт</td>
        <td>ID системы-отправителя</td>
        <td></td>
    </tr>
    <tr>
        <td><code>compid</code></td>
        <td>1 байт</td>
        <td>ID компонента-отправителя</td>
        <td></td>
    </tr>
    <tr>
        <td><code>msgid</code></td>
        <td>3 байта</td>
        <td>ID сообщения</td>
        <td></td>
    </tr>
    <tr style="background: #fffee6">
        <td rowspan="11"><div style="transform: rotate(-90deg)">Данные (пример)</div></td>
        <td><code>target_system</code></td>
        <td>1 байт</td>
        <td>ID системы-получателя</td>
        <td></td>
    </tr>
    <tr style="background: #fffee6">
        <td><code>target_component</code></td>
        <td>1 байт</td>
        <td>ID компонента–получателя</td>
        <td></td>
    </tr>
    <tr style="background: #fffee6">
        <td><code>command</code></td>
        <td>2 байта</td>
        <td>ID команды</td>
        <td></td>
    </tr>
    <tr style="background: #fffee6">
        <td><code>confirmation</code></td>
        <td>1 байт</td>
        <td>Номер для подтверждения</td>
        <td></td>
    </tr>
    <tr style="background: #fffee6">
        <td><code>param1</code></td>
        <td>4 байта</td>
        <td>Параметр 1</td>
        <td rowspan="7">Число с плавающей точкой одинарной точности</td>
    </tr>
    <tr style="background: #fffee6">
        <td><code>param2</code></td>
        <td>4 байта</td>
        <td>Параметр 2</td>
    </tr>
    <tr style="background: #fffee6">
        <td><code>param3</code></td>
        <td>4 байта</td>
        <td>Параметр 3</td>
    </tr>
    <tr style="background: #fffee6">
        <td><code>param4</code></td>
        <td>4 байта</td>
        <td>Параметр 4</td>
    </tr>
    <tr style="background: #fffee6">
        <td><code>param5</code></td>
        <td>4 байта</td>
        <td>Параметр 5</td>
    </tr>
    <tr style="background: #fffee6">
        <td><code>param6</code></td>
        <td>4 байта</td>
        <td>Параметр 6</td>
    </tr>
    <tr style="background: #fffee6">
        <td><code>param7</code></td>
        <td>4 байта</td>
        <td>Параметр 7</td>
    </tr>
    <tr>
        <td></td>
        <td><code>checksum</code></td>
        <td>2 байта</td>
        <td>Контрольная сумма</td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td><code>signature</code></td>
        <td>13 байт</td>
        <td>Сигнатура (опционально)</td>
        <td>Позволяет убедиться, что пакет не был скомпрометирован.
Обычно не используется.</td>
    </tr>
</table>

<span style="background: #fffee6">Желтым</span> цветом выделены поля данных (полезной нагрузки). Для каждого типа сообщения существует свой набор таких полей.
