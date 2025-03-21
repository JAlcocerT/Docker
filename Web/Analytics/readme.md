1. Setup [**Umami** Web Analytics](https://fossengineer.com/selfhosting-umami-with-docker/)

2. Fathom WebAn - https://hub.docker.com/r/usefathom/fathom/

See also: https://github.com/geerlingguy/fathom-container

3. [Tianji](https://fossengineer.com/setup-tianji-with-docker/)

4. Medama


https://oss.medama.io/deployment/docker

```yml
version: '3.9'
services:
  medama:
    image: ghcr.io/medama-io/medama:latest
    container_name: medama
    restart: unless-stopped
    environment:
      - LOGGER=pretty
    ports:
      - "8085:8080"
    volumes:
      - ./data:/app/data
    networks:
      - nginx_nginx_default #for https

networks:
  nginx_nginx_default:
    external: true  
```

> You will need https to access with these: `admin/CHANGE_ME_ON_FIRST_LOGIN`


as per the docs:

Add Your First Website

Success! You can now add your first website to the analytics instance by visiting the web interface at `http://localhost:8080` or the publicly accessible hostname for your deployment.

The **default login credentials** are:

```txt
Username: admin
Password: CHANGE_ME_ON_FIRST_LOGIN
```

To successfully login, you must either use localhost or a HTTPS connection. Logging in via an unencrypted HTTP connection will not work.

For that, you can use NGINX!

5. Matomo

1. [Umami](https://fossengineer.com/selfhosting-umami-with-docker/)
2. [Tianji](https://fossengineer.com/setup-tianji-with-docker/)
3. https://github.com/Swetrix/swetrix
4. https://github.com/Litlyx/litlyx


> Powerful Analytics Solution. Setup in 30 seconds. Display all your data on a Simple, AI-powered dashboard. Fully self-hostable and GDPR compliant. Alternative to Google Analytics, MixPanel, Plausible, Umami & Matomo.

5. https://github.com/electerious/Ackee

https://docs.ackee.electerious.com/#/docs/Get%20started#with-docker

> MIT | Self-hosted, Node.js based analytics tool for those who care about privacy.



[![Star History Chart](https://api.star-history.com/svg?repos=langchain-ai/langchain,run-llama/llama_index,deepset-ai/haystack,Sinaptik-AI/pandas-ai&type=Date)](https://star-history.com/#langchain-ai/langchain&run-llama/llama_index&deepset-ai/haystack&Sinaptik-AI/pandas-ai&type=Date)

---

**PRODUCT TOOLS**


6. **Posthog**

* https://posthog.com/docs/self-host
* https://posthog.com/docs/how-posthog-works

```sh
#/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/posthog/posthog/HEAD/bin/deploy-hobby)"

wget https://raw.githubusercontent.com/posthog/posthog/HEAD/bin/deploy-hobby
/bin/bash deploy-hobby
```


7. Countly

8. GuideFox

9. UserTour

https://github.com/usertour/usertour?ref=selfh.st

>  Usertour is an open-source user onboarding platform designed for developers. It allows you to create in-app product tours, checklists, and launchers in minutes—effortlessly and with full control.The open-source alternative to Userflow and Appcues 