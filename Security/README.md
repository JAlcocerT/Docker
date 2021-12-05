## Fail2Ban
```
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Security/fail2ban > f2b.sh && chmod 775 f2b.sh && sudo ./f2b.sh
```

## VPN's

### Wireguard
```
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Security/Wireguard > wg.sh && chmod 775 wg.sh && sudo ./wg.sh &&
docker exec -it wireguard wg #to make sur eits running &&
docker logs wireguard #to check the logs
```
### OpenVPN

## PiHole


## watchtower
```
sudo docker run -d \
    --name watchtower \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower --run-once 
```
