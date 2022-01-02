#### VScode

#### Grocy

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

####

#### 
