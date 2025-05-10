from pymongo import MongoClient
from dotenv import load_dotenv
import os
from datetime import datetime

def create_user():
    try:
        # Load environment variables
        load_dotenv()
        
        # Get MongoDB URI from environment variable
        mongodb_uri = os.getenv('MONGODB_URI')
        if not mongodb_uri:
            raise ValueError("MONGODB_URI environment variable is not set")
        
        # Connect to MongoDB
        client = MongoClient(mongodb_uri)
        db = client.uapply
        
        # Create new user
        new_user = {
            "email": "user@example.com",
            "password": "password123",  # In production, this should be hashed
            "first_name": "John",
            "last_name": "Doe",
            "education": [
                {
                    "degree": "BS",
                    "field": "Computer Science",
                    "university": "Example University",
                    "graduation_year": 2023
                }
            ],
            "work_experience": [
                {
                    "company": "Tech Company",
                    "position": "Software Developer",
                    "duration": "2 years",
                    "description": "Full-stack development"
                }
            ],
            "skills": ["Python", "JavaScript", "React", "Node.js", "MongoDB"],
            "created_at": datetime.utcnow()
        }
        
        # Insert user into database
        db.users.insert_one(new_user)
        print("Successfully created new user!")
        print("\nUser credentials:")
        print("Email: user@example.com")
        print("Password: password123")
        
    except Exception as e:
        print(f"Error creating user: {str(e)}")
    finally:
        client.close()

if __name__ == "__main__":
    create_user() 