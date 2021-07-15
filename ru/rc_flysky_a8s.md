# Работа с приёмником Flysky FS-A8S

Приёмник Flysky FS-A8S совместим с пультами Flysky FS-i6 и FS-i6x. Связь с полётным контроллером может происходить как с использованием аналогового протокола PPM, так и при помощи цифровых протоколов S.Bus/i-Bus.

Для подключения к полётному контроллеру рекомендуется использовать протокол S.Bus.

## Изготовление кабеля для подключения к полётному контроллеру

> **Note** Если в вашем наборе уже есть кабель для подключения приёмника к полётному контроллеру, совместимому с вашим, переходите к [следующему этапу](#rc_bind).

1. Аккуратно извлеките жёлтый провод из коннектора, идущего к приёмнику. Для того, чтобы вытащить провод, приподнимите острым пинцетом замок коннектора:

    <div class="image-group">
        <img src="../assets/flysky_a8s/01_remove_cable_fs.png" width=300 class="zoom border" alt="a8s wire removal 1">
        <img src="../assets/flysky_a8s/02_remove_cable_fs.png" width=300 class="zoom border" alt="a8s wire removal 2">
    </div>

2. [При использовании полётного контроллера Pixracer] Извлеките 2 провода - зелёный и коричневый - из 5-пинового коннектора для полётного контроллера:

    <div class="image-group">
        <img src="../assets/flysky_a8s/03_remove_cable_pixracer.png" width=300 class="zoom border" alt="pixracer wire removal 1">
        <img src="../assets/flysky_a8s/04_remove_cable_pixracer.png" width=300 class="zoom border" alt="pixracer wire removal 2">
    </div>

3. [При использовании полётного контроллера COEX Pix] Извлеките зелёный (или синий, в зависимости от комплектации) провод из 4-пинового коннектора для полётного контроллера:

    <div class="image-group">
        <img src="../assets/flysky_a8s/05_remove_cable_coexpix.png" width=300 class="zoom border" alt="coexpix wire removal 1">
        <img src="../assets/flysky_a8s/06_remove_cable_coexpix.png" width=300 class="zoom border" alt="coexpix wire removal 2">
    </div>

4. С помощью бокорезов обрежьте концы кабелей с разъёмами Dupont (чёрными):

    <div class="image-group">
        <img src="../assets/flysky_a8s/07_wirecuts_1.png" width=300 class="zoom border" alt="wire cutting">
        <img src="../assets/flysky_a8s/08_wirecuts_2.png" width=300 class="zoom border" alt="wire cuts">
    </div>

5. Зачистите и залудите 5-7 мм провода с каждой стороны:

    <img src="../assets/flysky_a8s/09_wirecuts_stripped.png" width=300 class="zoom border center" alt="tinning prep">

6. Наденьте термоусадочные трубки на провода:

    <img src="../assets/flysky_a8s/10_heatshrink.png" width=300 class="zoom border center" alt="shrink tubing">

7. Спаяйте провода по следующей схеме:
    * чёрный провод приёмника с чёрным проводом кабеля полётного контроллера;
    * красный провод приёмника с красным проводом кабеля полётного контроллера;
    * белый провод приёмника с белым (при использовании Pixracer) или жёлтым (при использовании COEX Pix) проводом кабеля полётного контроллера:

    <img src="../assets/flysky_a8s/11_solder_scheme.png" width=300 class="zoom border center" alt="wire soldering">

8. Переместите термоусадочные трубки на места пайки и прогрейте их феном:

    <img src="../assets/flysky_a8s/12_heatshrink_heat.png" width=300 class="zoom border center" alt="shrink tube heating">

9. Скрутите готовые кабели:

    <img src="../assets/flysky_a8s/13_cable_twist.png" width=300 class="zoom border center" alt="twisted cables">

С помощью изготовленного кабеля подключите приёмник к полётному контроллеру к порту RC IN:

<div class="image-group">
    <img src="../assets/flysky_a8s/14_pixracer_rcin.png" width=300 class="zoom border center" alt="pixracer connection">
    <img src="../assets/flysky_a8s/14_coexpix_rcin.png" width=300 class="zoom border center" alt="coex pix connection">
</div>

> **Hint** Убедитесь, что провод, идущий в COEX Pix, подключен к порту RC IN:
<img src="../assets/coexpix-bottom.jpg" width=300 class="zoom border center" alt="coex pix pinout">

## Сопряжение приёмника с пультом {#rc_bind}

Для сопряжения приёмника с пультом:

1. Убедитесь, что полётный контроллер выключен.
2. Зажмите кнопку **BIND** на приёмнике:

    <img src="../assets/flysky_a8s/15_bind_key.png" width=300 class="zoom border center" alt="bind key">

3. Включите полётный контроллер. Светодиод на приёмнике должен замигать с высокой частотой.

    <img src="../assets/flysky_a8s/16_blink_fast.gif" width=300 class="zoom border center" alt="fast blink">

4. Зажмите клавишу **BIND KEY** на пульте и включите его. На пульте должно появиться сообщение **RX Binding...**

    <img src="../assets/flysky_a8s/17_controller_rxbind.png" width=300 class="zoom border center" alt="rx binding">

5. Светодиод на приёмнике должен замигать с низкой частотой.

    <img src="../assets/flysky_a8s/16_blink_slow.gif" width=300 class="zoom border center" alt="slow blink">

6. Выключите и включите пульт. Светодиод на приёмнике должен светиться непрерывно.

    <img src="../assets/flysky_a8s/16_bind_indicator.png" width=300 class="zoom border center" alt="steady glow">

> **Note** Данный приёмник не передаёт телеметрию обратно на пульт. Это значит, что на экране пульта не будет отображаться информация об уровне сигнала и напряжении на приёмнике. Эта особенность приёмника не является неисправностью и не влияет на управление.

## Выбор режима приёмника

Откройте QGroundControl и подключите полётный контроллер к компьютеру. Откройте вкладку Radio:

![qgc radio pane](../assets/flysky_a8s/18_qgc_radio.png)

Если справа (под изображением пульта) не показано ни одного канала, зажмите кнопку **BIND** на приёмнике на 2 секунды. Должно появиться 18 каналов:

![qgc radio with channels](../assets/flysky_a8s/19_qgc_channels.png)
