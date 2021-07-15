# Configuring Wi-Fi

The Raspberry Pi Wi-Fi adapter has two main operating modes:

1. **Client mode** – RPi connects to an existing Wi-Fi network.
2. **Access point mode** – RPi creates a Wi-Fi network that you can connect to.

On our [RPi image](image.md) the Wi-Fi adapter is configured to use the [access point mode](wifi.md) by default.

## Changing the password or SSID (of the network name)

1. Edit the `/etc/wpa_supplicant/wpa_supplicant.conf` file (using [SSH connection](ssh.md)):

    ```bash
    sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
    ```

    In order to change the name of the Wi-Fi network, change the value of the `ssid` parameter; to change the password, change the `psk` parameter. For example:

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

2. Restart Raspberry Pi.

> **Caution** The Wi-Fi network password should be **at least** 8 characters.
>
> If your `wpa_supplicant.conf` is not valid, Raspberry Pi will not allow Wi-Fi connections!

## Switching adapter to the client mode

1. Disable the `dnsmasq` service.

    ```bash
    sudo systemctl stop dnsmasq
    sudo systemctl disable dnsmasq
    ```

2. Enable DHCP client on the wireless interface to obtain IP address. In order to do this, remove the following lines from the `etc/dhcpcd.conf` file:

    ```conf
    interface wlan0
    static ip_address=192.168.11.1/24
    ```

3. Configure `wpa_supplicant` to connect to an existing access point. Change your `/etc/wpa_supplicant/wpa_supplicant.conf` to contain the following:

    ```
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    country=GB

    network={
        ssid="SSID"
        psk="password"
    }
    ```

    where `SSID` is the name of the network, and `password` is its password.

4. Restart the `dhcpcd` service.

    ```bash
    sudo systemctl restart dhcpcd
    ```

## Switching the adapter to the access point mode

1. Enable the static IP address in the wireless interface. Add the following lines to your `/etc/dhcpcd.conf` file:

    ```conf
    interface wlan0
    static ip_address=192.168.11.1/24
    ```

2. Configure wpa_supplicant to work in the access point mode. Change your `/etc/wpa_supplicant/wpa_supplicant.conf` file to contain the following:

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

    where `clover-1234` is the network name and `cloverwifi` is the password.

3. Enable the `dnsmasq` service.

    ```bash
    sudo systemctl enable dnsmasq
    sudo systemctl start dnsmasq
    ```

4. Restart the `dhcpcd` service.

    ```bash
    sudo systemctl restart dhcpcd
    ```

___

Below you can read more about how RPi networking is organized.

## RPi network organization

Network operation in the [image](image.md) is supported by two pre-installed services:

* **networking** — the service enables all network interfaces at startup [5].
* **dhcpcd** — the service ensures that configuration of addressing and routing on the interfaces is obtained dynamically or specified statically in the config file.

To work in the router (access point) mode, RPi requires a DHCP server. It is used to automatically send the settings of the current network to connected clients. `isc-dhcp-server` or `dnsmasq` may be used for this.

### dhcpcd

Starting with Raspbian Jessie, network settings are no longer defined in the `/etc/network/interfaces` file. Now `dhcpcd` is used for sending addressing and routing settings[4].

By default, a dhcp client is enabled in all interfaces. Settings for network interfaces are changed in the `/etc/dhcpcd.conf` file. An access point should have a static IP address. To specify one, add the following lines to the end of the file:

```
interface wlan0
static ip_address=192.168.11.1/24
```

> **Note** If the interface is wireless (wlan), the `dhcpcd` service triggers `wpa_supplicant` [13], which in turn works directly with the Wi-Fi adapter, and sets it to the specified state.

### wpa_supplicant

**wpa_supplicant** — the service configures the Wi-Fi adapter. The `wpa_supplicant` service does not run as a standalone service (although it exists as such), but is instead launched as a `dhcpcd` child process.

By default the config file is `/etc/wpa_supplicant/wpa_supplicant.conf`.
An example of the configuration file:

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

Inside the config file, general `wpa_supplicant` settings, and the settings for the adapter configuration are specified. The configuration file also contains `network` section with the basic settings of the Wi-Fi network, such as network SSID, password, adapter operating mode. There may be several `network` sections, but only the first valid one is used. For example, if the first section contains a connection to an unavailable network, the adapter will be configured according to a next valid section, if there is one. Read more about the syntax of `wpa_supplicant.conf` [TODO WIKI].

