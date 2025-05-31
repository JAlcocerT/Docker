> Big thanks to JIM's GARAGE: [Video](https://www.youtube.com/watch?v=CmUzMi5QLzI)

This is **Traefik v3.3 working**.


```sh
nano ./config/acme.json
chmod 600 ./config/acme.json

nano ./cf-token

nano ./config/config.yaml
nano ./config/traefik.yaml
```

```sh
sudo docker compose up -d
```

**Working examples with labels**

1. with groq youtube summarizer, forked from phidata:

```sh
docker compose -f ytgroq_docker-compose.yml ps
```

2. with pigallery

```sh
docker compose -f PiGalleryTraefik_docker-compose.yml ps
```
