#### VScode

#### Grocy :heavy_check_mark:

```
docker run --name grocy -d \
  --name=grocy \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/Paris \
  -p 9283:80 \
  -v ~/Docker/Grocy:/config \
  --restart unless-stopped \
  lscr.io/linuxserver/grocy
```

#### Focalboard (x86 only :heavy_check_mark:)

It needs to have running already the [nginx container](https://github.com/JAlcocerT/Docker/blob/main/Security/nginx_docker_compose.yaml) (with its nginx_default network).
```
#docker run --name focalboard -d -p 807:8000 mattermost/focalboard
sudo docker run --name=focalboard -d -p 807:8000 mattermost/focalboard  -v ~/Docker/focalboard/data:/data --network nginx_default --restart unless-stopped
```

To have a persistant volume, the folder must by owned by user 'nobody':

```
sudo chown -R nobody ~/Docker/focalboard/data
docker build -t focalboard .
docker run -it -v "~/Docker/focalboard/data:/data" -p 807:8000 focalboard
```

#### Kanboard (x86 only)

```
version: '2'
services:
  db:
    image: mariadb:latest
    command: --default-authentication-plugin=mysql_native_password
    volumes:
      - ~/Docker/Kanboard2/:/var/lib/mysql
    environment:
      - MYSQL_ROOT_PASSWORD=UVxY26hNL4qmo
      - MYSQL_DATABASE=kanboard
      - MYSQL_USER=kanboard
      - MYSQL_PASSWORD=kanboard
    restart: always
      
  kanboard:
    image: kanboard/kanboard:latest
    ports:
      - 88:80
    volumes:
      - ~/Docker/Kanboard2/kanboard_data:/var/www/app/data
      - ~/Docker/Kanboard2/kanboard_plugins:/var/www/app/plugins
      - ~/Docker/Kanboard2/kanboard_ssl:/etc/nginx/ssl
    environment:
      - DATABASE_HOST=db
      - DATABASE_USER=kanboard
      - DATABASE_PASSWORD=kanboard
      - DATABASE_NAME=kanboard
    depends_on:
      - db
    links:
      - db:db
    restart: always
    ```
