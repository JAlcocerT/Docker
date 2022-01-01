### Torrents

#### rTorrent

```javascript
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/rtorrent > rtorrent.sh && chmod 775 rtorrent.sh && sudo ./rtorrent.sh
docker-compose up -d
```

OR:

```javascript
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/rtorrent_docker_compose_w_environment > docker-compose.yaml

wget  -cO - https://raw.githubusercontent.com/reisikei/Ubuntu/main/variables.env?token=ANL2TWHRX5WRKS3O3ZYJVULBKDBEU > .env
```

#### qBitTorrent 

```javascript
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/Qbittorrent_docker-compose.yaml > docker-compose.yaml

docker-compose up -d
```

OR:

(:heavy_check_mark: Sept 2021)

```javascript
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/Qbittorrent_docker-compose_wenvironment.yaml > docker-compose.yaml

wget  -cO - https://raw.githubusercontent.com/reisikei/Ubuntu/main/variables.env?token=ANL2TWHRX5WRKS3O3ZYJVULBKDBEU > .env
```

#### Transmission

```javascript
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/Transmission_docker_compose > docker-compose.yaml

docker-compose up -d

docker run -d \
  --name=transmission \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/Madrid \
  -p 9091:9091 \
  -p 51413:51413 \
  -p 51413:51413/udp \
  -v /home/pi/Docker/Transmission/config:/config \
  -v /media/pi/Nowy1/DOWNLOADS:/downloads \
  -v /home/pi/Downloads/Transmission/watch:/watch \
  --restart unless-stopped \
  ghcr.io/linuxserver/transmission
```

OR:

```javascript
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/Transmission_docker_compose_w_environment > docker-compose.yaml

wget  -cO - https://raw.githubusercontent.com/reisikei/Ubuntu/main/variables.env?token=ANL2TWHRX5WRKS3O3ZYJVULBKDBEU > .env
```


## Multimedia Center

### Kodi
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/kodi_docker_compose > docker-compose.yaml

### Plex

## Media


#### Bazarr

```
docker run -d --name=bazarr\
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/Madrid \
  -p 6767:6767 \
  -v ~/Docker/Bazarr/config:/config \
  -v ~/Downloads:/movies `#optional` \
  -v ~/Downloads:/tv `#optional` \
  --restart unless-stopped \
  linuxserver/bazarr
  
  #ghcr.io/linuxserver/bazarr
```


#### Couchpotato
```
docker run -d --name=couchpotato\
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
