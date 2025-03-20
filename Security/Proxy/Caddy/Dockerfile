# For prod you'd want to pin the version: e.g., 2.9.1-builder
#FROM caddy:builder AS builder
FROM caddy:2.9.1-builder AS builder 
#https://hub.docker.com/_/caddy/tags?name=builder

RUN xcaddy build \
    --with github.com/caddy-dns/cloudflare
FROM caddy:latest

COPY --from=builder /usr/bin/caddy /usr/bin/caddy