#### wpa_passphrase

`wpa_passphrase` — a utility for creating the `network` section.

 ```bash
wpa_passphrase SSID PASSWORD
```

After running the command, copy the resulting section to your config file. You may remove the commented field `psk`, and leave only the field with the password hash, or vice versa.

```bash
network={
	ssid="SSID"
	#psk="PASSWORD"
	psk=c2161655c6ba444d8df94cbbf4e9c5c4c61fc37702b9c66ed37aee1545a5a333
}
```

### Multiple Wi-Fi adapters

The system may use multiple Wi-Fi adapters. If drivers are properly connected to them, they may be viewed by calling `ifconfig` (e.g. `wlan0` and `wlan1`).

If you have multiple adapters, the same working `network` section will be used for all of them. This is due to the fact that for each interface, `dhcpcd` separately creates a child `wpa_supplicant` process, which runs the same code ( since the config is the same).

To make multiple adapters work with individual settings, the mechanism for running different configuration scripts is implemented in the called standard `dhcpcd` script. To use it, rename the standard config file as follows: `wpa_supplicant-<interface name>.conf`, for example `wpa_supplicant-wlan0.conf`.

To apply the settings, restart the parent process — the `dhcpcd` service. This can be done by running the following command:

```bash
sudo systemctl restart dhcpcd
```

### DHCP server

#### dnsmasq-base

`dnsmasq-base` — a command-line utility, which is not a service. To use dnsmasq as a service, install the `dnsmasq` package.

```bash
sudo apt install dnsmasq-base
```

```bash
# Calling dnsmasq-base
sudo dnsmasq --interface=wlan0 --address=/clover/coex/192.168.11.1 --no-daemon --dhcp-range=192.168.11.100,192.168.11.200,12h --no-hosts --filterwin2k --bogus-priv --domain-needed --quiet-dhcp6 --log-queries

# More about dnsmasq-base
dnsmasq --help

# or
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

## Links

1. [habr.com Linux WiFi from the command line with wpa_supplicant](https://habr.com/post/315960/)
2. [wiki.archlinux.org WPA supplicant (Russian)](https://wiki.archlinux.org/index.php/WPA_supplicant_%28%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9%29)
3. [blog.hoxnox.com: WiFi access point with wpa_supplicant](http://blog.hoxnox.com/gentoo/wifi-hotspot.html)
4. [dmitrysnotes.ru: Raspberry Pi 3. Assigning a static IP addresses](http://dmitrysnotes.ru/raspberry-pi-3-prisvoenie-staticheskogo-ip-adresa)
5. [thegeekdiary.com: Linux OS Service ‘network’](https://www.thegeekdiary.com/linux-os-service-network/)
6. [frillip.com: Using your new Raspberry Pi 3 as a Wi-Fi access point with hostapt](https://frillip.com/using-your-raspberry-pi-3-as-a-wifi-access-point-with-hostapd/) (it also contains instructions for setting up forwarding for using RPi as an Internet gateway)
7. [habr.com: Configuring a ddns server on a GNU/Linux Debian 6](https://habr.com/sandbox/30433/) (Good article on configuring a ddns server based on `bind` and `isc-dhcp-server`)
8. [pro-gram.ru to: Setting up and configuring a DHCP server in Ubuntu 16.04.](https://pro-gram.ru/dhcp-server-ubuntu.html) (setup isc-dhcp-server)
9. [expert-orda.ru: Configuring a DHCP server in Ubuntu](http://expert-orda.ru/posts/liuxnewbie/125--dhcp-ubuntu) (setup isc-dhcp-server)
10. [academicfox.com: A Raspberry Pi wireless access point (WiFi access point)](http://academicfox.com/raspberry-pi-besprovodnaya-tochka-dostupa-wifi-access-point/) (setting the routes, hostapd, isc-dhcp-server)
11. [weworkweplay.com: Automatically connect a Raspberry Pi to a Wifi network](http://weworkweplay.com/play/automatically-connect-a-raspberry-pi-to-a-wifi-network/) (Contains settings for creating an open access point)
12. [wiki.archlinux.org: WPA supplicant](https://wiki.archlinux.org/index.php/WPA%20supplicant)
13. [wiki.archlinux.org: dhcpcd](https://wiki.archlinux.org/index.php/Dhcpcd#10-wpa_supplicant) (dhcpcd hook wpa_supplicant)
