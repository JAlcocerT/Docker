#!/usr/bin/env python3
"""
Script to create PocketBase collections on the demo instance
Demo URL: https://pocketbase.io/demo/
Demo Credentials: test@example.com / 123456

This script demonstrates collection creation without affecting your local setup.
"""

import requests
import json
import os
# from dotenv import load_dotenv  # Commented out for demo

# Commented out for demo - using hardcoded demo credentials instead
# load_dotenv()

# PocketBase Demo configuration
# Note: Demo instance may have different endpoints or may not be available
POCKETBASE_URL = "https://pocketbase.io"
ADMIN_EMAIL = "test@example.com"  # Demo admin email
ADMIN_PASSWORD = "123456"  # Demo admin password

# Alternative: You can also test against your local instance by changing these:
# POCKETBASE_URL = "http://localhost:8080"
# ADMIN_EMAIL = os.getenv("PB_ADMIN_EMAIL", "test@example.com")
# ADMIN_PASSWORD = os.getenv("PB_ADMIN_PASS", "123456")

def check_instance_health():
    """Check if the PocketBase instance is accessible"""
    try:
        health_url = f"{POCKETBASE_URL}/api/health"
        response = requests.get(health_url, timeout=10)
        if response.status_code == 200:
            print(f"✅ PocketBase instance is healthy")
            return True
        else:
            print(f"⚠️  PocketBase health check returned: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Cannot reach PocketBase instance: {e}")
        return False

def authenticate_admin():
    """Authenticate as admin and return the auth token"""
    auth_url = f"{POCKETBASE_URL}/api/admins/auth-with-password"
    
    auth_data = {
        "identity": ADMIN_EMAIL,
        "password": ADMIN_PASSWORD
    }
    
    print(f"🌐 Connecting to PocketBase: {POCKETBASE_URL}")
    
    try:
        response = requests.post(auth_url, json=auth_data, timeout=10)
        
        if response.status_code == 200:
            auth_result = response.json()
            return auth_result["token"]
        else:
            print(f"Authentication failed: {response.status_code} - {response.text}")
            print(f"💡 Tip: Make sure the demo instance is available or try with your local instance")
            return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection error: {e}")
        print(f"💡 Tip: Check your internet connection or try with a local PocketBase instance")
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

def get_existing_collections(token):
    """Get list of existing collections to avoid duplicates"""
    collections_url = f"{POCKETBASE_URL}/api/collections"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    response = requests.get(collections_url, headers=headers)
    
    if response.status_code == 200:
        collections_data = response.json()
        return [col['name'] for col in collections_data.get("items", [])]
    else:
        print(f"❌ Failed to fetch collections: {response.status_code} - {response.text}")
        return []

