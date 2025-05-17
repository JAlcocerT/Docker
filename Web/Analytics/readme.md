1. Setup [**Umami** Web Analytics](https://fossengineer.com/selfhosting-umami-with-docker/)

```sh
openssl rand -base64 32 #tweak the HASH_SALT first
docker-compose -f umami_docker-compose.yml up -d
```

> Which can be run with cloudflare

2. Fathom WebAn - https://hub.docker.com/r/usefathom/fathom/

```sh
docker-compose -f fathom_docker-compose.yml up -d
```

3. [Tianji](https://fossengineer.com/setup-tianji-with-docker/) - You get web analytics and [hardware monitoring](https://jalcocert.github.io/JAlcocerT/how-to-setup-beszel-monitoring/)

```sh
docker-compose -f Tianji_docker-compose.yml up -d
```

> Which I covered at: https://jalcocert.github.io/JAlcocerT/how-to-setup-beszel-monitoring/#tianji as not just web analytics solution!


4. [Medama](https://fossengineer.com/medama-web-analytics-selfhosting)

```sh
docker-compose -f medama_docker-compose.yml up -d
```

5. Matomo

6. Aptabase

https://github.com/aptabase/aptabase
https://github.com/aptabase/aptabase?tab=AGPL-3.0-1-ov-file#readme

7. [Rybbit](https://fossengineer.com/rybbit-web-analytics-selfhosted/)

```sh
docker-compose -f rybbit_docker-compose.yml up -d
```

8. [Liwan](https://fossengineer.com/liwan-selfhosting/)

```sh
docker-compose -f liwan_docker-compose.yml up -d
```

9. [Swetrix](https://fossengineer.com/swetrix-webanalytics-selfhosting/) 

```sh
#.env.swetrix
docker-compose -f swetrix_docker-compose.yml up -d
```

10. https://github.com/Litlyx/litlyx

```sh
docker-compose -f litlyx_docker-compose.yml up -d
```

11. https://github.com/electerious/Ackee


> MIT | Self-hosted, Node.js based analytics tool for those who care about privacy.


12. [Vince](https://fossengineer.com/selfhosting-vince-webanalytics/)

```sh
docker-compose -f vince_docker-compose.yml up -d
```


13. https://github.com/pirsch-analytics/pirsch


14. Dashflare

```sh
docker-compose -f dashflare_docker-compose.yml up -d
```

15. GoatCounter

* https://github.com/arp242/goatcounter

> Lightweight tracker (<1KB) without cookies, IP addresses, or additional identifiers, ensuring compliance with GDPR, PECR, and other regulations.