## FlowiseAI

* https://github.com/FlowiseAI/Flowise/tree/main/docker
* https://hub.docker.com/r/flowiseai/flowise

```sh
git clone https://github.com/FlowiseAI/Flowise
cd ./Flowise/docker
cp .env.example .env

cat <<EOL >> .env
FLOWISE_USERNAME=teco
FLOWISE_PASSWORD=paco
EOL
```

* API:

```sh
curl http://localhost:3010/api/v1/prediction/f99a1945-64ae-4e39-93ae-46c272e2b584 \
     -X POST \
     -d '{"question": "Carrot"}' \
     -H "Content-Type: application/json"
```