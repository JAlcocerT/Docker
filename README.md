Public repo that serves as a pillar for the github page built on: https://jalcocert.github.io/docker/

### Intro

Docker is a tool designed to make it easier to create, deploy, and run applications by using containers.

Containers allow us to package up an application with all of the parts it needs to work properly -  such as libraries and other dependencies, and deploy it as one package.
By doing this, the application will run on any other Linux machine (also windows or ios) regardless of any customized settings that machine might have that could differ from the machine used for writing and testing the code.

 Containers remain lightweight by sharing the OS they run on while isolating processes within user space.
 
Everything needed to run a software application successfully can be stored in a container to make development and deployment more efficient. For this reason, containers are perfect for running microservices.


### Content structure

* Backups:
    * Duplicati :heavy_check_mark:
    * Duplicity
    * Urbackup
    * Filerun
      * Ubuntu :heavy_check_mark:
      * RPI :heavy_check_mark:
    * Nextcloud
      * Ubuntu :heavy_check_mark:
      * RPI :heavy_check_mark:
    * Photos: 
      * Lychee 
      * Photoprism
      * Piwigo
    * RClone :heavy_check_mark:
    * RSync
    * RSnapshot
    * Syncthing :heavy_check_mark:
    * Webdav
    
* Business:
   * ERPs:
       * ERPNext
       * Dolibarr :heavy_check_mark:
       * Odoo (ex- OpenERP) :heavy_check_mark:
    * Management:
       * Vikunja :heavy_check_mark:
       * Leantime (x86 & ARM, :heavy_check_mark:)
* Communication:
   * Chats:
       * Discourse 
       * Jitsi
       * Matrix with synapse :heavy_check_mark:
       * Revolt
       * RocketChat
   * Mail:
       * iRedMail
       * Mailcow
       * Mailinabox
       * Mailserver
       * Mailu (rspamd)
       * Poste
       * Postfix
   * FreshRSS :heavy_check_mark:
    
* IoT:
   * Automations:
        * Domoticz
        * Home Assistant :heavy_check_mark:
        * Home Bridge
        * OpenHab
    * Internet speed tracker :heavy_check_mark:
    * Flame 
    * GPIO
    * Dashboards:
       * NetData :heavy_check_mark:
       * Grafana with Prometheus (internet speed) :heavy_check_mark:
       * Grafana with Prometheus (internet + device with node exporter)
       * Grafana with Graphite StatsD
       * Grafana with InfluxDB (Temperature measuring)
       * Grafana with Proxmox and InfluxDB
       * Grafana with Proxmox and Graphite
       * Grafana with Node-Red
       * EFK stack for logs(Elastic search, Fluentd, Kibana)
       * ELK stack (ES, Logstash, Kibana)
    * Redash
    * GOtify
    * Ntfy (notify)
    * Uptime Kuma
    
* Media
    * Jellyfin :heavy_check_mark:
    * Kodi
    * Plex
    * Emby
    * Calibre :heavy_check_mark:
    * Supysonic    
    * Transmission :heavy_check_mark:
    * rtorrent :heavy_check_mark:
    * Qbittorrent :heavy_check_mark:
    * Bazar :heavy_check_mark:
    * Couchpotato :heavy_check_mark:
    * Jacket :heavy_check_mark:
    * Radarr :heavy_check_mark:
    * Sonarr :heavy_check_mark:
    * ArchiveBox
    * Supysonic
    * Navidrome
    * Mumble
    * Podgrab

* Security:
    * Cloudflare - zero trust tunnel :heavy_check_mark:
    * CoreDNS
    * Unbound :heavy_check_mark:
    * Watchyourlan :heavy_check_mark:
    * Wireshark :heavy_check_mark:
    * Whoogle :heavy_check_mark:
    * Proxies
      * Caddy 
      * NGINX + SSL :heavy_check_mark:
      * NGINX + SSL + Fail2ban
      * NGINX + SSL + Fail2ban + Authelia
      * NGINX + SSL + Fail2ban + Authelia + DuckDNS
      * Traefik
      * Traefik + failban
    * VPN's
      * Gluetun
      * OpenVPN
      * Wirehole
      * Wireguard :heavy_check_mark:
    * Authelia   
    * Crowdsec 
    * Fail2ban  
    * Pihole :heavy_check_mark:
    * PiHole + Cloudflare (DNS over HTTPs)
    * Pi-Alert
    * Watchtower :heavy_check_mark:
    
*  Others:
    * Management:
      * Focalboard :heavy_check_mark:
      * Kanboard
      * OpenProject (Asana alternative)
      * Personal management system
      * Wecan (Kanban board)
    * Grocy :heavy_check_mark:
    * Tiddlywiki
    * VSCode
    * Webtops

* Web
    * Analytics
       * Umami
       * Plausible
    * Dynamic DNS
       * DuckDNS :heavy_check_mark:
       * No-IP
    * Hosting
      * Bludit
      * Wordpress Ubuntu single site :heavy_check_mark:
      * Wordpress Ubuntu multi site
      * Wordpress RPi single site :heavy_check_mark:
      * Wordpress RPi single sites X NginX --> multi sites
      * Wix
      * Ghost
      * Chevereto
    * Instagram alternatives
      * Pixelfed
      * Vero
    * Firefox :heavy_check_mark:
    * Moodle
 * Python apps
 * Shiny dashboards



