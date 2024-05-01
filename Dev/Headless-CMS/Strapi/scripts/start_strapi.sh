#!/bin/bash

# Create Strapi app and input "y"
echo -ne "y\n" | npx create-strapi-app@latest my-project3 --quickstart


echo "JWT_SECRET=$(openssl rand -base64 32)" >> ./my-project3/.env

# Change directory
cd my-project3
npm install
npm run develop


#chmod +x scripts/start_strapi.sh