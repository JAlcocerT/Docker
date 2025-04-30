I tinkered with LangFuse at the DSC Tools for D&A Project [Post](https://jalcocert.github.io/JAlcocerT/big-data-tools-for-data-analytics/#dsc-tools-for-da-projects)

This is how to set it up with Docker containers: https://raw.githubusercontent.com/langfuse/langfuse/refs/heads/main/docker-compose.yml

> LangFuse is an LLM monitoring alternative to LangSmith.

Run it locally with docker:

```sh
# Get a copy of the latest Langfuse repository
git clone https://github.com/langfuse/langfuse.git #https://langfuse.com/self-hosting/docker-compose
cd langfuse

# Run the langfuse docker compose
docker compose up #important DONT DO docker-compose, it works using v2
#sudo docker stop portainer #if you get port 9000 conflict
#sudo docker start portainre
```

> Go to port `3000` to see the web UI

It uses few other containers:

* clickhouse: https://hub.docker.com/r/clickhouse/clickhouse-server/tags
* redis:
* minio:

> See more info at [langfuse docs](https://langfuse.com/self-hosting/upgrade-guides/upgrade-v2-to-v3#docker-compose)