### Install docker & docker compose & portainer :heavy_check_mark:
```
sudo apt install docker.io -y & sudo docker version

sudo apt-get install docker-compose -y & sudo docker-compose --version

sudo docker run -d -p 9000:9000 -p 8000:8000 --name portainer --restart always -v /var/run/docker.sock:/var/run/docker.sock -v ~/Docker/portainer:/data portainer/portainer-ce

```

To get to know what's the private address of your device and access portainer, simply use: ifconfig, then privateipserver:9000

### Install Yacht (Portainer alternative) :heavy_check_mark:

```
docker run -d -p 8000:8000 -v /var/run/docker.sock:/var/run/docker.sock -v ~/Dockeryacht:/config selfhostedpro/yacht
```

## Useful Docker commands

* see processes running
 ``` 
 ps fax 
 ```

* List containers:
  ```
  docker ps
  ```

* List all containers, even the stopped:
  ```
  docker ps -a | head
  ```

* list all images
  ```
  docker image ls
  ```

* remove unsed images
  ```
  docker image prune -a
  ```

* Test that docker works with this image:
* 
  ```
  docker run hello-world
  ```

* Another image to test:
  ```
  docker pull alpine
  docker pull alpine:3.7
  ```

* Run some command inside the cointainer
  ```
  docker run alpine:3.7 ls -l
  ```
  
* Interactive terminal of the container (execute it and stops the container) :
  ```
  docker run -it alpine:3.7 sh
  ```

* Execute a process inside a container and keep it running if needed :
  ```
  docker run -d nginx:1.15.7 
  docker run -p 80:80 -d nginx (start nginx web server on port 80)
  ```

* executes a command on a running container
  ```
  docker exec -it 554kjgIDfgeofm sh
   
  exit
  docker stop yjbf7i3ID3jkj67
  docker rm yjbf7i3ID3jkj67
  ```
  
* Kali on docker
```
docker pull kalilinux/kali-rolling
docker run --tty --interactive kalilinux/kali-rolling
```

* mount volumes:
  in docker folder:
```
  docker run -v ~/docker/index.html:/usr/share/nginx/html/index.html:ro -d nginx:1.15.7
                 mount this file    into this path with this name, read only  keep it running, image
```
* ports:
```
  expose a port from the container to the host (machine:container)
  docker run -v ~/docker/index.html:/usr/share/nginx/html/index.html:ro -p 8080:80 -d nginx:1.15.7      
```

* change the restart policy of an existing container:
  ```
  docker update --restart unless-stopped running_container_name
  ```
  
* Change the policy of all the containers running:
  ```
  docker update --restart unless-stopped $(docker ps -q)
  ```
 
* Restart all containers:
 ```
 docker restart $(docker ps -a -q)
 ```
 
 * Stop all containers
 ```
 docker container stop $(docker container ls -aq)
 ```
 
 * Remove all stopped containers
 ```
 docker container rm $(docker container ls -aq)
 ```

* create image of a container:
  ```
  docker commit 4699hf7ID7hfty
  docker image ls | head
  ```
  
* create a tag for the image:
  ```
  docker image tag 4699hf7ID7hfty midocker
  docker image tag 4699hf7ID7hfty midocker:1.0

  docker run midocker figlet hola (figlet installed previously in the container and hola as argument)
  docker run ubuntu figlet hola (wont run since it does not have figlet by default)
  ```

* docker file: container based on other image
  FROM ubuntu

  vim Dockerfile
  RUN apt-get update && apt-get install figlet -y

  cd docker/
  docker build -t midocker:1.1
  docker run midocker:1.1 figlet hola

* see the history of an image (historical commands)
  ```
  docker image history 4699hf7ID7hfty
  ```



### DOCKER VOLUMES: 
  * changes inside the container will be gone unless volumes are used
  * mount points inside the container
  
  * check the data stored in volumes (the same volume mounted on a new container, will have the same info available):
  
  ```
  docker volume ls
  ```


### ENV files:
  By having an .env file on the same folder that the docker-compose.yaml file,
  the file can be simplified:


    ### (CLI)
    docker run -d --name example --env-file vars_file.env ubuntu:latest --restart unless-stopped

    ### (Docker compose)
    ---
    version: "2.1"
    services:
      syncthing:
        image: ghcr.io/linuxserver/syncthing
        container_name: syncthing
        hostname: syncthing #optional
        environment:
          - PUID=1000
          - PGID=1000
          - TZ=Europe/Warsaw
        volumes:
          - /home/pi/Docker/Syncthing/config:/config
          - /media/pi/Nowy1/SYNC:/data1
        ports:
          - ${APP_PORT}:8384 ##it will be written in the env file as: APP_PORT=8384 for example
          - 22000:22000/tcp
          - 22000:22000/udp
          - 21027:21027/udp
        restart: unless-stopped
