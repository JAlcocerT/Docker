#!/bin/bash

# Create the traefik_public network if it doesn't exist
if ! docker network ls | grep -q traefik_public; then
    echo "Creating traefik_public network..."
    docker network create traefik_public
fi

# Generate random secrets if they don't exist
if [ ! -f .env ]; then
    echo "Generating environment variables..."
    cp zitadel.env .env
    
    # Generate secure random strings
    sed -i "s/ZITADEL_MASTERKEY=.*/ZITADEL_MASTERKEY=$(openssl rand -base64 32)/" .env
    sed -i "s/ZITADEL_MACHINE_KEY=.*/ZITADEL_MACHINE_KEY=$(openssl rand -base64 32)/" .env
    
    echo "Generated .env file with random secrets"
    echo "Please review and edit the .env file if needed"
fi

# Start Zitadel
echo "Starting Zitadel..."
docker-compose -f Zitadel_Docker-compose.yml --env-file .env up -d

echo "\nZitadel is starting up..."
echo "\nAccess the Zitadel Console at: https://${ZITADEL_DOMAIN:-zitadel.localhost}"
echo "Admin username: ${ZITADEL_ADMIN_USERNAME:-admin}"
echo "Admin password: ${ZITADEL_ADMIN_PASSWORD:-ChangeThisPassword123!}"
echo "\nTo check the logs: docker-compose -f Zitadel_Docker-compose.yml logs -f"
