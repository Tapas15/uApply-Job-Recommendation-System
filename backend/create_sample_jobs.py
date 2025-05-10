from pymongo import MongoClient
from dotenv import load_dotenv
import os
from datetime import datetime

def create_sample_jobs():
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
        
        # Drop existing job postings
        if 'job_posting' in db.list_collection_names():
            db.job_posting.drop()
            print("Dropped existing job postings")
        
        # Create new job postings collection
        job_posting = db['job_posting']
        
        # Sample jobs data
        sample_jobs = [
            {
                "job_id": 1,
                "company_name": "Google",
                "job_title": "Senior Software Engineer",
                "location": "Mountain View, CA",
                "job_description": "Join our team to build next-gen cloud solutions and AI-powered applications",
                "required_skills": ["Python", "Java", "Cloud Computing", "Machine Learning"],
                "job_type": "Full-time",
                "experience_level": "Senior",
                "salary_range": "$150,000 - $200,000",
                "job_link": "https://careers.google.com/jobs/1"
            },
            {
                "job_id": 2,
                "company_name": "Microsoft",
                "job_title": "Frontend Developer",
                "location": "Redmond, WA",
                "job_description": "Create beautiful and responsive user interfaces for our cloud products",
                "required_skills": ["React", "JavaScript", "CSS", "TypeScript"],
                "job_type": "Full-time",
                "experience_level": "Mid-level",
                "salary_range": "$120,000 - $160,000",
                "job_link": "https://careers.microsoft.com/jobs/2"
            },
            {
                "job_id": 3,
                "company_name": "Amazon",
                "job_title": "Data Scientist",
                "location": "Seattle, WA",
                "job_description": "Work on machine learning models and data analysis for e-commerce",
                "required_skills": ["Python", "Machine Learning", "SQL", "Statistics"],
                "job_type": "Full-time",
                "experience_level": "Senior",
                "salary_range": "$140,000 - $190,000",
                "job_link": "https://careers.amazon.com/jobs/3"
            },
            {
                "job_id": 4,
                "company_name": "Meta",
                "job_title": "Full Stack Developer",
                "location": "Menlo Park, CA",
                "job_description": "Build scalable web applications for social media platforms",
                "required_skills": ["React", "Node.js", "Python", "AWS"],
                "job_type": "Full-time",
                "experience_level": "Mid-level",
                "salary_range": "$130,000 - $170,000",
                "job_link": "https://careers.meta.com/jobs/4"
            },
            {
                "job_id": 5,
                "company_name": "Apple",
                "job_title": "iOS Developer",
                "location": "Cupertino, CA",
                "job_description": "Develop next-generation iOS applications",
                "required_skills": ["Swift", "Objective-C", "iOS SDK", "Xcode"],
                "job_type": "Full-time",
                "experience_level": "Mid-level",
                "salary_range": "$125,000 - $165,000",
                "job_link": "https://careers.apple.com/jobs/5"
            },
            {
                "job_id": 6,
                "company_name": "Netflix",
                "job_title": "Backend Engineer",
                "location": "Los Gatos, CA",
                "job_description": "Build scalable backend services for streaming platform",
                "required_skills": ["Java", "Spring Boot", "AWS", "Microservices"],
                "job_type": "Full-time",
                "experience_level": "Senior",
                "salary_range": "$160,000 - $220,000",
                "job_link": "https://careers.netflix.com/jobs/6"
            },
            {
                "job_id": 7,
                "company_name": "Twitter",
                "job_title": "DevOps Engineer",
                "location": "San Francisco, CA",
                "job_description": "Manage cloud infrastructure and deployment pipelines",
                "required_skills": ["AWS", "Docker", "Kubernetes", "CI/CD"],
                "job_type": "Full-time",
                "experience_level": "Mid-level",
                "salary_range": "$130,000 - $170,000",
                "job_link": "https://careers.twitter.com/jobs/7"
            },
            {
                "job_id": 8,
                "company_name": "LinkedIn",
                "job_title": "Machine Learning Engineer",
                "location": "Sunnyvale, CA",
                "job_description": "Develop ML models for job recommendations",
                "required_skills": ["Python", "TensorFlow", "PyTorch", "MLOps"],
                "job_type": "Full-time",
                "experience_level": "Senior",
                "salary_range": "$150,000 - $200,000",
                "job_link": "https://careers.linkedin.com/jobs/8"
            },
            {
                "job_id": 9,
                "company_name": "Uber",
                "job_title": "Mobile Developer",
                "location": "San Francisco, CA",
                "job_description": "Build mobile applications for ride-sharing platform",
                "required_skills": ["Kotlin", "Swift", "Android SDK", "iOS SDK"],
                "job_type": "Full-time",
                "experience_level": "Mid-level",
                "salary_range": "$130,000 - $170,000",
                "job_link": "https://careers.uber.com/jobs/9"
            },
            {
                "job_id": 10,
                "company_name": "Airbnb",
                "job_title": "Full Stack Developer",
                "location": "San Francisco, CA",
                "job_description": "Build features for the world's largest accommodation platform",
                "required_skills": ["React", "Node.js", "GraphQL", "AWS"],
                "job_type": "Full-time",
                "experience_level": "Senior",
                "salary_range": "$140,000 - $190,000",
                "job_link": "https://careers.airbnb.com/jobs/10"
            }
        ]
        
        # Insert jobs into database
        job_posting.insert_many(sample_jobs)
        print(f"Successfully inserted {len(sample_jobs)} sample jobs")
        
    except Exception as e:
        print(f"Error creating sample jobs: {str(e)}")
    finally:
        client.close()

if __name__ == "__main__":
    create_sample_jobs() 