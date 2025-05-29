#!/bin/bash

# Generate random secrets
echo "Generating Authelia secrets..."

# JWT Secret
openssl rand -base64 32 > ./jwt

# Session Secret
openssl rand -base64 32 > ./session

# Storage Encryption Key
openssl rand -base64 32 > ./encryption

# Reset Password JWT Secret
openssl rand -base64 32 > ./jwt_reset

# Set proper permissions
chmod 600 ./jwt ./session ./encryption ./jwt_reset

echo "Secrets generated successfully!"
echo "Please make sure to back up these files in a secure location."
