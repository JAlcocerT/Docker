#!/bin/bash

# Create .env file with default values
echo "# Traefik Configuration" > .env
echo "TRAEFIK_DOMAIN=groq.yourdomain.com" >> .env
echo "TRAEFIK_EMAIL=your-email@example.com" >> .env
echo ""
# Generate a secure password for basic auth
PASSWORD=$(openssl rand -base64 12)
HASH=$(docker run --rm httpd:2.4-alpine htpasswd -nbB admin "$PASSWORD" | cut -d ":" -f 2)
echo "# Basic Auth Credentials" >> .env
echo "# Username: admin" >> .env
echo "# Password: $PASSWORD" >> .env
echo "TRAEFIK_BASIC_AUTH=admin:${HASH}" >> .env
echo ""
# Add Groq API Key placeholder
echo "# Groq API Key" >> .env
echo "GROQ_API_KEY=your_groq_api_key_here" >> .env

# Set permissions
chmod 600 .env

# Create letsencrypt directory with proper permissions
mkdir -p letsencrypt
chmod 600 letsencrypt/acme.json

echo "\nEnvironment setup complete!"
echo "1. Edit the .env file and replace the placeholder values with your actual configuration."
echo "2. Make sure to set your GROQ_API_KEY and update TRAEFIK_DOMAIN and TRAEFIK_EMAIL."
echo "3. The Traefik dashboard will be available at: https://traefik.$(grep TRAEFIK_DOMAIN .env | cut -d '=' -f2 | cut -d '.' -f2-)"
echo "   Username: admin"
echo "   Password: $PASSWORD"
