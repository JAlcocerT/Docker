
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

#use a matrix client, like element, and enjoy
```

#### Revolt


```
```



#### Rocket.Chat


```
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
