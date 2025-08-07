#!/usr/bin/env python3
"""
Flask Web App with PocketBase Authentication
Demonstrates how to integrate Flask with PocketBase for user management
"""

from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import requests
import json
import os
from datetime import datetime, timedelta
from functools import wraps
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'your-secret-key-change-this')

# PocketBase configuration
POCKETBASE_URL = "http://localhost:8080"
ADMIN_EMAIL = os.getenv("PB_ADMIN_EMAIL")
ADMIN_PASSWORD = os.getenv("PB_ADMIN_PASS")

class PocketBaseClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
    
    def authenticate_user(self, email, password):
        """Authenticate user with PocketBase"""
        try:
            response = self.session.post(
                f"{self.base_url}/api/collections/users/auth-with-password",
                json={"identity": email, "password": password}
            )
            
            if response.status_code == 200:
                data = response.json()
                return {
                    'success': True,
                    'user': data.get('record', {}),
                    'token': data.get('token', ''),
                    'expires': datetime.now() + timedelta(hours=24)
                }
            else:
                return {'success': False, 'error': 'Invalid credentials'}
                
        except requests.exceptions.RequestException as e:
            return {'success': False, 'error': f'Connection error: {str(e)}'}
    
    def register_user(self, email, password, name=None):
        """Register new user with PocketBase"""
        try:
            user_data = {
                "email": email,
                "password": password,
                "passwordConfirm": password
            }
            if name:
                user_data["name"] = name
            
            response = self.session.post(
                f"{self.base_url}/api/collections/users/records",
                json=user_data
            )
            
            if response.status_code == 200:
                return {'success': True, 'user': response.json()}
            else:
                error_data = response.json()
                return {'success': False, 'error': error_data.get('message', 'Registration failed')}
                
        except requests.exceptions.RequestException as e:
            return {'success': False, 'error': f'Connection error: {str(e)}'}
    
    def get_user_data(self, user_id, token):
        """Get user data from PocketBase"""
        try:
            headers = {'Authorization': f'Bearer {token}'}
            response = self.session.get(
                f"{self.base_url}/api/collections/users/records/{user_id}",
                headers=headers
            )
            
            if response.status_code == 200:
                return {'success': True, 'user': response.json()}
            else:
                return {'success': False, 'error': 'Failed to fetch user data'}
                
        except requests.exceptions.RequestException as e:
            return {'success': False, 'error': f'Connection error: {str(e)}'}
    
    def create_post(self, title, content, author_email, token):
        """Create a new post (requires posts collection)"""
        try:
            headers = {'Authorization': f'Bearer {token}'}
            post_data = {
                "title": title,
                "content": content,
                "author": author_email,
                "published": True
            }
            
            response = self.session.post(
                f"{self.base_url}/api/collections/posts/records",
                json=post_data,
                headers=headers
            )
            
            if response.status_code == 200:
                return {'success': True, 'post': response.json()}
            else:
                return {'success': False, 'error': 'Failed to create post'}
                
        except requests.exceptions.RequestException as e:
            return {'success': False, 'error': f'Connection error: {str(e)}'}
    
    def get_posts(self, limit=10):
        """Get published posts"""
        try:
            response = self.session.get(
                f"{self.base_url}/api/collections/posts/records",
                params={
                    'filter': 'published=true',
                    'sort': '-created',
                    'perPage': limit
                }
            )
            
            if response.status_code == 200:
                data = response.json()
                return {'success': True, 'posts': data.get('items', [])}
            else:
                return {'success': False, 'error': 'Failed to fetch posts'}
                
        except requests.exceptions.RequestException as e:
            return {'success': False, 'error': f'Connection error: {str(e)}'}

# Initialize PocketBase client
pb = PocketBaseClient(POCKETBASE_URL)

def login_required(f):
    """Decorator to require login for routes"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    """Home page showing recent posts"""
    posts_result = pb.get_posts(limit=5)
    posts = posts_result.get('posts', []) if posts_result['success'] else []
    
    return render_template('index.html', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login page"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        if not email or not password:
            flash('Please provide both email and password.', 'error')
            return render_template('login.html')
        
        # Authenticate with PocketBase
        result = pb.authenticate_user(email, password)
        
        if result['success']:
            # Store user session
            session['user_id'] = result['user']['id']
            session['user_email'] = result['user']['email']
            session['user_name'] = result['user'].get('name', email)
            session['token'] = result['token']
            session['expires'] = result['expires'].isoformat()
            
            flash(f'Welcome back, {session["user_name"]}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash(result['error'], 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration page"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        name = request.form.get('name')
        
        if not email or not password:
            flash('Please provide both email and password.', 'error')
            return render_template('register.html')
        
        if password != confirm_password:
            flash('Passwords do not match.', 'error')
            return render_template('register.html')
        
        # Register with PocketBase
        result = pb.register_user(email, password, name)
        
        if result['success']:
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash(result['error'], 'error')
    
    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    """User dashboard"""
    return render_template('dashboard.html')

@app.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    """Create a new post"""
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        if not title or not content:
            flash('Please provide both title and content.', 'error')
            return render_template('create_post.html')
        
        # Create post in PocketBase
        result = pb.create_post(
            title=title,
            content=content,
            author_email=session['user_email'],
            token=session['token']
        )
        
        if result['success']:
            flash('Post created successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash(result['error'], 'error')
    
    return render_template('create_post.html')

@app.route('/logout')
def logout():
    """User logout"""
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/api/user')
@login_required
def api_user():
    """API endpoint to get current user data"""
    return jsonify({
        'user_id': session['user_id'],
        'email': session['user_email'],
        'name': session['user_name']
    })

@app.route('/api/posts')
def api_posts():
    """API endpoint to get posts"""
    posts_result = pb.get_posts(limit=20)
    if posts_result['success']:
        return jsonify({'posts': posts_result['posts']})
    else:
        return jsonify({'error': posts_result['error']}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
