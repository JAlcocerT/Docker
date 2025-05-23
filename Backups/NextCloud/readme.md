> See how I [selfhosted NC with a Pi](https://jalcocert.github.io/RPi/posts/selfhosting-nextcloud/) and recap [here](https://jalcocert.github.io/JAlcocerT/selfhosted-apps-spring-2025/)


```sh
sudo docker compose -f NextCloud_RPi_Stack.yaml up -d #working for x86
sudo docker compose -f nc_mariadb.yml up -d #working for arm32
```


---

## Nextcloud CLIs

```sh
sudo docker run -d -v ~/nextcloud:/var/www/html -p 8080:80 --name nextcloud_container nextcloud 
```

Use this command to query the list of trusted_domains:
```sh
sudo docker exec --user www-data nextcloud_container php occ config:system:get trusted_domains
```

And set a new one:
```sh
sudo docker exec --user www-data nextcloud_container php occ config:system:set trusted_domains 7 --value 192.168.1.11:8080
```

Remember that to upload folders from the web browser, only Chrome seems to be supported (Oct 2021)

To know whats the local ip addres, use: ifconfig.

To further make it simpler, its possible to use hostname -I with grep to get that ip address directly:

```sh
hostname -I | head -c12
```

Therefore we could do:

```sh
sudo docker run -d -v ~/nextcloud:/var/www/html -p 8080:80 --name nextcloud_container nextcloud  \
sudo docker exec --user www-data nextcloud_container php occ config:system:set trusted_domains 7 --value hostname -I | head -c12
```

Add the internal vpn (tailscale) as a trusted domain:

```sh
sudo docker exec --user www-data nextcloud_container php occ config:system:set trusted_domains 7 --value 100.82.151.45:8080
```

```sh
sudo fdisk -l
```

Google brings me at this old post when looking for the same problem.
I just solved by assigning uid and grid to www-data

the fstab entry should look like:

```sh
/dev/LogicalVolume1/Volume1 /home/jollyj/server ntfs defaults,uid=www-data,grid=www-data umask=007 0 1
```

The problem was solved by editing the /etc/fstab as follow:

```sh
(Your Shared Folder) (Your Path to Mountpoint) vboxsf defaults,uid=www-data,gid=www-data,dmask=007 0 0
```

to make it read from an external drive


92C269FAC269E2C9

To get this UUID, run this command:

```sh
sudo ls -l /dev/disk/by-uuid/


sudo fdisk -l

sudo umount /mnt/usb

sudo mount /dev/sda1 /mnt/usb -o uid=pi,gid=pi
```