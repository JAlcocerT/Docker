### Filerun :heavy_check_mark:

* Raspberry Pi version (ARM): :heavy_check_mark:

 ```sh
 sudo wget -c https://raw.githubusercontent.com/JAlcocerT/Docker/main/Backups/Filerun_rpi.yaml -O docker-compose.yaml
 ```

* Ubuntu version: :heavy_check_mark:

   <https://github.com/JAlcocerT/Docker/blob/main/Backups/Filerun_ubuntu.yaml>
   
 * Ubuntu version connected to existing nginx: 
 
   <https://github.com/JAlcocerT/Docker/blob/main/Security/nginx_docker_compose.yaml>
   <https://github.com/JAlcocerT/Docker/blob/main/Backups/Filerun_ubuntu.yaml>

### NextCloud :heavy_check_mark:

> Nextcloud can be your webdav as seen [here](https://jalcocert.github.io/JAlcocerT/selfhosted-apps-spring-2025/#nextcloud)


* Raspberry Pi version (ARM): :heavy_check_mark:
   * <https://github.com/JAlcocerT/Docker/blob/main/Backups/NextCloud%20RPi.yaml>

```sh
sudo wget -c https://github.com/JAlcocerT/Docker/blob/main/Backups/NextCloud%20RPi.yaml -O docker-compose.yaml
```

* Ubuntu version with existing nginx (A): :heavy_check_mark:

   * <https://github.com/JAlcocerT/Docker/blob/main/Security/nginx_docker_compose.yaml>
   * <https://github.com/JAlcocerT/Docker/blob/main/Backups/Nextcloud_ubuntu_nginx_existing.yaml>
   * Add the proxy host in the nginx portal: domain needed + name of the container (nextcloud-app for this one) + port 80 (its the default in the nextcloud container defined, has not been changed to 8080 or so)

* Ubuntu version with new nginx (B):
   * <https://github.com/JAlcocerT/Docker/blob/main/Backups/Nextcloud_ubuntu_with_nginx.yaml>


Remember in any case to update the list of trusted domains (through an environment variable or via the CLI).

Modify  `config/config.php` file to include: 'overwriteprotocol' => 'https'

It is recommended to add 2FA to your nextcloud server, specially if you are going to expose it to the internet, we can do it with the app: Two-Factor TOTP Provider, <https://apps.nextcloud.com/apps/twofactor_totp> 

As well as:
            
* <https://apps.nextcloud.com/apps/bruteforcesettings>
* <https://apps.nextcloud.com/apps/duplicatefinder>
* <https://apps.nextcloud.com/apps/fileslibreofficeedit>
* <https://apps.nextcloud.com/apps/phonetrack>



To copy faster all your document, try: cp -a <source> <destination>

```sh
cp -a /home/$USER/Archive /media/$USER/USB_drive/        
```

Then, update the DB of the container (so that the changes are visible) with:

```sh
sudo docker exec -ti --user www-data your_nextcloud_containers_name /var/www/html/occ files:scan --all
```
            
On a given folder, check the timestamp with:

```sh
ls -la --time-style=full-iso
```    

### RClone

```sh
#sudo apt install rclone

#sudo -v ; curl https://rclone.org/install.sh | sudo bash
#rclone v1.69.2 has successfully installed.
#rclone config

#protondrive
#https://blog.otterlord.dev/posts/proton-drive-rclone/
rclone lsd protondrive: #list all directories, providing that you named the remote also protondrive
rclone lsd protondrive:13-Sync
rclone ls protondrive:x13-Sync

#rclone sync --dry-run <my_remote>:<protondrivedirectory> <localdirectory> -v
rclone sync --dry-run protondrive:x13-Sync /home/jalcocert/Desktop/ProtonDrive -v

rclone sync protondrive:x13-Sync /home/jalcocert/Desktop/ProtonDrive #from cloud to local (one time)
rclone mount protondrive:x13-Sync /home/jalcocert/Desktop/ProtonDrive --vfs-cache-mode full #this makes it bidirectional

#docker run -it -v ~/.config/rclone:/config/rclone  rclone/rclone:beta config
```

```sh
docker-compose -f rclone_docker-compose.yml up -d
```

## Container volumes backup

Normally db's in docker-compose files are referenced here.

Back up this folder to re-build your containers:

```sh
/var/lib/docker/volumes/
```