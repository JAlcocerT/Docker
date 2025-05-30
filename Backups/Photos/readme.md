> [!IMPORTANT]
> Tested some of these, [**here**](https://jalcocert.github.io/JAlcocerT/photo-management-tools/), also [here](https://jalcocert.github.io/JAlcocerT/software-for-weddings/)

* Thanks to
    * https://medevel.com/os-photo-collection-self-hosted/

---

## Selfhosted Photo Tools

* Photoview - https://github.com/photoview/photoview
* Piwigo - https://github.com/Piwigo/Piwigo
* LibrePhotos - https://github.com/LibrePhotos/librephotos
* PhotoPrism - https://github.com/photoprism/photoprism
* Lychee - https://github.com/LycheeOrg/Lychee

1. Immich

```sh
wget -O docker-compose.yml https://github.com/immich-app/immich/releases/latest/download/docker-compose.yml
wget -O .env https://github.com/immich-app/immich/releases/latest/download/example.env
```

> Thanks to [TechHut](https://www.youtube.com/watch?v=s1ufPvO0BVE)

2. [PhotoView](https://fossengineer.com/selfhosting-Photoview-docker/)

3. [PiGallery](https://github.com/JAlcocerT/Docker/blob/main/Backups/Photos/PiGallery_docker-compose.yml)

```sh
docker compose -f PiGallery_docker-compose.yml up -d
docker compose -f PiGalleryTraefik_docker-compose.yml up -d
#admin/admin
```

> Its file first, **no database!**

4. Piwigo:

```sh
docker compose -f PiwigoTraefik_docker-compose.yml up -d
```