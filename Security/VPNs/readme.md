### WIREGUARD ###

https://hub.docker.com/r/linuxserver/wireguard

cd /home/pi/Docker
mkdir wireguard-server
sudo chown pi:pi /home/pi/Docker/wireguard-server
sudo nano docker-compose.yaml

sudo docker-compose up -d


docker exec -it wireguard /app/show-peer 1 #to show QR
sudo docker-compose up -d --force-recreate wireguard #to relaunch wireguard, for example after adding more pairs to docker compose file

cd config
ls

```yml
version: "2.1"
services:
  wireguard:
    image: linuxserver/wireguard
    container_name: wireguard
    cap_add:
      - NET_ADMIN
      - SYS_MODULE
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Madrid
      - SERVERURL=auto #optional
      - SERVERPORT=51820 #optional
      - PEERS=1 #optional
      - PEERDNS=auto #optional
      - INTERNAL_SUBNET=10.13.13.0 #optional
    volumes:
      - /opt/wireguard-server/config:/config
      - /lib/modules:/lib/modules
    ports:
      - 51820:51820/udp
    sysctls:
      - net.ipv4.conf.all.src_valid_mark=1
    restart: unless-stopped
```




### OpenVPN ###

https://hub.docker.com/r/kylemanna/openvpn
https://github.com/pablokbs/peladonerd/tree/master/varios/6
https://www.youtube.com/watch?v=Ulew2JHUHfE&t=444s

apt-get update && apt-get install docker.io docker-compose -y
vim docker-compose.yaml

version: '2'
services:
  openvpn:
    cap_add:
     - NET_ADMIN
    image: kylemanna/openvpn
    container_name: openvpn
    ports:
     - "1194:1194/udp"
    restart: always
    volumes:
     - ./openvpn-data/conf:/etc/openvpn


#to generate the default configuration, include the server public ip address
docker-compose run --rm openvpn ovpn_genconfig -u udp://209...
#create the certifies (main key for the server vpn)
docker-compose run --rm openvpn ovpn_initpki

#it will ask for password to secure that

sudo chown -R $(whoami): ./openvpn-data
docker-compose up -d

#container´s logs
docker-compose logs -f

#Generar un certificado de cliente
export CLIENTNAME=dabo
# con contraseña
docker-compose run --rm openvpn easyrsa build-client-full $CLIENTNAME
# sin contraseña
docker-compose run --rm openvpn easyrsa build-client-full $CLIENTNAME nopass

#Crea el archivo de configuración del cliente
docker-compose run --rm openvpn ovpn_getclient $CLIENTNAME > $CLIENTNAME.ovpn


#Revoca el certificado de un cliente
# Dejando los archivos crt, key y req.
docker-compose run --rm openvpn ovpn_revokeclient $CLIENTNAME
# Borrando los correspondientes archivos crt, key y req.
docker-compose run --rm openvpn ovpn_revokeclient $CLIENTNAME remove


