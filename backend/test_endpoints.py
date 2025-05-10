import requests
import json
import time

BASE_URL = "http://127.0.0.1:5000"

def wait_for_server():
    max_retries = 5
    retry_delay = 2
    
    for i in range(max_retries):
        try:
            response = requests.get(f"{BASE_URL}/")
            if response.status_code == 200:
                print("Server is running!")
                return True
        except requests.exceptions.ConnectionError:
            print(f"Waiting for server to start... (attempt {i+1}/{max_retries})")
            time.sleep(retry_delay)
    
    print("Server is not responding. Please make sure the Flask server is running.")
    return False

def test_register():
    print("\n=== Testing Register Endpoint ===")
    register_data = {
        "fullname": "Test User",
        "firstname": "Test",
        "lastname": "User",
        "email": "testuser@example.com",
        "password": "test123",
        "password2": "test123",
        "resume": "Experienced software developer with Python and React skills",
        "education": json.dumps([{
            "degree": "MS",
            "field": "Computer Science",
            "university": "Test University",
            "graduation_year": 2024
        }]),
        "workExperience": json.dumps([{
            "company": "Test Corp",
            "position": "Software Engineer",
            "duration": "3 years",
            "description": "Full-stack development"
        }]),
        "skills": json.dumps(["Python", "React", "Node.js", "MongoDB"])
    }
    
    try:
        response = requests.post(f"{BASE_URL}/", json=register_data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.json()
    except Exception as e:
        print(f"Error in register test: {str(e)}")
        return None

def test_login():
    print("\n=== Testing Login Endpoint ===")
    login_data = {
        "email": "testuser@example.com",
        "password": "test123"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/login", json=login_data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.json()
    except Exception as e:
        print(f"Error in login test: {str(e)}")
        return None

def test_recommendations(access_token):
    print("\n=== Testing Recommendations Endpoint ===")
    headers = {"Authorization": f"Bearer {access_token}"}
    data = {
        "firstname": "Test",
        "lastname": "User"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/recommendation", 
                               headers=headers,
                               json=data)
        print(f"Status Code: {response.status_code}")
        print(f"Number of recommended jobs: {len(response.json().get('jobs', []))}")
        return response.json()
    except Exception as e:
        print(f"Error in recommendations test: {str(e)}")
        return None

def test_save_job(access_token):
    print("\n=== Testing Save Job Endpoint ===")
    headers = {"Authorization": f"Bearer {access_token}"}
    data = {"job_id": 1}  # Save Google job
    
    try:
        response = requests.post(f"{BASE_URL}/save-jobs", 
                               headers=headers,
                               json=data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.json()
    except Exception as e:
        print(f"Error in save job test: {str(e)}")
        return None

def test_get_saved_jobs(access_token):
    print("\n=== Testing Get Saved Jobs Endpoint ===")
    headers = {"Authorization": f"Bearer {access_token}"}
    
    try:
        response = requests.get(f"{BASE_URL}/get-saved-jobs", 
                              headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Number of saved jobs: {len(response.json())}")
        return response.json()
    except Exception as e:
        print(f"Error in get saved jobs test: {str(e)}")
        return None

def test_logout(access_token):
    print("\n=== Testing Logout Endpoint ===")
    headers = {"Authorization": f"Bearer {access_token}"}
    
    try:
        response = requests.post(f"{BASE_URL}/logout", 
                               headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.json()
    except Exception as e:
        print(f"Error in logout test: {str(e)}")
        return None

def run_all_tests():
    if not wait_for_server():
        return
    
    # Test registration
    print("\n1. Testing User Registration...")
    register_response = test_register()
    
    # Test login
    print("\n2. Testing User Login...")
    login_response = test_login()
    access_token = login_response.get('access_token') if login_response else None
    
    if access_token:
        # Test recommendations
        print("\n3. Testing Get Job Recommendations...")
        recommendations = test_recommendations(access_token)
        
        # Test save job
        print("\n4. Testing Save Job...")
        save_response = test_save_job(access_token)
        
        # Test get saved jobs
        print("\n5. Testing Get Saved Jobs...")
        saved_jobs = test_get_saved_jobs(access_token)
        
        # Test logout
        print("\n6. Testing Logout...")
        logout_response = test_logout(access_token)
    else:
        print("Login failed, skipping remaining tests")

if __name__ == "__main__":
    run_all_tests() 