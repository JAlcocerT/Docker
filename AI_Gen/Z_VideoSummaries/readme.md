* Groq+Streamlit
    * https://www.youtube.com/watch?v=XaooOHWqxEw
        * https://github.com/phidatahq/phidata/tree/main/cookbook/llms/groq/video_summary
        * https://console.groq.com/keys

```sh
git clone --depth=1 https://github.com/phidatahq/phidata
cd phidata
git sparse-checkout init
git sparse-checkout set cookbook/llms/groq/video_summary
git pull origin main
```

```sh
python3 -m venv ~/.venvs/aienv

source ~/.venvs/aienv/bin/activate
export GROQ_API_KEY=***


pip install -r cookbook/llms/groq/video_summary/requirements.txt
streamlit run cookbook/llms/groq/video_summary/app.py
```