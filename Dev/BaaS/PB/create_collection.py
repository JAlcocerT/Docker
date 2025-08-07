#!/usr/bin/env python3
"""
Script to create PocketBase collections programmatically
Make sure PocketBase is running on localhost:8080
"""

import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# PocketBase configuration
POCKETBASE_URL = "http://localhost:8080"
ADMIN_EMAIL = os.getenv("PB_ADMIN_EMAIL")
ADMIN_PASSWORD = os.getenv("PB_ADMIN_PASS")

def authenticate_admin():
    """Authenticate as admin and return the auth token"""
    auth_url = f"{POCKETBASE_URL}/api/admins/auth-with-password"
    
    auth_data = {
        "identity": ADMIN_EMAIL,
        "password": ADMIN_PASSWORD
    }
    
    response = requests.post(auth_url, json=auth_data)
    
    if response.status_code == 200:
        auth_result = response.json()
        return auth_result["token"]
    else:
        print(f"Authentication failed: {response.status_code} - {response.text}")
        return None

def create_collection(token, collection_schema):
    """Create a new collection with the given schema"""
    collections_url = f"{POCKETBASE_URL}/api/collections"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(collections_url, json=collection_schema, headers=headers)
    
    if response.status_code == 200:
        collection = response.json()
        print(f"✅ Collection '{collection['name']}' created successfully!")
        return collection
    else:
        print(f"❌ Failed to create collection: {response.status_code} - {response.text}")
        return None

def main():
    # Check if environment variables are loaded
    if not ADMIN_EMAIL or not ADMIN_PASSWORD:
        print("❌ Missing credentials. Please check your .env file.")
        print("Required variables: PB_ADMIN_EMAIL, PB_ADMIN_PASS")
        return
    
    # Authenticate as admin
    print(f"🔐 Authenticating as admin ({ADMIN_EMAIL})...")
    token = authenticate_admin()
    
    if not token:
        print("❌ Failed to authenticate. Please check your credentials.")
        return
    
    print("✅ Authentication successful!")
    
    # Example collection schema for a "posts" collection
    posts_collection = {
        "name": "posts",
        "type": "base",  # "base" for regular collections, "auth" for user collections
        "schema": [
            {
                "name": "title",
                "type": "text",
                "required": True,
                "options": {
                    "min": 1,
                    "max": 200
                }
            },
            {
                "name": "content",
                "type": "editor",  # Rich text editor
                "required": True
            },
            {
                "name": "author",
                "type": "text",
                "required": True
            },
            {
                "name": "published",
                "type": "bool",
                "required": False,
                "options": {
                    "default": False
                }
            },
            {
                "name": "tags",
                "type": "select",
                "required": False,
                "options": {
                    "maxSelect": 5,
                    "values": ["tech", "lifestyle", "tutorial", "news", "review"]
                }
            },
            {
                "name": "featured_image",
                "type": "file",
                "required": False,
                "options": {
                    "maxSelect": 1,
                    "maxSize": 5242880,  # 5MB
                    "mimeTypes": ["image/jpeg", "image/png", "image/webp"]
                }
            }
        ],
        "listRule": "",  # Public read access
        "viewRule": "",  # Public read access
        "createRule": "@request.auth.id != ''",  # Only authenticated users can create
        "updateRule": "@request.auth.id != '' && author = @request.auth.email",  # Only author can update
        "deleteRule": "@request.auth.id != '' && author = @request.auth.email"   # Only author can delete
    }
    
    # Create the posts collection
    print("📝 Creating 'posts' collection...")
    create_collection(token, posts_collection)
    
    # Example: Create a simple "categories" collection
    categories_collection = {
        "name": "categories",
        "type": "base",
        "schema": [
            {
                "name": "name",
                "type": "text",
                "required": True,
                "options": {
                    "min": 1,
                    "max": 50
                }
            },
            {
                "name": "description",
                "type": "text",
                "required": False,
                "options": {
                    "max": 500
                }
            },
            {
                "name": "color",
                "type": "text",
                "required": False,
                "options": {
                    "pattern": "^#[0-9A-Fa-f]{6}$"  # Hex color validation
                }
            }
        ],
        "listRule": "",  # Public read
        "viewRule": "",  # Public read
        "createRule": "@request.auth.id != ''",  # Authenticated users only
        "updateRule": "@request.auth.id != ''",
        "deleteRule": "@request.auth.id != ''"
    }
    
    print("📂 Creating 'categories' collection...")
    create_collection(token, categories_collection)

if __name__ == "__main__":
    main()
