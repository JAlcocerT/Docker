LangGraph is ais a **low-level orchestration framework** for building controllable agents.
 
While langchain provides integrations and composable components to streamline LLM application development, the LangGraph library enables agent orchestration — offering customizable architectures, long-term memory, and human-in-the-loop to reliably handle complex tasks.


```sh
pip install langgraph==0.3.27
#pip install python-dotenv
```

* https://www.youtube.com/watch?v=1Q_MDOWaljk



* https://github.com/whitew1994WW/LangGraphForBeginners
    * https://github.com/whitew1994WW/LangGraphForBeginners/blob/main/tutorial_react.ipynb



---

* https://pypi.org/project/langgraph/
    * https://pypi.org/project/langgraph/
    * https://pypi.org/project/langchain-openai/


```sh
#python -m venv solvingerror_venv #create the venv
python3 -m venv lg_venv #create the venv

#solvingerror_venv\Scripts\activate #activate venv (windows)
source lg_venv/bin/activate #(linux)
```

**Install dependencies** with:

```sh
#pip install langchain-openai langgraph
pip install -r requirements.txt #all at once
#pip freeze | grep langchain

#pip show mlflow
pip list
#pip freeze > requirements-export.txt #generate a txt with the ones you have!
```