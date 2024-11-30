## CrewAI


[Framework for orchestrating](https://fossengineer.com/ai-agents-crewai/) role-playing, autonomous AI agents. AutoGen Alternative.

* 👉  <https://www.youtube.com/watch?v=GKr5URJvNDQ&t=12s>

* https://github.com/joaomdmoura/crewAI
    * https://github.com/joaomdmoura/crewAI/blob/main/LICENSE
    * https://github.com/joaomdmoura/CrewAI/wiki
* https://pypi.org/project/crewai/


```sh
docker build -t crewai .
```

### With Ollama


```sh
ollama run openhermes
#https://ollama.ai/library/openhermes/tags
```

### Dependencies

#### WIth conda

```sh
conda info --envs
conda create -n CREWAI python=3.11
conda activate CREWAI

pip install crewai
pip install langchain

#pip show crewai
```