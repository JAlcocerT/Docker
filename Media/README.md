## Media Containers

### Multimedia Center

* Kodi

```sh
wget  -cO - https://raw.githubusercontent.com/JAlcocerT/Docker/main/Media/kodi_docker_compose.yml > docker-compose.yaml
```

* Jellyfin

* Plex

By default: `kodi` and `kodi`

`admin` and `admin123`.

Remember to add the following file to the library location to be able to select the location of your books and save it (restart the container):

```sh
cd ~/Docker/CalibreWeb/library
wget https://github.com/xe-nvdk/awesome-docker/raw/main/calibre-web/metadata.db
```

#### P2P

* [qBittorrent :heavy_check_mark:](https://fossengineer.com/selfhosting-qBittorrent-with-docker-and-VPN/)

<details>
  <summary>Click to know How 👈</summary>
  &nbsp;

```sh
docker run -d --name=qbittorrent\
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/Madrid \
  -e WEBUI_PORT=8083 \
  -p 6883:6881 \
  -p 6883:6881/udp \
  -p 8083:8080 \
  -v ~/Docker/qbittorrent/config:/config \
  -v ~/Docker/qbittorrent/DOWNLOADS:/downloads \
  --restart unless-stopped \
  ghcr.io/linuxserver/qbittorrent
```

OR: :heavy_check_mark: *Jul 2022*

```sh
sudo wget -c https://raw.githubusercontent.com/JAlcocerT/Docker/main/Media/Qbittorrent_docker-compose.yaml -O docker-compose.yaml

wget  -cO - https://raw.githubusercontent.com/JAlcocerT/docker/main/Media/Qbittorrent_docker-compose_wenvironment.yaml > docker-compose.yaml

wget  -cO - https://raw.githubusercontent.com/JAlcocerT/Ubuntu/main/variables.env?token=ANL2TWHRX5WRKS3O3ZYJVULBKDBEU > .env
```

</details>

Remember: the default username/password is `admin/adminadmin`

* [Transmission](https://fossengineer.com/torrent-with-transmission-and-VPN) :heavy_check_mark:
