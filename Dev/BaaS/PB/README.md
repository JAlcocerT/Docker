
Navigate into the directory where your docker-compose.yaml is located.

* Build your container: `docker build -t pb .`
* Run your container: `docker run -p 8080:8080 pb`

Run:

```sh
#docker compose up -d
docker compose -f PB_docker-compose.yml up -d
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
```

## Usage

### Python Script
```bash
# Install dependencies
pip install -r requirements.txt

# Run the script
python3 create_collection.py
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

## What Gets Created

Each script creates example collections with different schemas:

- **Python**: Creates `posts` and `categories` collections
- **JavaScript**: Creates `products` and `reviews` collections (with relations)
- **Bash**: Creates `blog_posts` and `comments` collections

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
