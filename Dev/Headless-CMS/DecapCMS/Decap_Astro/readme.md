* https://docs.astro.build/en/guides/cms/decap-cms/

```sh
git clone https://github.com/gxanshu/astro-decap-cms-starter
cd astro-decap-cms-starter
npm install
npm run dev
```

```sh
mkdir ./public/admin #https://decapcms.org/docs/install-decap-cms/

echo '<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="robots" content="noindex" />
    <title>Content Manager</title>
  </head>
  <body>
    <!-- Include the script that builds the page and powers Decap CMS -->
    <script src="https://unpkg.com/decap-cms@^3.0.0/dist/decap-cms.js"></script>
  </body>
</html>' > ./admin/index.html
```

```sh
npm install decap-cms-app --save
```

Modify the `config.yml` for local dev

```yml
# when using the default proxy server port
local_backend: true #https://decapcms.org/docs/working-with-a-local-git-repository/

backend:
  name: git-gateway
```

```sh
npx decap-server #will listen on 8081
npm run dev #
```

Now go to: `localhost:3001/admin` #port as per theme

* Astros Theme