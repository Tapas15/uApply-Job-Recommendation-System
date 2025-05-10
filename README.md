# uApply - Job Recommendation System

A full-stack job recommendation system that matches job seekers with relevant job postings using AI-powered recommendations.

## Project Structure

```
uApply-Job-Recommendation-System/
├── backend/                 # Flask backend server
│   ├── app.py              # Main Flask application
│   ├── create_new_database.py  # Database initialization script
│   ├── test_new_db.py      # Test script for API endpoints
│   └── database/           # Database connection and models
├── client/                 # Frontend application
└── notebooks/              # Jupyter notebooks for data processing
```

## Prerequisites

- Python 3.8 or higher
- MongoDB Atlas account
- Node.js and npm (for frontend)

## Setup Instructions

### 1. Backend Setup

1. Create a virtual environment and activate it:
   ```bash
python -m venv myenv
# On Windows
myenv\Scripts\activate
# On Unix/MacOS
source myenv/bin/activate
```

2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
```

3. Create a `.env` file in the backend directory with the following content:
```
JWT_SECRET_KEY=uapply-secret-key-2024
MONGODB_URI=your_mongodb_atlas_connection_string
```

4. Initialize the database:
```bash
cd backend
python create_new_database.py
```

5. Start the backend server:
```bash
cd backend
$env:FLASK_APP = "app.py"  # On Windows PowerShell
flask run
```

The backend server will start at `http://localhost:5000`

### 2. Frontend Setup

1. Navigate to the client directory:
   ```bash
cd client
```

2. Install dependencies:
   ```bash
   npm install
```

3. Start the frontend development server:
   ```bash
   npm start
```

The frontend application will start at `http://localhost:3000`

## Testing the API

You can test the API endpoints using the provided test script:

   ```bash
cd backend
python test_new_db.py
```

### Sample User Credentials

```
Email: john@example.com
Password: password123
```

## API Endpoints

1. **Register User**
   - POST `/`
   - Body: User registration details

2. **Login**
   - POST `/login`
   - Body: `{ "email": "user@example.com", "password": "password" }`

3. **Get Job Recommendations**
   - POST `/recommendation`
   - Headers: `Authorization: Bearer <token>`
   - Body: `{ "firstname": "John", "lastname": "Doe" }`

4. **Save Job**
   - POST `/save-jobs`
   - Headers: `Authorization: Bearer <token>`
   - Body: `{ "job_id": 1 }`

5. **Get Saved Jobs**
   - GET `/get-saved-jobs`
   - Headers: `Authorization: Bearer <token>`

6. **Get Account Info**
   - GET `/user/account`
   - Headers: `Authorization: Bearer <token>`

7. **Unsave Job**
   - DELETE `/unsave-jobs`
   - Headers: `Authorization: Bearer <token>`
   - Body: `{ "job_id": 1 }`

8. **Logout**
   - POST `/logout`
   - Headers: `Authorization: Bearer <token>`

## Postman Testing Guide

### Setup Postman Environment

1. Create a new environment in Postman:
   - Click "Environments" → "Create New"
   - Name it "uApply Local"
   - Add these variables:
     - `base_url`: `http://localhost:5000`
     - `token`: Leave empty (will be set after login)

### Testing Steps

1. **Register a New User**
   - Method: POST
   - URL: `{{base_url}}/`
   - Body (raw JSON):
   ```json
   {
     "email": "test@example.com",
     "password": "test123",
     "firstname": "Test",
     "lastname": "User",
     "education": [
       {
         "degree": "BS",
         "field": "Computer Science"
       }
     ],
     "work_experience": [
       {
         "employerName": "Test Company",
         "position": "Software Engineer"
       }
     ],
     "tags": ["Python", "Web Development"]
   }
   ```

2. **Login**
   - Method: POST
   - URL: `{{base_url}}/login`
   - Body (raw JSON):
   ```json
   {
     "email": "john@example.com",
     "password": "password123"
   }
   ```
   - After successful login, copy the `access_token` from the response and set it as the `token` environment variable

3. **Get Job Recommendations**
   - Method: POST
   - URL: `{{base_url}}/recommendation`
   - Headers:
     - `Authorization`: `Bearer {{token}}`
   - Body (raw JSON):
   ```json
   {
     "firstname": "John",
     "lastname": "Doe"
   }
   ```

4. **Save a Job**
   - Method: POST
   - URL: `{{base_url}}/save-jobs`
   - Headers:
     - `Authorization`: `Bearer {{token}}`
   - Body (raw JSON):
   ```json
   {
     "job_id": 1
   }
   ```

5. **Get Saved Jobs**
   - Method: GET
   - URL: `{{base_url}}/get-saved-jobs`
   - Headers:
     - `Authorization`: `Bearer {{token}}`

6. **Get Account Info**
   - Method: GET
   - URL: `{{base_url}}/user/account`
   - Headers:
     - `Authorization`: `Bearer {{token}}`

7. **Unsave a Job**
   - Method: DELETE
   - URL: `{{base_url}}/unsave-jobs`
   - Headers:
     - `Authorization`: `Bearer {{token}}`
   - Body (raw JSON):
   ```json
   {
     "job_id": 1
   }
   ```

8. **Logout**
   - Method: POST
   - URL: `{{base_url}}/logout`
   - Headers:
     - `Authorization`: `Bearer {{token}}`

### Expected Responses

1. **Register User**
   - Status: 201 Created
   - Response: `{"message": "User registered successfully"}`

2. **Login**
   - Status: 200 OK
   - Response: `{"access_token": "jwt_token_here", "message": "Login successful"}`

3. **Get Job Recommendations**
   - Status: 200 OK
   - Response: JSON object containing recommended jobs and students

4. **Save Job**
   - Status: 201 Created
   - Response: `{"message": "Job saved successfully"}`

5. **Get Saved Jobs**
   - Status: 200 OK
   - Response: Array of saved job objects

6. **Get Account Info**
   - Status: 200 OK
   - Response: User profile information

7. **Unsave Job**
   - Status: 200 OK
   - Response: `{"message": "Job unsaved successfully"}`

8. **Logout**
   - Status: 200 OK
   - Response: `{"message": "Successfully logged out"}`

### Common Issues and Solutions

1. **401 Unauthorized**
   - Check if the token is correctly set in the environment variable
   - Verify the token format: `Bearer your_token_here`
   - Try logging in again to get a fresh token

2. **404 Not Found**
   - Verify the base URL is correct
   - Check if the endpoint path is correct
   - Ensure the backend server is running

3. **500 Internal Server Error**
   - Check the backend server logs for detailed error messages
   - Verify the MongoDB connection is working
   - Ensure all required environment variables are set

## Database Collections

The MongoDB database contains three main collections:
- `users`: Stores user profiles and credentials
- `saved_jobs`: Stores jobs saved by users
- `job_posting`: Stores job postings and their details

## Troubleshooting

1. If you encounter MongoDB connection issues:
   - Verify your MongoDB Atlas connection string in the `.env` file
   - Ensure your IP address is whitelisted in MongoDB Atlas

2. If the Flask server fails to start:
   - Make sure you're in the correct directory
   - Verify that all required packages are installed
   - Check if the `.env` file exists and contains the correct values

3. If API endpoints return 401 errors:
   - Verify that you're including the correct JWT token in the Authorization header
   - Check if the token has expired (tokens expire after 24 hours)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
