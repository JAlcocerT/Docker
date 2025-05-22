From powerpoints to kanban boards.

1. Leantime
2. OpenProject
3. FocalBoard
4. Claper (Audience interaction)
5. Vikunja
6. Excalidraw
7. Drawio
8. Slidev Selfhosted

### Huly

* Accessing the URL `http://localhost:8087` will lead you to the app in production mode.
    * <https://huly.io/blog/symphony-of-productivity>

```sh
git clone https://github.com/fergmar/huly

cd ./dev/
rush build    # Will build all the required packages.
rush bundle   # Will prepare bundles.
rush docker:build   # Will build Docker containers for all applications in the local Docker environment.
docker compose up -d --force-recreate # Will set up all the containers
```