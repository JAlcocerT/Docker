# PrivateGPT

* 👉 <https://www.youtube.com/watch?v=XFiof0V3nhA>
    * <https://gist.github.com/mberman84/9b3c281ae5e3e92b7e946f6a09787cde>
* <https://github.com/imartinez/privateGPT>
    * <https://docs.privategpt.dev/>


* It can run a server and you can use its API to port 8001: **python3 api-privategpt.py**
    * <https://docs.privategpt.dev/#section/API>
    * Chat completion API (same as OpenAI): <https://docs.privategpt.dev/#tag/Contextual-Completions/operation/prompt_completion_v1_completions_post>

```sh 
docker build -t privategpt .
docker-compose up -d
```

```sh
git clone https://github.com/imartinez/privateGPT

#conda create -n privategpt python=3.11
#conda activate privategpt

pip install poetry
#conda install -c conda-forge pipx
#pipx install poetry

poetry --version

apt update
apt-get install build-essential # C and C++ compilers installed on your system.

poetry lock
poetry install --with ui,local

#review the model to use: local/amazon sagemaker/openai -> settings.yaml

poetry run python scripts/setup #download models

PGPT_PROFILES=local make run

#pyproject.toml -> openai="0.28.0"
#poetry update


#GPT_PROFILES=local make run
```

When the server is started it will print a log Application startup complete. Navigate to http://localhost:8001 to use the Gradio UI or to http://localhost:8001/docs (API section) to try the API using Swagger UI.


## Poetry

Poetry is a Python dependency management and packaging tool. It provides a way to manage Python project dependencies, create virtual environments, and package your Python projects for distribution. Poetry aims to simplify and streamline the process of managing Python projects by providing a unified and consistent toolset.