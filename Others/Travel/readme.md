**Some container for your travel / trips / adventures**.

> See also [tech for a trip](https://jalcocert.github.io/JAlcocerT/tech-for-a-trip/)

---

1. [AdventureLog](https://fossengineer.com/selfhosting-adventurelog/)

```sh
docker-compose -f adventurelog_docker-compose.yml up -d

#docker exec -it adventurelog-db psql -U adventure -d database
#\dt
#docker exec -it adventurelog-db psql -U adventure -d database -c "\d+ account_emailaddress"
```

> Which is a Django Python Web App and can be [integrated](https://adventurelog.app/docs/configuration/immich_integration.html) with Immich and Umami!

2. [AirTrail](https://fossengineer.com/selfhosting-airtrail/)

3. Wanderer - with komoot/Strava integration!

* https://github.com/IoTechCrafts/wanderer

```sh
wget https://raw.githubusercontent.com/IoTechCrafts/wanderer/main/docker-compose.yml

wget https://raw.githubusercontent.com/Flomp/wanderer/main/docker-compose.yml
docker compose up -d
#docker stats $(docker-compose -f docker-compose.yml ps -q)

docker stats $(docker-compose ps -q)
```