# Flask + PocketBase Integration Guide

This guide demonstrates the powerful combination of **Flask** (Python web framework) and **PocketBase** (backend-as-a-service) for rapid web application development.

## 🚀 What You Can Build with Python + PocketBase

### **Web Applications:**
- **User Authentication Systems** - Login, registration, session management
- **Content Management Systems** - Blogs, news sites, documentation
- **Social Platforms** - Forums, comment systems, user profiles
- **E-commerce Sites** - Product catalogs, shopping carts, order management
- **Dashboard Applications** - Analytics, admin panels, monitoring tools
- **API Services** - RESTful APIs, microservices, data processing

### **Real-World Examples:**
- **Blog Platform** (like our demo) - Users create accounts and publish posts
- **Task Management** - Teams collaborate on projects with real-time updates
- **Customer Support** - Ticket systems with user authentication
- **Learning Management** - Course platforms with user progress tracking
- **Inventory Systems** - Stock management with user roles and permissions

## 🏗️ Architecture Overview

```
┌─────────────────┐    HTTP/JSON    ┌─────────────────┐
│                 │ ──────────────> │                 │
│   Flask App     │                 │   PocketBase    │
│   (Frontend)    │ <────────────── │   (Backend)     │
│                 │    API Calls    │                 │
└─────────────────┘                 └─────────────────┘
│                                   │
├─ User Interface                   ├─ User Management
├─ Session Management               ├─ Data Storage
├─ Form Handling                    ├─ Authentication
├─ Template Rendering               ├─ File Storage
└─ Business Logic                   └─ Real-time APIs
```

## 📁 Project Structure

```
flask-pocketbase-app/
├── flask_pocketbase_app.py      # Main Flask application
├── flask_requirements.txt       # Python dependencies
├── .env                         # Environment variables
├── templates/                   # HTML templates
│   ├── base.html               # Base template
│   ├── index.html              # Home page
│   ├── login.html              # Login form
│   ├── register.html           # Registration form
│   ├── dashboard.html          # User dashboard
│   └── create_post.html        # Post creation
└── static/                     # CSS, JS, images (optional)
```

## 🛠️ Setup Instructions

### 1. **Start PocketBase**

```bash
# Make sure PocketBase is running
docker compose -f PB_docker-compose.yml up -d

# Verify it's working
curl -s http://localhost:8080/api/health
```

### 2. **Install Flask Dependencies**

```bash
# Install Python packages
pip install -r flask_requirements.txt

# Or install individually
pip install Flask requests python-dotenv
```

### 3. **Configure Environment**

```bash
# Make sure your .env file has:
PB_ADMIN_EMAIL=your-admin@example.com
PB_ADMIN_PASS=your-admin-password
FLASK_SECRET_KEY=your-secret-key-for-sessions
```

### 4. **Create Required Collections**

```bash
# Create the posts collection (required for the demo)
python3 create_collection.py
```

### 5. **Run the Flask App**

```bash
# Start the Flask development server
python3 flask_pocketbase_app.py

# App will be available at: http://localhost:5000
```

## 🔧 Key Features Demonstrated

### **1. User Authentication**
- **Registration**: Create new user accounts in PocketBase
- **Login**: Authenticate users and create Flask sessions
- **Session Management**: Maintain user state across requests
- **Logout**: Clear sessions and redirect users

### **2. Data Operations**
- **Create**: Add new posts to PocketBase collections
- **Read**: Fetch and display posts from PocketBase
- **Update**: Modify existing records (can be extended)
- **Delete**: Remove records (can be extended)

### **3. API Integration**
- **RESTful Calls**: HTTP requests to PocketBase API
- **Error Handling**: Graceful handling of API failures
- **Token Management**: JWT token handling for authenticated requests
- **JSON Processing**: Parse and format API responses

### **4. Web Interface**
- **Responsive Design**: Bootstrap-based UI that works on all devices
- **Form Validation**: Client and server-side validation
- **Flash Messages**: User feedback for actions
- **Live Updates**: Real-time status checks and previews

## 🎯 Advanced Use Cases

### **1. Real-Time Chat Application**

```python
# Use PocketBase realtime subscriptions
import asyncio
import websockets

class ChatApp:
    def __init__(self):
        self.pb_client = PocketBaseClient("http://localhost:8080")
    
    async def listen_for_messages(self):
        # Subscribe to chat_messages collection
        # Update UI when new messages arrive
        pass
```

### **2. File Upload System**

