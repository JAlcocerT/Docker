I was testing this **flask container setup** for:

* https://jalcocert.github.io/JAlcocerT/making-flask-cms-for-ssg/
* https://github.com/JAlcocerT/morita-astroportfolio-flasked

**Build:**

```sh
docker build -f Dockerfile -t pb .
docker compose -f docker-compose.yml build
```

**Run** - Try the container:

```sh
docker run --rm -d --name flask-cms \
  -p 5050:5050 \
  --entrypoint tail \
  flask-cms -f /dev/null
```

```sh
docker exec -it flask-cms sh
uv run app.py
```

Send the command directly:

```sh
docker run --rm -d --name flask-cms \
  -p 5050:5050 \
  -e CONTENT_DIR=/app/src/content \
  flask-cms sh -lc "uv run app.py"
```

```sh
docker run --rm -d --name flask-cms \
  -p 5050:5050 \
  -e CONTENT_DIR=/app/src/content \
  flask-cms sh -lc "uv run gunicorn app:app -b 0.0.0.0:5050 --workers 2 --threads 4 --timeout 60"
```

```sh
docker logs -f flask-cms
```