* https://mlflow.org/docs/latest/getting-started/intro-quickstart/


```sh
#sudo docker build mlflow .
docker run -d --name mlflow_container -p 8080:8080 -v vol_mlflow:/app mlflow mlflow server --host 0.0.0.0 --port 8080
```

---

```sh
#mlflow server --host 127.0.0.1 --port 8080
mlflow server --host 0.0.0.0 --port 8080
```

```py
import mlflow

mlflow.set_tracking_uri("http://localhost:8080")
```

> Go to Port 8080!

---

* https://pypi.org/project/mlflow/

```sh
#python -m venv solvingerror_venv #create the venv
python3 -m venv mlflow_venv #create the venv

#solvingerror_venv\Scripts\activate #activate venv (windows)
source mlflow_venv/bin/activate #(linux)
```

**Install dependencies** with:

```sh
#pip install mlflow==2.21.3
pip install -r requirements.txt #all at once
#pip freeze | grep langchain

#pip show mlflow
pip list
#pip freeze > requirements-export.txt #generate a txt with the ones you have!
```