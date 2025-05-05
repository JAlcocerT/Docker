* https://docs.hoppscotch.io/documentation/self-host/community-edition/install-and-build

* https://hub.docker.com/r/hoppscotch/hoppscotch

```sh
docker run -d --name hoppscotch -p 3000:3000 --restart=unless-stopped hoppscotch/hoppscotch:latest
```