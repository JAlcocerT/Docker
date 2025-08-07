Navigate into the directory where your docker-compose.yaml is located.

* Build your container: `docker build -t pb .`
* Run your container: `docker run -p 8080:8080 pb`

Run:

```sh
#docker compose up -d
docker compose -f PB_docker-compose.yml up -d
```