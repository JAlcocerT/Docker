# Docker and Self-Hosting Setup Guides

A pillar for self-hosting pourposes and anyone starting their journey with Docker, a companion for:

* My RPi guide: <https://jalcocert.github.io/RPi/#Prerequisites>
* My Linux guide: <https://github.com/JAlcocerT/Linux>
* The [self-hosting](https://fossengineer.com/tags/self-hosting/) and [docker](https://fossengineer.com/tags/docker/) entries in my blog <https://fossengineer.com/>.
  * [Install Portainer and get ready to deploy docker containers with a UI.](https://fossengineer.com/selfhosting-portainer-docker/)

## Repository Structure:
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
By doing this, the application will run on any other Linux machine (also windows or ios) regardless of any customized settings that machine might have that could differ from the machine used for writing and testing the code.

Containers remain lightweight by sharing the OS they run on while isolating processes within user space.
 
Everything needed to run a software application successfully can be stored in a container to make development and deployment more efficient. For this reason, containers are perfect for running microservices.

## Docker and your favourite Apps

I have been collecting the config files to install with Docker several Apps and consolidated it on this repository for anyone that might find it helpful.

<details>
  <summary>Click to know which Apps</summary>
  &nbsp;

### [Backups:](https://github.com/JAlcocerT/Docker/tree/main/Backups)
  * Duplicati :heavy_check_mark:
  * Duplicity
  * Urbackup
  * Filerun
    * Ubuntu :heavy_check_mark:
    * RPI :heavy_check_mark:
  * Nextcloud
    * Ubuntu :heavy_check_mark:
    * [RPI](https://jalcocert.github.io/RPi/projects/nextcloud_with_rpi/) :heavy_check_mark:
    * Recommended apps: cospend (moneybuster android)
  * Photos: 
    * LibrePhotos
    * Lychee 
    * Photonix
    * Photoprism
    * [Photoview :page_with_curl:](https://fossengineer.com/selfhosting-Photoview-docker/) :heavy_check_mark: -> file system friendly
    * Piwigo
  * RClone :heavy_check_mark:
  * RSync
  * RSnapshot
  * Samba :heavy_check_mark:
  * Seafile
  * Syncthing :heavy_check_mark:
    
### [Business:](https://github.com/JAlcocerT/Docker/tree/main/Business)
   * ERPs:
      * ERPNext
      * Dolibarr :heavy_check_mark:
      * Odoo (ex- OpenERP) :heavy_check_mark:
    * Invoicing:
      * Crater Invoices
      * Invoice Ninja
      * Solid Invoice (x86 only)
    * Management:
       * Vikunja :heavy_check_mark:
       * Leantime (x86 & ARM, :heavy_check_mark:)
### [Communication:](https://github.com/JAlcocerT/Docker/tree/main/Communication)
   * Chats:
       * Discourse 
       * Jitsi
       * [Matrix with Synapse :page_with_curl:](https://fossengineer.com/selfhosting-matrix-synapse-docker/) :heavy_check_mark:
       * Revolt
       * RocketChat
   * Mail:
       * iRedMail
       * Mailcow
       * Mailinabox
       * Mailserver
       * Mailu (rspamd)
       * Poste
       * Postfix
   * FreshRSS :heavy_check_mark:
### [Dev](https://github.com/JAlcocerT/Docker/tree/main/Dev)
* Gitea :heavy_check_mark:
* [Python DASH Apps :page_with_curl:](https://fossengineer.com/dash-docker-gcr/)
* Shiny Dashboards 
* VSCode
* Gitbucket
* OneDev #includes kanban board
* SnippetBox :heavy_check_mark:   
### [IoT:](https://github.com/JAlcocerT/Docker/tree/main/IoT)
* Automations:
  * Domoticz
  * Home Assistant :heavy_check_mark:
  * Home Bridge
  * OpenHab
* Internet speed tracker :heavy_check_mark:
* OpenSpeedTest :heavy_check_mark:
* GPIO
* Dashboards:
  * cAdvisor :heavy_check_mark: 
  * NetData :heavy_check_mark:
  * Grafana with Prometheus (internet speed) :heavy_check_mark:
  * Grafana with Prometheus (internet + device with node exporter)
  * Grafana with Graphite StatsD
  * Grafana with InfluxDB (Temperature measuring)
  * Grafana with Proxmox and InfluxDB
  * Grafana with Proxmox and Graphite
  * Grafana with Node-Red
  * EFK stack for logs(Elastic search, Fluentd, Kibana)
  * ELK stack (ES, Logstash, Kibana)
  * Redash
  * GOtify
  * Ntfy (notify)
  * [Uptime Kuma :page_with_curl:](https://fossengineer.com/selfhosting-uptime-Kuma-docker/) :heavy_check_mark:
  * Flame :heavy_check_mark:   
  * Homer
    
### [Media](https://github.com/JAlcocerT/Docker/tree/main/Media)
* E-Books/Podcasts
  * Calibre :heavy_check_mark:
  * Kavita
  * Koodo reader
  * Audiobookshelf :heavy_check_mark:
  * Podgrab :heavy_check_mark:
* Photos: 
  * PiGallery :heavy_check_mark: -> Photo location, GPX support & file system friendly friendly (no DB required) :rocket:
* Entertainment  
  * Jellyfin :heavy_check_mark:
  * Kodi
  * Plex
  * Emby
  * Couchpotato :heavy_check_mark:
  * Jacket :heavy_check_mark:
  * Mylar3
  * Midarr      
  * Calibre :heavy_check_mark:
  * Readarr
  * P2P
    * Transmission :heavy_check_mark:
    * rTorrent :heavy_check_mark:
    * [Qbittorrent]() :heavy_check_mark:
    * Radarr :heavy_check_mark:
    * Sonarr :heavy_check_mark:
    * Bazar :heavy_check_mark:
* ArchiveBox
* Music
  * Ampache
  * Supysonic :heavy_check_mark:
  * Navidrome :heavy_check_mark:
* Mumble

### [Security:](https://github.com/JAlcocerT/Docker/tree/main/Security)
* Authelia  
* Blocky
* [Cloudflare - Zero Trust Tunnel :page_with_curl:](https://fossengineer.com/selfhosting-cloudflared-tunnel-docker/) :heavy_check_mark:
* Crowdsec 
* DNS:
  * CoreDNS
  * Unbound :heavy_check_mark:
  * [Pihole :page_with_curl:](https://fossengineer.com/selfhosting-PiHole-docker/) :heavy_check_mark: 
  * PiHole + Cloudflare (DNS over HTTPs)      
* EndleSSH
* Fail2ban 
* LAN:
  * Watchyourlan :heavy_check_mark:
  * Wireshark :heavy_check_mark:
  * Pi-Alert  
* Privacy:
  * [Whoogle :page_with_curl:](https://fossengineer.com/selfhosting-whoogle-docker/) :heavy_check_mark:
  * SearX :heavy_check_mark:
* Proxies
  * Caddy 
  * [NGINX + SSL :page_with_curl:](https://fossengineer.com/selfhosting-nginx-proxy-manager-docker/) :heavy_check_mark:
  * NGINX + SSL + Fail2ban
  * NGINX + SSL + Fail2ban + Authelia
  * NGINX + SSL + Fail2ban + Authelia + DuckDNS
  * Traefik
  * Traefik + failban
* VPN's
  * [Gluetun :page_with_curl:](https://fossengineer.com/using-bard-selfhosting-firefox-with-vpn-docker/)
  * OpenVPN
  * Tailscale
  * Wirehole
  * Wireguard :heavy_check_mark:
  * Windscribe 
* Watchtower :heavy_check_mark:
    
###  Others:
* Management:
  * Bookstack
  * Focalboard :heavy_check_mark:
  * Joplin (x86 only)
  * Kanboard :heavy_check_mark:
  * Logseq
  * OpenProject (Asana alternative)
  * [Leantime :page_with_curl:](https://fossengineer.com/selfhosting-Leantime-docker/) :heavy_check_mark:
  * Personal management system
  * Trilium :heavy_check_mark:
  * Tiddlywiki
  * Wecan (Kanban board)
* Youtube
  * MeTube :heavy_check_mark:
* Grocy :heavy_check_mark:
* [Firefox :page_with_curl:](https://fossengineer.com/using-bard-selfhosting-firefox-with-vpn-docker/)
* [WebTops](https://fossengineer.com/selfhosting-webtops-with-docker/)
* Libretranslate
* Design
  * Penpotapp
  * Drawio


### [Web](https://github.com/JAlcocerT/Docker/tree/main/Web)
* Analytics
  * Matomo
  * Plausible
  * Posthog
  * Umami :heavy_check_mark:
* Comment Engine
  * remark42
  * Isso
  * Giscus
* Dynamic DNS
  * DuckDNS :heavy_check_mark:
  * No-IP
* CMS/Sites
  * Bludit
  * [HUGO :page_with_curl:](https://fossengineer.com/web-guide-Hugo/) 
  * [Wordpress :page_with_curl:](https://fossengineer.com/selfhosting-wordpress-docker/) :heavy_check_mark:
  * [Ghost :page_with_curl:](https://fossengineer.com/selfhosting-ghost-docker/)
* Forms (HTML)
  * Alpaca
  * Drupal
  * OhMyForm
* Instagram alternatives
  * Chevereto
  * Pixelfed
  * Vero
* Static Web Server
  * [Apache :page_with_curl:](https://fossengineer.com/Selfhosting-Static-Webs-with-Apache-in-Docker/) 
  * NginX
* Subscriptions
   * Keila
   * Mailtrain
   * Moodle

**Legend:**
  * :heavy_check_mark: -> Self-hosting instructions available in this repository
  * :page_with_curl: -> Detailed instructions available in my blog: <https://fossengineer.com/>

</details>

## Powered Thanks To :heart:

* Markdown
* The fantastic community on the internet from where I learn all of this.

## :loudspeaker: Ways to Contribute 

Please feel free to fork the repository - try it out the guide for yourself and improve or add other config files.

If you enjoy self-hosting any of the apps listed, I would show appreciation directly to their creators. Please check the specific project for more details on that.

* If any of the docker-compose files or associated tutorials was helpful and you want to show gratitude:
 * Consider leaving feedback if you found some improvement / something can be explained better
 * Support additional weekends of self-hosting tinkering to bring new services to the list

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/FossEngineer)
