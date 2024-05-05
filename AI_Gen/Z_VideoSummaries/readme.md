## Groq+Streamlit = YT Summaries

* https://www.youtube.com/watch?v=XaooOHWqxEw
        * https://github.com/phidatahq/phidata/tree/main/cookbook/llms/groq/video_summary
        * https://console.groq.com/keys (!)

```sh
git clone --depth=1 https://github.com/phidatahq/phidata
cd phidata
git sparse-checkout init
git sparse-checkout set cookbook/llms/groq/video_summary
git pull origin main
```

```sh
#sudo apt-get install python3-venv


#python3 -m venv ~/.venvs/aienv
python3 -m venv ./aienv

#source ~/.venvs/aienv/bin/activate
source ./aienv/bin/activate
export GROQ_API_KEY=***

export GROQ_API_KEY=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

pip install -r cookbook/llms/groq/video_summary/requirements.txt
streamlit run cookbook/llms/groq/video_summary/app.py
```

sed -i 's/numpy==1\.26\.4/numpy==1.24.4/' requirements.txt
sed -i 's/numpy==1\.26\.4/numpy==1.24.4/; s/pandas==2\.2\.2/pandas==2.0.2/' requirements.txt
