### Internet Monitoring

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

#### open Speed test :heavy_check_mark:
docker run --restart=unless-stopped --name openspeedtest -d -p 3000:3000 -p 3001:3001 openspeedtest/latest

#### Internet Speed Tracker (X86 only :heavy_check_mark:)

wget -cO - https://raw.githubusercontent.com/reisikei/docker/main/IoT/InternetSpeedTracker.yaml > docker-compose.yaml
docker-compose up -d

#### Graphana with Prometheus

Prometheus is the standard for monitoring in kubernetes.
It can store the metrics in the disk, but not in the cloud by default.

#### NetData :heavy_check_mark:

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
### Server Monitoring
##### Using Grafana, Prometheus & Node Exporter :heavy_check_mark:

```
version: '3'

volumes:
  prometheus-data:
    driver: local

services:
  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    ports:
      - "9090:9090"
    volumes:
      - /etc/prometheus:/etc/prometheus
      - prometheus-data:/prometheus
    restart: unless-stopped
    command:
      - "--config.file=/etc/prometheus/prometheus.yml"
  node_exporter:
    image: quay.io/prometheus/node-exporter:latest
    container_name: node_exporter
    command:
      - '--path.rootfs=/host'
    pid: host
    restart: unless-stopped
    volumes:
      - '/:/host:ro,rslave' 
  grafana:
    image: grafana/grafana-oss:latest
    container_name: grafana
    ports:
      - "3457:3000"
    restart: unless-stopped
```
Below file must be created with the proper name and location, as specified by the upper yaml file:
```
global: 
  scrape_interval:     15s # By default, scrape targets every 15 seconds.

# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: 'prometheus'
    # Override the global default and scrape targets from this job every 5 seconds.
    scrape_interval: 5s
    static_configs:
      - targets: ['localhost:9090']

  # Example job for node_exporter
  - job_name: 'node_exporter'
    static_configs:
      - targets: ['node_exporter:9100'] #container_name
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
