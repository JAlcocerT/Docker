# PocketBase Collection Management Scripts

Complete guide to managing PocketBase collections with our automated scripts and Makefile targets.

## 📋 Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Makefile Commands](#makefile-commands)
- [Direct Script Usage](#direct-script-usage)
- [File Formats](#file-formats)
- [Common Workflows](#common-workflows)
- [Troubleshooting](#troubleshooting)

## 🎯 Overview

This collection management system provides:

- **JSON-driven collection creation** - Define collections in JSON, create programmatically
- **Selective export/import** - Work with specific collections or all at once
- **Multiple formats** - Full backups vs. creation-ready templates
- **Safe operations** - Confirmation prompts and dependency checking
- **Complete lifecycle** - Create, list, export, delete, recreate

## ⚡ Quick Start

```bash
# 1. Start PocketBase
make setup

# 2. Create collections from JSON definitions
make create-collections

# 3. List what was created
make list-collections

# 4. Export as template for backup
make export-template

# 5. Run Flask app
make flask-run
```

## 🛠️ Makefile Commands

### **System Management**

| Command | Description | Usage |
|---------|-------------|-------|
| `make help` | Show all available commands | `make help` |
| `make setup` | Start PocketBase with Docker | `make setup` |
| `make stop` | Stop PocketBase | `make stop` |
| `make status` | Check PocketBase status | `make status` |
| `make logs` | Show PocketBase logs | `make logs` |
| `make clean` | Clean up containers and volumes | `make clean` |
| `make reset` | Clean + setup (fresh start) | `make reset` |

### **Collection Discovery**

| Command | Description | Usage |
|---------|-------------|-------|
| `make list-collections` | List all existing collections | `make list-collections` |

**Example Output:**
```
📋 Available Collections (8):
================================================================================
👤 User Collections:
  🔐 users               │ auth     │  8 fields │ 2024-01-15
  📄 posts               │ base     │  6 fields │ 2024-01-15
  📄 user_settings       │ base     │  7 fields │ 2024-01-15
```

### **Collection Creation**

| Command | Description | Usage |
|---------|-------------|-------|
| `make create-collections` | Create all collections from JSON | `make create-collections` |
| `make create-specific` | Create specific collections | `make create-specific COLLECTIONS="posts user_settings"` |

**Examples:**
```bash
# Create all collections defined in collection_details.json
make create-collections

# Create only specific collections
make create-specific COLLECTIONS="posts"
make create-specific COLLECTIONS="posts user_settings chat_sessions"
```

### **Collection Export**

| Command | Description | Format | Usage |
|---------|-------------|--------|-------|
| `make export-all` | Export all collections with metadata | Full | `make export-all` |
| `make export-template` | Export all as creation-ready template | Template | `make export-template` |
| `make export-specific` | Export specific collections as template | Template | `make export-specific COLLECTIONS="posts"` |
| `make export-backup` | Create backup with custom filename | Full | `make export-backup OUTPUT="my_backup.json"` |
| `make backup-and-recreate` | Create both backup and template | Both | `make backup-and-recreate` |

**Examples:**
```bash
# Full backup with metadata
make export-all

# Template for recreation/migration
make export-template

# Export specific collections
make export-specific COLLECTIONS="posts user_settings"

# Custom backup filename
make export-backup OUTPUT="production_backup_$(date +%Y%m%d).json"

# Complete backup workflow
make backup-and-recreate
```

### **Collection Deletion**

| Command | Description | Safety | Usage |
|---------|-------------|--------|-------|
| `make delete-collection` | Delete with confirmation prompts | Safe | `make delete-collection COLLECTIONS="posts"` |
| `make delete-collection-force` | Delete without confirmation | Dangerous | `make delete-collection-force COLLECTIONS="test_collection"` |

**Examples:**
```bash
# Safe deletion (requires confirmation)
make delete-collection COLLECTIONS="old_collection"

# Delete multiple collections
make delete-collection COLLECTIONS="test1 test2 demo_collection"

# Force deletion (no confirmation - be careful!)
make delete-collection-force COLLECTIONS="temp_collection"
```

### **Development Workflow**

| Command | Description | Usage |
|---------|-------------|-------|
| `make dev` | Complete development setup | `make dev` |
| `make flask-deps` | Install Flask dependencies | `make flask-deps` |
| `make flask-run` | Run Flask application | `make flask-run` |

## 🔧 Direct Script Usage

### **Collection Creation: `create_json_collection.py`**

```bash
# Create all collections from collection_details.json
python3 create_json_collection.py

# Create specific collections
python3 create_json_collection.py posts user_settings

# Create single collection
python3 create_json_collection.py user_settings
```

**Features:**
- ✅ Dependency resolution (creates collections in correct order)
- ✅ Relation handling (converts collection names to IDs)
- ✅ Duplicate detection (skips existing collections)
- ✅ Detailed output (shows schema, rules, dependencies)

### **Collection Export: `export_collections_enhanced.py`**

```bash
# Export all collections (full format)
python3 export_collections_enhanced.py

# Export specific collections (full format)
python3 export_collections_enhanced.py posts user_settings

# Export as template (creation-ready)
python3 export_collections_enhanced.py --format=template

# Export with custom output file
python3 export_collections_enhanced.py --format=template --output=my_collections.json

# List available collections
python3 export_collections_enhanced.py --list
```

**Formats:**
- `--format=full` - Complete backup with metadata (default)
- `--format=template` - Creation-ready format for `create_json_collection.py`

### **Collection Deletion: `delete_collection.py`**

```bash
# Delete single collection (with confirmation)
python3 delete_collection.py posts

# Delete multiple collections
python3 delete_collection.py posts user_settings chat_sessions

# Force deletion (skip confirmation)
python3 delete_collection.py --force test_collection

# List collections before deletion
python3 delete_collection.py --list
```

**Safety Features:**
- ✅ Prevents deletion of auth collections
- ✅ Shows dependency warnings
- ✅ Requires exact name confirmation
- ✅ Detailed collection information before deletion

## 📄 File Formats

### **Template Format** (Creation-Ready)

Used by `create_json_collection.py` and `--format=template` exports:

```json
{
  "user_settings": {
    "name": "user_settings",
    "type": "base",
    "description": "User-specific settings and preferences",
    "dependencies": ["users"],
    "schema": [
      {
        "name": "user",
        "type": "relation",
        "required": true,
        "options": {
          "collectionName": "users",
          "cascadeDelete": true,
          "minSelect": 1,
          "maxSelect": 1
        }
      }
    ],
    "listRule": "@request.auth.id != '' && user = @request.auth.id",
    "viewRule": "@request.auth.id != '' && user = @request.auth.id",
    "createRule": "@request.auth.id != ''",
    "updateRule": "@request.auth.id != '' && user = @request.auth.id",
    "deleteRule": "@request.auth.id != '' && user = @request.auth.id"
  }
}
```

**Key Features:**
- Clean, portable format
- Uses `collectionName` for relations (not IDs)
- Includes `dependencies` array
- No timestamps or internal IDs
- Directly usable for recreation

### **Full Format** (Complete Backup)

Raw PocketBase format with all metadata:

```json
{
  "export_info": {
    "timestamp": "2025-08-08T09:53:41.230292",
    "pocketbase_url": "http://localhost:8080",
    "total_collections": 8,
    "exported_by": "admin@example.com"
  },
  "collections": [
    {
      "id": "_pb_users_auth_",
      "name": "users",
      "type": "auth",
      "created": "2025-08-07 12:23:51.491Z",
      "updated": "2025-08-07 12:23:51.491Z",
      "export_metadata": {
        "dependencies": [],
        "exported_at": "2025-08-08T09:53:41.230292",
        "field_count": 2,
        "field_types": ["file", "text"]
      }
    }
  ]
}
```

**Key Features:**
- Complete system backup
- All PocketBase metadata included
- Internal IDs and timestamps
- Export metadata and statistics
- Perfect for forensic analysis

## 🔄 Common Workflows

### **Development Setup**

```bash
# Fresh development environment
make reset                    # Clean slate
make create-collections       # Create collections
make flask-deps              # Install dependencies
make flask-run               # Start development
```

### **Before Major Changes**

```bash
# Create safety backup
make backup-and-recreate

# Files created:
# - backup_full_YYYYMMDD_HHMMSS.json (complete backup)
# - collection_details_backup.json (recreation template)

# Make your changes to collection_details.json
# Then recreate specific collections
make delete-collection COLLECTIONS="modified_collection"
make create-specific COLLECTIONS="modified_collection"
```

### **Migration Between Environments**

```bash
# On source environment
make export-template

# Copy exported_collections_template.json to target environment
scp exported_collections_template.json user@target:/path/to/pb/

# On target environment
cp exported_collections_template.json collection_details.json
make create-collections
```

### **Selective Collection Management**

```bash
# Work with specific collections
make export-specific COLLECTIONS="posts user_settings"
make delete-collection COLLECTIONS="old_posts old_settings"
make create-specific COLLECTIONS="new_posts new_settings"
```

### **Testing and Experimentation**

```bash
# Create test collections
make create-specific COLLECTIONS="test_collection"

# Experiment with your application...

# Clean up test collections
make delete-collection-force COLLECTIONS="test_collection"
```

### **Backup Strategies**

```bash
# Daily backup
make export-backup OUTPUT="daily_backup_$(date +%Y%m%d).json"

# Pre-deployment backup
make backup-and-recreate

# Quick template backup
make export-template
```

## 🚨 Troubleshooting

### **Authentication Issues**

```bash
# Check your .env file
cat .env

# Required variables:
PB_ADMIN_EMAIL=your-admin@example.com
PB_ADMIN_PASS=your-admin-password

# Test PocketBase connection
make status
```

### **Collection Creation Failures**

```bash
# Check dependencies
make list-collections

# Create dependencies first
make create-specific COLLECTIONS="users"
make create-specific COLLECTIONS="user_settings"

# Check collection_details.json syntax
python3 -m json.tool collection_details.json
```

### **Export Issues**

```bash
# List available collections first
make list-collections

# Try exporting specific collections
make export-specific COLLECTIONS="existing_collection"

# Check PocketBase logs
make logs
```

### **Deletion Problems**

```bash
# Check what depends on the collection
python3 delete_collection.py --list

# Delete dependent collections first
make delete-collection COLLECTIONS="dependent_collection"
make delete-collection COLLECTIONS="target_collection"
```

### **Flask App Issues**

```bash
# Install dependencies
make flask-deps

# Check PocketBase is running
make status

# Check collections exist
make list-collections

# Create required collections
make create-collections
```

## 📁 File Structure

```
PB/
├── Makefile                           # All management commands
├── collection_details.json           # Collection definitions
├── create_json_collection.py         # Creation script
├── export_collections_enhanced.py    # Export script
├── delete_collection.py              # Deletion script
├── flask_pocketbase_app.py           # Sample Flask app
├── flask_requirements.txt            # Flask dependencies
├── .env                              # Admin credentials
└── SCRIPT_USAGE.md                   # This documentation
```

## 🎯 Best Practices

### **Development**
- Always use `make backup-and-recreate` before major changes
- Use template format for version control
- Test collection changes in development first

### **Production**
- Regular backups with `make export-backup`
- Use `make export-template` for disaster recovery preparation
- Never use `delete-collection-force` in production

### **Team Collaboration**
- Share `collection_details.json` in version control
- Use template exports for environment synchronization
- Document custom collections in the JSON file

### **Security**
- Keep `.env` file secure and out of version control
- Use environment-specific admin credentials
- Regular security audits of collection rules

---

## 🎉 Summary

You now have a **complete PocketBase collection management system** with:

- ✅ **JSON-driven creation** - Define once, create anywhere
- ✅ **Safe operations** - Confirmations and dependency checking
- ✅ **Multiple formats** - Backup vs. recreation ready
- ✅ **Flexible workflows** - From development to production
- ✅ **Team-friendly** - Clear documentation and error messages

**Happy PocketBase development!** 🚀
