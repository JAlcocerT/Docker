```
sudo docker run -d -v ~/nextcloud:/var/www/html -p 8080:80 --name nextcloud_container nextcloud 
```

Use this command to query the list of trusted_domains:
```
sudo docker exec --user www-data nextcloud_container php occ config:system:get trusted_domains
```

And set a new one:
```
sudo docker exec --user www-data nextcloud_container php occ config:system:set trusted_domains 7 --value 192.168.1.11:8080
```

Remember that to upload folders from the web browser, only Chrome seems to be supported (Oct 2021)

To know whats the local ip addres, use: ifconfig.

To further make it simpler, its possible to use hostname -I with grep to get that ip address directly:

```
hostname -I | head -c12
```

Therefore we could do:

```
sudo docker run -d -v ~/nextcloud:/var/www/html -p 8080:80 --name nextcloud_container nextcloud  \
sudo docker exec --user www-data nextcloud_container php occ config:system:set trusted_domains 7 --value hostname -I | head -c12
```
