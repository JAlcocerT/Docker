1. **Supabase**

```sh
git clone https://github.com/supabase/supabase.git

cd supabase/docker
cp .env.example .env
nano .env
docker-compose up -d
```

* https://github.com/supabase/supabase
* https://supabase.com/docs/guides/database/extensions/wrappers/stripe
* https://docs.stripe.com/customer-management/integrate-customer-portal

> http://localhost:9000

2. **PocketBase**: with selfhosting only focus. **Great Selfhostable BaaS**.

```sh
#docker compose up -d
docker compose -f ./PB/PB_docker-compose.yml up -d
make setup
```