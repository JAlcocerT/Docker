## Torrents

### rTorrent

```javascript
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/rtorrent > rtorrent.sh && chmod 775 rtorrent.sh && sudo ./rtorrent.sh
docker-compose up -d
```

OR:

```javascript
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/rtorrent_docker_compose_w_environment > docker-compose.yaml

wget  -cO - https://raw.githubusercontent.com/reisikei/Ubuntu/main/variables.env?token=ANL2TWHRX5WRKS3O3ZYJVULBKDBEU > .env
```

### qBitTorrent 

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

### Transmission

```javascript
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/Transmission_docker_compose > docker-compose.yaml

docker-compose up -d
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

wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/Bazarr > Bazarr.sh && chmod 775 Bazarr.sh && sudo ./Bazarr.sh

wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/Couchpotato > Couchpotato.sh && chmod 775 Couchpotato.sh && sudo ./Couchpotato.sh

wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/Jackett > Jackett.sh && chmod 775 Jackett.sh && sudo ./Jackett.sh

wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/Radarr > Radarr.sh && chmod 775 Radarr.sh && sudo ./Radarr.sh

```
docker run -d \
  --name=radarr \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/Madrid \
  -p 7878:7878 \
  -v ~/Docker/Radarr/config:/config \
  -v /path/to/movies:/movies `#optional` \
  -v ~/Downloads/Radarr/downloads:/downloads `#optional` \
  --restart unless-stopped \
  #ghcr.io/linuxserver/radarr
  ```

wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/Sonarr > Sonarr.sh && chmod 775 Sonarr.sh && sudo ./Sonarr.sh

```
docker run -d \
  --name=sonarr \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/Madrid \
  -p 8989:8989 \
  -v ~/Docker/Sonarr/config:/config \
  -v /path/to/tvseries:/tv `#optional` \
  -v /path/to/downloadclient-downloads:/downloads `#optional` \
  --restart unless-stopped \
  #ghcr.io/linuxserver/sonarr
 ```
