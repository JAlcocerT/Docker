### Monitoring

#### Internet Speed
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


### Internet Speed Tracker

wget -cO - https://raw.githubusercontent.com/reisikei/docker/main/IoT/InternetSpeedTracker.yaml > docker-compose.yaml
docker-compose up -d

### Graphana with Prometheus

Prometheus is the standard for monitoring in kubernetes.
It can store the metrics in the disk, but not in the cloud by default.

### GPIO

### NetData
