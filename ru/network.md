# Настройка Wi-Fi

Wi-Fi адаптер на Raspberry Pi имеет два основных режима работы:

1. **Режим клиента** – RPi подключается к существующей Wi-Fi сети.
2. **Режим точки доступа** – RPi создает Wi-Fi сеть, к которой вы можете подключиться.

При использовании [образа для RPi](image.md) по умолчанию Wi-Fi адаптер работает в [режиме точки доступа](wifi.md).

## Изменение пароля или SSID (имени сети)

1. Отредактируйте файл `/etc/wpa_supplicant/wpa_supplicant.conf` (используя [SSH-соединение](ssh.md)):

    ```bash
    sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
    ```

    Измените значение параметра `ssid`, чтобы изменить название Wi-Fi сети, и параметра `psk`, чтобы изменить пароль. Например:

    ```txt
    network={
        ssid="my-super-ssid"
        psk="cloverwifi123"
        mode=2
        proto=RSN
        key_mgmt=WPA-PSK
        pairwise=CCMP
        group=CCMP
        auth_alg=OPEN
    }
    ```

2. Перезагрузите Raspberry Pi.

> **Caution** Длина пароля для Wi-Fi сети должна быть **не менее** 8 символов.
>
> При некорректных настройках `wpa_supplicant.conf` Raspberry Pi перестанет раздавать Wi-Fi!

## Переключение адаптера в режим клиента

1. Выключите службу `dnsmasq`.

    ```bash
    sudo systemctl stop dnsmasq
    sudo systemctl disable dnsmasq
    ```

2. Включите получение IP адреса на беспроводном интерфейсе DHCP клиентом. Для этого удалите из файла `/etc/dhcpcd.conf` строки:

    ```conf
    interface wlan0
    static ip_address=192.168.11.1/24
    ```

3. Настройте `wpa_supplicant` для подключения к существующей точке доступа. Для этого замените содержимое файла `/etc/wpa_supplicant/wpa_supplicant.conf` на:

    ```
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    country=GB

    network={
        ssid="SSID"
        psk="password"
    }
    ```

    где `SSID` – название сети, а `password` – пароль.

4. Перезапустите службу `dhcpcd`.

    ```bash
    sudo systemctl restart dhcpcd
    ```

## Переключение адаптера в режим точки доступа

1. Включите статический IP адрес на беспроводном интерфейсе. Для этого добавьте в файл `/etc/dhcpcd.conf` строки:

    ```conf
    interface wlan0
    static ip_address=192.168.11.1/24
    ```

2. Настроите `wpa_supplicant` на работу в режиме точки доступа. Для этого замените содержимое файла `/etc/wpa_supplicant/wpa_supplicant.conf` на:

    ```
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    country=GB

    network={
        ssid="clover-1234"
        psk="cloverwifi"
        mode=2
        proto=RSN
        key_mgmt=WPA-PSK
        pairwise=CCMP
        group=CCMP
        auth_alg=OPEN
    }
    ```

    где `clover-1234` – название сети, а `cloverwifi` – пароль.

3. Включите службу `dnsmasq`.

    ```bash
    sudo systemctl enable dnsmasq
    sudo systemctl start dnsmasq
    ```

4. Перезапустите службу `dhcpcd`.

    ```bash
    sudo systemctl start dhcpcd
    ```

___

Ниже вы можете узнать больше о том, как устроена работа с сетью на RPi.

## Устройство сети RPi

Работа сети на [образе](image.md) поддерживается двумя предустановленными службами:

* **networking** — служба включает все сетевые интерфейсы в момент запуска [5].
* **dhcpcd** — служба обеспечивает настройку адресации и маршрутизации на интерфейсах, полученных динамически или указанных в файле настроек статически.

Для работы в режиме роутера (точки доступа) RPi необходим DHCP сервер. Он служит для автоматической выдачи настроек текущей сети подключившимся клиентам. В роли такого сервера может выступать `isc-dhcp-server` или `dnsmasq`.

### dhcpcd

Начиная с Raspbian Jessie настройки сети больше не задаются в файле `/etc/network/interfaces`. Теперь за выдачу адресации и настройку маршрутизации отвечает `dhcpcd` [4].

