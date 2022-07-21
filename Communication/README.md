## Chats:

#### Discourse

```
sudo apt update && sudo apt upgrade -y && sudo apt-get install docker.io docker-compose -y
mkdir discourse && cd discourse/

git clone https://github.com/discourse/discourse_docker
cd discourse_docker/
cp samples/standalone.yml containers/app.yml && sudo nano containers/app.yml
```

https://github.com/discourse/discourse/blob/main/docs/INSTALL-email.md

```
#install discourse
sudo ./discourse-setup
#./launcher bootstrap app
#Start Discourse
/var/docker/launcher start app
```

#### Jitsi

```
```

#### Mattermost


```
```

#### Matrix with synapse :heavy_check_mark:

First step - generate the configuration with
```
sudo docker run -it --rm -v ~/Docker/synapse/data:/data -e SYNAPSE_SERVER_NAME=matrix.yourdomain.com -e SYNAPSE_REPORT_STATS=yes matrixdotorg/synapse:latest generate

#or if the latest does not generate a proper configfile, try a previous one:

sudo docker run -it --rm -v ~/Docker/synapse/data:/data -e SYNAPSE_SERVER_NAME=matrix.yourdomain.com -e SYNAPSE_REPORT_STATS=yes matrixdotorg/synapse:v1.60.0 generate
```

* Creating a new nginx proxy for this  :heavy_check_mark:
```
mkdir reverse-proxy && cd reverse-proxy

docker network create server
nano docker-compose.yaml #1st part
docker compose up -d #to the first part

mkdir synapse && cd synapse
nano docker-compose.yaml #2nd part
mkdir data
docker-compose run --rm synapse generate
nano homeserver.yaml #allow registrations
docker-compose up -d
#docker-compose restart synapse #if its already running

#use a matrix client, like element, and enjoy
```

* Reusing an existing nginx proxy manager :heavy_check_mark:

If there is already an instance of [nginx running](https://github.com/JAlcocerT/Docker/blob/main/Security/nginx_docker_compose.yaml), you can deploy the below docker compose file (nginx_default is the name of nginx network that is already created by default, but you could have named it in another way).

```
version: "3.3"

services:
    synapse:
        image: "matrixdotorg/synapse:latest"
        container_name: "synapse"
        volumes:
            - "./data:/data"
        environment:
            VIRTUAL_HOST: "your.domain.com"
            VIRTUAL_PORT: 8008
            LETSENCRYPT_HOST: "your.domain.com"
            SYNAPSE_SERVER_NAME: "your.domain.com"
            SYNAPSE_REPORT_STATS: "yes"
        networks: ["nginx_default"]


networks:
    nginx_default:
        external: true
```
Then, use nginx portal to add the domain + name of the docker container (synapse) + the port as 8008 (as defined here).

#### Revolt


```
```



#### Rocket.Chat


```
```

## Mails: (mail tester: <https://www.mail-tester.com/>)

### iredmail

### mailcow

```
#in /opt
sudo git clone https://github.com/mailcow/mailcow-dockerized
sudo bash generate_config.sh 
sudo nano mailcow.conf
```

#### FreshRSS :heavy_check_mark:

```
---
version: "2.1"
services:
  freshrss:
    image: lscr.io/linuxserver/freshrss
    container_name: freshrss
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - /path/to/data:/config
    ports:
      - 70:80
    restart: unless-stopped
 ```
