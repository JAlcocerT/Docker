### Filerun :heavy_check_mark:

* Raspberry Pi version (ARM): :heavy_check_mark:

    <https://github.com/JAlcocerT/Docker/blob/main/Backups/Filerun_rpi.yaml>

* Ubuntu version: :heavy_check_mark:

   <https://github.com/JAlcocerT/Docker/blob/main/Backups/Filerun_ubuntu.yaml>
   
 * Ubuntu version connected to existing nginx: 
 
   <https://github.com/JAlcocerT/Docker/blob/main/Security/nginx_docker_compose.yaml>
   <https://github.com/JAlcocerT/Docker/blob/main/Backups/Filerun_ubuntu.yaml>

### NextCloud :heavy_check_mark:

* Ubuntu version:

wget -cO - https://raw.githubusercontent.com/reisikei/docker/main/Security/fail2ban > f2b.sh && chmod 775 f2b.sh && sudo ./f2b.sh

* Raspberry Pi version (ARM): :heavy_check_mark:
   * <https://github.com/JAlcocerT/Docker/blob/main/Backups/NextCloud%20RPi.yaml>

* Ubuntu version with existing nginx (A): :heavy_check_mark:

   * <https://github.com/JAlcocerT/Docker/blob/main/Security/nginx_docker_compose.yaml>
   * <https://github.com/JAlcocerT/Docker/blob/main/Backups/Nextcloud_ubuntu_nginx_existing.yaml>
   * Add the proxy host in the nginx portal: domain needed + name of the container (nextcloud-app for this one) + port 80 (its the default in the nextcloud container defined, has not been changed to 8080 or so)

* Ubuntu version with new nginx (B):

   * <https://github.com/JAlcocerT/Docker/blob/main/Backups/Nextcloud_ubuntu_with_nginx.yaml>


Remember in any case to update the list of trusted domains (through an environment variable or via the CLI).

Modify  config/config.php file to include: 'overwriteprotocol' => 'https'

It is recommended to add 2FA to your nextcloud server, specially if you are going to expose it to the internet, we can do it with the app: Two-Factor TOTP Provider, <https://apps.nextcloud.com/apps/twofactor_totp> 

As well as:
            
  * <https://apps.nextcloud.com/apps/bruteforcesettings>
  *  <https://apps.nextcloud.com/apps/duplicatefinder>
  *   <https://apps.nextcloud.com/apps/fileslibreofficeedit>
  *   <https://apps.nextcloud.com/apps/phonetrack>






To copy faster all your document, try: cp -a <source> <destination>

```
cp -a /home/$USER/Archive /media/$USER/USB_drive/        
```

Then, update the DB of the container (so that the changes are visible) with:

```
sudo docker exec -ti --user www-data your_nextcloud_containers_name /var/www/html/occ files:scan --all
```
            
On a given folder, check the timestamp with: ls -la --time-style=full-iso
    
### Syncthing :heavy_check_mark:

wget -cO - https://raw.githubusercontent.com/reisikei/docker/main/Backups/Syncthing > syncthing.sh && chmod 775 syncthing.sh && sudo ./syncthing.sh


### Duplicati :heavy_check_mark:

wget -cO - https://raw.githubusercontent.com/reisikei/docker/main/Backups/Duplicati > duplicati.sh && chmod 775 duplicati.sh && sudo ./duplicati.sh


### RClone :heavy_check_mark:

docker run -it -v ~/.config/rclone:/config/rclone  rclone/rclone:beta config
