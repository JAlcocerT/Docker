
## Why Guacamole?

<https://www.youtube.com/watch?v=2SqeaKLwlM4>

Keep your desktop in the cloud.

The idea is simple: Get Guacamole install in a computer. Use another PC with a browser to control that first computer.

<https://guacamole.apache.org/>

## What is Guacamole?
<https://www.youtube.com/watch?v=LWdxhZyHT_8>

https://www.wundertech.net/how-to-setup-apache-guacamole-on-a-raspberry-pi/

## Deploying Guacamole with Docker

### Guacamole Docker CLI


### Guacamole Docker Stack 

Previously: https://hub.docker.com/r/oznu/guacamole/

<https://hub.docker.com/r/jwetzell/guacamole/>
<https://github.com/jwetzell/docker-guacamole>


```yml
version: "3"
services:
  guacamole:
    image: jwetzell/guacamole
    container_name: guacamole
    volumes:
      - guacamole_config:/config
    ports:
      - 8066:8080

volumes:
  guacamole_config:
```

<!-- The default username is guacadmin with password guacadmin.
 -->


<!-- ```yml
version: "3"
services:
  guacamole:
    image: jwetzell/guacamole:arm64
    container_name: guacamole
    volumes:
      - ./guacamole/config:/config
    ports:
      - 8066:8080

``` -->


https://192.168.3.130:8443/#

### Configuring Guacamole

**The default logins are** username: guacadmin, password: guadcadmin
    * Create your user: go to settings -> Users -> New User
    * Then enter with your user that you just created and disable de login of the default user for security reasons.

* At this point we are ready to **create a connection**:
    * Settings -> Connections
    * Choose between the protocols: SSH (for terminal only), VNC to have full desktop
    * Under Parameters -> Network -> fill your own Hostname (you can try local ip first) and port (5901)
    * Visit Home, to see your connections and try it

You need to make sure that the host machine is having VNC installed.

<https://www.tecmint.com/install-tightvnc-access-remote-desktop-in-linux/>

Also, [check that the VNC port]() is opened.

vncserver GUI:

sudo apt-get update && sudo apt-get upgrade
sudo apt-get install -y ubuntu-desktop gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal


## FAQ

<!-- 
### Wake on Lan -->


<!-- 
WINDOWS RDP -->

### How to check VNC port status

<https://jalcocert.github.io/Linux/docs/debian/securing_linux/#firewall-setup-ufw>

The port for VNC is 5900 by default.

```sh
sudo apt-get install nmap
#nmap --version
```

Then, check with:

nmap localhost

```sh
apt install ufw
sudo ufw status
sudo ufw enable

sudo ufw allow 5900/tcp
sudo ufw status
```