#!/usr/bin/env python3
"""
Script to test PocketBase security configuration
Tests if admin endpoints are properly blocked while regular API works
"""

import requests
import json

# Configuration
POCKETBASE_URL = "http://localhost:8080"

def test_endpoint(endpoint, expected_status, description):
    """Test an endpoint and check if it returns the expected status"""
    try:
        response = requests.get(f"{POCKETBASE_URL}{endpoint}", timeout=5)
        status = response.status_code
        
        if status == expected_status:
            print(f"✅ {description}")
            print(f"   {endpoint} → {status} (Expected: {expected_status})")
        else:
            print(f"❌ {description}")
            print(f"   {endpoint} → {status} (Expected: {expected_status})")
            if response.text:
                print(f"   Response: {response.text[:100]}...")
        
        return status == expected_status
        
    except requests.exceptions.RequestException as e:
        print(f"❌ {description}")
        print(f"   {endpoint} → Error: {e}")
        return False

def test_post_endpoint(endpoint, data, expected_status, description):
    """Test a POST endpoint"""
    try:
        response = requests.post(f"{POCKETBASE_URL}{endpoint}", json=data, timeout=5)
        status = response.status_code
        
        if status == expected_status:
            print(f"✅ {description}")
            print(f"   POST {endpoint} → {status} (Expected: {expected_status})")
        else:
            print(f"❌ {description}")
            print(f"   POST {endpoint} → {status} (Expected: {expected_status})")
            if response.text:
                print(f"   Response: {response.text[:100]}...")
        
        return status == expected_status
        
    except requests.exceptions.RequestException as e:
        print(f"❌ {description}")
        print(f"   POST {endpoint} → Error: {e}")
        return False

def main():
    print("🔒 PocketBase Security Test")
    print("=" * 50)
    
    tests_passed = 0
    total_tests = 0
    
    # Test 1: Health check should work
    total_tests += 1
    if test_endpoint("/api/health", 200, "Health check should be accessible"):
        tests_passed += 1
    
    print()
    
    # Test 2: Admin authentication should be blocked
    total_tests += 1
    if test_post_endpoint("/api/admins/auth-with-password", 
                         {"identity": "test", "password": "test"}, 
                         403, "Admin authentication should be blocked"):
        tests_passed += 1
    
    # Test 3: Collections list should be blocked
    total_tests += 1
    if test_endpoint("/api/collections", 403, "Collections list should be blocked"):
        tests_passed += 1
    
    # Test 4: Admin UI should be blocked
    total_tests += 1
    if test_endpoint("/_/", 403, "Admin UI should be blocked"):
        tests_passed += 1
    
    # Test 5: Settings should be blocked
    total_tests += 1
    if test_endpoint("/api/settings", 403, "Settings should be blocked"):
        tests_passed += 1
    
    print()
    
    # Test 6: Regular collection data access should work (if collections exist)
    total_tests += 1
    # This might return 404 if no collections exist, which is fine
    status = requests.get(f"{POCKETBASE_URL}/api/collections/users/records").status_code
    if status in [200, 404]:  # 200 if accessible, 404 if collection doesn't exist
        print(f"✅ Collection records should be accessible (or return 404 if no collection)")
        print(f"   /api/collections/users/records → {status}")
        tests_passed += 1
    else:
        print(f"❌ Collection records should be accessible")
        print(f"   /api/collections/users/records → {status}")
    
    print()
    print("=" * 50)
    print(f"🎯 Security Test Results: {tests_passed}/{total_tests} tests passed")
    
    if tests_passed == total_tests:
        print("🎉 All security tests passed! Your PocketBase is properly secured.")
    else:
        print("⚠️  Some security tests failed. Check your configuration.")
        
    print()
    print("💡 Tips:")
    print("   • If health check fails, make sure PocketBase is running")
    print("   • If admin endpoints are not blocked, check your proxy configuration")
    print("   • Regular API endpoints should still work for your applications")

if __name__ == "__main__":
    main()
