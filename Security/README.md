#### Authelia

```

```

#### Fail2Ban :heavy_check_mark:
```
wget  -cO - https://raw.githubusercontent.com/jalcocert/docker/main/Security/fail2ban > f2b.sh && chmod 775 f2b.sh && sudo ./f2b.sh
```

```
 #fail2ban
sudo apt-get install -y \
apt-transport-https \
ca-certificates \
curl \
gnupg2 \
vim \
fail2ban \
ntfs-3g
```

```
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local && #copying it to edit
sudo nano /etc/fail2ban/jail.local
```

Add this to the file to ban for 24h if retry +3 times:


Copy
```
bantime = 86400
port    = ssh
logpath = %(sshd_log)s
backend = %(sshd_backend)s
maxretry = 3
```
```
sudo service fail2ban restart &&
sudo nano /var/log/fail2ban.log
```

https://geekland.eu/instalar-configurar-y-usar-fail2ban-para-evitar-ataques-de-fuerza-bruta/



#### watchtower :heavy_check_mark:
```
#to run once
sudo docker run -d \
    --name watchtower \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower --run-once 
    
#to run on a specific time and remove unused images    
sudo docker run -d \
    --name watchtower \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower --debug --cleanup --schedule "0 30 4 * * *"
    
#to monitor only a container (ex: shipyard)
#sudo docker run -d --name watchtower -v /var/run/docker.sock:/var/run/docker.sock v2tec/watchtower shipyard
```
#https://github.com/containrrr/watchtower
#https://hub.docker.com/r/containrrr/watchtower

#### Wireguard :heavy_check_mark:

```
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Security/Wireguard_docker_compose.yaml > docker-compose.yaml
sudo docker-compose up -d

sudo docker-compose logs wireguard
```

#### PiHole :heavy_check_mark:

```

sudo docker-compose up -d   

#Change DNS on the device or on the router(applicable to all devices connected to the LAN) to the rpi address. For example to 192.168.1.31
    
#nslookup (windows to check router address)
    
  
docker container ls
docker inspect 4648tgIDngkfo30 #get IP address
docker logs 4648tgIDngkfo30 | grep pass #get the password 

#change update frequency when cron updates pihole
sudo nano /etc/cron.d/pihole

#blocklist updates in group management + update the gravity under tools
https://firebog.net/
https://v.firebog.net/hosts/lists.php?type=tick
```


#### NginX :heavy_check_mark:

```
version: "3"
services:
  app:
    image: 'jc21/nginx-proxy-manager:latest'
    restart: unless-stopped
    ports:
      # These ports are in format <host-port>:<container-port>
      - '80:80' # Public HTTP Port
      - '443:443' # Public HTTPS Port
      - '81:81' # Admin Web Port
      # Add any other Stream port you want to expose
      # - '21:21' # FTP

    # Uncomment the next line if you uncomment anything in the section
    # environment:
      # Uncomment this if you want to change the location of 
      # the SQLite DB file within the container
      # DB_SQLITE_FILE: "/data/database.sqlite"

      # Uncomment this if IPv6 is not enabled on your host
      # DISABLE_IPV6: 'true'

    volumes:
      #- ./data:/data
      #- ./letsencrypt:/etc/letsencrypt
      - ~/Docker/Nginx/data:/data
      - ~/Docker/Nginx/letsencrypt:/etc/letsencrypt
```

For the initial setup, check: https://nginxproxymanager.com/setup/#initial-run

Remember to portforward your router to the chosen NginX selected ports on the host.

#### Traefik with fail2ban
https://geekland.eu/usar-fail2ban-con-traefik-para-proteger-servicios-que-corren-en-docker/

#### Authelia



## Communication


#### Jitsi :heavy_check_mark:

```
sudo apt update 
sudo apt upgrade -y
sudo apt-get install docker.io docker-compose -y
git clone https://github.com/jitsi/docker-jitsi-meet && cd docker-jitsi-meet
cp env.example .env
```
sudo nano .env
sudo nano docker-compose.yml --use the latest stable https://hub.docker.com/r/jitsi/web/tags?page=1 (5076)
sudo docker-compose up

#### Matrix

```
sudo apt update & sudo apt upgrade -y 
sudo apt-get install docker.io docker-compose -y 
docker run -it --rm -v /root/synapse-data:/data -e SYNAPSE_SERVER_NAME=matrix.fossengineer.com -e SYNAPSE_REPORT_STATS=yes matrixdotorg/synapse:latest generate 
sudo su
cd
ls
nano docker-compose.yaml
```

```
version: '3.3'

services:

  nginx-proxy:
    image: jwilder/nginx-proxy:0.6.0
    restart: always
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - /var/run/docker.sock:/tmp/docker.sock:ro
      - certs:/etc/nginx/certs:ro
      - confd:/etc/nginx/conf.d
      - vhostd:/etc/nginx/vhost.d
      - html:/usr/share/nginx/html
    labels:
      - com.github.jrcs.letsencrypt_nginx_proxy_companion.nginx_proxy

  letsencrypt:
    image: jrcs/letsencrypt-nginx-proxy-companion:v1.12
    restart: always
    volumes:
      - certs:/etc/nginx/certs:rw
      - confd:/etc/nginx/conf.d
      - vhostd:/etc/nginx/vhost.d
      - html:/usr/share/nginx/html
      - /var/run/docker.sock:/var/run/docker.sock:ro

  synapse:
    image: matrixdotorg/synapse
    restart: always
    expose:
      - "8008"
    volumes:
      - ./synapse-data:/data
    environment:
      VIRTUAL_HOST: matrix.fossengineer.com
      VIRTUAL_PORT: 8008
      LETSENCRYPT_HOST: matrix.fossengineer.com
      LETSENCRYPT_EMAIL: jesalctag@gmail.com

volumes:
  certs:
  confd:
  vhostd:
  html:
```
```
nano synapse-data/homeserver.yaml
enable_registration: true
docker-compose restart synapse
```


### VPN's

##### Wireguard
```
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Security/Wireguard > wg.sh && chmod 775 wg.sh && sudo ./wg.sh &&
docker exec -it wireguard wg #to make sur eits running &&
docker logs wireguard #to check the logs
```
##### OpenVPN




