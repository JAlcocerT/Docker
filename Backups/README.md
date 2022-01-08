### NextCloud :heavy_check_mark:

* Ubuntu version:
wget -cO - https://raw.githubusercontent.com/reisikei/docker/main/Security/fail2ban > f2b.sh && chmod 775 f2b.sh && sudo ./f2b.sh

* Raspberry Pi version (ARM):

Remember in any case to update the list of trusted domains (through an environment variable or via the CLI).

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
    
### Syncthing :heavy_check_mark:

wget -cO - https://raw.githubusercontent.com/reisikei/docker/main/Backups/Syncthing > syncthing.sh && chmod 775 syncthing.sh && sudo ./syncthing.sh


### Duplicati :heavy_check_mark:

wget -cO - https://raw.githubusercontent.com/reisikei/docker/main/Backups/Duplicati > duplicati.sh && chmod 775 duplicati.sh && sudo ./duplicati.sh


### RClone :heavy_check_mark:

docker run -it -v ~/.config/rclone:/config/rclone  rclone/rclone:beta config
