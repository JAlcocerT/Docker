#!/bin/bash

# Generate a secure random secret
TINYAUTH_SECRET="Sbffjht+ihEcWc60QpJUkrXfTFsq+fKt0mb+CtXyoo0="

# Generate a hashed password (replace 'your-secure-password' with your desired password)
# Note: You'll be prompted to enter the password
TINYAUTH_USERS="admin:$(openssl passwd -5)"

# Create the environment file
cat > tinyauth.env <<EOL
# TinyAuth Configuration
TINYAUTH_SECRET=${TINYAUTH_SECRET}
TINYAUTH_USERS="${TINYAUTH_USERS}"

# App URL (must match your domain)
APP_URL=https://gibme.duckdns.org
EOL

echo "Updated tinyauth.env with a new secret and password
echo "Please remember to change the password in tinyauth.env"
