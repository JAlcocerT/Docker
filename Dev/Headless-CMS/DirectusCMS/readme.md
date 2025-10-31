See https://directus.io/docs/getting-started/create-a-project

* https://docs.directus.io/guides/headless-cms/reusable-components.html

* https://www.youtube.com/watch?v=J7tFWxAGkh4

* https://www.youtube.com/watch?v=a5TUZcaCpIk

```sh
# mkdir -p database uploads extensions
# sudo chown -R 1000:1000 database uploads extensions
# sudo chmod -R 775 database uploads extensions
docker compose -f Directus_Docker-compose.yml up
```

Go to `http://localhost:8055/admin/login` with the user/pwd provided as environment in the compose.

> Thanks to Lukas: https://www.youtube.com/watch?v=RceFoASxO00