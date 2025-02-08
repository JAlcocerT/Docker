## A collection of Security Tools

> To setup with Docker Containers!

* [WatchYourLan](https://fossengineer.com/selfhosting-WatchYourLAN-docker/) :heavy_check_mark:

Remember to use the proper IFACE, according to what the command provides in your docker's host machine.

* [Wireshark](https://fossengineer.com/setup-wireshark-with-docker) :heavy_check_mark:

You can check what is going on in your network with Wireshark, or for example, if unbound DNS is doing its job.

```sh
wget https://raw.githubusercontent.com/JAlcocerT/Docker/refs/heads/main/Security/Lan_Monitoring/wireshark_docker-compose.yaml
sudo docker-compose up -d #port 3000 by default
```

* [Wireguard](https://jalcocert.github.io/JAlcocerT/how-to-use-wg-easy-with-a-vps/) :heavy_check_mark:

Check if it worked with `curl ifconfig.io`


* **[Fail2Ban](https://fossengineer.com/setup-fail2ban-with-docker/)**


## Proxies

* **Cloudflared** - zero trust :heavy_check_mark:

Tunnels allow you to easily and securely connect your environment to Cloudflare so that your users can reach public or private resources.

<https://dash.teams.cloudflare.com/>

Create a tunnel and you will get a docker run command like:

```
sudo docker run cloudflare/cloudflared:latest tunnel --no-autoupdate run --token whatevertokencloudflarewillassigntoyou
```

* NginX :heavy_check_mark:

```
#curl https://raw.githubusercontent.com/JAlcocerT/Docker/main/Security/nginx_docker_compose.yaml -O 
wget -c https://raw.githubusercontent.com/JAlcocerT/Docker/main/Security/nginx_docker_compose.yaml -O docker-compose.yml
sudo docker-compose up -d
```

For the initial setup, check: https://nginxproxymanager.com/setup/#initial-run

Remember to portforward your router to the chosen NginX selected ports on **the docker host**.

When adding new services behind this nginx, they must be on the same network as nginx, normally nginx_default, this can be done:

* in portainer, in the container section, connected networks, then join nginx_default network
* by including it in the docker compose files with:

```yml
     networks: ["nginx_default"]

networks:
    nginx_default:
        external: true
```

Example <https://github.com/JAlcocerT/Docker/blob/main/Media/podgrab_docker-compose.yml>

By CLI with:

```sh
docker network connect nginx_default your_new_container_to_go_on_nginx_network
```

### DNS

* [PiHole](https://jalcocert.github.io/RPi/posts/selfh-internet-better/#pi-alert) :heavy_check_mark:

```sh
sudo docker-compose up -d   

#Change DNS on the device or on the router(applicable to all devices connected to the LAN) to the rpi address. For example to 192.168.1.31
    
#nslookup (to check which dns you are using)
#sudo apt-get install dnsutils
#nslookup reddit.com/pi.hole  #you should see the server/rpi local lan ip address as the server and the port 53 as its the default for DNS  
#if you are running tailscale, be aware of the conflicts with magicdns if its enabled there  
  
docker container ls
docker inspect 4648tgIDngkfo30 #get IP address
docker logs 4648tgIDngkfo30 | grep pass #get the password 

#change update frequency when cron updates pihole
sudo nano /etc/cron.d/pihole

#blocklist updates in group management + update the gravity under tools
https://firebog.net/
https://v.firebog.net/hosts/lists.php?type=tick
```

* [Unbound](https://jalcocert.github.io/RPi/posts/selfh-internet-better/#unbound-dns)

It can be used together with Pi-Hole, add the container ip and port in: 

`Settings` -> `DNS` -> `upstream DNS server`

```sh
sudo docker run --name my-unbound-dns -d -p 54:53/udp -p 54:53/tcp \
--restart=always mvance/unbound:latest


sudo docker run --name my-unbound-dns -d -p 5335:53/udp -p 5335:53/tcp \
--restart=always mvance/unbound-rpi:latest
```



* Watchtower


### Communication


* Jitsi :heavy_check_mark:
* [Matrix](https://fossengineer.com/selfhosting-matrix-synapse-docker/) :heavy_check_mark:


### Privacy

* Invidious

```
git clone https://github.com/iv-org/invidious.git
cd invidious
nano docker-compose.yml #modify it to your preferences
```

* Piped

* [Whoogle](https://fossengineer.com/selfhosting-whoogle-docker/) :heavy_check_mark:

```sh
docker run --publish 5000:5000 --detach --name whoogle-search benbusby/whoogle-search:latest
```

* [SearX](https://jalcocert.github.io/RPi/posts/selfh-internet-better/#searxng---private-web-search) :heavy_check_mark: