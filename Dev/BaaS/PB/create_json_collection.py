#!/usr/bin/env python3
"""
JSON-driven PocketBase Collection Creator

This script reads collection definitions from collection_details.json and creates
them in PocketBase. It handles dependencies, relations, and provides detailed output.

Usage:
    python3 create_json_collection.py                    # Create all collections
    python3 create_json_collection.py user_settings      # Create specific collection
    python3 create_json_collection.py posts chat_sessions # Create multiple collections
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

class PocketBaseCollectionManager:
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
    
    def collection_exists(self, collection_name: str) -> bool:
        """Check if a collection exists"""
        return collection_name in self.existing_collections
    
    def get_collection_id(self, collection_name: str) -> Optional[str]:
        """Get collection ID by name"""
        if collection_name in self.existing_collections:
            return self.existing_collections[collection_name]["id"]
        return None
    
    def resolve_relation_collection_id(self, collection_name: str) -> Optional[str]:
        """Resolve collection name to ID for relations"""
        # Special handling for built-in collections
        if collection_name == "users":
            for name, collection in self.existing_collections.items():
                if collection.get("type") == "auth" and name == "users":
                    return collection["id"]
        
        return self.get_collection_id(collection_name)
    
    def process_schema_field(self, field: Dict[str, Any]) -> Dict[str, Any]:
        """Process a schema field, resolving relation collection IDs"""
        processed_field = field.copy()
        
        if field["type"] == "relation":
            options = field.get("options", {})
            collection_name = options.get("collectionName")
            
            if collection_name:
                collection_id = self.resolve_relation_collection_id(collection_name)
                if collection_id:
                    processed_field["options"] = options.copy()
                    processed_field["options"]["collectionId"] = collection_id
                    # Remove collectionName as it's not needed in the API
                    processed_field["options"].pop("collectionName", None)
                else:
                    raise ValueError(f"Cannot resolve collection '{collection_name}' for relation field '{field['name']}'")
        
        return processed_field
    
    def create_collection(self, collection_config: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Create a collection from configuration"""
        if not self.token:
            return None
            
        collections_url = f"{self.base_url}/api/collections"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        
        # Process the schema to resolve relations
        processed_schema = []
        for field in collection_config.get("schema", []):
            try:
                processed_field = self.process_schema_field(field)
                processed_schema.append(processed_field)
            except ValueError as e:
                print(f"❌ Schema processing error: {e}")
                return None
        
        # Build the collection payload
        collection_payload = {
            "name": collection_config["name"],
            "type": collection_config["type"],
            "schema": processed_schema,
            "listRule": collection_config.get("listRule", ""),
            "viewRule": collection_config.get("viewRule", ""),
            "createRule": collection_config.get("createRule", ""),
            "updateRule": collection_config.get("updateRule", ""),
            "deleteRule": collection_config.get("deleteRule", "")
        }
        
        try:
            response = requests.post(collections_url, json=collection_payload, headers=headers)
            
            if response.status_code == 200:
                collection = response.json()
                print(f"✅ Collection '{collection['name']}' created successfully!")
                
                # Update our local cache
                self.existing_collections[collection["name"]] = collection
                
                return collection
            else:
                print(f"❌ Failed to create collection '{collection_config['name']}': {response.status_code}")
                print(f"   Response: {response.text}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"❌ Connection error creating collection: {str(e)}")
            return None
    
    def print_collection_info(self, collection: Dict[str, Any], config: Dict[str, Any]):
        """Print detailed information about a collection"""
        print(f"\n📋 Collection Details:")
        print(f"   Name: {collection['name']}")
        print(f"   ID: {collection['id']}")
        print(f"   Type: {collection['type']}")
        print(f"   Description: {config.get('description', 'No description')}")
        
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
                if options.get('cascadeDelete'):
                    print(f"     └─ Cascade Delete: Yes")
            elif field_type == 'number':
                if 'min' in options:
                    print(f"     └─ Min Value: {options['min']}")
                if 'max' in options:
                    print(f"     └─ Max Value: {options['max']}")
            elif field_type == 'text':
                if 'min' in options:
                    print(f"     └─ Min Length: {options['min']}")
                if 'max' in options:
                    print(f"     └─ Max Length: {options['max']}")
            elif field_type == 'select':
                if 'values' in options:
                    print(f"     └─ Values: {', '.join(options['values'])}")
                if 'maxSelect' in options:
                    print(f"     └─ Max Select: {options['maxSelect']}")
            elif field_type == 'file':
                if 'maxSelect' in options:
                    print(f"     └─ Max Files: {options['maxSelect']}")
                if 'maxSize' in options:
                    size_mb = options['maxSize'] / (1024 * 1024)
                    print(f"     └─ Max Size: {size_mb:.1f} MB")
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
            rule_text = rule if rule else "❌ No access"
            print(f"   {action:8} │ {rule_text}")

def load_collection_definitions(json_file: str = "collection_details.json") -> Dict[str, Any]:
    """Load collection definitions from JSON file"""
    try:
        with open(json_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Collection definitions file '{json_file}' not found!")
        print("   Please create collection_details.json with your collection definitions.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in '{json_file}': {e}")
        sys.exit(1)

def check_dependencies(collections: Dict[str, Any], collection_name: str, manager: PocketBaseCollectionManager) -> List[str]:
    """Check if all dependencies for a collection are satisfied"""
    collection_config = collections.get(collection_name)
    if not collection_config:
        return [f"Collection '{collection_name}' not found in definitions"]
    
    missing_deps = []
    dependencies = collection_config.get("dependencies", [])
    
    for dep in dependencies:
        if not manager.collection_exists(dep):
            missing_deps.append(dep)
    
    return missing_deps

def resolve_creation_order(collections: Dict[str, Any], target_collections: List[str]) -> List[str]:
    """Resolve the order in which collections should be created based on dependencies"""
    ordered = []
    remaining = target_collections.copy()
    
    # Simple dependency resolution (assumes no circular dependencies)
    while remaining:
        progress_made = False
        
        for collection_name in remaining.copy():
            collection_config = collections.get(collection_name, {})
            dependencies = collection_config.get("dependencies", [])
            
            # Check if all dependencies are either already created or in our ordered list
            deps_satisfied = all(
                dep in ordered or dep == "users"  # users is built-in
                for dep in dependencies
            )
            
            if deps_satisfied:
                ordered.append(collection_name)
                remaining.remove(collection_name)
                progress_made = True
        
        if not progress_made and remaining:
            print(f"❌ Circular dependency detected or missing dependencies for: {remaining}")
            break
    
    return ordered

def main():
    # Check if environment variables are loaded
    if not ADMIN_EMAIL or not ADMIN_PASSWORD:
        print("❌ Missing credentials. Please check your .env file.")
        print("Required variables: PB_ADMIN_EMAIL, PB_ADMIN_PASS")
        return
    
    # Load collection definitions
    collections = load_collection_definitions()
    
    # Determine which collections to create
    if len(sys.argv) > 1:
        target_collections = sys.argv[1:]
        # Validate that all requested collections exist in definitions
        invalid_collections = [name for name in target_collections if name not in collections]
        if invalid_collections:
            print(f"❌ Unknown collections: {invalid_collections}")
            print(f"Available collections: {list(collections.keys())}")
            return
    else:
        target_collections = list(collections.keys())
    
    print("🚀 JSON-driven PocketBase Collection Creator")
    print("=" * 60)
    print(f"Target: {POCKETBASE_URL}")
    print(f"Admin: {ADMIN_EMAIL}")
    print(f"Collections to create: {', '.join(target_collections)}")
    print("=" * 60)
    
    # Initialize manager and authenticate
    manager = PocketBaseCollectionManager(POCKETBASE_URL, ADMIN_EMAIL, ADMIN_PASSWORD)
    
    print("🔐 Authenticating as admin...")
    if not manager.authenticate_admin():
        print("❌ Failed to authenticate. Please check your credentials.")
        return
    
    print("✅ Authentication successful!")
    
    # Fetch existing collections
    print("📋 Fetching existing collections...")
    if not manager.fetch_existing_collections():
        print("❌ Failed to fetch existing collections.")
        return
    
    print(f"✅ Found {len(manager.existing_collections)} existing collections")
    
    # Check which collections already exist
    existing_targets = [name for name in target_collections if manager.collection_exists(name)]
    if existing_targets:
        print(f"⚠️  Collections already exist: {existing_targets}")
        target_collections = [name for name in target_collections if name not in existing_targets]
        
        if not target_collections:
            print("✅ All requested collections already exist!")
            return
    
    # Resolve creation order based on dependencies
    print("🔗 Resolving dependencies...")
    creation_order = resolve_creation_order(collections, target_collections)
    
    if len(creation_order) != len(target_collections):
        print("❌ Could not resolve all dependencies.")
        return
    
    print(f"📝 Creation order: {' → '.join(creation_order)}")
    
    # Create collections in order
    created_collections = []
    
    for collection_name in creation_order:
        print(f"\n🏗️  Creating collection: {collection_name}")
        
        # Final dependency check
        missing_deps = check_dependencies(collections, collection_name, manager)
        if missing_deps:
            print(f"❌ Missing dependencies for '{collection_name}': {missing_deps}")
            continue
        
        collection_config = collections[collection_name]
        result = manager.create_collection(collection_config)
        
        if result:
            created_collections.append(collection_name)
            manager.print_collection_info(result, collection_config)
        else:
            print(f"❌ Failed to create collection '{collection_name}'")
            break
    
    # Summary
    print(f"\n🎉 Collection Creation Summary")
    print("=" * 40)
    print(f"✅ Successfully created: {len(created_collections)} collections")
    for name in created_collections:
        print(f"   • {name}")
    
    if len(created_collections) != len(target_collections):
        failed = set(target_collections) - set(created_collections)
        print(f"❌ Failed to create: {len(failed)} collections")
        for name in failed:
            print(f"   • {name}")
    
    print(f"\n🌐 Admin Panel: {POCKETBASE_URL}/_/")
    print(f"📚 Collection definitions: collection_details.json")

if __name__ == "__main__":
    main()
