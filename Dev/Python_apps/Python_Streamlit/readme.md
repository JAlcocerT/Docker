See example of a [**Streamlit Containerized** Project](https://github.com/JAlcocerT/Streamlit-MultiChat)

* https://pypi.org/project/streamlit/

```sh
sudo docker build -t streamlit_webapp .
#sudo docker-compose up -d
docker compose --file Streamlit_Docker-compose.yml up -d
```


---


```sh
#git clone https://github.com/JAlcocerT/Streamlit-MultiChat
#python -m venv multichat_venv #create the venv
python3 -m venv multichat_venv #linux

#multichat_venv\Scripts\activate #activate venv (windows)
source multichat_venv/bin/activate #(linux)
```

Then, provide the API Keys and run the scripts:

```sh
pip install streamlit==1.44.1
pip install streamlit_webrtc

#sudo apt install libportaudio2
#pip install -r requirements.txt
```