```python
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    
    # Upload to PocketBase
    files = {'file': (file.filename, file.stream, file.content_type)}
    response = requests.post(
        f"{POCKETBASE_URL}/api/files",
        files=files,
        headers={'Authorization': f'Bearer {session["token"]}'}
    )
    
    return jsonify(response.json())
```

### **3. Admin Dashboard**

```python
@app.route('/admin')
@admin_required
def admin_dashboard():
    # Get admin token
    admin_token = authenticate_admin()
    
    # Fetch collections, users, system stats
    collections = get_collections(admin_token)
    users = get_users(admin_token)
    
    return render_template('admin.html', 
                         collections=collections, 
                         users=users)
```

### **4. API Endpoints**

```python
@app.route('/api/posts', methods=['GET'])
def api_get_posts():
    posts = pb.get_posts(limit=request.args.get('limit', 10))
    return jsonify(posts)

@app.route('/api/posts', methods=['POST'])
@login_required
def api_create_post():
    data = request.get_json()
    result = pb.create_post(
        title=data['title'],
        content=data['content'],
        author_email=session['user_email'],
        token=session['token']
    )
    return jsonify(result)
```

## 🔒 Security Best Practices

### **1. Environment Variables**

```python
# Never hardcode sensitive data
SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
PB_URL = os.getenv('POCKETBASE_URL', 'http://localhost:8080')
```

### **2. Input Validation**

```python
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class PostForm(FlaskForm):
    title = StringField('Title', [validators.Length(min=1, max=200)])
    content = TextAreaField('Content', [validators.Length(min=10)])
```

### **3. CSRF Protection**

```python
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect(app)
```

### **4. Rate Limiting**

```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.route('/api/posts', methods=['POST'])
@limiter.limit("5 per minute")
def create_post():
    # Limited to 5 posts per minute
    pass
```

## 🚀 Deployment Options

### **1. Docker Deployment**

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY flask_requirements.txt .
RUN pip install -r flask_requirements.txt

COPY . .
EXPOSE 5000

CMD ["python", "flask_pocketbase_app.py"]
```

### **2. Production WSGI**

```python
# wsgi.py
from flask_pocketbase_app import app

if __name__ == "__main__":
    app.run()
```

```bash
# Run with Gunicorn
pip install gunicorn
gunicorn --bind 0.0.0.0:5000 wsgi:app
```

### **3. Nginx + Gunicorn**

```nginx
server {
    listen 80;
    server_name your-domain.com;
    
    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## 📊 Performance Tips

### **1. Connection Pooling**
```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class OptimizedPocketBaseClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        
        # Configure retries and connection pooling
        retry_strategy = Retry(total=3, backoff_factor=1)
        adapter = HTTPAdapter(max_retries=retry_strategy, pool_connections=20)
        
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
```

### **2. Caching**
```python
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/posts')
@cache.cached(timeout=300)  # Cache for 5 minutes
def get_posts():
    return pb.get_posts()
```

### **3. Background Tasks**
```python
from celery import Celery

celery = Celery('flask_app')

@celery.task
def send_email_notification(user_id, post_id):
    # Send email in background
    pass

@app.route('/create_post', methods=['POST'])
def create_post():
    # Create post
    result = pb.create_post(...)
    
    # Queue background task
    send_email_notification.delay(user_id, post_id)
    
    return result
```

## 🎉 Why This Combination Works

### **Flask Strengths:**
- **Flexible**: Minimal framework, easy to customize
- **Python Ecosystem**: Access to thousands of libraries
- **Template Engine**: Jinja2 for dynamic HTML
- **Development Speed**: Rapid prototyping and iteration

### **PocketBase Strengths:**
- **No Backend Code**: Focus on frontend logic
- **Built-in Auth**: User management out of the box
- **Real-time**: WebSocket support for live updates
- **File Storage**: Handle uploads without complexity
- **Admin UI**: Manage data without custom admin panels

### **Together They Provide:**
- **Rapid Development**: Get from idea to working app quickly
- **Scalability**: Both can handle growing user bases
- **Maintainability**: Clean separation of concerns
- **Cost Effective**: Minimal infrastructure requirements

## 🚀 Getting Started

1. **Clone or create the files** from this guide
2. **Start PocketBase** with your docker-compose
3. **Install Flask dependencies** with pip
4. **Create the required collections** with our scripts
5. **Run the Flask app** and start building!

This combination gives you a powerful, modern web application stack that's perfect for MVPs, prototypes, and production applications alike! 🎯
