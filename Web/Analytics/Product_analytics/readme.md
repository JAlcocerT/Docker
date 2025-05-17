#### Product Analytics

https://github.com/usefathom/fathom
https://github.com/openreplay/openreplay
https://docs.openreplay.com/en/deployment/deploy-ubuntu/



https://github.com/openreplay/openreplay

Focus on what your customer wants - https://fider.io/#get-started



POSTHOG EU SERVER: https://github.com/JAlcocerT/Docker/blob/main/Web/posthog_docker-compose.md

https://github.com/posthog/posthog
https://posthog.com/docs/session-replay/installation
https://posthog.com/docs/webhooks --> slack/discord/others?


copy the js to the head section

https://www.youtube.com/watch?v=yZmDcH1_KuQ



**PRODUCT TOOLS**

1. OpenReplay

```sh
# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/openreplay/openreplay/main/scripts/docker-compose/docker-install.sh)"

wget https://raw.githubusercontent.com/openreplay/openreplay/main/scripts/docker-compose/docker-install.sh -O docker-install.sh
/bin/bash docker-install.sh
```

2. RRWeb

https://github.com/rrweb-io/rrweb

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

* https://github.com/usertour/usertour?ref=selfh.st
* https://github.com/usertour/usertour/blob/main/.env.example
* https://docs.usertour.io/open-source/self-hosting#create-a-docker-compose-yml

>  Usertour is an open-source user onboarding platform designed for developers. It allows you to create in-app product tours, checklists, and launchers in minutes—effortlessly and with full control.The open-source alternative to Userflow and Appcues 

---

## Others

1. **SerpBear** is an open-source **Search Engine Position Tracking App**. It's a tool that allows you to monitor your website's keyword rankings in Google search results.

```sh
docker-compose -f SerpBear_Docker-compose.yml up -d
```

Here's a breakdown of what SerpBear offers:

**Key Features:**

* **Unlimited Keywords & Domains:** Track an unlimited number of keywords across multiple websites.
* **SERP Tracking:** Monitors your website's position for specific keywords in Google search results.
* **Notifications:** Get email notifications about changes in your keyword positions (daily, weekly, or monthly).
* **SERP API:** Comes with a built-in API that you can use to integrate the data with other marketing and reporting tools.
* **Google Search Console Integration:** Connect with Google Search Console to see actual visits, impressions, and more data for your tracked keywords. This can help you discover new keywords and identify top-performing ones.
* **Keyword Research:** Offers the ability to research keywords and generate ideas by integrating with your Google Ads test account. You can also view monthly search volume data.
* **Export CSV:** Export your keyword data into CSV files for further analysis or reporting.
* **Mobile App (PWA):** Offers a Progressive Web App for a better mobile experience.
* **Self-Hostable:** Being open-source, you can host SerpBear on your own server (or free platforms like mogenius.com or Fly.io), giving you control over your data and potentially saving on subscription costs.
* **Scraping:** It uses third-party scrapers (like ScrapingAnt, ScrapingRobot, or your own proxies) to fetch Google search results and identify your website's ranking.

**In essence, SerpBear is a free and open-source alternative to many paid SEO rank tracking tools.** It allows you to keep an eye on your website's performance in Google for your target keywords, understand your competition, and potentially identify new opportunities.