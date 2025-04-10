* https://fossengineer.com/selfhosting-llms-ollama/

```sh
docker run -d --name ollama -p 11434:11434 -v ollama_data:/root/.ollama ollama/ollama

docker exec -it ollama ollama --version
docker exec -it ollama sh

ollama pull deepseek-r1:8b
```