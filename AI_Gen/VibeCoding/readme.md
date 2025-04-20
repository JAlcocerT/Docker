vibe coding stuff...


1. Codex

```sh
docker build -t python-codex .
#


#docker run -it python-codex
#export OPENAI_API_KEY="your-api-key-here"
docker run -it -e OPENAI_API_KEY="your-api-key-here" python-codex
```