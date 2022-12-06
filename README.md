Public repo that serves as a pillar for self-hosting pourposes, a companion for:
* Github Page built on: <https://jalcocert.github.io/RPi/#Prerequisites>
* The Linux GH page: <https://github.com/JAlcocerT/Linux>

This document is done in markdown [(try it! :black_nib:).](https://github.com/JAlcocerT/Docker/edit/main/README.md)

### Intro: Why Docker?

Docker is a tool designed to make it easier to create, deploy, and run applications by using containers.

Containers allow us to package up an application with all of the parts it needs to work properly -  such as libraries and other dependencies, and deploy it as one package.
By doing this, the application will run on any other Linux machine (also windows or ios) regardless of any customized settings that machine might have that could differ from the machine used for writing and testing the code.

Containers remain lightweight by sharing the OS they run on while isolating processes within user space.
 
Everything needed to run a software application successfully can be stored in a container to make development and deployment more efficient. For this reason, containers are perfect for running microservices.


## Repo's Content Structure:

* Backups:
    * Duplicati :heavy_check_mark:
    * Duplicity
    * Urbackup
    * Filerun
      * Ubuntu :heavy_check_mark:
      * RPI :heavy_check_mark:
    * Nextcloud
      * Ubuntu :heavy_check_mark:
      * RPI :heavy_check_mark:
      * Recommended apps: cospend (moneybuster android)
    * Photos: 
      * LibrePhotos
      * Lychee 
      * Photonix
      * Photoprism
      * Photoview :heavy_check_mark: -> file system friendly
      * Piwigo
    * RClone :heavy_check_mark:
    * RSync
    * RSnapshot
    * Samba :heavy_check_mark:
    * Seafile
    * Syncthing :heavy_check_mark:
    * Webdav
    
* Business:
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
* Communication:
   * Chats:
       * Discourse 
       * Jitsi
       * Matrix with synapse :heavy_check_mark:
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
    
* IoT:
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
    * Uptime Kuma :heavy_check_mark:
    * Flame :heavy_check_mark:   
    * Homer
    
* Media
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
      * Qbittorrent :heavy_check_mark:
      * Radarr :heavy_check_mark:
      * Sonarr :heavy_check_mark:
      * Bazar :heavy_check_mark:
    * ArchiveBox
    * Music
      * Ampache
      * Supysonic :heavy_check_mark:
      * Navidrome :heavy_check_mark:
    * Mumble

* Security:
    * Cloudflare - zero trust tunnel :heavy_check_mark:
    * Blocky
    * CoreDNS
    * Unbound :heavy_check_mark:
    * Watchyourlan :heavy_check_mark:
    * Wireshark :heavy_check_mark:
    * Whoogle :heavy_check_mark:
    * SearX :heavy_check_mark:
    * Proxies
      * Caddy 
      * NGINX + SSL :heavy_check_mark:
      * NGINX + SSL + Fail2ban
      * NGINX + SSL + Fail2ban + Authelia
      * NGINX + SSL + Fail2ban + Authelia + DuckDNS
      * Traefik
      * Traefik + failban
    * VPN's
      * Gluetun
      * OpenVPN
      * Tailscale
      * Wirehole
      * Wireguard :heavy_check_mark:
      * Windscribe
    * Authelia   
    * Crowdsec 
    * Fail2ban 
    * EndleSSH
    * Pihole :heavy_check_mark:
    * PiHole + Cloudflare (DNS over HTTPs)
    * Pi-Alert
    * Watchtower :heavy_check_mark:
    
*  Others:
    * Management:
      * Bookstack
      * Drawio
      * Focalboard :heavy_check_mark:
      * Joplin (x86 only)
      * Kanboard :heavy_check_mark:
      * OpenProject (Asana alternative)
      * Personal management system
      * Trilium :heavy_check_mark:
      * Wecan (Kanban board)
    * Youtube
      * MeTube :heavy_check_mark:
    * Grocy :heavy_check_mark:
    * Tiddlywiki
    * Dev
      * VSCode
      * Gitea
      * SnippetBox :heavy_check_mark:
    * Firefox
    * Webtops

* Web
    * Analytics
       * Matomo
       * Plausible
       * Posthog
       * Umami :heavy_check_mark:
    * Dynamic DNS
       * DuckDNS :heavy_check_mark:
       * No-IP
    * CMS/Sites
      * Bludit
      * HUGO 
      * Wordpress Ubuntu single site :heavy_check_mark:
      * Wordpress Ubuntu multi site
      * Wordpress RPi single site :heavy_check_mark:
      * Wordpress RPi single sites X NginX --> multi sites
      * Wix
      * Ghost
    * Forms (HTML)
      * Alpaca
      * Drupal
      * OhMyForm
    * Instagram alternatives
      * Chevereto
      * Pixelfed
      * Vero
    * Static Web Server
      * Apache
      * NginX
    * Subscriptions
      * Keila
      * Mailtrain
    * Moodle
 * Dev
    * Gitea :heavy_check_mark:
    * Python apps
    * Shiny dashboards
