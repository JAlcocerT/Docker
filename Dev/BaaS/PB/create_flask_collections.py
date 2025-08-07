#!/usr/bin/env python3
"""
Script to create collections specifically required for the Flask + PocketBase webapp
Creates only the essential collections needed for the demo to work
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

def check_collection_exists(token, collection_name):
    """Check if a collection already exists"""
    collections_url = f"{POCKETBASE_URL}/api/collections"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    response = requests.get(collections_url, headers=headers)
    
    if response.status_code == 200:
        collections_data = response.json()
        existing_names = [col['name'] for col in collections_data.get("items", [])]
        return collection_name in existing_names
    else:
        return False

def main():
    # Check if environment variables are loaded
    if not ADMIN_EMAIL or not ADMIN_PASSWORD:
        print("❌ Missing credentials. Please check your .env file.")
        print("Required variables: PB_ADMIN_EMAIL, PB_ADMIN_PASS")
        return
    
    print("🚀 Flask + PocketBase Collections Setup")
    print("=" * 50)
    print(f"Target: {POCKETBASE_URL}")
    print(f"Admin: {ADMIN_EMAIL}")
    print("=" * 50)
    
    # Authenticate as admin
    print("🔐 Authenticating as admin...")
    token = authenticate_admin()
    
    if not token:
        print("❌ Failed to authenticate. Please check your credentials.")
        return
    
    print("✅ Authentication successful!")
    
    # Check if posts collection already exists
    print("\n📋 Checking existing collections...")
    if check_collection_exists(token, "posts"):
        print("✅ 'posts' collection already exists!")
        print("✅ 'users' collection exists (built-in auth collection)")
        print("\n🎉 All required collections are ready!")
        print("🚀 You can now run the Flask app: python3 flask_pocketbase_app.py")
        return
    
    print("📝 Creating required collections...")
    
    # Create posts collection - minimal schema for Flask app
    posts_collection = {
        "name": "posts",
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
                "type": "editor",  # Rich text editor
                "required": True
            },
            {
                "name": "author",
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
                    "default": True  # Auto-publish for demo simplicity
                }
            }
        ],
        # API Rules - public read, authenticated write
        "listRule": "published = true",  # Only show published posts
        "viewRule": "published = true",  # Only view published posts
        "createRule": "@request.auth.id != ''",  # Only authenticated users can create
        "updateRule": "@request.auth.id != '' && author = @request.auth.email",  # Only author can update
        "deleteRule": "@request.auth.id != '' && author = @request.auth.email"   # Only author can delete
    }
    
    print("📝 Creating 'posts' collection...")
    posts_result = create_collection(token, posts_collection)
    
    if posts_result:
        print(f"\n📊 Collection Details:")
        print(f"   Name: {posts_result['name']}")
        print(f"   ID: {posts_result['id']}")
        print(f"   Fields: {len(posts_result['schema'])} fields")
        
        print(f"\n🏗️  Schema:")
        for field in posts_result['schema']:
            required = "✅ Required" if field.get('required', False) else "⚪ Optional"
            print(f"   • {field['name']} ({field['type']}) - {required}")
        
        print(f"\n🔒 Access Rules:")
        print(f"   LIST: {posts_result.get('listRule', 'No rule')}")
        print(f"   VIEW: {posts_result.get('viewRule', 'No rule')}")
        print(f"   CREATE: {posts_result.get('createRule', 'No rule')}")
        print(f"   UPDATE: {posts_result.get('updateRule', 'No rule')}")
        print(f"   DELETE: {posts_result.get('deleteRule', 'No rule')}")
        
        print(f"\n🎉 Flask webapp collections setup completed!")
        print(f"📱 Collections ready:")
        print(f"   ✅ users (built-in auth collection)")
        print(f"   ✅ posts (created successfully)")
        
        print(f"\n🚀 Next Steps:")
        print(f"   1. Install Flask dependencies: pip install -r flask_requirements.txt")
        print(f"   2. Run the Flask app: python3 flask_pocketbase_app.py")
        print(f"   3. Open http://localhost:5000 in your browser")
        print(f"   4. Register a new user and start creating posts!")
        
        print(f"\n🌐 Admin Panel: {POCKETBASE_URL}/_/")
    else:
        print("❌ Failed to create posts collection.")
        print("💡 You can create it manually in the PocketBase admin panel.")

if __name__ == "__main__":
    main()
