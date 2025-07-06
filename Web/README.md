## Checks


**Do I have broken links?**

```sh
#podman run --rm -it ghcr.io/linkchecker/linkchecker:latest --verbose https://fossengineer.com > linkchecker_output.txt

docker run --rm -it -u $(id -u):$(id -g) ghcr.io/linkchecker/linkchecker:latest --verbose https://www.example.com
```

## Analytics

* PostHog
* Open Web Analytics
* [Umami](https://fossengineer.com/selfhosting-umami-with-docker/) :heavy_check_mark:


---

## CMS

* [Ghost](https://fossengineer.com/selfhosting-ghost-docker/)
  * Ghost + Gatsby SSG
  * [Ghost + Astro SSG](https://jalcocert.github.io/JAlcocerT/ghost-cms-for-astro/)

* SaleOR - https://github.com/JAlcocerT/Docker/tree/main/Business

* [Grav](https://fossengineer.com/selfhosting-grav-docker/)
* [Wordpress](https://fossengineer.com/selfhosting-wordpress-docker/)

---

<details>
  <summary>Wordpress with Docker 👈</summary>
  &nbsp;

*  Ubuntu single site :heavy_check_mark:


```sh
#wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Web/Wordpress > wp.sh && chmod 775 wp.sh && sudo ./wp.sh
```

Remember to check the latest WP image available with apache and php to avoid compatibility problems with themes and plugins.

* <https://hub.docker.com/_/wordpress>

If you need to upload with the plug in 'All-in-One-WP Migration' a file bigger than 2MB, you will need:

Edit .htaccess file

```
php_value upload_max_filesize 128M
php_value post_max_size 128M
php_value memory_limit 256M
php_value max_execution_time 300
php_value max_input_time 300
```
Edit wp-config.php file
```
@ini_set( 'upload_max_filesize' , '128M' );
@ini_set( 'post_max_size', '128M');
@ini_set( 'memory_limit', '256M' );
@ini_set( 'max_execution_time', '300' );
@ini_set( 'max_input_time', '300' );
```

* Wordpress RPi single site :heavy_check_mark:

```
#Wordpress RPi Docker compose.yml
sudo docker-compose up -d
```

</details>

You might be interested in SSG's: HUGO, Jekyll, Astro... 🤘

---

## Social Media

### Pixelfed

```sh
git clone https://github.com/pixelfed/pixelfed && cd pixelfed
git config --global --add safe.directory /home/reisikei/Docker/pixelfed
git tag
git checkout tags/v0.11.2
```

### Chevereto

[Setup Chevereto](https://fossengineer.com/selfhosting-chevereto-docker/) with docker compose:

```sh
#sudo mkdir ~/Docker/chevereto/chevereto_images/
#sudo chmod -R a+rwx ~/Docker/chevereto/chevereto_images/
#pwd
#sudo chmod -R a+rwx /home/jesalctag/Docker/chevereto/chevereto_images/
#sudo chmod -R a+rwx chevereto_images/
#docker pull linuxserver/chevereto:1.6.2
```

## DNS

### Dynamic DNS

They can work in combination with [Nginx](https://github.com/JAlcocerT/Docker/blob/main/Security/nginx_docker_compose.yaml)

1. No-IP
2. DuckDNS

### DuckDNS 

```sh
https://raw.githubusercontent.com/JAlcocerT/Docker/main/Web/DuckDNS_docker_compose.yaml
```


```sh
docker run -d \
  --name=duckdns \
  --net=host `#optional` \
  -e PUID=1000 `#optional` \
  -e PGID=1000 `#optional` \
  -e TZ=Etc/UTC `#optional` \
  -e SUBDOMAINS=subdomain1,subdomain2 \
  -e TOKEN=token \
  -e UPDATE_IP=ipv4 `#optional` \
  -e LOG_FILE=false `#optional` \
  -v /path/to/appdata/config:/config `#optional` \
  --restart unless-stopped \
  lscr.io/linuxserver/duckdns:latest
```

```sh
docker run \
  --name=duckdns \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/Madrid \
  -e SUBDOMAINS=subdomain1,subdomain2 \
  -e TOKEN=yourtoken-270b-from-bd0c-duckdns \
  --restart unless-stopped \
  linuxserver/duckdns
  ```