По умолчанию на всех интерфейсах включен dhcp-клиент. Настройки интерфейсов меняются в файле `/etc/dhcpcd.conf`. Для того, чтобы поднять точку доступа необходимо прописать статический ip-адрес. Для этого в конец файла необходимо добавить следующие строки:

```
interface wlan0
static ip_address=192.168.11.1/24
```

> **Note** Если интерфейс является беспроводным (wlan), то служба `dhcpcd` триггерит `wpa_supplicant` [13], который в свою очередь работает непосредственно с wifi-адаптером и переводит его в заданное состояние.

### wpa_supplicant

**wpa_supplicant** – служба конфигурирует Wi-Fi адаптер. Служба `wpa_supplicant` работает не как самостоятельная (хотя как таковая существует), а запускается как дочерний процесс от `dhcpcd`.

Конфигурационный файл по умолчанию должен иметь путь `/etc/wpa_supplicant/wpa_supplicant.conf`.
Пример конфигурационного файла:

```conf
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=GB

network={
        ssid=\"my-clover\"
        psk=\"cloverwifi\"
        mode=2
        proto=RSN
        key_mgmt=WPA-PSK
        pairwise=CCMP
        group=CCMP
        auth_alg=OPEN
}
```

Внутри конфига указываются общие настройки `wpa_supplicant` и параметры для настройки адаптера. Также конфигурационный файл содержит секции `network` – основные настройки Wi-Fi сети такие как SSID сети, пароль, режим работы адаптера. Таких блоков может быть несколько, но используется первый рабочий. Например, если вы указали в первом блоке подключение к некоторой недоступной сети, то адаптер будет настроен следующей удачной секцией, если такая есть. Подробнее о синтаксисе `wpa_supplicant.conf` [TODO WIKI].

#### wpa_passphrase

`wpa_passphrase` – утилита для создания секции `network`.

 ```bash
wpa_passphrase SSID PASSWORD
```

После выполнения команды скопируйте полученную секцию в ваш конфигурационный файл. Можно удалить закоментированное поле `psk` и оставить только поле с хешем пароля, либо наоборот.

```bash
network={
	ssid="SSID"
	#psk="PASSWORD"
	psk=c2161655c6ba444d8df94cbbf4e9c5c4c61fc37702b9c66ed37aee1545a5a333
}
```

### Несколько Wi-Fi адаптеров

В системе может быть несколько Wi-Fi адаптеров. Если для них корректно подключены драйвера, то их можно увидеть вызвав `ifconfig` (например `wlan0` и `wlan1`).

Если у вас несколько адаптеров, для всех будет использоваться одна и таже самая рабочая секция `network`. Это связано с тем, что для каждого интерфейса, `dhcpcd` отдельно создает по дочернему процессу `wpa_supplicant`, в котором выполняется один тот же код (т. к. конфиг один и тот же).

Для работы нескольких адаптеров с отдельными настройками для каждого, в стандартном вызываемом скрипте `dhcpcd` реализован механизм запуска разных конфигурационных скриптов. Для его использования необходимо переименовать стандартный файл конфига по следующему образцу: `wpa_supplicant-<имя интерфейса>.conf`, например `wpa_supplicant-wlan0.conf`.

Для применения настроек необходимо перезапустить родительский процесс – службу `dhcpcd`. Сделать это можно следующей командой:

```bash
sudo systemctl restart dhcpcd
```

### DHCP сервер

#### dnsmasq-base

`dnsmasq-base` – консольная утилита, не являющаяся службой, для использования dnsmasq как службы надо установить пакет `dnsmasq`.

```bash
sudo apt install dnsmasq-base
```

```bash
# Вызов dnsmasq-base
sudo dnsmasq --interface=wlan0 --address=/clover/coex/192.168.11.1 --no-daemon --dhcp-range=192.168.11.100,192.168.11.200,12h --no-hosts --filterwin2k --bogus-priv --domain-needed --quiet-dhcp6 --log-queries

# Подробнее о dnsmasq-base
dnsmasq --help

# или
man dnsmasq
```

