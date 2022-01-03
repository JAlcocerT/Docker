#### VScode

#### Grocy :heavy_check_mark:

```
docker run -d \
  --name=grocy \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/Paris \
  -p 9283:80 \
  -v ~/Docker/Grocy:/config \
  --restart unless-stopped \
  lscr.io/linuxserver/grocy
```

#### Focalboard :heavy_check_mark:

It works for x86:
```
docker run -it -p 807:8000 mattermost/focalboard
```
