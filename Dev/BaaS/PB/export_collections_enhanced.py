#!/usr/bin/env python3
"""
Enhanced PocketBase Collection Export Script

This script exports PocketBase collection configurations to JSON format compatible
with create_json_collection.py. Supports selective export and multiple output formats.

Usage:
    python3 export_collections_enhanced.py                          # Export all collections
    python3 export_collections_enhanced.py posts user_settings      # Export specific collections
    python3 export_collections_enhanced.py --format=template        # Export as template (no IDs)
    python3 export_collections_enhanced.py --output=my_config.json  # Custom output file
    python3 export_collections_enhanced.py --list                   # List available collections
"""

import requests
import json
import os
import sys
from datetime import datetime
from dotenv import load_dotenv
from typing import Dict, List, Optional, Any

# Load environment variables from .env file
load_dotenv()

# PocketBase configuration
POCKETBASE_URL = "http://localhost:8080"
ADMIN_EMAIL = os.getenv("PB_ADMIN_EMAIL")
ADMIN_PASSWORD = os.getenv("PB_ADMIN_PASS")

class PocketBaseExporter:
    def __init__(self, base_url: str, admin_email: str, admin_password: str):
        self.base_url = base_url
        self.admin_email = admin_email
        self.admin_password = admin_password
        self.token = None
        self.collections = {}
        
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
    
    def fetch_collections(self) -> bool:
        """Fetch all collections and store them"""
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
                collections_list = collections_data.get("items", [])
                
                # Store collections by name for easy lookup
                for collection in collections_list:
                    self.collections[collection["name"]] = collection
                
                return True
            else:
                print(f"❌ Failed to fetch collections: {response.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"❌ Connection error fetching collections: {str(e)}")
            return False
    
    def list_collections(self):
        """List all available collections"""
        if not self.collections:
            print("📋 No collections found.")
            return
        
        print(f"📋 Available Collections ({len(self.collections)}):")
        print("=" * 80)
        
        # Separate system and user collections
        system_collections = []
        user_collections = []
        
        for name, collection in self.collections.items():
            if collection.get("system", False):
                system_collections.append((name, collection))
            else:
                user_collections.append((name, collection))
        
        if user_collections:
            print("👤 User Collections:")
            for name, collection in sorted(user_collections):
                col_type = collection.get("type", "unknown")
                schema_count = len(collection.get("schema", []))
                created = collection.get("created", "unknown")[:10]
                
                type_icon = "🔐" if col_type == "auth" else "📄"
                print(f"  {type_icon} {name:20} │ {col_type:8} │ {schema_count:2} fields │ {created}")
        
        if system_collections:
            print("\n🔧 System Collections:")
            for name, collection in sorted(system_collections):
                col_type = collection.get("type", "unknown")
                schema_count = len(collection.get("schema", []))
                print(f"  ⚙️  {name:20} │ {col_type:8} │ {schema_count:2} fields │ (system)")
        
        print("=" * 80)
    
    def resolve_collection_dependencies(self, collection: Dict[str, Any]) -> List[str]:
        """Determine what collections this collection depends on"""
        dependencies = []
        schema = collection.get("schema", [])
        
        for field in schema:
            if field.get("type") == "relation":
                options = field.get("options", {})
                collection_id = options.get("collectionId")
                
                if collection_id:
                    # Find collection name by ID
                    for name, coll in self.collections.items():
                        if coll["id"] == collection_id:
                            if name != collection["name"]:  # Don't include self-references
                                dependencies.append(name)
                            break
        
        return list(set(dependencies))  # Remove duplicates
    
    def convert_to_template_format(self, collection: Dict[str, Any], include_dependencies: bool = True) -> Dict[str, Any]:
        """Convert PocketBase collection to template format compatible with create_json_collection.py"""
        
        # Process schema fields
        template_schema = []
        for field in collection.get("schema", []):
            template_field = {
                "name": field["name"],
                "type": field["type"],
                "required": field.get("required", False),
                "options": field.get("options", {}).copy()
            }
            
            # Convert relation collectionId to collectionName for template
            if field["type"] == "relation" and "collectionId" in template_field["options"]:
                collection_id = template_field["options"]["collectionId"]
                
                # Find collection name by ID
                for name, coll in self.collections.items():
                    if coll["id"] == collection_id:
                        template_field["options"]["collectionName"] = name
                        del template_field["options"]["collectionId"]
                        break
            
            template_schema.append(template_field)
        
        # Build template collection
        template_collection = {
            "name": collection["name"],
            "type": collection["type"],
            "description": f"Exported from PocketBase on {datetime.now().strftime('%Y-%m-%d')}",
            "schema": template_schema,
            "listRule": collection.get("listRule", ""),
            "viewRule": collection.get("viewRule", ""),
            "createRule": collection.get("createRule", ""),
            "updateRule": collection.get("updateRule", ""),
            "deleteRule": collection.get("deleteRule", "")
        }
        
        # Add dependencies if requested
        if include_dependencies:
            dependencies = self.resolve_collection_dependencies(collection)
            template_collection["dependencies"] = dependencies
        
        return template_collection
    
    def export_collections(self, collection_names: List[str] = None, export_format: str = "full", 
                          output_file: str = None) -> Dict[str, Any]:
        """Export collections in specified format"""
        
        # Determine which collections to export
        if collection_names:
            # Validate requested collections exist
            missing = [name for name in collection_names if name not in self.collections]
            if missing:
                print(f"❌ Collections not found: {missing}")
                return None
            
            collections_to_export = {name: self.collections[name] for name in collection_names}
        else:
            # Export all non-system collections by default
            collections_to_export = {
                name: coll for name, coll in self.collections.items() 
                if not coll.get("system", False)
            }
        
        if not collections_to_export:
            print("❌ No collections to export!")
            return None
        
        print(f"📦 Exporting {len(collections_to_export)} collections...")
        
        if export_format == "template":
            # Export in template format compatible with create_json_collection.py
            exported_data = {}
            for name, collection in collections_to_export.items():
                exported_data[name] = self.convert_to_template_format(collection)
                print(f"  ✅ {name} (template format)")
            
        elif export_format == "full":
            # Export with full metadata
            exported_collections = []
            for name, collection in collections_to_export.items():
                # Add extra metadata
                enhanced_collection = collection.copy()
                enhanced_collection["export_metadata"] = {
                    "exported_at": datetime.now().isoformat(),
                    "dependencies": self.resolve_collection_dependencies(collection),
                    "field_count": len(collection.get("schema", [])),
                    "field_types": list(set([f.get("type") for f in collection.get("schema", [])]))
                }
                exported_collections.append(enhanced_collection)
                print(f"  ✅ {name} (full format)")
            
            exported_data = {
                "export_info": {
                    "timestamp": datetime.now().isoformat(),
                    "pocketbase_url": self.base_url,
                    "total_collections": len(collections_to_export),
                    "exported_by": self.admin_email,
                    "format": "full"
                },
                "collections": exported_collections
            }
        
        else:
            print(f"❌ Unknown export format: {export_format}")
            return None
        
        # Save to file if specified
        if output_file:
            if self.save_to_file(exported_data, output_file):
                print(f"✅ Exported to: {output_file}")
            else:
                print(f"❌ Failed to save to: {output_file}")
        
        return exported_data
    
    def save_to_file(self, data: Dict[str, Any], filename: str) -> bool:
        """Save data to JSON file with pretty formatting"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False, sort_keys=True)
            return True
        except Exception as e:
            print(f"❌ Error saving to {filename}: {e}")
            return False

def show_usage():
    """Show usage information"""
    print("Enhanced PocketBase Collection Export Script")
    print("=" * 50)
    print("Usage:")
    print("  python3 export_collections_enhanced.py                          # Export all collections")
    print("  python3 export_collections_enhanced.py posts user_settings      # Export specific collections")
    print("  python3 export_collections_enhanced.py --format=template        # Export as template")
    print("  python3 export_collections_enhanced.py --output=my_config.json  # Custom output file")
    print("  python3 export_collections_enhanced.py --list                   # List available collections")
    print("  python3 export_collections_enhanced.py --help                   # Show this help")
    print("\nFormats:")
    print("  full     - Complete export with metadata (default)")
    print("  template - Template format compatible with create_json_collection.py")
    print("\nExamples:")
    print("  python3 export_collections_enhanced.py --format=template --output=my_collections.json")
    print("  python3 export_collections_enhanced.py posts --format=template")
    print("  python3 export_collections_enhanced.py --list")

def parse_arguments(args: List[str]) -> Dict[str, Any]:
    """Parse command line arguments"""
    parsed = {
        "collection_names": [],
        "format": "full",
        "output_file": None,
        "list_mode": False,
        "help_mode": False
    }
    
    for arg in args:
        if arg.startswith("--format="):
            parsed["format"] = arg.split("=", 1)[1]
        elif arg.startswith("--output="):
            parsed["output_file"] = arg.split("=", 1)[1]
        elif arg == "--list":
            parsed["list_mode"] = True
        elif arg == "--help" or arg == "-h":
            parsed["help_mode"] = True
        elif not arg.startswith("--"):
            parsed["collection_names"].append(arg)
    
    return parsed

def main():
    # Check if environment variables are loaded
    if not ADMIN_EMAIL or not ADMIN_PASSWORD:
        print("❌ Missing credentials. Please check your .env file.")
        print("Required variables: PB_ADMIN_EMAIL, PB_ADMIN_PASS")
        return
    
    # Parse command line arguments
    args = parse_arguments(sys.argv[1:])
    
    if args["help_mode"]:
        show_usage()
        return
    
    print("📤 Enhanced PocketBase Collection Exporter")
    print("=" * 60)
    print(f"Target: {POCKETBASE_URL}")
    print(f"Admin: {ADMIN_EMAIL}")
    print("=" * 60)
    
    # Initialize exporter and authenticate
    exporter = PocketBaseExporter(POCKETBASE_URL, ADMIN_EMAIL, ADMIN_PASSWORD)
    
    print("🔐 Authenticating as admin...")
    if not exporter.authenticate_admin():
        print("❌ Failed to authenticate. Please check your credentials.")
        return
    
    print("✅ Authentication successful!")
    
    # Fetch collections
    print("📋 Fetching collections...")
    if not exporter.fetch_collections():
        print("❌ Failed to fetch collections.")
        return
    
    print(f"✅ Found {len(exporter.collections)} collections")
    
    # Handle list mode
    if args["list_mode"]:
        exporter.list_collections()
        return
    
    # Generate output filename if not specified
    if not args["output_file"]:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        if args["collection_names"]:
            collections_part = "_".join(args["collection_names"][:3])  # Limit filename length
            if len(args["collection_names"]) > 3:
                collections_part += f"_and_{len(args['collection_names'])-3}_more"
        else:
            collections_part = "all"
        
        args["output_file"] = f"pb_export_{collections_part}_{args['format']}_{timestamp}.json"
    
    # Export collections
    result = exporter.export_collections(
        collection_names=args["collection_names"] if args["collection_names"] else None,
        export_format=args["format"],
        output_file=args["output_file"]
    )
    
    if result:
        print(f"\n🎉 Export completed successfully!")
        print(f"📁 Output file: {args['output_file']}")
        print(f"📊 Format: {args['format']}")
        
        if args["format"] == "template":
            print(f"💡 You can now use this file with: python3 create_json_collection.py")
        
        print(f"\n🌐 Admin Panel: {POCKETBASE_URL}/_/")
    else:
        print("❌ Export failed!")

if __name__ == "__main__":
    main()
