from pymongo import MongoClient
from dotenv import load_dotenv
import os
from datetime import datetime

def create_new_database():
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
        
        # Drop existing collections
        collections = ['users', 'saved_jobs', 'job_posting']
        for collection in collections:
            if collection in db.list_collection_names():
                db[collection].drop()
                print(f"Dropped collection: {collection}")
        
        # Create new collections
        users = db['users']
        saved_jobs = db['saved_jobs']
        job_posting = db['job_posting']
        
        # Insert sample job postings
        sample_jobs = [
            {
                "job_id": 1,
                "company_name": "Google",
                "job_title": "Software Engineer",
                "location": "Mountain View, CA",
                "job_description": "Join our team to build next-gen cloud solutions",
                "required_skills": ["Python", "Java", "Cloud Computing"],
                "job_type": "Full-time",
                "experience_level": "Mid-level",
                "salary_range": "$120,000 - $180,000",
                "job_link": "https://careers.google.com/jobs/1"
            },
            {
                "job_id": 2,
                "company_name": "Microsoft",
                "job_title": "Frontend Developer",
                "location": "Redmond, WA",
                "job_description": "Create beautiful user interfaces for our products",
                "required_skills": ["React", "JavaScript", "CSS"],
                "job_type": "Full-time",
                "experience_level": "Entry-level",
                "salary_range": "$90,000 - $130,000",
                "job_link": "https://careers.microsoft.com/jobs/2"
            },
            {
                "job_id": 3,
                "company_name": "Amazon",
                "job_title": "Data Scientist",
                "location": "Seattle, WA",
                "job_description": "Work on machine learning and data analysis",
                "required_skills": ["Python", "Machine Learning", "SQL"],
                "job_type": "Full-time",
                "experience_level": "Senior",
                "salary_range": "$150,000 - $200,000",
                "job_link": "https://careers.amazon.com/jobs/3"
            }
        ]
        
        job_posting.insert_many(sample_jobs)
        print(f"Inserted {len(sample_jobs)} job postings")
        
        # Insert sample user
        sample_user = {
            "email": "test@example.com",
            "password": "test123",  # In production, this should be hashed
            "first_name": "Test",
            "last_name": "User",
            "education": [
                {
                    "degree": "BS",
                    "field": "Computer Science",
                    "university": "Test University",
                    "graduation_year": 2023
                }
            ],
            "work_experience": [
                {
                    "company": "Test Company",
                    "position": "Software Engineer",
                    "duration": "2 years",
                    "description": "Full-stack development"
                }
            ],
            "skills": ["Python", "JavaScript", "React", "Node.js"],
            "created_at": datetime.utcnow()
        }
        
        users.insert_one(sample_user)
        print("Created sample user")
        
        # Insert sample saved jobs
        sample_saved_jobs = [
            {
                "user_email": "test@example.com",
                "job_id": 1,
                "saved_at": datetime.utcnow()
            },
            {
                "user_email": "test@example.com",
                "job_id": 2,
                "saved_at": datetime.utcnow()
            }
        ]
        
        saved_jobs.insert_many(sample_saved_jobs)
        print(f"Inserted {len(sample_saved_jobs)} saved jobs")
        
        print("\nDatabase initialization completed successfully!")
        print("\nSample user credentials:")
        print("Email: test@example.com")
        print("Password: test123")
        
    except Exception as e:
        print(f"Error initializing database: {str(e)}")
    finally:
        client.close()

if __name__ == "__main__":
    create_new_database() 