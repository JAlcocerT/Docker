Wrote about this at [**this post**](https://jalcocert.github.io/JAlcocerT/pocketbase-redux/)

Navigate into the directory where your `docker-compose.yaml` is located.

* Build your container: `docker build -t pb .`
* Run your container: `docker run -p 8080:8080 pb`

**Run:**

```sh
#docker compose up -d
docker compose -f PB_docker-compose.yml up -d
make setup


curl -s http://127.0.0.1:8080/api/health
```

---

# PocketBase Collection Creator

Scripts to create PocketBase collections programmatically using your existing `.env` configuration.

## Setup

1. Make sure your `.env` file contains:
   
```
PB_ADMIN_EMAIL=email@gmail.com
PB_ADMIN_PASS=pb_admin_12345@
```

2. Ensure PocketBase is running:

```bash
docker-compose -f PB_docker-compose.yml up -d
curl -s http://127.0.0.1:8080/api/health
```

## Usage

### Python Script
```bash
# Install dependencies
pip install -r requirements.txt

# Run the script
python3 create_collection.py
```

### Export Collections Script
```bash
# Export all collections and their schemas to JSON
python3 export_collections.py
```

### View API Rules Script
```bash
# View API rules in a clean format
python3 view_api_rules.py
```

### Create User Settings Collection

```bash
# Create the user_settings collection for frontend integration
python3 create_user_settings.py
```

### Create Chat Collections

```bash
# Create chat_sessions and chat_messages collections for chat functionality
python3 create_chat_collections.py
```

### Demo Scripts

```bash
# Check if PocketBase demo is healthy
curl -s https://pocketbase.io/api/health

# Try to create demo collections (may not work on public demo for security)
python3 create_collection_demo.py

# Create demo collections on your local PocketBase instance (recommended)
python3 create_collection_local_demo.py
```

### JavaScript Script

```bash
# Install dependencies
npm install

# Run the script
node create_collection.js
# or
npm run create-collections
```

### Bash Script

```bash
# Make executable (if not already)
chmod +x create_collection.sh

# Run the script
./create_collection.sh
```

## Available Scripts

### Collection Creation Scripts
Each script creates example collections with different schemas:

- **`create_collection.py`**: Creates `posts` and `categories` collections
- **`create_collection.js`**: Creates `products` and `reviews` collections (with relations)
- **`create_collection.sh`**: Creates `blog_posts` and `comments` collections

### Collection Management Scripts
- **`export_collections.py`**: Exports all collections and schemas to JSON files
- **`view_api_rules.py`**: Displays API rules in a clean, readable format
- **`create_user_settings.py`**: Creates the `user_settings` collection for frontend integration
- **`create_chat_collections.py`**: Creates `chat_sessions` and `chat_messages` collections for chat functionality

### Demo Scripts
- **`create_collection_demo.py`**: Creates demo collections on PocketBase demo instance
- **`create_collection_local_demo.py`**: Creates demo collections on your local PocketBase instance

## Collection Features Demonstrated

- Text fields with validation
- Rich text editor fields
- File upload fields
- Boolean fields
- Select/dropdown fields
- Date fields
- Relation fields (JavaScript example)
- Access rules (public read, authenticated write, etc.)

## Verification

After running any script, visit your PocketBase admin panel at: `http://localhost:8080/_/`

You should see the new collections in the Collections section.

## Customization

Edit any of the scripts to modify:
- Collection names
- Field types and validation
- Access rules
- Default values

## Field Types Available

- `text` - Text input
- `editor` - Rich text editor
- `number` - Numeric input
- `bool` - Boolean/checkbox
- `email` - Email validation
- `url` - URL validation
- `date` - Date picker
- `select` - Dropdown/multi-select
- `relation` - Link to other collections
- `file` - File upload
- `json` - JSON data
