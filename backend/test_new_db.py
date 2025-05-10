import requests
import json

BASE_URL = "http://localhost:5000"

def test_new_database():
    # 1. Test user login with sample user
    print("\n1. Testing User Login...")
    login_data = {
        "email": "john@example.com",
        "password": "password123"
    }
    try:
        response = requests.post(f"{BASE_URL}/login", json=login_data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        token = response.json().get('access_token')
    except Exception as e:
        print(f"Error: {str(e)}")
        token = None

    # 2. Test get job recommendations
    print("\n2. Testing Get Job Recommendations...")
    if token:
        headers = {'Authorization': f'Bearer {token}'}
        try:
            response = requests.post(f"{BASE_URL}/recommendation", 
                                  headers=headers,
                                  json={"firstname": "John", "lastname": "Doe"})
            print(f"Status Code: {response.status_code}")
            print(f"Number of recommended jobs: {len(response.json().get('jobs', []))}")
            print(f"Number of recommended students: {len(response.json().get('students', []))}")
        except Exception as e:
            print(f"Error: {str(e)}")

    # 3. Test get saved jobs
    print("\n3. Testing Get Saved Jobs...")
    if token:
        headers = {'Authorization': f'Bearer {token}'}
        try:
            response = requests.get(f"{BASE_URL}/get-saved-jobs", headers=headers)
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.json()}")
        except Exception as e:
            print(f"Error: {str(e)}")

    # 4. Test get account info
    print("\n4. Testing Get Account Info...")
    if token:
        headers = {'Authorization': f'Bearer {token}'}
        try:
            response = requests.get(f"{BASE_URL}/user/account", headers=headers)
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.json()}")
        except Exception as e:
            print(f"Error: {str(e)}")

    # 5. Test save a new job
    print("\n5. Testing Save New Job...")
    if token:
        headers = {'Authorization': f'Bearer {token}'}
        try:
            response = requests.post(f"{BASE_URL}/save-jobs", 
                                  headers=headers,
                                  json={"job_id": 3})
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.json()}")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_new_database() 