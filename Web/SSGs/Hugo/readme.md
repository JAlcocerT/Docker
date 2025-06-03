> https://jalcocert.github.io/JAlcocerT/using-hugo-as-website/#hugo-container

1. Clone a repo like the [Portfolio](https://github.com/JAlcocerT/Portfolio)
2. Follow the steps below

```sh
git clone https://github.com/JAlcocerT/Portfolio
cd Portfolio
hugo server #http://localhost:1313/portfolio/
hugo #builds and go to /public
```

It can be run live with:

And with [Container](https://jalcocert.github.io/JAlcocerT/using-hugo-as-website/#hugo-container), as seen [here](https://github.com/JamesTurland/JimsGarage/tree/main/Web-Servers)

This executes `hugo server` for dev:

```sh
docker run -d \
  --name hugo \
  -p 1313:1313 \
  -v "/home/jalcocert/Desktop/Portfolio/:/src" \
  klakegg/hugo:0.101.0 \
  server
```