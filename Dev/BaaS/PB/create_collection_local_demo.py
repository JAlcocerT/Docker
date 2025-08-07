#!/usr/bin/env python3
"""
Script to create demo collections on your LOCAL PocketBase instance
This is a safe way to test collection creation with demo data
Uses your existing .env credentials
"""

import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# PocketBase configuration - using your local instance
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
    # Check if environment variables are loaded
    if not ADMIN_EMAIL or not ADMIN_PASSWORD:
        print("❌ Missing credentials. Please check your .env file.")
        print("Required variables: PB_ADMIN_EMAIL, PB_ADMIN_PASS")
        return
    
    print("🚀 PocketBase Local Demo Collection Creator")
    print("=" * 50)
    print(f"Local URL: {POCKETBASE_URL}")
    print(f"Admin Email: {ADMIN_EMAIL}")
    print("=" * 50)
    
    # Authenticate as admin
    print(f"🔐 Authenticating as admin...")
    token = authenticate_admin()
    
    if not token:
        print("❌ Failed to authenticate. Make sure your local PocketBase is running.")
        print("💡 Run: docker compose -f PB_docker-compose.yml up -d")
        return
    
    print("✅ Authentication successful!")
    
    # Get existing collections
    print("📋 Checking existing collections...")
    existing_collections = get_existing_collections(token)
    print(f"Found {len(existing_collections)} existing collections: {', '.join(existing_collections)}")
    
    # Demo collection 1: Task Management
    demo_tasks_name = "demo_tasks"
    if demo_tasks_name not in existing_collections:
        print(f"🏗️  Creating '{demo_tasks_name}' collection...")
        
        demo_tasks_collection = {
            "name": demo_tasks_name,
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
                    "name": "description",
                    "type": "text",
                    "required": False,
                    "options": {
                        "max": 1000
                    }
                },
                {
                    "name": "status",
                    "type": "select",
                    "required": True,
                    "options": {
                        "maxSelect": 1,
                        "values": ["todo", "in_progress", "done", "cancelled"]
                    }
                },
                {
                    "name": "priority",
                    "type": "select",
                    "required": False,
                    "options": {
                        "maxSelect": 1,
                        "values": ["low", "medium", "high", "urgent"]
                    }
                },
                {
                    "name": "due_date",
                    "type": "date",
                    "required": False
                },
                {
                    "name": "completed",
                    "type": "bool",
                    "required": False,
                    "options": {
                        "default": False
                    }
                }
            ],
            "listRule": "",  # Public read access
            "viewRule": "",  # Public read access
            "createRule": "",  # Anyone can create
            "updateRule": "",  # Anyone can update
            "deleteRule": ""   # Anyone can delete
        }
        
        create_collection(token, demo_tasks_collection)
    else:
        print(f"⚠️  Collection '{demo_tasks_name}' already exists, skipping...")
    
    # Demo collection 2: Simple Events
    demo_events_name = "demo_events"
    if demo_events_name not in existing_collections:
        print(f"🏗️  Creating '{demo_events_name}' collection...")
        
        demo_events_collection = {
            "name": demo_events_name,
            "type": "base",
            "schema": [
                {
                    "name": "title",
                    "type": "text",
                    "required": True,
                    "options": {
                        "min": 1,
                        "max": 150
                    }
                },
                {
                    "name": "description",
                    "type": "editor",
                    "required": False
                },
                {
                    "name": "start_date",
                    "type": "date",
                    "required": True
                },
                {
                    "name": "end_date",
                    "type": "date",
                    "required": False
                },
                {
                    "name": "location",
                    "type": "text",
                    "required": False,
                    "options": {
                        "max": 200
                    }
                },
                {
                    "name": "category",
                    "type": "select",
                    "required": False,
                    "options": {
                        "maxSelect": 1,
                        "values": ["meeting", "conference", "workshop", "social", "other"]
                    }
                },
                {
                    "name": "max_attendees",
                    "type": "number",
                    "required": False,
                    "options": {
                        "min": 1
                    }
                },
                {
                    "name": "is_public",
                    "type": "bool",
                    "required": False,
                    "options": {
                        "default": True
                    }
                }
            ],
            "listRule": "is_public = true",  # Only show public events
            "viewRule": "is_public = true",  # Only view public events
            "createRule": "",  # Anyone can create
            "updateRule": "",  # Anyone can update
            "deleteRule": ""   # Anyone can delete
        }
        
        create_collection(token, demo_events_collection)
    else:
        print(f"⚠️  Collection '{demo_events_name}' already exists, skipping...")
    
    # Demo collection 3: Simple Notes
    demo_notes_name = "demo_notes"
    if demo_notes_name not in existing_collections:
        print(f"🏗️  Creating '{demo_notes_name}' collection...")
        
        demo_notes_collection = {
            "name": demo_notes_name,
            "type": "base",
            "schema": [
                {
                    "name": "title",
                    "type": "text",
                    "required": True,
                    "options": {
                        "min": 1,
                        "max": 100
                    }
                },
                {
                    "name": "content",
                    "type": "editor",
                    "required": True
                },
                {
                    "name": "tags",
                    "type": "select",
                    "required": False,
                    "options": {
                        "maxSelect": 5,
                        "values": ["personal", "work", "idea", "reminder", "important"]
                    }
                },
                {
                    "name": "color",
                    "type": "select",
                    "required": False,
                    "options": {
                        "maxSelect": 1,
                        "values": ["yellow", "blue", "green", "red", "purple", "orange"]
                    }
                },
                {
                    "name": "pinned",
                    "type": "bool",
                    "required": False,
                    "options": {
                        "default": False
                    }
                },
                {
                    "name": "archived",
                    "type": "bool",
                    "required": False,
                    "options": {
                        "default": False
                    }
                }
            ],
            "listRule": "archived != true",  # Don't show archived notes
            "viewRule": "",  # Anyone can view
            "createRule": "",  # Anyone can create
            "updateRule": "",  # Anyone can update
            "deleteRule": ""   # Anyone can delete
        }
        
        create_collection(token, demo_notes_collection)
    else:
        print(f"⚠️  Collection '{demo_notes_name}' already exists, skipping...")
    
    print(f"\n🎉 Local demo collections setup completed!")
    print(f"🌐 Visit your local admin panel: {POCKETBASE_URL}/_/")
    print(f"📱 You can now test these collections in your local environment")
    
    print(f"\n💡 Demo Collections Created:")
    print(f"   • {demo_tasks_name} - Task management with status and priority")
    print(f"   • {demo_events_name} - Event scheduling with public/private visibility")
    print(f"   • {demo_notes_name} - Note-taking with tags and organization")
    
    print(f"\n🔧 These collections demonstrate:")
    print(f"   • Different field types (text, editor, select, date, bool, number)")
    print(f"   • Validation rules (min/max lengths, required fields)")
    print(f"   • Access control (public read, filtered lists)")
    print(f"   • Real-world use cases")

if __name__ == "__main__":
    main()
