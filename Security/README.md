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

#### NginX :heavy_check_mark:

<https://github.com/JAlcocerT/Docker/blob/main/Security/nginx_docker_compose.yaml>
```
sudo docker-compose up -d
```

For the initial setup, check: https://nginxproxymanager.com/setup/#initial-run

Remember to portforward your router to the chosen NginX selected ports on the host.


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




#### Traefik with fail2ban
https://geekland.eu/usar-fail2ban-con-traefik-para-proteger-servicios-que-corren-en-docker/





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

#### Wireguard :heavy_check_mark:

```
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Security/Wireguard_docker_compose.yaml > docker-compose.yaml
sudo docker-compose up -d

sudo docker-compose logs wireguard
```




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


### VPN's

##### Wireguard :heavy_check_mark:

```
<https://github.com/JAlcocerT/Docker/blob/main/Security/Wireguard_docker_compose.yaml>
```

```
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Security/Wireguard > wg.sh && chmod 775 wg.sh && sudo ./wg.sh &&
docker exec -it wireguard wg #to make sur eits running &&
docker logs wireguard #to check the logs
```
##### OpenVPN




