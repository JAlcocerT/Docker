

#https://strapi.io/
#https://github.com/strapi/strapi

#https://market.strapi.io/
#https://github.com/strapi-community/awesome-strapi

#https://docs.strapi.io/dev-docs/quick-start
#https://docs.strapi.io/dev-docs/installation/docker

#open-source headless CMS. It’s 100% JavaScript/TypeScript, fully customizable and developer-first. 

* Strapi
    * https://strapi.io/blog/how-to-self-host-your-headless-cms-using-docker-compose
  * Strapi + Astro - https://docs.astro.build/en/guides/cms/strapi/


## Installing Strapi 


```sh
node -v
npm -v
#yarn --version #another package manager for js
#npm install --global yarn

git --version
```

Then:

```sh
npx create-strapi-app@latest my-project3 --quickstart #https://docs.strapi.io/dev-docs/installation/cli
cd my-project
npm install
npm run develop #yes, not: npm run dev
```

* `http://localhost:1337/admin/`
* The DB is sqlite by default and it is at: `my-project/.tmp`
    * For self-hosted Strapi projects, all your content is saved in a database file (by default, SQLite) found in the .tmp subfolder in your project's folder.
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