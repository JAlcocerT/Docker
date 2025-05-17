1. Setup [**Umami** Web Analytics](https://fossengineer.com/selfhosting-umami-with-docker/)

```sh
docker-compose -f umami_docker-compose.yml up -d
```

2. Fathom WebAn - https://hub.docker.com/r/usefathom/fathom/

> See also: https://github.com/geerlingguy/fathom-container

3. [Tianji](https://fossengineer.com/setup-tianji-with-docker/)

```sh
docker-compose -f Tianji_docker-compose.yml up -d
```

4. Medama

```sh
docker-compose -f medama_docker-compose.yml up -d
```


5. Matomo

6. OpenReplay

```sh
# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/openreplay/openreplay/main/scripts/docker-compose/docker-install.sh)"

wget https://raw.githubusercontent.com/openreplay/openreplay/main/scripts/docker-compose/docker-install.sh -O docker-install.sh
/bin/bash docker-install.sh
```

7. [Rybbit](https://fossengineer.com/rybbit-web-analytics-selfhosted/)

```sh
docker-compose -f rybbit_docker-compose.yml up -d
```

8. [Liwan](https://fossengineer.com/liwan-selfhosting/)

```sh
docker-compose -f liwan_docker-compose.yml up -d
```

9. Swetrix https://github.com/Swetrix/swetrix

```sh
docker-compose -f liwan_docker-compose.yml up -d
```

10. https://github.com/Litlyx/litlyx


> Powerful Analytics Solution. Setup in 30 seconds. Display all your data on a Simple, AI-powered dashboard. Fully self-hostable and GDPR compliant. Alternative to Google Analytics, MixPanel, Plausible, Umami & Matomo.

11. https://github.com/electerious/Ackee


> MIT | Self-hosted, Node.js based analytics tool for those who care about privacy.


12. 