### Multimedia Center

#### Kodi
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/kodi_docker_compose > docker-compose.yaml

#### Plex
```
---
version: "2.1"
services:
  plex:
    #image: linuxserver/plex:arm64v8-latest #for RPi
    #image: linuxserver/plex:amd64-latest #for am64
    container_name: plex
    network_mode: host
    environment:
      - PUID=1000
      - PGID=1000
      - VERSION=docker
    volumes:
      - ~/Docker/Plex/config:/config
      - /media/pi/Nowy:/media #(Ruta donde tenéis montado vuestro disco duro)
    restart: unless-stopped
```
Port 32400

### Torrents

#### Transmission :heavy_check_mark:

```
docker run -d --name=transmission \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/Madrid \
  -e USER=username `#optional` \
  -e PASS=password `#optional` \
  -p 9091:9091 \
  -p 51413:51413 \
  -p 51413:51413/udp \
  -v ~/Docker/Transmission/config:/config \
  -v ~/Downloads/Torrents/Transmission:/downloads \
  -v ~/Downloads/Torrents/watch:/watch \
  --restart unless-stopped \
  ghcr.io/linuxserver/transmission
```

#### rTorrent :heavy_check_mark:

```
docker run -d --name=rutorrent\
  -e PUID=1000 \
  -e PGID=1000 \
  -p 8087:80 \
  -p 5007:5000 \
  -p 51417:51413 \
  -p 6887:6881/udp \
  -v ~/Docker/rtorrent:/config \
  -v /media/pi/Nowy/DOWNLOADS:/downloads \
  --restart unless-stopped \
  ghcr.io/linuxserver/rutorrent
```

OR:

```javascript
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/rtorrent_docker_compose_w_environment > docker-compose.yaml

wget  -cO - https://raw.githubusercontent.com/reisikei/Ubuntu/main/variables.env?token=ANL2TWHRX5WRKS3O3ZYJVULBKDBEU > .env
```

#### qBitTorrent :heavy_check_mark:

```
docker run -d --name=qbittorrent\
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/Madrid \
  -e WEBUI_PORT=8083 \
  -p 6883:6881 \
  -p 6883:6881/udp \
  -p 8083:8080 \
  -v ~/Docker/qbittorrent/config:/config \
  -v /media/pi/Nowy/DOWNLOADS:/downloads \
  --restart unless-stopped \
  ghcr.io/linuxserver/qbittorrent
```

OR:

(:heavy_check_mark: Sept 2021)

```javascript
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/Qbittorrent_docker-compose_wenvironment.yaml > docker-compose.yaml

wget  -cO - https://raw.githubusercontent.com/reisikei/Ubuntu/main/variables.env?token=ANL2TWHRX5WRKS3O3ZYJVULBKDBEU > .env
```



### Extra

#### Bazarr

```
docker run -d --name=bazarr \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/Madrid \
  -p 6780:6767 \
  -v ~/Docker/Bazarr/config:/config \
  -v ~/Downloads:/movies `#optional` \
  -v ~/Downloads:/tv `#optional` \
  --restart unless-stopped \
  linuxserver/bazarr
  
  #ghcr.io/linuxserver/bazarr
```


#### Couchpotato :heavy_check_mark:
```
docker run -d --name=couchpotato \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/Madrid \
  -p 5050:5050 \
  -v ~/Docker/couchpotato/config:/config \
  -v ~/Downloads/couchpotato/downloads:/downloads \
  -v ~/Downloads/couchpotato/movies:/movies \
  --restart unless-stopped \
  linuxserver/couchpotato
  
  #ghcr.io/linuxserver/couchpotato
```

#### Jacket :heavy_check_mark:

```
docker run -d --name=jackett \
-e PUID=1000 \
-e PGID=1000 \
-e TZ=Europe/Madrid \
-p 9117:9117 \
-v ~/Docker/Jackett/config:/config \
-v ~/Downloads/Jackett/downloads:/downloads \
--restart unless-stopped \
linuxserver//jackett

 #ghcr.io/linuxserver/jackett
```

#### Radarr :heavy_check_mark:

```
docker run -d --name=radarr \
-e PUID=1000 \
-e PGID=1000 \
-e TZ=Europe/Madrid \
-p 7878:7878 \
-v ~/Docker/Radarr/config:/config \
-v /path/to/movies:/movies `#optional` \
-v ~/Downloads/Radarr/downloads:/downloads `#optional` \
--restart unless-stopped \
linuxserver/radarr

#ghcr.io/linuxserver/radarr
  ```

#### Sonarr :heavy_check_mark:

```
docker run -d --name=sonarr \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/Madrid \
  -p 8989:8989 \
  -v ~/Docker/Sonarr/config:/config \
  -v /path/to/tvseries:/tv `#optional` \
  -v /path/to/downloadclient-downloads:/downloads `#optional` \
  --restart unless-stopped \
  linuxserver/sonarr
  
  #ghcr.io/linuxserver/sonarr
 ```