def main():
    print("🚀 PocketBase Demo Collection Creator")
    print("=" * 50)
    print(f"Target URL: {POCKETBASE_URL}")
    print(f"Admin Email: {ADMIN_EMAIL}")
    print("=" * 50)
    
    # Check if instance is accessible
    print("🔍 Checking PocketBase instance...")
    if not check_instance_health():
        print("\n💡 Alternative: You can run this script against your local PocketBase:")
        print("   1. Make sure your local PocketBase is running (docker compose up)")
        print("   2. Edit this script to use: POCKETBASE_URL = 'http://localhost:8080'")
        print("   3. Use your local admin credentials")
        return
    
    # Authenticate as admin
    print(f"🔐 Authenticating as admin...")
    token = authenticate_admin()
    
    if not token:
        print("❌ Failed to authenticate with demo instance.")
        print("\n🔍 This is expected! Public demo instances typically don't allow admin operations.")
        print("\n💡 Instead, try the local demo script which works with your own PocketBase:")
        print("   python3 create_collection_local_demo.py")
        print("\n🌐 Or visit the PocketBase demo to explore existing features:")
        print("   https://pocketbase.io")
        return
    
    print("✅ Authentication successful!")
    
    # Get existing collections
    print("📋 Checking existing collections...")
    existing_collections = get_existing_collections(token)
    print(f"Found {len(existing_collections)} existing collections: {', '.join(existing_collections)}")
    
    # Demo collection 1: Simple blog posts
    demo_collection_name = "demo_blog_posts"
    if demo_collection_name not in existing_collections:
        print(f"🏗️  Creating '{demo_collection_name}' collection...")
        
        demo_blog_collection = {
            "name": demo_collection_name,
            "type": "base",
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
                    "type": "editor",
                    "required": True
                },
                {
                    "name": "author_name",
                    "type": "text",
                    "required": True,
                    "options": {
                        "min": 1,
                        "max": 100
                    }
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
                        "values": ["tech", "demo", "tutorial", "example", "test"]
                    }
                },
                {
                    "name": "view_count",
                    "type": "number",
                    "required": False,
                    "options": {
                        "min": 0,
                        "default": 0
                    }
                }
            ],
            "listRule": "published = true",  # Only show published posts
            "viewRule": "published = true",  # Only view published posts
            "createRule": "",  # Anyone can create (for demo purposes)
            "updateRule": "",  # Anyone can update (for demo purposes)
            "deleteRule": ""   # Anyone can delete (for demo purposes)
        }
        
        create_collection(token, demo_blog_collection)
    else:
        print(f"⚠️  Collection '{demo_collection_name}' already exists, skipping...")
    
    # Demo collection 2: Simple products catalog
    demo_products_name = "demo_products"
    if demo_products_name not in existing_collections:
        print(f"🏗️  Creating '{demo_products_name}' collection...")
        
        demo_products_collection = {
            "name": demo_products_name,
            "type": "base",
            "schema": [
                {
                    "name": "name",
                    "type": "text",
                    "required": True,
                    "options": {
                        "min": 1,
                        "max": 100
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
                    "name": "price",
                    "type": "number",
                    "required": True,
                    "options": {
                        "min": 0
                    }
                },
                {
                    "name": "category",
                    "type": "select",
                    "required": True,
                    "options": {
                        "maxSelect": 1,
                        "values": ["electronics", "books", "clothing", "home", "demo"]
                    }
                },
                {
                    "name": "in_stock",
                    "type": "bool",
                    "required": False,
                    "options": {
                        "default": True
                    }
                },
                {
                    "name": "rating",
                    "type": "number",
                    "required": False,
                    "options": {
                        "min": 1,
                        "max": 5
                    }
                }
            ],
            "listRule": "",  # Public read access
            "viewRule": "",  # Public read access
            "createRule": "",  # Anyone can create (for demo)
            "updateRule": "",  # Anyone can update (for demo)
            "deleteRule": ""   # Anyone can delete (for demo)
        }
        
        create_collection(token, demo_products_collection)
    else:
        print(f"⚠️  Collection '{demo_products_name}' already exists, skipping...")
    
    # Demo collection 3: Simple feedback/comments
    demo_feedback_name = "demo_feedback"
    if demo_feedback_name not in existing_collections:
        print(f"🏗️  Creating '{demo_feedback_name}' collection...")
        
        demo_feedback_collection = {
            "name": demo_feedback_name,
            "type": "base",
            "schema": [
                {
                    "name": "name",
                    "type": "text",
                    "required": True,
                    "options": {
                        "min": 1,
                        "max": 100
                    }
                },
                {
                    "name": "email",
                    "type": "email",
                    "required": True
                },
                {
                    "name": "message",
                    "type": "text",
                    "required": True,
                    "options": {
                        "min": 10,
                        "max": 1000
                    }
                },
                {
                    "name": "rating",
                    "type": "select",
                    "required": False,
                    "options": {
                        "maxSelect": 1,
                        "values": ["excellent", "good", "average", "poor", "terrible"]
                    }
                },
                {
                    "name": "approved",
                    "type": "bool",
                    "required": False,
                    "options": {
                        "default": False
                    }
                }
            ],
            "listRule": "approved = true",  # Only show approved feedback
            "viewRule": "approved = true",  # Only view approved feedback
            "createRule": "",  # Anyone can create feedback
            "updateRule": "",  # Anyone can update (for demo)
            "deleteRule": ""   # Anyone can delete (for demo)
        }
        
        create_collection(token, demo_feedback_collection)
    else:
        print(f"⚠️  Collection '{demo_feedback_name}' already exists, skipping...")
    
    print(f"\n🎉 Demo collections setup completed!")
    print(f"🌐 Visit the demo admin panel: {POCKETBASE_URL}/_/")
    print(f"📱 You can now test these collections in the demo environment")
    
    print(f"\n💡 Demo Collections Created:")
    print(f"   • {demo_collection_name} - Blog posts with publishing workflow")
    print(f"   • {demo_products_name} - Product catalog with ratings")
    print(f"   • {demo_feedback_name} - User feedback with approval system")
    
    print(f"\n⚠️  Note: Demo data is temporary and may be reset periodically!")

if __name__ == "__main__":
    main()
