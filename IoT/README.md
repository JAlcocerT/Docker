### Monitoring

#### Internet Speed :heavy_check_mark:
##### With Graphana, Promotheus,  SpeedTest, Nodeexp

```
cd ~/Docker
git clone https://github.com/geerlingguy/internet-monitoring MonitoringInternet
cd internet-monitoring
sudo nano docker-compose.yml
#https://github.com/geerlingguy/internet-monitoring
#pass to be modified in the env file located at grafana/config.monitoring
```
docker-compose up -d


#### Internet Speed Tracker

wget -cO - https://raw.githubusercontent.com/reisikei/docker/main/IoT/InternetSpeedTracker.yaml > docker-compose.yaml
docker-compose up -d

#### Graphana with Prometheus

Prometheus is the standard for monitoring in kubernetes.
It can store the metrics in the disk, but not in the cloud by default.

#### NetData

```
docker run -d --name=netdata \
  -p 19997:19999 \
  -v ~/Docker/netdata/passwd:/host/etc/passwd:ro \
  -v ~/Docker/netdata/group:/host/etc/group:ro \
  -v ~/Docker/netdata/proc:/host/proc:ro \
  -v ~/Docker/netdata/sys:/host/sys:ro \
  -v ~/Docker/netdata/var/run/docker.sock:/var/run/docker.sock:ro \
  --cap-add SYS_PTRACE \
  --security-opt apparmor=unconfined \
  netdata/netdata
  
  docker run -d --name=netdata --hostname=friday \
-e UID=1000 \
-e GID=100  \
-p 19999:19999 \
-v /etc/passwd:/host/etc/passwd:ro \
-v /etc/group:/host/etc/group:ro \
-v /proc:/host/proc:ro \
-v /sys:/host/sys:ro \
-v /etc/os-release:/host/etc/os-release:ro \
-v /var/run/docker.sock:/var/run/docker.sock:ro \
--restart always \
--cap-add SYS_PTRACE \
--security-opt apparmor=unconfined \
netdata/netdata
```

### GPIO

### Home Assistant :heavy_check_mark:

```
docker run -d \
  --name=homeassistant \
  --net=host \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/Paris \
  -p 8123:8123 `#optional` \
  -v ~/Docker/HomeAssistant:/config \
  --restart unless-stopped \
  lscr.io/linuxserver/homeassistant
```
https://hub.docker.com/r/linuxserver/homeassistant
