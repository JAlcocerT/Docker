#!/bin/bash

# Create necessary directories
mkdir -p letsencrypt nginx-html duckdns

# Set proper permissions
chmod 600 letsencrypt

# Create a sample index.html for the protected site
cat > nginx-html/index.html <<EOL
<!DOCTYPE html>
<html>
<head>
    <title>Protected Site</title>
</head>
<body>
    <h1>Welcome to your protected site!</h1>
    <p>This site is secured with TinyAuth.</p>
</body>
</html>
EOL

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    # Generate a random secret for TinyAuth
    TINYAUTH_SECRET=$(openssl rand -hex 32)
    
    # Create .env file
    cat > .env <<EOL
# TinyAuth Configuration
TINYAUTH_SECRET=${TINYAUTH_SECRET}
TINYAUTH_USERS="admin:$(openssl passwd -5 your-secure-password)"  # Change the password

# DuckDNS Configuration
DUCKDNS_TOKEN=your-duckdns-token  # Replace with your DuckDNS token
DUCKDNS_DOMAIN=gibme.duckdns.org

# Email for Let's Encrypt notifications
LETSENCRYPT_EMAIL=your-email@example.com
EOL
    
    echo "Created .env file. Please edit it with your configuration."
else
    echo ".env file already exists. Skipping creation."
fi

echo "Setup complete! Next steps:"
echo "1. Edit the .env file with your configuration"
echo "2. Run: docker-compose -f TinyAuth_docker-compose.yml up -d"
echo "3. Access your site at https://gibme.duckdns.org"
