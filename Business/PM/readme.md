From powerpoints to kanban boards.

1. Leantime
2. OpenProject
3. FocalBoard
4. Claper (Audience interaction)
5. Vikunja
6. Excalidraw
7. Drawio
8. Slidev Selfhosted
9. StirlingPDF

### Huly

* Accessing the URL `http://localhost:8087` will lead you to the app in production mode.
    * <https://huly.io/blog/symphony-of-productivity>

```sh
git clone https://github.com/fergmar/huly

cd ./dev/
rush build    # Will build all the required packages.
rush bundle   # Will prepare bundles.
rush docker:build   # Will build Docker containers for all applications in the local Docker environment.
docker compose up -d --force-recreate # Will set up all the containers
```

## Time management


* Kanboard (x86 only)
* Wekan
 

#### Focalboard 

> x86 only :heavy_check_mark

It needs to have running already the [nginx container](https://github.com/JAlcocerT/Docker/blob/main/Security/nginx_docker_compose.yaml) (with its nginx_default network).

```sh
#docker run --name focalboard -d -p 807:8000 mattermost/focalboard
sudo docker run --name=focalboard -d -p 807:8000 mattermost/focalboard  -v ~/Docker/focalboard/data:/data --network nginx_default --restart unless-stopped
```

To have a persistant volume, the folder must by owned by user 'nobody':

```sh
sudo chown -R nobody ~/Docker/focalboard/data
docker build -t focalboard .
docker run -it -v "~/Docker/focalboard/data:/data" -p 807:8000 focalboard
```

#### Planka 

* https://github.com/plankanban/planka

```sh
curl -L https://raw.githubusercontent.com/plankanban/planka/master/docker-compose.yml -o docker-compose.yml

openssl rand -hex 64 #for random secret_key generation

docker-compose up -d
```