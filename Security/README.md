#### Fail2Ban
```
wget  -cO - https://raw.githubusercontent.com/jalcocert/docker/main/Security/fail2ban > f2b.sh && chmod 775 f2b.sh && sudo ./f2b.sh
```

#### watchtower :heavy_check_mark:
```
sudo docker run -d \
    --name watchtower \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower --run-once 
```

#### PiHole

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
sudo nano docker-compose.yml --use the latest stable https://hub.docker.com/r/jitsi/web/tags?page=1
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




