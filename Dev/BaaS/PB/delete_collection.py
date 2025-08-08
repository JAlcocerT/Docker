#!/usr/bin/env python3
"""
PocketBase Collection Deletion Script

This script safely deletes collections from PocketBase by name.
It includes safety checks and confirmation prompts to prevent accidental deletions.

Usage:
    python3 delete_collection.py collection_name              # Delete single collection
    python3 delete_collection.py posts user_settings          # Delete multiple collections
    python3 delete_collection.py --force collection_name      # Skip confirmation (dangerous!)
    python3 delete_collection.py --list                       # List all collections
"""

import requests
import json
import os
import sys
from dotenv import load_dotenv
from typing import Dict, List, Optional, Any

# Load environment variables from .env file
load_dotenv()

# PocketBase configuration
POCKETBASE_URL = "http://localhost:8080"
ADMIN_EMAIL = os.getenv("PB_ADMIN_EMAIL")
ADMIN_PASSWORD = os.getenv("PB_ADMIN_PASS")

class PocketBaseCollectionDeleter:
    def __init__(self, base_url: str, admin_email: str, admin_password: str):
        self.base_url = base_url
        self.admin_email = admin_email
        self.admin_password = admin_password
        self.token = None
        self.existing_collections = {}
        
    def authenticate_admin(self) -> bool:
        """Authenticate as admin and return success status"""
        auth_url = f"{self.base_url}/api/admins/auth-with-password"
        
        auth_data = {
            "identity": self.admin_email,
            "password": self.admin_password
        }
        
        try:
            response = requests.post(auth_url, json=auth_data)
            
            if response.status_code == 200:
                auth_result = response.json()
                self.token = auth_result["token"]
                return True
            else:
                print(f"❌ Authentication failed: {response.status_code} - {response.text}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"❌ Connection error during authentication: {str(e)}")
            return False
    
    def fetch_existing_collections(self) -> bool:
        """Fetch all existing collections and store them"""
        if not self.token:
            return False
            
        collections_url = f"{self.base_url}/api/collections"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.get(collections_url, headers=headers)
            
            if response.status_code == 200:
                collections_data = response.json()
                collections = collections_data.get("items", [])
                
                # Store collections by name for easy lookup
                for collection in collections:
                    self.existing_collections[collection["name"]] = collection
                
                return True
            else:
                print(f"❌ Failed to fetch collections: {response.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"❌ Connection error fetching collections: {str(e)}")
            return False
    
    def list_collections(self):
        """List all existing collections with details"""
        if not self.existing_collections:
            print("📋 No collections found.")
            return
        
        print(f"📋 Found {len(self.existing_collections)} collections:")
        print("=" * 80)
        
        for name, collection in self.existing_collections.items():
            collection_type = collection.get("type", "unknown")
            schema_count = len(collection.get("schema", []))
            created = collection.get("created", "unknown")
            
            # Special handling for built-in collections
            if collection_type == "auth":
                type_display = "🔐 auth (built-in)"
            elif collection_type == "base":
                type_display = "📄 base"
            else:
                type_display = f"❓ {collection_type}"
            
            print(f"• {name:20} │ {type_display:15} │ {schema_count:2} fields │ {created[:10]}")
        
        print("=" * 80)
        print("💡 Use 'python3 delete_collection.py collection_name' to delete a collection")
    
    def get_collection_info(self, collection_name: str) -> Optional[Dict[str, Any]]:
        """Get detailed information about a collection"""
        return self.existing_collections.get(collection_name)
    
    def check_collection_dependencies(self, collection_name: str) -> List[str]:
        """Check if other collections depend on this collection"""
        dependencies = []
        target_collection = self.existing_collections.get(collection_name)
        
        if not target_collection:
            return dependencies
        
        target_id = target_collection["id"]
        
        # Check all other collections for relations to this collection
        for name, collection in self.existing_collections.items():
            if name == collection_name:
                continue
                
            schema = collection.get("schema", [])
            for field in schema:
                if field.get("type") == "relation":
                    options = field.get("options", {})
                    if options.get("collectionId") == target_id:
                        dependencies.append(f"{name}.{field['name']}")
        
        return dependencies
    
    def delete_collection(self, collection_name: str) -> bool:
        """Delete a collection by name"""
        if not self.token:
            return False
        
        collection = self.existing_collections.get(collection_name)
        if not collection:
            print(f"❌ Collection '{collection_name}' not found!")
            return False
        
        collection_id = collection["id"]
        delete_url = f"{self.base_url}/api/collections/{collection_id}"
        
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.delete(delete_url, headers=headers)
            
            if response.status_code == 204:
                print(f"✅ Collection '{collection_name}' deleted successfully!")
                # Remove from our local cache
                del self.existing_collections[collection_name]
                return True
            else:
                print(f"❌ Failed to delete collection '{collection_name}': {response.status_code}")
                if response.text:
                    print(f"   Response: {response.text}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"❌ Connection error deleting collection: {str(e)}")
            return False
    
    def safe_delete_collection(self, collection_name: str, force: bool = False) -> bool:
        """Safely delete a collection with checks and confirmation"""
        collection = self.get_collection_info(collection_name)
        if not collection:
            print(f"❌ Collection '{collection_name}' not found!")
            return False
        
        # Safety check: prevent deletion of built-in auth collections
        if collection.get("type") == "auth":
            print(f"🚫 Cannot delete built-in authentication collection '{collection_name}'!")
            print("   This would break user authentication.")
            return False
        
        # Check for dependencies
        dependencies = self.check_collection_dependencies(collection_name)
        if dependencies:
            print(f"⚠️  Warning: Other collections depend on '{collection_name}':")
            for dep in dependencies:
                print(f"   • {dep}")
            print("   Deleting this collection may break these relations!")
        
        # Show collection details
        schema_count = len(collection.get("schema", []))
        created = collection.get("created", "unknown")
        
        print(f"\n📋 Collection to delete:")
        print(f"   Name: {collection_name}")
        print(f"   Type: {collection.get('type', 'unknown')}")
        print(f"   Fields: {schema_count}")
        print(f"   Created: {created}")
        print(f"   ID: {collection['id']}")
        
        # Confirmation prompt (unless forced)
        if not force:
            print(f"\n⚠️  This action cannot be undone!")
            print(f"   All data in '{collection_name}' will be permanently lost.")
            
            while True:
                confirm = input(f"\nType '{collection_name}' to confirm deletion: ").strip()
                if confirm == collection_name:
                    break
                elif confirm.lower() in ['n', 'no', 'cancel', 'quit', 'exit']:
                    print("❌ Deletion cancelled.")
                    return False
                else:
                    print(f"❌ Please type '{collection_name}' exactly to confirm.")
        
        # Perform deletion
        return self.delete_collection(collection_name)

def show_usage():
    """Show usage information"""
    print("PocketBase Collection Deletion Script")
    print("=" * 40)
    print("Usage:")
    print("  python3 delete_collection.py collection_name              # Delete single collection")
    print("  python3 delete_collection.py posts user_settings          # Delete multiple collections")
    print("  python3 delete_collection.py --force collection_name      # Skip confirmation (dangerous!)")
    print("  python3 delete_collection.py --list                       # List all collections")
    print("  python3 delete_collection.py --help                       # Show this help")
    print("\nExamples:")
    print("  python3 delete_collection.py posts")
    print("  python3 delete_collection.py user_settings chat_messages")
    print("  python3 delete_collection.py --list")

def main():
    # Check if environment variables are loaded
    if not ADMIN_EMAIL or not ADMIN_PASSWORD:
        print("❌ Missing credentials. Please check your .env file.")
        print("Required variables: PB_ADMIN_EMAIL, PB_ADMIN_PASS")
        return
    
    # Parse command line arguments
    args = sys.argv[1:]
    
    if not args or "--help" in args or "-h" in args:
        show_usage()
        return
    
    # Check for special flags
    force_mode = "--force" in args
    list_mode = "--list" in args
    
    # Remove flags from collection names
    collection_names = [arg for arg in args if not arg.startswith("--")]
    
    if list_mode:
        if collection_names:
            print("⚠️  --list flag ignores collection names")
    elif not collection_names:
        print("❌ No collection names provided!")
        show_usage()
        return
    
    print("🗑️  PocketBase Collection Deletion Tool")
    print("=" * 50)
    print(f"Target: {POCKETBASE_URL}")
    print(f"Admin: {ADMIN_EMAIL}")
    if force_mode:
        print("⚠️  FORCE MODE: Skipping confirmations!")
    print("=" * 50)
    
    # Initialize deleter and authenticate
    deleter = PocketBaseCollectionDeleter(POCKETBASE_URL, ADMIN_EMAIL, ADMIN_PASSWORD)
    
    print("🔐 Authenticating as admin...")
    if not deleter.authenticate_admin():
        print("❌ Failed to authenticate. Please check your credentials.")
        return
    
    print("✅ Authentication successful!")
    
    # Fetch existing collections
    print("📋 Fetching existing collections...")
    if not deleter.fetch_existing_collections():
        print("❌ Failed to fetch existing collections.")
        return
    
    print(f"✅ Found {len(deleter.existing_collections)} existing collections")
    
    # Handle list mode
    if list_mode:
        deleter.list_collections()
        return
    
    # Delete collections
    deleted_count = 0
    failed_count = 0
    
    for collection_name in collection_names:
        print(f"\n🗑️  Processing: {collection_name}")
        
        if deleter.safe_delete_collection(collection_name, force_mode):
            deleted_count += 1
        else:
            failed_count += 1
    
    # Summary
    print(f"\n📊 Deletion Summary")
    print("=" * 30)
    print(f"✅ Successfully deleted: {deleted_count}")
    print(f"❌ Failed to delete: {failed_count}")
    
    if deleted_count > 0:
        print(f"\n🌐 Admin Panel: {POCKETBASE_URL}/_/")
        print("💡 Refresh the admin panel to see changes")

if __name__ == "__main__":
    main()
