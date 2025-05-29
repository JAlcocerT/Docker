# Project YT_Groq with Traefik

This project sets up a Streamlit application for YouTube video summarization using Groq's API, with Traefik as a reverse proxy and SSL termination.

## Prerequisites

1. Docker and Docker Compose installed
2. A domain name pointing to your server (for SSL certificates)
3. Groq API key

## Setup

1. **Configure Environment Variables**
   ```bash
   # Copy the example .env file
   cp .env.example .env
   
   # Edit the .env file with your details
   nano .env
   ```

2. **Update the following variables in .env**:
   - `TRAEFIK_DOMAIN`: Your domain (e.g., `groq.yourdomain.com`)
   - `TRAEFIK_EMAIL`: Your email for Let's Encrypt
   - `GROQ_API_KEY`: Your Groq API key
   - `TRAEFIK_BASIC_AUTH`: Basic auth credentials (generated automatically)

3. **Start the services**
   ```bash
   docker-compose -f docker-compose_traefik.yml up -d
   ```

## Accessing Services

- **Your Application**: https://your-domain.com
- **Traefik Dashboard**: https://traefik.your-domain.com
  - Username: `admin`
  - Password: (check your .env file or the output of setup_env.sh)

## Ports

- `80`: HTTP traffic (automatically redirects to HTTPS)
- `443`: HTTPS traffic
- `8080`: Traefik dashboard (internal)

## Security

- All HTTP traffic is automatically redirected to HTTPS
- Basic authentication is enabled for the Traefik dashboard
- Let's Encrypt is used for automatic SSL certificate management

## Troubleshooting

Check the logs:
```bash
docker-compose -f docker-compose_traefik.yml logs -f
```

## Stopping the Services

```bash
docker-compose -f docker-compose_traefik.yml down
```

## Updating

To update the services:

```bash
docker-compose -f docker-compose_traefik.yml pull
docker-compose -f docker-compose_traefik.yml up -d --force-recreate
```
