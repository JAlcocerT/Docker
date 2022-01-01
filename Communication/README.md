* Discourse

```

sudo apt update 
sudo apt upgrade -y
sudo apt-get install docker.io docker-compose -y
mkdir discourse
cd discourse/

git clone https://github.com/discourse/discourse_docker
cd discourse_docker/
cp samples/standalone.yml containers/app.yml
sudo nano containers/app.yml
```

https://github.com/discourse/discourse/blob/main/docs/INSTALL-email.md

```
./launcher bootstrap app
#Start Discourse
/var/docker/launcher start app
```
