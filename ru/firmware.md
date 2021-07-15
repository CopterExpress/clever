Прошивка полетного контроллера
===

Pixhawk, Pixracer и [COEX Pix](coex_pix.md) можно прошить, используя QGroundControl или утилиты командной строки.

Прошивка для Клевера
---

Для Клевера рекомендуется использование специальной сборки PX4, которая содержит необходимые исправления и более подходящие параметры по умолчанию. Используйте последний стабильный релиз в [GitHub-репозитории](https://github.com/CopterExpress/Firmware/releases), содержащий слово `clover`, например `v1.8.2-clover.4`.

<div id="release" style="display:none">
<p>Последний стабильный релиз: <strong><a id="download-latest-release"></a></strong>.</p>

<ul>
<li>Скачать файл прошивки для COEX Pix и Pixracer (<strong>Клевер 4 / Клевер 3</strong>) – <a id="firmware-pixracer" href=""><code>px4fmu-v4_default.px4</code></a>.</li>
<li>Скачать файл прошивки для Pixhawk (<strong>Клевер 2</strong>) – <a id="firmware-pixhawk" href=""><code>px4fmu-v2_lpe.px4</code></a>.</li>
</ul>
</div>

<script type="text/javascript">
    // get latest release from GitHub
    fetch('https://api.github.com/repos/CopterExpress/Firmware/releases').then(function(res) {
        return res.json();
    }).then(function(data) {
        // look for stable release
        let stable;
        for (let release of data) {
            let clover = (release.name.indexOf('clover') != -1) || (release.name.indexOf('clever') != -1);
            if (clover && !release.prerelease && !release.draft) {
                stable = release;
                break;
            }
        }
        let el = document.querySelector('#download-latest-release');
        el.innerHTML = stable.name;
        el.href = stable.html_url;
        document.querySelector('#release').style.display = 'block';
        for (let asset of stable.assets) {
            console.log(asset.name);
            if (asset.name == 'px4fmu-v4_default.px4') {
                document.querySelector('#firmware-pixracer').href = asset.browser_download_url;
            } else if (asset.name == 'px4fmu-v2_lpe.px4') {
                document.querySelector('#firmware-pixhawk').href = asset.browser_download_url;
            }
        }
    });
</script>

QGroundControl
---

В QGroundControl откройте раздел Firmware. **После** этого подключите полетный контроллер по USB.

Выберите PX4 Flight Stack. Для скачивания и загрузки стандартной прошивки (вариант с EKF2 для Pixhawk) выберите пункт меню "Standard Version", для загрузки собственного файла прошивки выберите пункт "Custom firmware file...", затем нажмите OK.

> **Warning** Не отключайте USB-кабель до окончания процесса прошивки.

<!-- TODO: Иллюстрация. -->

Варианты прошивок
---

В названии файла прошивки кодируется информации о целевой плате и варианте сборки. Примеры:

* `px4fmu-v4_default.px4` — прошивка для COEX Pix и Pixracer с EKF2 и LPE (**Клевер 3** / **Клевер 4**).
* `px4fmu-v2_lpe.px4` — прошивка для Pixhawk с LPE (**Клевер 2**).
* `px4fmu-v2_default.px4` — прошивка для Pixhawk с EKF2.
* `px4fmu-v3_default.px4` — прошивка для более новых версий Pixhawk (чип ревизии 3, см. илл. + Bootloader v5) с EKF2 и LPE.

![STM revision](../assets/stmrev.jpg)

> **Note** Для загрузки `px4fmu-v3_default.px4` может понадобиться использование команды `force_upload` из командной строки.

Командная строка
---

PX4 может быть собран из исходников и загружен в плату автоматически из командной строки.

Для это склонируйте репозиторий PX4:

```bash
git clone https://github.com/PX4/Firmware.git
```

Выберите необходимую версию (тэг) с помощью `git checkout`. Затем соберите и загрузите прошивку:

```
make px4fmu-v4_default upload
```

Где `px4fmu-v4_default` – требуемый вариант прошивки.

Для загрузки прошивки `v3` в Pixhawk может понадобиться команда `force_upload`:

```
make px4fmu-v3_default force-upload
```
