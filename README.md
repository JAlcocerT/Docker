<div align="center">
  <h1>Docker and Self-Hosting Setup Guides</h1>
</div>

<div align="center">
  <h3>A reference for Self-Hosting pourposes and for anyone starting their journey with Docker</h3>
</div>

<p align="center">
  <a href="https://github.com/JAlcocerT/Docker?tab=MIT-1-ov-file#readme" style="margin-right: 5px;">
    <img alt="Code License" src="https://img.shields.io/badge/License-MIT-blue.svg" />
  </a>
  <a href="https://youtube.com/@JAlcocerTech">
    <img alt="YouTube Channel" src="https://img.shields.io/badge/YouTube-Channel-red" />
  </a>
  <a href="https://GitHub.com/JAlcocerT/Docker/graphs/commit-activity" style="margin-right: 5px;">
    <img alt="Maintained" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" />
  </a>
  <a href="https://github.com/JAlcocerT/Docker">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/JAlcocerT/Docker" />
  </a>
  <a href="https://github.com/JAlcocerT/Docker">
    <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/JAlcocerT/Docker" />
  </a>
</p>


---

A companion for This [public and open blog →](https://jalcocert.github.io/JAlcocerT/blog/)

* My [**Raspberry Pi** guide](https://jalcocert.github.io/RPi/posts/selfhosting-with-docker/)
* My [**Linux** guide](https://jalcocert.github.io/Linux/docs/debian/docker/)
* [Self-hosting](https://jalcocert.github.io/Linux/docs/linux__cloud/selfhosting/)
  * [Install **Portainer/Dockge** and get ready to deploy docker containers with a UI.](https://fossengineer.com/understanding-containers-for-selfhosting/)
  * You can also [build **MultiArch** container images](https://jalcocert.github.io/JAlcocerT/github-actions-use-cases/) for your projects with GHActions. [Example Project](https://github.com/JAlcocerT/Streamlit-MultiChat)

## Repository Structure
  * [Introduction: Why Docker?](#Intro)
  * [Back-up related containers](#Backups)
  * [Business apps related containers](#business)
  * [Communication apps related containers](#communication)
  * [IoT Containers](#iot)
  * [Media Containers](#media)
  * [Security and Privacy related Containers](#security)
  * [Web related Containers](#Web)
  * [Ways to Contribute](#contribute)

## Why Docker?

[Docker is a tool](https://fossengineer.com/docker-first-steps-guide-for-data-analytics/) designed to make it easier to **create, deploy, and run applications by using *containers*.**

Containers allow us to **package up an application with all of the parts it needs to work properly** -  such as libraries and other dependencies, and deploy it as one package.
 
Everything needed to run a software application successfully can be stored in a container to **make development and deployment more efficient**.

## Docker and your favourite Apps

I have been **collecting/adapting the config files** to install several Apps with Docker.

Consolidated them on this public repository for anyone that might find it helpful.

<details>
  <summary>Click to know which Apps 🐋👈</summary>
  &nbsp;

### [Backups:](https://github.com/JAlcocerT/Docker/tree/main/Backups)
  * Duplicati :heavy_check_mark:
  * Filerun :heavy_check_mark:
  * [Nextcloud](https://jalcocert.github.io/JAlcocerT/sync-file-tools/#nextcloud) :heavy_check_mark:
    * [RPI](https://jalcocert.github.io/RPi/posts/selfhosting-nextcloud/) :heavy_check_mark:
  * Photos: 
    * LibrePhotos
    * [Immich](https://github.com/JAlcocerT/Docker/blob/main/Media/Photo/Immich_Docker-Compose.yml)
    * Lychee 
    * Photonix
    * Photoprism
    * [Photoview :page_with_curl:](https://fossengineer.com/selfhosting-Photoview-docker/) :heavy_check_mark: -> file system friendly
    * Piwigo
  * [RClone](https://github.com/JAlcocerT/Docker/blob/main/Backups/rclone_docker-compose.yml) :heavy_check_mark:
  * RSync :heavy_check_mark:
  * [Samba](https://fossengineer.com/selfhosting-samba/) :heavy_check_mark:
  * Syncthing
    
### [Business:](https://github.com/JAlcocerT/Docker/tree/main/Business)
   * ERPs:
      * ERPNext
      * Dolibarr :heavy_check_mark:
      * Odoo (ex- OpenERP) :heavy_check_mark:
    * Invoicing:
      * Crater Invoices
      * Invoice Ninja
      * Solid Invoice (x86 only)
      * [Serverless Invoices and React Invoice Generator](https://fossengineer.com/open-source-invoice-creator/)
    * Management:
       * https://github.com/JAlcocerT/Docker/blob/main/Business/PM/vikunja_docker-compose.yaml :heavy_check_mark:
       * [Leantime](https://fossengineer.com/selfhosting-Leantime-docker/) (x86 & ARM, :heavy_check_mark:)
### [Communication:](https://github.com/JAlcocerT/Docker/tree/main/Communication)
   * Chats:
       * [Matrix with Synapse :page_with_curl:](https://fossengineer.com/selfhosting-matrix-synapse-docker/) :heavy_check_mark:
       * Others: Revolt, RocketChat, Jitsi, Discourse
   * [FreshRSS](https://fossengineer.com/freshrss-docker-setup/) :heavy_check_mark:
### [Dev](https://github.com/JAlcocerT/Docker/tree/main/Dev)
* [WebTops](https://fossengineer.com/selfhosting-webtops-with-docker/)
* [Gitea](https://fossengineer.com/selfhosting-Gitea-docker/) :heavy_check_mark:
* [Gogs](https://fossengineer.com/selfhosting-Gogs-with-Docker/)
* [Gitlab CE](https://fossengineer.com/selfhosting-Gitlab-with-Docker)
* [VSCode Server](https://github.com/JAlcocerT/Docker/blob/main/Dev/vscode-server_Docker-compose.yml) :heavy_check_mark:
* [Jenkins](https://fossengineer.com/selfhosting-jenkins-ci-cd/)
* [Airflow](https://fossengineer.com/selfhosting-airflow-with-docker)
* [OneDev](https://github.com/JAlcocerT/Docker/blob/main/Dev/GIT/OneDev_Docker-compose.yml): includes kanban board
* [SnippetBox](https://github.com/JAlcocerT/Docker/blob/main/Others/snippetbox_docker-compose.yml) :heavy_check_mark:
* [SSGs](https://github.com/JAlcocerT/Docker/tree/main/Web/SSGs)
### [IoT:](https://github.com/JAlcocerT/Docker/tree/main/IoT)
* Automations:
  * Domoticz
  * [Home Assistant](https://jalcocert.github.io/RPi/posts/rpi-iot-dht11-influxdb/#how-can-i-install-home-assistant) :heavy_check_mark:
  * Home Bridge
  * OpenHab
* [Internet speed tracker](https://jalcocert.github.io/RPi/posts/self-internet-monit/#speedtest-tracker) :heavy_check_mark:
* [OpenSpeedTest](https://jalcocert.github.io/RPi/posts/self-internet-monit/#openspeedtest) :heavy_check_mark:
* GPIO
  * TIO: https://github.com/tio/tio
* [BI Tools](https://jalcocert.github.io/JAlcocerT/setup-bi-tools-docker/):
  * [Metabase](https://jalcocert.github.io/RPi/posts/rpi-iot-dht1122-mongo/#metabase)
  * [Apache Superset](https://jalcocert.github.io/RPi/posts/rpi-gps-superset/#apache-superset-setup)
  * [Redash](https://jalcocert.github.io/JAlcocerT/setup-bi-tools-docker/#redash)
  * Grafana
* Dashboards:
  * [NetData](https://fossengineer.com/selfhosting-server-monitoring-with-netdata-and-docker/) :heavy_check_mark:
  * Grafana with Prometheus (internet speed) :heavy_check_mark:
  * Grafana with Prometheus (internet + device with node exporter)
  * EFK stack for logs(Elastic search, Fluentd, Kibana)
  * ELK stack (ES, Logstash, Kibana)
  * GOtify
  * Ntfy (notify)
  * [Uptime Kuma :page_with_curl:](https://fossengineer.com/selfhosting-uptime-Kuma-docker/) :heavy_check_mark:
  * Flame :heavy_check_mark:   
  * Homarr :heavy_check_mark:
  * Dockge :heavy_check_mark:
    
### [Media](https://github.com/JAlcocerT/Docker/tree/main/Media)
* E-Books/Podcasts
  * Calibre :heavy_check_mark:
  * Audiobookshelf :heavy_check_mark:
  * Podgrab :heavy_check_mark:
* [Photos](https://github.com/JAlcocerT/Docker/tree/main/Backups/Photos): 
  * [PiGallery](https://github.com/JAlcocerT/Docker/blob/main/Backups/Photos/PiGallery_docker-compose.yml) :heavy_check_mark: -> Photo location, GPX support & file system friendly friendly (no DB required) :rocket:
* FileSharing
  * Anonupload
  * Picoshare
  * Pingvin
  * [FileBrowser](https://fossengineer.com/selfhosting-filebrowser-docker)
* Entertainment  
  * [Jellyfin](https://jalcocert.github.io/JAlcocerT/media-server-with-open-source/) :heavy_check_mark:
  * Kodi
  * Plex
  * Emby
  * Couchpotato :heavy_check_mark:
  * [Jacket](https://github.com/JAlcocerT/Docker/blob/main/Media/jacket_docker-compose.yml) :heavy_check_mark:
  * Others: Mylar3, Midarr, Readarr
  * [Calibre](https://github.com/JAlcocerT/Docker/blob/main/Media/calibre_docker-compose.yml) :heavy_check_mark:
  * P2P
    * [Transmission](https://fossengineer.com/transmission-with-vpn-torrent/) :heavy_check_mark:
    * rTorrent :heavy_check_mark:
    * [Qbittorrent](https://fossengineer.com/selfhosting-qBittorrent-with-docker-and-VPN) :heavy_check_mark:
    * Radarr :heavy_check_mark:
    * [Sonarr](https://github.com/JAlcocerT/Docker/blob/main/Media/Video/sonarr_docker-compose.yml) :heavy_check_mark:
    * Bazarr :heavy_check_mark:
    * JDownloader :heavy_check_mark:
* ArchiveBox
* [Music](https://github.com/JAlcocerT/Docker/tree/main/Media/Music)
  * [Supysonic](https://github.com/JAlcocerT/Docker/blob/main/Media/Music/supysonic_docker-compose.yml) :heavy_check_mark:
  * [Navidrome](https://github.com/JAlcocerT/Docker/blob/main/Media/Music/Navidrome_Docker-compose.yml) :heavy_check_mark: it has synergy with [youtube-dl](https://jalcocert.github.io/RPi/posts/youtube-video-download/#youtube-dl-material)

### [Security:](https://github.com/JAlcocerT/Docker/tree/main/Security)
* Authelia  
* Blocky
* [Cloudflare - Zero Trust Tunnel :page_with_curl:](https://fossengineer.com/selfhosting-cloudflared-tunnel-docker/) :heavy_check_mark:
* Crowdsec 
* DNS:
  * CoreDNS
  * [Unbound](https://jalcocert.github.io/RPi/posts/selfh-internet-better/#unbound-dns) :heavy_check_mark:
  * [Pihole :page_with_curl:](https://fossengineer.com/selfhosting-PiHole-docker/) :heavy_check_mark: 
  * PiHole + Cloudflare (DNS over HTTPs)      
  * Dynamic DNS
    * DuckDNS :heavy_check_mark:
    * No-IP  
* EndleSSH
* [Fail2ban](https://fossengineer.com/setup-fail2ban-with-docker) 
* LAN:
  * [Watchyourlan](https://fossengineer.com/selfhosting-WatchYourLAN-docker/) :heavy_check_mark:
  * [Wireshark](https://fossengineer.com/setup-wireshark-with-docker/) :heavy_check_mark:
  * Pi-Alert  
* Privacy:
  * [Whoogle :page_with_curl:](https://fossengineer.com/selfhosting-whoogle-docker/) :heavy_check_mark:
  * [SearXNG](https://jalcocert.github.io/RPi/posts/selfh-internet-better/#searxng) :heavy_check_mark:
* Proxies
  * Caddy 
  * [NGINX + SSL + DuckDNS :page_with_curl:](https://fossengineer.com/selfhosting-nginx-proxy-manager-docker/) :heavy_check_mark:
  * NGINX + SSL + Fail2ban
  * NGINX + SSL + Fail2ban + Authelia
  * Traefik
  * Traefik + failban
* VPN's
  * [Gluetun :page_with_curl:](https://fossengineer.com/using-bard-selfhosting-firefox-with-vpn-docker/)
  * [Tailscale](https://jalcocert.github.io/Linux/docs/debian/linux_vpn_setup/)
  * Headscale
  * [Wireguard and wg-easy](https://jalcocert.github.io/JAlcocerT/how-to-use-wg-easy-with-a-vps/) :heavy_check_mark:
* [Watchtower](https://fossengineer.com/setup-watchtower-with-docker/) :heavy_check_mark:
    
###  Others:
* Management:
  * [Focalboard](https://fossengineer.com/focalboard-docker/) :heavy_check_mark:
  * [Logseq](https://fossengineer.com/selfhosting-logseq/)
  * OpenProject
  * [Leantime :page_with_curl:](https://fossengineer.com/selfhosting-Leantime-docker/) :heavy_check_mark:
  * [Timtelite](https://fossengineer.com/selfhosting-timelite-free-tracking-tool-with-docker/)
  * [Trilium](https://fossengineer.com/selfhosting-Trilium-docker/) :heavy_check_mark:
* Youtube
  * MeTube :heavy_check_mark:
* [Grocy](https://github.com/JAlcocerT/Docker/tree/main/Others) :heavy_check_mark:
* [Firefox :page_with_curl:](https://fossengineer.com/using-bard-selfhosting-firefox-with-vpn-docker/)
* Libretranslate
* Design
  * Penpotapp
  * [Drawio](https://fossengineer.com/selfhosting-drawio-with-docker/)
  * Excalidraw

### [Web](https://github.com/JAlcocerT/Docker/tree/main/Web)
* [Analytics](https://github.com/JAlcocerT/Docker/tree/main/Web/Analytics)
  * [Matomo](https://github.com/JAlcocerT/Docker/blob/main/Web/Analytics/matomo_Docker-compose.yml)
  * [Plausible](https://github.com/JAlcocerT/Docker/blob/main/Web/Analytics/plausible_Docker-compose.yml)
  * [Posthog](https://github.com/JAlcocerT/Docker/blob/main/Web/Analytics/Product_analytics/posthog_docker-compose.yml)
  * [Umami](https://fossengineer.com/selfhosting-umami-with-docker/) :heavy_check_mark:
* Comment Engines
  * remark42
* [CMS](https://github.com/JAlcocerT/Docker/tree/main/Web/CMS)
  * [Wordpress :page_with_curl:](https://fossengineer.com/selfhosting-wordpress-docker/) :heavy_check_mark:
  * [Ghost :page_with_curl:](https://fossengineer.com/selfhosting-ghost-docker/)
* [Forms (HTML)](https://jalcocert.github.io/JAlcocerT/blog/dev-forms/#forms)
  * [Drupal](https://github.com/JAlcocerT/Docker/blob/main/Others/drupal_docker-compose.yml)
  * [Forms](https://github.com/JAlcocerT/Docker/tree/main/Web/Forms)
    * [OhMyForm](https://github.com/JAlcocerT/Docker/blob/main/Web/Forms/OhMyForm_Docker-compose.yml)
    * [FormBricks](https://jalcocert.github.io/JAlcocerT/blog/dev-forms/#formbricks)
* Instagram alternatives
  * [Chevereto](https://fossengineer.com/selfhosting-chevereto-docker/)
  * Pixelfed
  * Vero
* Static Web Servers
  * [Apache :page_with_curl:](https://fossengineer.com/Selfhosting-Static-Webs-with-Apache-in-Docker/) 
  * NginX
* [Subscriptions/Newsletters](https://jalcocert.github.io/JAlcocerT/blog/dev-forms/#newsletters)
   * Keila
   * Mailtrain
   * Moodle

**Legend:**
  * :heavy_check_mark: -> Self-hosting instructions available in this repository
  * :page_with_curl: -> Detailed instructions available

</details>

### AI-Gen

* [Ollama with Docker](https://fossengineer.com/selfhosting-llms-ollama/)
* [PrivateGPT with Docker](https://fossengineer.com/selfhosting-local-llms-with-privateGPT/)
* [TextGenWebUI with Docker](https://fossengineer.com/Generative-AI-LLMs-locally-with-cpu/)
* [CrewAI with Docker](https://fossengineer.com/ai-agents-crewai/)

> You can also do [**AI Projects** with a Raspberry Pi](https://jalcocert.github.io/RPi/posts/raspberry-ai-projects/).

## Powered Thanks To :heart:

* Markdown/OCI
* The fantastic community on the internet from where I've learnt the basis to put together all of this.


> [!IMPORTANT]
> Share it with someone it could help!

## :loudspeaker: Ways to Contribute 

Try it out the guide for yourself and improve or add other config files.

If you enjoy self-hosting any of the apps listed, I would **show appreciation directly to their creators**. 

Please check the specific project for more details on that.

* If any of the docker-compose files or associated tutorials was helpful and you want to show gratitude:
 * Consider leaving feedback if you found some improvement / something can be explained better
 * Support additional weekends of self-hosting tinkering to bring new services to the list

<p align="center">
  <a href="https://ko-fi.com/Z8Z1QPGUM">
    <img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="ko-fi" />
  </a>
</p>