#### dnsmasq

```bash
sudo apt install dnsmasq
```

```bash
cat << EOF | sudo tee -a /etc/dnsmasq.conf
interface=wlan0
address=/clover/coex/192.168.11.1
dhcp-range=192.168.11.100,192.168.11.200,12h
no-hosts
filterwin2k
bogus-priv
domain-needed
quiet-dhcp6

EOF
```

#### isc-dhcp-server

```bash
sudo apt install isc-dhcp-server
```

```bash
# https://www.shellhacks.com/ru/sed-find-replace-string-in-file/
sed -i 's/INTERFACESv4=\"\"/INTERFACESv4=\"wlan0\"/' /etc/default/isc-dhcp-server
```

```bash
cat << EOF | sudo tee /etc/dhcp/dhcpd.conf
subnet 192.168.11.0 netmask 255.255.255.0 {
  range 192.168.11.11 192.168.11.254;
  #option domain-name-servers 8.8.8.8;
  #option domain-name "rpi.local";
  option routers 192.168.11.1;
  option broadcast-address 192.168.11.255;
  default-lease-time 600;
  max-lease-time 7200;
}

EOF
```

```bash
cat << EOF | sudo tee /etc/network/if-up.d/isc-dhcp-server && sudo chmod +x /etc/network/if-up.d/isc-dhcp-server
#!/bin/sh
if [ "\$IFACE" = "--all" ];
then sleep 10 && systemctl start isc-dhcp-server.service &
fi

EOF
```

## Ссылки

1. [habr.com: Linux WiFi из командной строки с wpa_supplicant](https://habr.com/post/315960/)
2. [wiki.archlinux.org: WPA supplicant (Русский)](https://wiki.archlinux.org/index.php/WPA_supplicant_%28%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9%29)
3. [blog.hoxnox.com: WiFi access point with wpa_supplicant](http://blog.hoxnox.com/gentoo/wifi-hotspot.html)
4. [dmitrysnotes.ru: Raspberry Pi 3. Присвоение статического IP-адреса](http://dmitrysnotes.ru/raspberry-pi-3-prisvoenie-staticheskogo-ip-adresa)
5. [thegeekdiary.com: Linux OS Service ‘network’](https://www.thegeekdiary.com/linux-os-service-network/)
6. [frillip.com: Using your new Raspberry Pi 3 as a Wi-Fi access point with hostapt](https://frillip.com/using-your-raspberry-pi-3-as-a-wifi-access-point-with-hostapd/) (также здесь есть инструкция по настройке форвардинга для использования RPi в качестве шлюза для выхода в интернет)
7. [habr.com: Настраиваем ddns-сервер на GNU/Linux Debian 6](https://habr.com/sandbox/30433/) (Хорошая статья по настройке ddns-сервера на основе `bind` и `isc-dhcp-server`)
8. [pro-gram.ru: Установка и настройка DHCP сервера на Ubuntu 16.04.](https://pro-gram.ru/dhcp-server-ubuntu.html) (Настройка isc-dhcp-server)
9. [expert-orda.ru: Настройка DHCP-сервера на Ubuntu](http://expert-orda.ru/posts/liuxnewbie/125--dhcp-ubuntu) (Настройка isc-dhcp-server)
10. [academicfox.com: Raspberry Pi беспроводная точка доступа (WiFi access point)](http://academicfox.com/raspberry-pi-besprovodnaya-tochka-dostupa-wifi-access-point/) (Настройка маршрутов, hostapd, isc-dhcp-server)
11. [weworkweplay.com: Automatically connect a Raspberry Pi to a Wifi network](http://weworkweplay.com/play/automatically-connect-a-raspberry-pi-to-a-wifi-network/) (Есть настройки для создания открытой точки доступа)
12. [wiki.archlinux.org: WPA supplicant](https://wiki.archlinux.org/index.php/WPA%20supplicant)
13. [wiki.archlinux.org: dhcpcd](https://wiki.archlinux.org/index.php/Dhcpcd#10-wpa_supplicant) (dhcpcd hook wpa_supplicant)
