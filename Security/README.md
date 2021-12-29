#### Fail2Ban
```
wget  -cO - https://raw.githubusercontent.com/jalcocert/docker/main/Security/fail2ban > f2b.sh && chmod 775 f2b.sh && sudo ./f2b.sh
```

#### watchtower :heavy_check_mark:
```
sudo docker run -d \
    --name watchtower \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower --run-once 
```

#### PiHole

## Communication

#### Matrix



#### Jitsi

```
sudo apt update 
sudo apt upgrade -y
sudo apt-get install docker.io docker-compose -y
git clone https://github.com/jitsi/docker-jitsi-meet && cd docker-jitsi-meet
cp env.example .env
```

sudo docker-compose up

### VPN's

##### Wireguard
```
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Security/Wireguard > wg.sh && chmod 775 wg.sh && sudo ./wg.sh &&
docker exec -it wireguard wg #to make sur eits running &&
docker logs wireguard #to check the logs
```
##### OpenVPN




