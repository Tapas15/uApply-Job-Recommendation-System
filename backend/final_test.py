import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:5000"

def test_user_flow(user_num):
    print(f"\n=== Testing User {user_num} ===")
    email = f"user{user_num}@example.com"
    password = f"password{user_num}"
    
    # 1. Login
    print("\n1. Testing Login...")
    login_response = requests.post(
        f"{BASE_URL}/login",
        json={"email": email, "password": password}
    )
    print(f"Status Code: {login_response.status_code}")
    
    if login_response.status_code != 200:
        print(f"Login failed for user {user_num}")
        return False
    
    token = login_response.json().get('access_token')
    headers = {"Authorization": f"Bearer {token}"}
    
    # 2. Get Job Recommendations
    print("\n2. Testing Job Recommendations...")
    rec_response = requests.post(
        f"{BASE_URL}/recommendation",
        headers=headers,
        json={"firstname": "Test", "lastname": "User"}
    )
    print(f"Status Code: {rec_response.status_code}")
    if rec_response.status_code == 200:
        data = rec_response.json()
        print(f"Number of recommended jobs: {len(data.get('recommended_jobs', []))}")
        print(f"Number of recommended students: {len(data.get('recommended_students', []))}")
    
    # 3. Save a Job
    print("\n3. Testing Save Job...")
    save_response = requests.post(
        f"{BASE_URL}/save-jobs",
        headers=headers,
        json={"job_id": 1}
    )
    print(f"Status Code: {save_response.status_code}")
    print(f"Response: {save_response.json()}")
    
    # 4. Get Saved Jobs
    print("\n4. Testing Get Saved Jobs...")
    saved_response = requests.get(
        f"{BASE_URL}/get-saved-jobs",
        headers=headers
    )
    print(f"Status Code: {saved_response.status_code}")
    if saved_response.status_code == 200:
        print(f"Number of saved jobs: {len(saved_response.json())}")
    
    # 5. Get Account Info
    print("\n5. Testing Get Account Info...")
    account_response = requests.get(
        f"{BASE_URL}/user/account",
        headers=headers
    )
    print(f"Status Code: {account_response.status_code}")
    if account_response.status_code == 200:
        print("Account info retrieved successfully")
    
    # 6. Unsave a Job
    print("\n6. Testing Unsave Job...")
    unsave_response = requests.delete(
        f"{BASE_URL}/unsave-jobs",
        headers=headers,
        json={"job_id": 1}
    )
    print(f"Status Code: {unsave_response.status_code}")
    print(f"Response: {unsave_response.json()}")
    
    # 7. Logout
    print("\n7. Testing Logout...")
    logout_response = requests.post(
        f"{BASE_URL}/logout",
        headers=headers
    )
    print(f"Status Code: {logout_response.status_code}")
    print(f"Response: {logout_response.json()}")
    
    return True

def run_final_test():
    print("=== Starting Final System Test ===")
    print(f"Test started at: {datetime.now()}")
    
    # Test a sample of users (1, 25, 50, 75, 100)
    test_users = [1, 25, 50, 75, 100]
    successful_tests = 0
    
    for user_num in test_users:
        if test_user_flow(user_num):
            successful_tests += 1
    
    print("\n=== Test Summary ===")
    print(f"Total users tested: {len(test_users)}")
    print(f"Successful tests: {successful_tests}")
    print(f"Test completed at: {datetime.now()}")
    
    if successful_tests == len(test_users):
        print("\n✅ All tests passed successfully!")
    else:
        print(f"\n❌ {len(test_users) - successful_tests} tests failed")

if __name__ == "__main__":
    run_final_test() 