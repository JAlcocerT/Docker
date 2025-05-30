> Big thanks to JIM's GARAGE: [Video](https://www.youtube.com/watch?v=CmUzMi5QLzI)


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

Working example with groq youtube summarizer, forked from phidata:

```sh
docker compose -f ytgroq_docker-compose.yml ps
```