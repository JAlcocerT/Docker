
## Good to know

### Install docker & docker compose & portainer

```
#sudo apt update & apt upgrade
sudo apt install docker.io -y & sudo docker version

sudo apt-get install docker-compose -y & sudo docker-compose --version

sudo docker run -d -p 9000:9000 -p 8000:8000 --name portainer --restart always -v /var/run/docker.sock:/var/run/docker.sock -v ~/Docker/portainer:/data portainer/portainer-ce
```

To get to know what's the private address of your device and access portainer, simply use: ifconfig, then privateipserver:9000

### Install Yacht (Portainer alternative)

```
docker run -d -p 8000:8000 -v /var/run/docker.sock:/var/run/docker.sock -v ~/Dockeryacht:/config selfhostedpro/yacht
```

### Useful Docker commands

* Processes running:

 ``` 
 ps fax 
 ```

* List containers:

  ```
  docker ps
  ```

* List all containers, even the stopped:

  ```
  docker ps -a | head
  ```

* List all images:

  ```
  docker image ls
  ```

* Remove unsed images:

  ```
  docker image prune -a
  ```

* Test that docker works with this image:

  ```
  docker run hello-world
  ```

* Another image to test:

  ```
  docker pull alpine
  docker pull alpine:3.7 #a specific version
  ```

* Run some command inside the cointainer:

  ```
  docker run alpine:3.7 ls -l
  ```
  
* Interactive terminal of the container (execute it and stops the container) :

  ```
  docker run -it alpine:3.7 sh
  ```

* Execute a process inside a container and keep it running if needed:

  ```
  docker run -d nginx:1.15.7 
  docker run -p 80:80 -d nginx (start nginx web server on port 80)
  ```

* Executes a command on a running container:

  ```
  docker exec -it 554kjgIDfgeofm sh
   
  exit
  docker stop yjbf7i3ID3jkj67 #contained ID
  docker rm yjbf7i3ID3jkj67
  ```
  
* Kali on docker:

```
docker pull kalilinux/kali-rolling
docker run --tty --interactive kalilinux/kali-rolling
```

* Mount volumes:
  in docker folder:
```
  docker run -v ~/docker/index.html:/usr/share/nginx/html/index.html:ro -d nginx:1.15.7
                 #mount this file --->  #into this path with this name, read only image & version
```

* Ports:

```
  #expose a port from the container to the host --->                 (machine:container)
  docker run -v ~/docker/index.html:/usr/share/nginx/html/index.html:ro -p 8080:80 -d nginx:1.15.7      
```

* Change the restart policy of an existing container:
* 
  ```
  docker update --restart unless-stopped running_container_name
  ```
  
* Change the policy of all the containers running:

  ```
  docker update --restart unless-stopped $(docker ps -q)
  ```
 
* Restart all containers:

 ```
 docker restart $(docker ps -a -q)
 ```
 
 * Stop all containers:
 
 ```
 docker container stop $(docker container ls -aq)
 ```
 
 * Remove all stopped containers:
 
 ```
 docker container rm $(docker container ls -aq)
 ```

* Create image of a container:

  ```
  docker commit 4699hf7ID7hfty
  docker image ls | head
  ```
  
* Create a tag for the image:

  ```
  docker image tag 4699hf7ID7hfty midocker
  docker image tag 4699hf7ID7hfty midocker:1.0

  docker run midocker figlet hola (figlet installed previously in the container and hola as argument)
  docker run ubuntu figlet hola (wont run since it does not have figlet by default)
  ```

* Docker file: container based on other image
  FROM ubuntu

  vim Dockerfile
  RUN apt-get update && apt-get install figlet -y

  cd docker/
  docker build -t midocker:1.1
  docker run midocker:1.1 figlet hola

* See the history of an image (historical commands)
  ```
  docker image history 4699hf7ID7hfty
  ```


#### DOCKER VOLUMES: 

  * Changes inside the container will be gone unless volumes are used
  * Mount points inside the container
  
  * Check the data stored in volumes (the same volume mounted on a new container, will have the same info available):
  
  ```
  docker volume ls
  ```


#### ENV files:

  By having an .env file on the same folder that the docker-compose.yaml file, will make the configuration file simpler/allow us to automate:


* With CLI:

```
    docker run -d --name example --env-file vars_file.env ubuntu:latest --restart unless-stopped
```

* With Docker compose:

```
    ---
    version: "2.1"
    services:
      syncthing:
        image: ghcr.io/linuxserver/syncthing
        container_name: syncthing
        hostname: syncthing #optional
        environment:
          - PUID=1000
          - PGID=1000
          - TZ=Europe/Warsaw
        volumes:
          - /home/pi/Docker/Syncthing/config:/config
          - /media/pi/Nowy1/SYNC:/data1
        ports:
          - ${APP_PORT}:8384 ##it will be written in the env file as: APP_PORT=8384 for example
          - 22000:22000/tcp
          - 22000:22000/udp
          - 21027:21027/udp
        restart: unless-stopped
```
