* [See this related **blog post** →](https://jalcocert.github.io/JAlcocerT/how-to-use-wg-easy-with-a-vps/)

1. Wireguard
2. [OpenVPN](#openvpn)

---


### WIREGUARD ###

* https://hub.docker.com/r/linuxserver/wireguard


```sh
cd /home/pi/Docker
mkdir wireguard-server
sudo chown pi:pi /home/pi/Docker/wireguard-server
sudo nano docker-compose.yaml

sudo docker-compose up -d
```

```sh
docker exec -it wireguard /app/show-peer 1 #to show QR
sudo docker-compose up -d --force-recreate wireguard #to relaunch wireguard, for example after adding more pairs to docker compose file

cd config
ls
```


### OpenVPN ###

* https://hub.docker.com/r/kylemanna/openvpn
* https://github.com/pablokbs/peladonerd/tree/master/varios/6
* https://www.youtube.com/watch?v=Ulew2JHUHfE&t=444s

```sh
apt-get update && apt-get install docker.io docker-compose -y
vim docker-compose.yaml
```

```yml
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
```


```sh
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
```