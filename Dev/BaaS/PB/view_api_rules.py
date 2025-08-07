#!/usr/bin/env python3
"""
Script to view PocketBase API rules in a clean, readable format
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

def get_all_collections(token):
    """Get all collections"""
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

def format_rule(rule_value):
    """Format rule for better readability"""
    if rule_value == "":
        return "🌍 PUBLIC (anyone can access)"
    elif rule_value is None:
        return "🚫 DENIED (no access)"
    elif "@request.auth.id != \"\"" in rule_value:
        return f"🔐 AUTH REQUIRED: {rule_value}"
    else:
        return f"📋 CUSTOM RULE: {rule_value}"

def print_api_rules(collections):
    """Print API rules in a clean format"""
    print(f"\n🔒 PocketBase API Rules Summary")
    print(f"{'='*60}")
    
    # Filter out system collections for cleaner view
    user_collections = [c for c in collections if not c.get("system", False)]
    
    for collection in user_collections:
        name = collection["name"]
        col_type = collection["type"]
        
        print(f"\n📦 Collection: {name} ({col_type})")
        print(f"   ID: {collection['id']}")
        print(f"   {'─'*50}")
        
        rules = {
            "LIST": collection.get("listRule"),
            "VIEW": collection.get("viewRule"),
            "CREATE": collection.get("createRule"),
            "UPDATE": collection.get("updateRule"),
            "DELETE": collection.get("deleteRule")
        }
        
        for action, rule in rules.items():
            formatted_rule = format_rule(rule)
            print(f"   {action:8} │ {formatted_rule}")
        
        # Show field count
        schema = collection.get("schema", [])
        print(f"   FIELDS   │ {len(schema)} fields total")
        
        print()

def export_rules_to_json(collections, filename="api_rules_export.json"):
    """Export just the API rules to JSON"""
    rules_data = []
    
    for collection in collections:
        if collection.get("system", False):
            continue  # Skip system collections
            
        collection_rules = {
            "collection_name": collection["name"],
            "collection_id": collection["id"],
            "collection_type": collection["type"],
            "rules": {
                "listRule": collection.get("listRule"),
                "viewRule": collection.get("viewRule"),
                "createRule": collection.get("createRule"),
                "updateRule": collection.get("updateRule"),
                "deleteRule": collection.get("deleteRule")
            },
            "field_count": len(collection.get("schema", []))
        }
        
        rules_data.append(collection_rules)
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(rules_data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"❌ Error saving to {filename}: {e}")
        return False

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
    
    print("📥 Fetching collections and API rules...")
    collections = get_all_collections(token)
    
    if collections is None:
        print("❌ Failed to fetch collections.")
        return
    
    print(f"✅ Found {len(collections)} collections!")
    
    # Print rules to console
    print_api_rules(collections)
    
    # Ask if user wants to export to JSON
    print("💾 Export API rules to JSON file? (y/n): ", end="")
    try:
        choice = input().lower().strip()
        if choice in ['y', 'yes']:
            filename = "pocketbase_api_rules.json"
            if export_rules_to_json(collections, filename):
                print(f"✅ API rules exported to {filename}")
            else:
                print("❌ Failed to export API rules.")
    except KeyboardInterrupt:
        print("\n👋 Export skipped.")
    
    print(f"\n🎉 API rules review completed!")

if __name__ == "__main__":
    main()
