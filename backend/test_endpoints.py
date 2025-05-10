import requests
import json

BASE_URL = "http://localhost:5000"

def test_endpoints():
    # 1. Test user registration
    print("\n1. Testing User Registration...")
    register_data = {
        "fullname": "Test User",
        "firstname": "Test",
        "lastname": "User",
        "email": "test@example.com",
        "password": "test123",
        "password2": "test123",
        "resume": "Experienced software engineer with Python and web development skills.",
        "education": json.dumps([{"degree": "BS", "field": "Computer Science"}]),
        "workExperience": json.dumps([{"employerName": "Tech Corp", "position": "Software Engineer"}]),
        "skills": json.dumps(["Python", "Web Development", "JavaScript"])
    }
    try:
        response = requests.post(f"{BASE_URL}/", json=register_data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {str(e)}")

    # 2. Test user login
    print("\n2. Testing User Login...")
    login_data = {
        "email": "test@example.com",
        "password": "test123"
    }
    try:
        response = requests.post(f"{BASE_URL}/login", json=login_data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        token = response.json().get('access_token')
    except Exception as e:
        print(f"Error: {str(e)}")
        token = None

    # 3. Test get job recommendations (requires authentication)
    print("\n3. Testing Get Job Recommendations...")
    if token:
        headers = {'Authorization': f'Bearer {token}'}
        try:
            response = requests.post(f"{BASE_URL}/recommendation", 
                                  headers=headers,
                                  json={"firstname": "Test", "lastname": "User"})
            print(f"Status Code: {response.status_code}")
            print(f"Number of recommended jobs: {len(response.json().get('jobs', []))}")
            print(f"Number of recommended students: {len(response.json().get('students', []))}")
        except Exception as e:
            print(f"Error: {str(e)}")

    # 4. Test save job (requires authentication)
    print("\n4. Testing Save Job...")
    if token:
        headers = {'Authorization': f'Bearer {token}'}
        try:
            response = requests.post(f"{BASE_URL}/save-jobs", 
                                  headers=headers,
                                  json={"job_id": 1})
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.json()}")
        except Exception as e:
            print(f"Error: {str(e)}")

    # 5. Test get saved jobs (requires authentication)
    print("\n5. Testing Get Saved Jobs...")
    if token:
        headers = {'Authorization': f'Bearer {token}'}
        try:
            response = requests.get(f"{BASE_URL}/get-saved-jobs", headers=headers)
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.json()}")
        except Exception as e:
            print(f"Error: {str(e)}")

    # 6. Test get account info (requires authentication)
    print("\n6. Testing Get Account Info...")
    if token:
        headers = {'Authorization': f'Bearer {token}'}
        try:
            response = requests.get(f"{BASE_URL}/user/account", headers=headers)
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.json()}")
        except Exception as e:
            print(f"Error: {str(e)}")

    # 7. Test logout (requires authentication)
    print("\n7. Testing Logout...")
    if token:
        headers = {'Authorization': f'Bearer {token}'}
        try:
            response = requests.post(f"{BASE_URL}/logout", headers=headers)
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.json()}")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_endpoints() 