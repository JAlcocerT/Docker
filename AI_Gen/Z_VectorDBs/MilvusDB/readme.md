* https://www.youtube.com/watch?v=OD5FS7qUfBQ&t=49s

* https://milvus.io/docs/v2.0.x/install_standalone-docker.md


```sh
wget https://github.com/milvus-io/milvus/releases/download/v2.0.2/milvus-standalone-docker-compose.yml -O docker-compose.yml
sudo docker compose up -d
```


* https://milvus.io/docs/manage-collections.md

---


See also https://github.com/zilliztech/attu

> Web UI for Milvus Vector Database

```sh
#docker run -p 8000:3000 -e MILVUS_URL={milvus server IP}:19530 zilliz/attu:v2.5
#docker run -p 3000:3000 -e MILVUS_URL=localhost:19530 zilliz/attu:v2.5
docker run -d --name attu -p 3000:3000 --network milvus -e MILVUS_URL=milvus-standalone:19530 zilliz/attu:v2.5
```