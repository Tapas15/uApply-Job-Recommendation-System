import os
from dotenv import load_dotenv
from pymongo import MongoClient
import bcrypt
import random
from datetime import datetime

# Load environment variables
load_dotenv()

# MongoDB connection
client = MongoClient(os.getenv('MONGODB_URI'))
db = client.uapply

# Sample data for generating varied profiles
first_names = [
    "John", "Emma", "Michael", "Sophia", "William", "Olivia", "James", "Ava", "Alexander", "Isabella",
    "David", "Mia", "Joseph", "Charlotte", "Daniel", "Amelia", "Matthew", "Harper", "Andrew", "Evelyn",
    "Joshua", "Abigail", "Christopher", "Emily", "Anthony", "Elizabeth", "Ryan", "Sofia", "Nicholas", "Avery"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"
]

degrees = ["BS", "MS", "PhD", "BA", "MA"]
fields = [
    "Computer Science", "Data Science", "Software Engineering", "Information Technology",
    "Electrical Engineering", "Mechanical Engineering", "Business Administration",
    "Mathematics", "Physics", "Chemistry", "Biology", "Psychology"
]

companies = [
    "Tech Corp", "Data Solutions", "Innovation Labs", "Digital Systems", "Future Tech",
    "Smart Solutions", "Global Tech", "Advanced Systems", "Creative Technologies",
    "Next Generation Tech"
]

positions = [
    "Software Engineer", "Data Scientist", "Web Developer", "Systems Analyst",
    "Network Engineer", "Database Administrator", "IT Consultant", "Project Manager",
    "Business Analyst", "DevOps Engineer"
]

skills = [
    "Python", "Java", "JavaScript", "C++", "SQL", "React", "Node.js", "Machine Learning",
    "Data Analysis", "Cloud Computing", "AWS", "Docker", "Kubernetes", "Git",
    "Agile", "Project Management", "UI/UX Design", "Mobile Development"
]

def generate_user(index):
    # Generate a unique email
    email = f"user{index}@example.com"
    
    # Generate a random password and hash it
    password = f"password{index}"
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    # Generate random education history (1-2 entries)
    education = []
    num_education = random.randint(1, 2)
    for _ in range(num_education):
        education.append({
            "degree": random.choice(degrees),
            "field": random.choice(fields)
        })
    
    # Generate random work experience (1-3 entries)
    work_experience = []
    num_experience = random.randint(1, 3)
    for _ in range(num_experience):
        work_experience.append({
            "employerName": random.choice(companies),
            "position": random.choice(positions)
        })
    
    # Generate random skills (3-6 skills)
    num_skills = random.randint(3, 6)
    user_skills = random.sample(skills, num_skills)
    
    return {
        "email": email,
        "password": hashed_password,
        "firstname": random.choice(first_names),
        "lastname": random.choice(last_names),
        "education": education,
        "work_experience": work_experience,
        "tags": user_skills,
        "created_at": datetime.utcnow()
    }

def create_sample_users():
    try:
        # Drop existing users collection
        db.users.drop()
        print("Dropped existing users collection")
        
        # Generate and insert 100 users
        users = [generate_user(i) for i in range(1, 101)]
        result = db.users.insert_many(users)
        
        print(f"Successfully created {len(result.inserted_ids)} users")
        print("\nSample user credentials:")
        print("Email: user1@example.com")
        print("Password: password1")
        
    except Exception as e:
        print(f"Error creating sample users: {str(e)}")

if __name__ == "__main__":
    create_sample_users() 