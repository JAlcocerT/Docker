## Torrents

### rTorrent
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/rtorrent > rtorrent.sh && chmod 775 rtorrent.sh && sudo ./rtorrent.sh

docker-compose up -d

### qBitTorrent
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/Qbittorrent_docker-compose.yaml > Wordpress_docker-compose.yaml

docker-compose up -d

### Transmission
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/Transmission_docker_compose > Wordpress_docker-compose.yaml

docker-compose up -d


## Media

wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/Bazarr > Bazarr.sh && chmod 775 Bazarr.sh && sudo ./Bazarr.sh

wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/Couchpotato > Couchpotato.sh && chmod 775 Couchpotato.sh && sudo ./Couchpotato.sh

wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/Jackett > Jackett.sh && chmod 775 Jackett.sh && sudo ./Jackett.sh

wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/Radarr > Radarr.sh && chmod 775 Radarr.sh && sudo ./Radarr.sh

wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Media/Sonarr > Sonarr.sh && chmod 775 Sonarr.sh && sudo ./Sonarr.sh
