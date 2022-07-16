## VPN's

Check: curl ifconfig.io

##### OpenVPN

```

```

#### Wireguard :heavy_check_mark:

```
<https://github.com/JAlcocerT/Docker/blob/main/Security/Wireguard_docker_compose.yaml>
```

```
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Security/Wireguard > wg.sh && chmod 775 wg.sh && sudo ./wg.sh &&
docker exec -it wireguard wg #to make sur eits running &&
docker logs wireguard #to check the logs
```

* The environment variable PEERS is set to a number or a list of strings separated by comma, the container will run in server mode and the necessary server and peer/client confs will be generated. 

* The peer/client config qr codes will be output in the docker log. They will also be saved in text and png format under /config/peerX in case PEERS is a variable and an integer or /config/peer_X in case a list of names was provided instead of an integer.

* In the config folder -> there is wg0.conf with the server keys and info, then also you see the peer's folders with their needed QR/.conf files
##### Wirehole

```

```




#### Authelia

```
version: '3.3'
    
services:
  authelia:
    image: authelia/authelia
    container_name: authelia
    volumes:
      - ~/Docker/Authelia:/config 
    ports:
      - 9091:9091
    environment:
      - TZ=Europe/Paris
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

## Proxies

#### NginX :heavy_check_mark:

<https://github.com/JAlcocerT/Docker/blob/main/Security/nginx_docker_compose.yaml>
```
#curl https://raw.githubusercontent.com/JAlcocerT/Docker/main/Security/nginx_docker_compose.yaml -O 
wget -c https://raw.githubusercontent.com/JAlcocerT/Docker/main/Security/nginx_docker_compose.yaml -O docker-compose.yml
sudo docker-compose up -d
```

For the initial setup, check: https://nginxproxymanager.com/setup/#initial-run
#admin@example.com
#changeme

Remember to portforward your router to the chosen NginX selected ports on the host.

When adding new services behind this nginx, they must be on the same network as nginx, normally nginx_default, this can be done in portainer or by including it in the docker compose files with:

```
     networks: ["nginx_default"]
     
     
networks:
    nginx_default:
        external: true
```






#### Traefik with fail2ban
https://geekland.eu/usar-fail2ban-con-traefik-para-proteger-servicios-que-corren-en-docker/


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



#### Watchtower :heavy_check_mark:
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

#### Matrix :heavy_check_mark:

```
sudo apt update & sudo apt upgrade -y 
sudo apt-get install docker.io docker-compose -y 
docker run -it --rm -v /root/synapse-data:/data -e SYNAPSE_SERVER_NAME=your.domain.com -e SYNAPSE_REPORT_STATS=yes matrixdotorg/synapse:latest generate 
sudo su
cd
ls
nano docker-compose.yaml
```

<https://github.com/JAlcocerT/Docker/blob/main/Security/matrix_nginx_docker_compose.yaml>
 
Remember to enable registrations:
```
nano synapse-data/homeserver.yaml
enable_registration: true
docker-compose restart synapse
```






