## Analytics

#### Matomo

#### Open web analytics

#### Plausible

## Wordpress

* Wordpress Ubuntu single site :heavy_check_mark:

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

## Dynamic DNS

They can work in combination with [Nginx](https://github.com/JAlcocerT/Docker/blob/main/Security/nginx_docker_compose.yaml)

#### DuckDNS

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

## Others



#### Firefox :heavy_check_mark:

#### NGINX
<https://github.com/JAlcocerT/Docker/blob/main/Security/nginx_docker_compose.yaml>

#### Traefik
https://geekland.eu/instalar-y-configurar-el-proxy-inverso-traefik-en-docker/
https://geekland.eu/limitar-acceso-servicio-o-web-por-ip-con-traefik/
