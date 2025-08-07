#!/usr/bin/env python3
"""
Script to create the user_settings collection for PocketBase
This collection is required for the frontend refactor to function correctly.
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

def get_users_collection_id(token):
    """Get the users collection ID to create the relation"""
    collections_url = f"{POCKETBASE_URL}/api/collections"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    response = requests.get(collections_url, headers=headers)
    
    if response.status_code == 200:
        collections_data = response.json()
        collections = collections_data.get("items", [])
        
        # Find the users collection
        for collection in collections:
            if collection.get("name") == "users" and collection.get("type") == "auth":
                return collection.get("id")
        
        print("❌ Users collection not found. Make sure you have a users collection.")
        return None
    else:
        print(f"❌ Failed to fetch collections: {response.status_code} - {response.text}")
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
        collections = collections_data.get("items", [])
        
        for collection in collections:
            if collection.get("name") == collection_name:
                return True
        return False
    else:
        return False

def create_user_settings_collection(token, users_collection_id):
    """Create the user_settings collection with the specified schema"""
    collections_url = f"{POCKETBASE_URL}/api/collections"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    # Define the user_settings collection schema
    user_settings_collection = {
        "name": "user_settings",
        "type": "base",
        "schema": [
            {
                "name": "user",
                "type": "relation",
                "required": True,
                "options": {
                    "collectionId": users_collection_id,
                    "cascadeDelete": True,
                    "minSelect": 1,
                    "maxSelect": 1,
                    "displayFields": ["email"]
                }
            },
            {
                "name": "documentsNumber",
                "type": "number",
                "required": False,
                "options": {
                    "min": 0
                }
            },
            {
                "name": "modelType",
                "type": "text",
                "required": False,
                "options": {
                    "max": 100
                }
            },
            {
                "name": "strictMode",
                "type": "bool",
                "required": False,
                "options": {
                    "default": False
                }
            },
            {
                "name": "storedResources",
                "type": "json",
                "required": False,
                "options": {}
            },
            {
                "name": "storedRolePrompts",
                "type": "json",
                "required": False,
                "options": {}
            }
        ],
        # API Rules - ensure users can only access their own settings
        "listRule": "@request.auth.id = user.id",
        "viewRule": "@request.auth.id = user.id", 
        "createRule": "@request.auth.id = @request.data.user",
        "updateRule": "@request.auth.id = user.id",
        "deleteRule": "@request.auth.id = user.id"
    }
    
    response = requests.post(collections_url, json=user_settings_collection, headers=headers)
    
    if response.status_code == 200:
        collection = response.json()
        print(f"✅ Collection '{collection['name']}' created successfully!")
        return collection
    else:
        print(f"❌ Failed to create collection: {response.status_code} - {response.text}")
        return None

def print_collection_info(collection):
    """Print detailed information about the created collection"""
    print(f"\n📋 Collection Details:")
    print(f"   Name: {collection['name']}")
    print(f"   ID: {collection['id']}")
    print(f"   Type: {collection['type']}")
    
    print(f"\n🏗️  Schema Fields:")
    for field in collection['schema']:
        field_name = field['name']
        field_type = field['type']
        required = "✅ Required" if field.get('required', False) else "⚪ Optional"
        
        print(f"   • {field_name} ({field_type}) - {required}")
        
        # Show specific options for each field type
        options = field.get('options', {})
        if field_type == 'relation':
            print(f"     └─ Collection ID: {options.get('collectionId')}")
            print(f"     └─ Max Select: {options.get('maxSelect', 1)}")
        elif field_type == 'number' and 'min' in options:
            print(f"     └─ Min Value: {options['min']}")
        elif field_type == 'text' and 'max' in options:
            print(f"     └─ Max Length: {options['max']}")
        elif field_type == 'bool' and 'default' in options:
            print(f"     └─ Default: {options['default']}")
    
    print(f"\n🔒 API Rules:")
    rules = [
        ("LIST", collection.get('listRule')),
        ("VIEW", collection.get('viewRule')),
        ("CREATE", collection.get('createRule')),
        ("UPDATE", collection.get('updateRule')),
        ("DELETE", collection.get('deleteRule'))
    ]
    
    for action, rule in rules:
        print(f"   {action:8} │ {rule}")

def main():
    # Check if environment variables are loaded
    if not ADMIN_EMAIL or not ADMIN_PASSWORD:
        print("❌ Missing credentials. Please check your .env file.")
        print("Required variables: PB_ADMIN_EMAIL, PB_ADMIN_PASS")
        return
    
    print(f"🔐 Authenticating as admin ({ADMIN_EMAIL})...")
    token = authenticate_admin()
    
    if not token:
        print("❌ Failed to authenticate. Please check your credentials.")
        return
    
    print("✅ Authentication successful!")
    
    # Check if user_settings collection already exists
    print("🔍 Checking if user_settings collection already exists...")
    if check_collection_exists(token, "user_settings"):
        print("⚠️  Collection 'user_settings' already exists!")
        print("   To recreate it, please delete the existing collection first.")
        return
    
    # Get users collection ID
    print("🔍 Finding users collection...")
    users_collection_id = get_users_collection_id(token)
    
    if not users_collection_id:
        print("❌ Cannot create user_settings without users collection.")
        print("   Please ensure you have a users collection first.")
        return
    
    print(f"✅ Found users collection (ID: {users_collection_id})")
    
    # Create the user_settings collection
    print("🏗️  Creating user_settings collection...")
    collection = create_user_settings_collection(token, users_collection_id)
    
    if collection:
        print_collection_info(collection)
        
        print(f"\n🎉 user_settings collection created successfully!")
        print(f"📱 You can now use this collection in your frontend application.")
        print(f"🌐 Visit the admin panel: {POCKETBASE_URL}/_/")
        
        print(f"\n💡 Usage Tips:")
        print(f"   • Each user can only access their own settings")
        print(f"   • The 'user' field links to the users collection")
        print(f"   • JSON fields can store complex data structures")
        print(f"   • All fields except 'user' are optional")
    else:
        print("❌ Failed to create user_settings collection.")

if __name__ == "__main__":
    main()
