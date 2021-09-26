## Torrents

### rTorrent
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/rtorrent > rtorrent.sh && chmod 775 rtorrent.sh && sudo ./rtorrent.sh

docker-compose up -d

OR:

wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/rtorrent_docker_compose_w_environment > docker-compose.yaml

wget  -cO - https://raw.githubusercontent.com/reisikei/Ubuntu/main/variables.env?token=ANL2TWHRX5WRKS3O3ZYJVULBKDBEU > .env

### qBitTorrent 
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/Qbittorrent_docker-compose.yaml > docker-compose.yaml

docker-compose up -d

OR:

(:heavy_check_mark: Sept 2021)

wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/Qbittorrent_docker-compose_wenvironment.yaml > docker-compose.yaml

wget  -cO - https://raw.githubusercontent.com/reisikei/Ubuntu/main/variables.env?token=ANL2TWHRX5WRKS3O3ZYJVULBKDBEU > .env


### Transmission
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/Transmission_docker_compose > docker-compose.yaml

docker-compose up -d

OR:

wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/Transmission_docker_compose_w_environment > docker-compose.yaml

wget  -cO - https://raw.githubusercontent.com/reisikei/Ubuntu/main/variables.env?token=ANL2TWHRX5WRKS3O3ZYJVULBKDBEU > .env



## Multimedia Center

### Kodi
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/kodi_docker_compose > docker-compose.yaml

### Plex

## Media

wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/Bazarr > Bazarr.sh && chmod 775 Bazarr.sh && sudo ./Bazarr.sh

wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/Couchpotato > Couchpotato.sh && chmod 775 Couchpotato.sh && sudo ./Couchpotato.sh

wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/Jackett > Jackett.sh && chmod 775 Jackett.sh && sudo ./Jackett.sh

wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/Radarr > Radarr.sh && chmod 775 Radarr.sh && sudo ./Radarr.sh

wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/Sonarr > Sonarr.sh && chmod 775 Sonarr.sh && sudo ./Sonarr.sh
