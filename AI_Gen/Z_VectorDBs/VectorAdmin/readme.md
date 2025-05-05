# Vector Admin

**GUI for vector DB**'s like: **Qdrant, ChromaDB** or Pinecone...

The universal tool suite for vector database management. Manage Pinecone, Chroma, Qdrant, Weaviate and more vector databases with ease. 

* <https://www.youtube.com/watch?v=cW8Eohz6pzs>

<https://github.com/Mintplex-Labs/vector-admin>

* <https://vectoradmin.com/>

```sh
git clone git@github.com:Mintplex-Labs/vector-admin.git ./vector-admin
cd vector-admin
cd docker
cp .env.example .env. #and adjust it
```

Once you have adjusted the .env, lets **build our VectorDB Docker** image:

```sh
sudo docker-compose up -d --build vector-admin
```

## Docker

<https://github.com/Mintplex-Labs/vector-admin/blob/master/docker/DOCKER.md>

```sh
git clone git@github.com:Mintplex-Labs/vector-admin.git ./vector-admin
cd vector-admin
cd docker
cp .env.example .env. #and adjust
```

#5432 will be ok as it is in the same stack

JWT_SECRET="some-random-string"
SYS_EMAIL="root@vectoradmin.com"
SYS_PASSWORD="password"
DATABASE_CONNECTION_STRING="postgresql://vectoradmin:password@postgres:5432/vdbms" # Valid PG Connection string.
INNGEST_SIGNING_KEY="some-random-string"


<!-- 
```yml
version: '3.8'
services:
  postgres:
    image: postgres:latest
    environment:
      POSTGRES_USER: vectoradmin
      POSTGRES_PASSWORD: password
      POSTGRES_DB: vdbms
    ports:
      - "5433:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:

``` -->

<!-- ```
JWT_SECRET="some-random-string"
SYS_EMAIL="root@vectoradmin.com"
SYS_PASSWORD="password"
DATABASE_CONNECTION_STRING="postgresql://vectoradmin:password@host.docker.internal:5433/vdbms" # Valid PG Connection string.
INNGEST_SIGNING_KEY="some-random-string"
``` -->

For external container:
<!-- ```
JWT_SECRET="some-random-string"
SYS_EMAIL="root@vectoradmin.com"
SYS_PASSWORD="password"
DATABASE_CONNECTION_STRING="postgresql://vectoradmin:password@localhost:5433/vdbms"
INNGEST_SIGNING_KEY="some-random-string"
``` -->

```sh
sudo docker-compose up -d --build vector-admin
```

localhost:3001

use You first login will require you to use the SYS_EMAIL and SYS_PASSWORD set via ENV during build or run. After onboarding this login will be permanently disabled.

Try and connect to qDrant with:

http://192.168.3.103:6333

And to Chroma:

Chroma running locally When trying to connect to a Chroma instance running also on the same machine use http://host.docker.internal:[CHROMA_PORT] as the URL to connect with.

http://localhost:8001




#if you stored something
http://localhost:8001/api/v1/collections