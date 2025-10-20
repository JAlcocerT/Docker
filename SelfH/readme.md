Selfhosting docs: https://jalcocert.github.io/JAlcocerT/docs/selfhosting/, particularly the [https section](https://jalcocert.github.io/JAlcocerT/docs/selfhosting/https).


> I'd recommend to use Traefik or CLoudflare tunnels for HTTPS.


```sh
#https://jalcocert.github.io/JAlcocerT/selfhosted-apps-oct-2025/
cd ./SelfH
docker compose -f 1025_docker-compose copy.yml up -d
```



```sh
#https://jalcocert.github.io/JAlcocerT/selfhosted-apps-06-2025/
cd ./SelfH
docker compose -f 0625_docker-compose copy.yml up -d

#docker compose -f May25_docker-compose.yml up -d
#...
```