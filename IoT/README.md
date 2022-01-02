### Monitoring

#### Internet Speed
##### With Graphana, Promotheus,  SpeedTest, Nodeexp

```
cd ~/Docker
git clone https://github.com/geerlingguy/internet-monitoring MonitoringInternet
cd internet-monitoring
sudo nano docker-compose.yml
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
