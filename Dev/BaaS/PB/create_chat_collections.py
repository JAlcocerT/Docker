#!/usr/bin/env python3
"""
Script to create chat-related collections for PocketBase:
- chat_sessions (if it doesn't exist)
- chat_messages (main collection)

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

def get_collection_id(token, collection_name, collection_type=None):
    """Get a collection ID by name and optionally type"""
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
                if collection_type is None or collection.get("type") == collection_type:
                    return collection.get("id")
        
        return None
    else:
        print(f"❌ Failed to fetch collections: {response.status_code} - {response.text}")
        return None

def check_collection_exists(token, collection_name):
    """Check if a collection already exists"""
    return get_collection_id(token, collection_name) is not None

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

def create_chat_sessions_collection(token, users_collection_id):
    """Create the chat_sessions collection if it doesn't exist"""
    chat_sessions_collection = {
        "name": "chat_sessions",
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
                "name": "title",
                "type": "text",
                "required": False,
                "options": {
                    "max": 200
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
                "name": "isActive",
                "type": "bool",
                "required": False,
                "options": {
                    "default": True
                }
            },
            {
                "name": "metadata",
                "type": "json",
                "required": False,
                "options": {}
            }
        ],
        # API Rules - users can only access their own sessions
        "listRule": "@request.auth.id = user.id",
        "viewRule": "@request.auth.id = user.id",
        "createRule": "@request.auth.id = @request.data.user",
        "updateRule": "@request.auth.id = user.id",
        "deleteRule": "@request.auth.id = user.id"
    }
    
    return create_collection(token, chat_sessions_collection)

def create_chat_messages_collection(token, users_collection_id, chat_sessions_collection_id):
    """Create the chat_messages collection with the specified schema"""
    chat_messages_collection = {
        "name": "chat_messages",
        "type": "base",
        "schema": [
            {
                "name": "session",
                "type": "relation",
                "required": True,
                "options": {
                    "collectionId": chat_sessions_collection_id,
                    "cascadeDelete": True,
                    "minSelect": 1,
                    "maxSelect": 1,
                    "displayFields": ["title"]
                }
            },
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
                "name": "message",
                "type": "json",
                "required": True,
                "options": {}
            },
            {
                "name": "timestamp",
                "type": "date",
                "required": True,
                "options": {}
            },
            {
                "name": "isRead",
                "type": "bool",
                "required": False,
                "options": {
                    "default": False
                }
            }
        ],
        # API Rules - users can only access their own messages
        "listRule": "@request.auth.id = user",
        "viewRule": "@request.auth.id = user",
        "createRule": "@request.auth.id = @request.data.user",
        "updateRule": "@request.auth.id = user",
        "deleteRule": "@request.auth.id = user",
        # Add indexes for better performance
        "indexes": [
            "CREATE INDEX idx_chat_messages_user ON chat_messages (user);",
            "CREATE INDEX idx_chat_messages_session ON chat_messages (session);",
            "CREATE INDEX idx_chat_messages_timestamp ON chat_messages (timestamp DESC);"
        ]
    }
    
    return create_collection(token, chat_messages_collection)

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
            if 'displayFields' in options:
                print(f"     └─ Display Fields: {options['displayFields']}")
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
    
    # Show indexes if any
    indexes = collection.get('indexes', [])
    if indexes:
        print(f"\n📊 Database Indexes:")
        for idx in indexes:
            print(f"   • {idx}")

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
    
    # Get users collection ID
    print("🔍 Finding users collection...")
    users_collection_id = get_collection_id(token, "users", "auth")
    
    if not users_collection_id:
        print("❌ Cannot create chat collections without users collection.")
        print("   Please ensure you have a users collection first.")
        return
    
    print(f"✅ Found users collection (ID: {users_collection_id})")
    
    # Check/Create chat_sessions collection
    print("🔍 Checking for chat_sessions collection...")
    chat_sessions_id = get_collection_id(token, "chat_sessions")
    
    if not chat_sessions_id:
        print("🏗️  Creating chat_sessions collection...")
        chat_sessions_collection = create_chat_sessions_collection(token, users_collection_id)
        if chat_sessions_collection:
            chat_sessions_id = chat_sessions_collection['id']
            print_collection_info(chat_sessions_collection)
        else:
            print("❌ Failed to create chat_sessions collection.")
            return
    else:
        print(f"✅ Found existing chat_sessions collection (ID: {chat_sessions_id})")
    
    # Check if chat_messages collection already exists
    print("🔍 Checking if chat_messages collection already exists...")
    if check_collection_exists(token, "chat_messages"):
        print("⚠️  Collection 'chat_messages' already exists!")
        print("   To recreate it, please delete the existing collection first.")
        return
    
    # Create the chat_messages collection
    print("🏗️  Creating chat_messages collection...")
    chat_messages_collection = create_chat_messages_collection(token, users_collection_id, chat_sessions_id)
    
    if chat_messages_collection:
        print_collection_info(chat_messages_collection)
        
        print(f"\n🎉 Chat collections setup completed!")
        print(f"📱 Collections created:")
        print(f"   • chat_sessions (for organizing conversations)")
        print(f"   • chat_messages (for storing individual messages)")
        print(f"🌐 Visit the admin panel: {POCKETBASE_URL}/_/")
        
        print(f"\n💡 Usage Tips:")
        print(f"   • Messages are automatically ordered by timestamp (newest first)")
        print(f"   • Each user can only access their own messages and sessions")
        print(f"   • The message field stores complete message objects as JSON")
        print(f"   • Use isRead field to track message read status")
        print(f"   • Consider soft delete for message history preservation")
    else:
        print("❌ Failed to create chat_messages collection.")

if __name__ == "__main__":
    main()
