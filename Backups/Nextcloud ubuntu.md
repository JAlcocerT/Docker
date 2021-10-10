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
