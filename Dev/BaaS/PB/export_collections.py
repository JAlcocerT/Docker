#!/usr/bin/env python3
"""
Script to export all PocketBase collections and their API rules to JSON
Make sure PocketBase is running on localhost:8080
"""

import requests
import json
import os
from datetime import datetime
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

def get_all_collections(token):
    """Get all collections with their full schema and rules"""
    collections_url = f"{POCKETBASE_URL}/api/collections"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    response = requests.get(collections_url, headers=headers)
    
    if response.status_code == 200:
        collections_data = response.json()
        return collections_data.get("items", [])
    else:
        print(f"❌ Failed to fetch collections: {response.status_code} - {response.text}")
        return None

def format_collection_data(collections):
    """Format collection data for better readability"""
    formatted_collections = []
    
    for collection in collections:
        formatted_collection = {
            "id": collection.get("id"),
            "name": collection.get("name"),
            "type": collection.get("type"),
            "system": collection.get("system", False),
            "schema": collection.get("schema", []),
            "indexes": collection.get("indexes", []),
            "listRule": collection.get("listRule"),
            "viewRule": collection.get("viewRule"),
            "createRule": collection.get("createRule"),
            "updateRule": collection.get("updateRule"),
            "deleteRule": collection.get("deleteRule"),
            "options": collection.get("options", {}),
            "created": collection.get("created"),
            "updated": collection.get("updated")
        }
        
        # Add field count and types summary
        schema = collection.get("schema", [])
        formatted_collection["field_summary"] = {
            "total_fields": len(schema),
            "field_types": list(set([field.get("type") for field in schema])),
            "required_fields": [field.get("name") for field in schema if field.get("required", False)]
        }
        
        # Add rules summary
        rules = {
            "listRule": collection.get("listRule"),
            "viewRule": collection.get("viewRule"),
            "createRule": collection.get("createRule"),
            "updateRule": collection.get("updateRule"),
            "deleteRule": collection.get("deleteRule")
        }
        
        # Categorize rules
        public_rules = []
        auth_required_rules = []
        custom_rules = []
        
        for rule_name, rule_value in rules.items():
            if rule_value == "":
                public_rules.append(rule_name)
            elif rule_value and "@request.auth.id" in rule_value:
                auth_required_rules.append(rule_name)
            elif rule_value:
                custom_rules.append(rule_name)
        
        formatted_collection["rules_summary"] = {
            "public_access": public_rules,
            "auth_required": auth_required_rules,
            "custom_rules": custom_rules
        }
        
        formatted_collections.append(formatted_collection)
    
    return formatted_collections

def save_to_json(data, filename):
    """Save data to JSON file with pretty formatting"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"❌ Error saving to {filename}: {e}")
        return False

def print_collections_summary(collections):
    """Print a summary of collections to console"""
    print(f"\n📊 Collections Summary:")
    print(f"{'='*50}")
    
    system_collections = [c for c in collections if c.get("system", False)]
    user_collections = [c for c in collections if not c.get("system", False)]
    
    print(f"Total Collections: {len(collections)}")
    print(f"  - System Collections: {len(system_collections)}")
    print(f"  - User Collections: {len(user_collections)}")
    
    print(f"\n📝 User Collections:")
    for collection in user_collections:
        name = collection["name"]
        col_type = collection["type"]
        field_count = collection["field_summary"]["total_fields"]
        field_types = ", ".join(collection["field_summary"]["field_types"])
        
        print(f"  • {name} ({col_type})")
        print(f"    Fields: {field_count} ({field_types})")
        
        # Show rules summary
        rules = collection["rules_summary"]
        if rules["public_access"]:
            print(f"    Public: {', '.join(rules['public_access'])}")
        if rules["auth_required"]:
            print(f"    Auth Required: {', '.join(rules['auth_required'])}")
        if rules["custom_rules"]:
            print(f"    Custom Rules: {', '.join(rules['custom_rules'])}")
        print()

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
    
    print("📥 Fetching all collections...")
    collections = get_all_collections(token)
    
    if collections is None:
        print("❌ Failed to fetch collections.")
        return
    
    print(f"✅ Found {len(collections)} collections!")
    
    # Format the data
    formatted_collections = format_collection_data(collections)
    
    # Create export data with metadata
    export_data = {
        "export_info": {
            "timestamp": datetime.now().isoformat(),
            "pocketbase_url": POCKETBASE_URL,
            "total_collections": len(collections),
            "exported_by": ADMIN_EMAIL
        },
        "collections": formatted_collections
    }
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"pocketbase_collections_export_{timestamp}.json"
    
    print(f"💾 Saving to {filename}...")
    if save_to_json(export_data, filename):
        print(f"✅ Export saved successfully to {filename}")
    else:
        print("❌ Failed to save export file.")
        return
    
    # Also save a simplified version (collections only)
    simple_filename = f"pocketbase_collections_simple_{timestamp}.json"
    print(f"💾 Saving simplified version to {simple_filename}...")
    if save_to_json(formatted_collections, simple_filename):
        print(f"✅ Simplified export saved to {simple_filename}")
    
    # Print summary to console
    print_collections_summary(formatted_collections)
    
    print(f"\n🎉 Export completed!")
    print(f"📁 Files created:")
    print(f"  - {filename} (full export with metadata)")
    print(f"  - {simple_filename} (collections only)")

if __name__ == "__main__":
    main()
