## Chats



### Matrix with Synapse 

To [setup Matrix with docker](https://fossengineer.com/selfhosting-matrix-synapse-docker/), we can:

First step - generate the configuration with: :heavy_check_mark:

```sh
sudo docker run -it --rm -v ~/Docker/synapse/data:/data -e SYNAPSE_SERVER_NAME=matrix.yourdomain.com -e SYNAPSE_REPORT_STATS=yes matrixdotorg/synapse:latest generate

#or if the latest does not generate a proper configfile, try a previous one:

sudo docker run -it --rm -v ~/Docker/synapse/data:/data -e SYNAPSE_SERVER_NAME=matrix.yourdomain.com -e SYNAPSE_REPORT_STATS=yes matrixdotorg/synapse:v1.60.0 generate
```

* Creating a new nginx proxy for this  :heavy_check_mark:

```sh
mkdir reverse-proxy && cd reverse-proxy

docker network create server
nano docker-compose.yaml #1st part
docker compose up -d #to the first part

mkdir synapse && cd synapse
nano docker-compose.yaml #2nd part
mkdir data
docker-compose run --rm synapse generate
nano homeserver.yaml #allow registrations
docker-compose up -d
#docker-compose restart synapse #if its already running

#use a matrix client, like element, and enjoy
```

* Reusing an existing nginx proxy manager :heavy_check_mark:

If there is already an instance of [nginx running](https://github.com/JAlcocerT/Docker/blob/main/Security/nginx_docker_compose.yaml), you can deploy the below docker compose file (nginx_default is the name of nginx network that is already created by default, but you could have named it in another way).

```sh
version: "3.3"

services:
    synapse:
        image: "matrixdotorg/synapse:latest"
        container_name: "synapse"
        volumes:
            - "./data:/data"
        environment:
            VIRTUAL_HOST: "your.domain.com"
            VIRTUAL_PORT: 8008
            LETSENCRYPT_HOST: "your.domain.com"
            SYNAPSE_SERVER_NAME: "your.domain.com"
            SYNAPSE_REPORT_STATS: "yes"
        networks: ["nginx_default"]


networks:
    nginx_default:
        external: true
```

Then, use nginx portal to add the domain + name of the docker container (synapse) + the port as 8008 (as defined in this config file).