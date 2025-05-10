from pymongo import MongoClient
import pandas as pd
import os
from dotenv import load_dotenv

def insert_job_data():
    try:
        # Load environment variables
        load_dotenv()
        
        # Get MongoDB URI from environment variable
        mongodb_uri = os.getenv('MONGODB_URI')
        if not mongodb_uri:
            raise ValueError("MONGODB_URI environment variable is not set")
        
        # Connect to MongoDB Atlas
        client = MongoClient(mongodb_uri)
        db = client['uapply']
        
        # Read the CSV file
        job_data_path = os.path.join('..', 'notebooks', 'job_posting_data.csv')
        if not os.path.exists(job_data_path):
            raise FileNotFoundError(f"Job data file not found at: {job_data_path}")
            
        job_data = pd.read_csv(job_data_path)
        
        # Add additional fields
        job_data['company_name'] = ['Tech Corp', 'Data Solutions', 'Product Co', 'Design Studio', 'Cloud Systems']
        job_data['location'] = ['New York', 'San Francisco', 'Boston', 'Seattle', 'Austin']
        job_data['formatted_work_type'] = ['Full-time', 'Full-time', 'Full-time', 'Full-time', 'Full-time']
        job_data['linkedin_url'] = ['https://linkedin.com/jobs/1', 'https://linkedin.com/jobs/2', 
                                  'https://linkedin.com/jobs/3', 'https://linkedin.com/jobs/4', 
                                  'https://linkedin.com/jobs/5']
        job_data['company_industry'] = ['Technology', 'Data & Analytics', 'Product', 'Design', 'Cloud Computing']
        job_data['salary_range'] = ['$100k-$150k', '$120k-$180k', '$90k-$140k', '$80k-$130k', '$110k-$160k']
        job_data['required_skills'] = [
            ['Python', 'Web Development', 'JavaScript', 'React'],
            ['Python', 'Machine Learning', 'Data Analysis', 'SQL'],
            ['Agile', 'Product Management', 'JIRA', 'Communication'],
            ['UI/UX', 'Figma', 'User Research', 'Prototyping'],
            ['AWS', 'Docker', 'Kubernetes', 'CI/CD']
        ]
        
        # Convert DataFrame to list of dictionaries
        job_records = job_data.to_dict('records')
        
        # Clear existing data
        db.job_posting.delete_many({})
        
        # Insert job records
        if job_records:
            result = db.job_posting.insert_many(job_records)
            print(f"Successfully inserted {len(result.inserted_ids)} job postings")
            
            # Print the inserted records
            print("\nInserted Job Postings:")
            for job in db.job_posting.find():
                print(f"\nTitle: {job['title']}")
                print(f"Company: {job['company_name']}")
                print(f"Location: {job['location']}")
                print(f"Skills: {', '.join(job['required_skills'])}")
        else:
            print("No job records to insert")
            
    except Exception as e:
        print(f"Error inserting job data: {str(e)}")
        raise

if __name__ == "__main__":
    insert_job_data() 