## LocalAI Project

* https://github.com/mudler/LocalAI
    * https://github.com/mudler/LocalAI?tab=MIT-1-ov-file#readme
    * https://localai.io/

```sh
git clone https://github.com/mudler/LocalAI
docker-compose up -d
```


```sh
#docker run -ti --name local-ai -p 8080:8080 localai/localai:latest-cpu
```

* Available after build at: `localhost:8080`


```sh
curl http://192.168.0.12:8081/v1/completions -H "Content-Type: application/json" -d '{
     "model": "your-model.gguf",
     "prompt": "A long time ago in a galaxy far, far away",
     "temperature": 0.7
   }'
```