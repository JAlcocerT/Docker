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
