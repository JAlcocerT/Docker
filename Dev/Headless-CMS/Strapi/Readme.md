

* https://strapi.io/
* https://github.com/strapi/strapi

```sh
docker compose up --build
#sudo docker-compose up -d


docker build -t my-strapi-app .
#docker run -p 1337:1337 my-strapi-app

#docker exec -it <container_name_or_id> sh
docker exec -it my-strapi-container sh

#sudo docker compose -f Strapi_Docker-compose.yml up -d
```

> Strapi is an open-source headless CMS. It’s 100% JavaScript/TypeScript, fully customizable and developer-first.

#https://market.strapi.io/
#https://github.com/strapi-community/awesome-strapi

#https://docs.strapi.io/dev-docs/quick-start
#https://docs.strapi.io/dev-docs/installation/docker

#open-source headless CMS. It’s 100% JavaScript/TypeScript, fully customizable and developer-first. 

* Strapi
    * https://strapi.io/blog/how-to-self-host-your-headless-cms-using-docker-compose
  * Strapi + Astro - https://docs.astro.build/en/guides/cms/strapi/


## Installing Strapi 

This 3h video helped me a lot to get started: https://www.youtube.com/watch?v=t1iUuap7vhw

```sh
node -v
npm -v
#yarn --version #another package manager for js
#npm install --global yarn

git --version
```

Then:

```sh
npx create-strapi-app@latest my-sample-project --quickstart #https://docs.strapi.io/dev-docs/installation/cli
cd my-sample-project
npm install
npm run develop #yes, not: npm run dev
```

Go to the **Strapi Admin panel**: `http://localhost:1337/admin/` and create the first admin user.

* The **DB is sqlite by default** and it is at: `my-project/.tmp`
    * For self-hosted Strapi projects, all your content is saved in a database file (by default, SQLite) found in the `.tmp` subfolder in your project's folder. See the `.env` generated at `my-sample-project`
    * https://docs.strapi.io/dev-docs/configurations/database

```sh
sqlite3 data.db
.tables
.schema table_name
#SELECT * FROM table_name;
```



## Strapi + CMSs

* Strapi + NextJS
* https://strapi.io/integrations/nextjs-cms
    * https://www.youtube.com/watch?v=KEmlt5bxo3M&list=PL7Q0DQYATmvjXSuHfB8CY_n_oUeqZzauZ&index=2
        * https://jwt.io/
    * Next.js is a very popular React framework
    * Strapi is also built on **React**

* Strapi + Astro
    * https://docs.astro.build/en/guides/cms/strapi/


## Marketplace

* http://localhost:1337/admin/marketplace?page=5


#https://market.strapi.io/plugins/strapi-plugin-cloudflare-pages
#https://market.strapi.io/plugins/strapi-plugin-graphs-builder
#https://market.strapi.io/plugins/@webvibe-io-strapi-plugin-instagram
#https://market.strapi.io/plugins/strapi-leaflet-geoman
#https://market.strapi.io/plugins/strapi-plugin-oembed
#https://market.strapi.io/plugins/strapi-stripe

* https://docs.strapi.io/dev-docs/configurations/sso


## Starter Themes

* https://strapi.io/showcases
* https://strapi.io/blog/introducing-the-new-strapi-starter-with-nextjs13-tailwind-and-typescript
* https://github.com/strapi/starters-and-templates/tree/main/packages/templates

* https://github.com/strapi-community/awesome-strapi