## Analytics

* PostHog
* Umami
* [Umami](https://fossengineer.com/selfhosting-umami-with-docker/)

#### OpenReplay

#### Matomo

#### Open web analytics




#### Plausible

---

## CMS

* [Ghost](https://fossengineer.com/selfhosting-ghost-docker/)
  * Ghost + Gatsby SSG
  * Ghost + Astro SSG

* Strapi
  * Strapi + Astro - https://docs.astro.build/en/guides/cms/strapi/

* SaleOR - https://github.com/JAlcocerT/Docker/tree/main/Business

* [Grav](https://fossengineer.com/selfhosting-grav-docker/)

* [Wordpress](https://fossengineer.com/selfhosting-wordpress-docker/)

<details>
  <summary>Wordpress with Docker 👈</summary>
  &nbsp;

*  Ubuntu single site :heavy_check_mark:


```
wget  -cO - https://raw.githubusercontent.com/reisikei/docker/main/Web/Wordpress > wp.sh && chmod 775 wp.sh && sudo ./wp.sh
```

Remember to check the latest WP image available with apache and php to avoid compatibility problems with themes and plugins.
<https://hub.docker.com/_/wordpress>

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

#### Pixelfed

```
git clone https://github.com/pixelfed/pixelfed && cd pixelfed
git config --global --add safe.directory /home/reisikei/Docker/pixelfed
git tag
git checkout tags/v0.11.2
```

#### Chevereto

```
#sudo mkdir ~/Docker/chevereto/chevereto_images/
#sudo chmod -R a+rwx ~/Docker/chevereto/chevereto_images/
#pwd
#sudo chmod -R a+rwx /home/jesalctag/Docker/chevereto/chevereto_images/
#sudo chmod -R a+rwx chevereto_images/
#docker pull linuxserver/chevereto:1.6.2

version: '2'

services:
  db:
    image: mariadb
    volumes:
      - ~/Docker/chevereto/database:/var/lib/mysql:rw # I haven't had good luck putting this database in a different directory
    restart: unless-stopped
    networks:
      - nginx_default
    environment:
      MYSQL_ROOT_PASSWORD: chevereto_root
      MYSQL_DATABASE: chevereto
      MYSQL_USER: chevereto
      MYSQL_PASSWORD: chevereto

  chevereto:
    depends_on:
      - db
    image: nmtan/chevereto:latest
    restart: unless-stopped
    networks:
      - nginx_default
    environment:
      CHEVERETO_DB_HOST: db
      CHEVERETO_DB_USERNAME: chevereto
      CHEVERETO_DB_PASSWORD: chevereto
      CHEVERETO_DB_NAME: chevereto
      CHEVERETO_DB_PREFIX: chv_
    volumes:
      - ~/Docker/chevereto/chevereto_images:/var/www/html/images:rw
      - ~/Docker/chevereto/conf/php.ini:/usr/local/etc/php/php.ini:ro
    ports:
      - 8686:80

networks:
  nginx_default:
volumes:
  database:
  chevereto_images:




```

#### Dynamic DNS

They can work in combination with [Nginx](https://github.com/JAlcocerT/Docker/blob/main/Security/nginx_docker_compose.yaml)

#### DuckDNS :heavy_check_mark:

```
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

https://raw.githubusercontent.com/JAlcocerT/Docker/main/Web/DuckDNS_docker_compose.yaml

#### No-IP

```

```

## Static web servers:

#### Apache


#### NginX

---

## Others



#### Firefox :heavy_check_mark:

#### NGINX :heavy_check_mark:
<https://github.com/JAlcocerT/Docker/blob/main/Security/nginx_docker_compose.yaml>

#### Traefik
https://geekland.eu/instalar-y-configurar-el-proxy-inverso-traefik-en-docker/
https://geekland.eu/limitar-acceso-servicio-o-web-por-ip-con-traefik/

#### Caddy