* https://fossengineer.com/selfhosting-llms-ollama/

```sh
docker run -d --name ollama -p 11434:11434 -v ollama_data:/root/.ollama ollama/ollama

docker exec -it ollama ollama --version
docker exec -it ollama sh

ollama pull deepseek-r1:8b
```

> Ollama can be used together with [Oterm](https://jalcocert.github.io/JAlcocerT/selfhosted-apps-may-2025/#ai-apps-im-selfhosting)