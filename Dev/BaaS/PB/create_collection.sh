#!/bin/bash

# Script to create PocketBase collections using cURL
# Make sure PocketBase is running on localhost:8080

# Load environment variables from .env file
if [ -f ".env" ]; then
    export $(grep -v '^#' .env | xargs)
else
    echo "❌ .env file not found!"
    exit 1
fi

# Check if required variables are set
if [ -z "$PB_ADMIN_EMAIL" ] || [ -z "$PB_ADMIN_PASS" ]; then
    echo "❌ Missing required environment variables: PB_ADMIN_EMAIL, PB_ADMIN_PASS"
    exit 1
fi

POCKETBASE_URL="http://localhost:8080"
ADMIN_EMAIL="$PB_ADMIN_EMAIL"
ADMIN_PASSWORD="$PB_ADMIN_PASS"

echo "🔐 Authenticating as admin ($ADMIN_EMAIL)..."

# Authenticate and get token
AUTH_RESPONSE=$(curl -s -X POST "$POCKETBASE_URL/api/admins/auth-with-password" \
  -H "Content-Type: application/json" \
  -d "{
    \"identity\": \"$ADMIN_EMAIL\",
    \"password\": \"$ADMIN_PASSWORD\"
  }")

# Extract token from response
TOKEN=$(echo $AUTH_RESPONSE | grep -o '"token":"[^"]*' | cut -d'"' -f4)

if [ -z "$TOKEN" ]; then
    echo "❌ Authentication failed. Please check your credentials."
    echo "Response: $AUTH_RESPONSE"
    exit 1
fi

echo "✅ Authentication successful!"

# Create a "blog_posts" collection
echo "📝 Creating 'blog_posts' collection..."

BLOG_COLLECTION='{
  "name": "blog_posts",
  "type": "base",
  "schema": [
    {
      "name": "title",
      "type": "text",
      "required": true,
      "options": {
        "min": 1,
        "max": 200
      }
    },
    {
      "name": "slug",
      "type": "text",
      "required": true,
      "options": {
        "min": 1,
        "max": 200,
        "pattern": "^[a-z0-9-]+$"
      }
    },
    {
      "name": "content",
      "type": "editor",
      "required": true
    },
    {
      "name": "excerpt",
      "type": "text",
      "required": false,
      "options": {
        "max": 500
      }
    },
    {
      "name": "featured_image",
      "type": "file",
      "required": false,
      "options": {
        "maxSelect": 1,
        "maxSize": 5242880,
        "mimeTypes": ["image/jpeg", "image/png", "image/webp"]
      }
    },
    {
      "name": "published",
      "type": "bool",
      "required": false,
      "options": {
        "default": false
      }
    },
    {
      "name": "publish_date",
      "type": "date",
      "required": false
    },
    {
      "name": "tags",
      "type": "select",
      "required": false,
      "options": {
        "maxSelect": 10,
        "values": ["technology", "programming", "tutorial", "news", "review", "opinion"]
      }
    }
  ],
  "listRule": "published = true",
  "viewRule": "published = true",
  "createRule": "@request.auth.id != \"\"",
  "updateRule": "@request.auth.id != \"\"",
  "deleteRule": "@request.auth.id != \"\""
}'

BLOG_RESPONSE=$(curl -s -X POST "$POCKETBASE_URL/api/collections" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d "$BLOG_COLLECTION")

if echo "$BLOG_RESPONSE" | grep -q '"name":"blog_posts"'; then
    echo "✅ Collection 'blog_posts' created successfully!"
else
    echo "❌ Failed to create 'blog_posts' collection"
    echo "Response: $BLOG_RESPONSE"
fi

# Create a "comments" collection
echo "💬 Creating 'comments' collection..."

COMMENTS_COLLECTION='{
  "name": "comments",
  "type": "base",
  "schema": [
    {
      "name": "post_id",
      "type": "text",
      "required": true,
      "options": {
        "min": 15,
        "max": 15
      }
    },
    {
      "name": "author_name",
      "type": "text",
      "required": true,
      "options": {
        "min": 1,
        "max": 100
      }
    },
    {
      "name": "author_email",
      "type": "email",
      "required": true
    },
    {
      "name": "content",
      "type": "text",
      "required": true,
      "options": {
        "min": 1,
        "max": 1000
      }
    },
    {
      "name": "approved",
      "type": "bool",
      "required": false,
      "options": {
        "default": false
      }
    }
  ],
  "listRule": "approved = true",
  "viewRule": "approved = true",
  "createRule": "",
  "updateRule": "@request.auth.id != \"\"",
  "deleteRule": "@request.auth.id != \"\""
}'

COMMENTS_RESPONSE=$(curl -s -X POST "$POCKETBASE_URL/api/collections" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d "$COMMENTS_COLLECTION")

if echo "$COMMENTS_RESPONSE" | grep -q '"name":"comments"'; then
    echo "✅ Collection 'comments' created successfully!"
else
    echo "❌ Failed to create 'comments' collection"
    echo "Response: $COMMENTS_RESPONSE"
fi

echo ""
echo "🎉 Collection creation script completed!"
echo ""
echo "📋 To view your collections, visit: $POCKETBASE_URL/_/"
