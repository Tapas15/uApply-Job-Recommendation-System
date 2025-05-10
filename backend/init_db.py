from pymongo import MongoClient
import pandas as pd
import os
from dotenv import load_dotenv

def init_database():
    try:
        # Load environment variables
        load_dotenv()
        print("MONGODB_URI:", os.getenv('MONGODB_URI'))
        
        # Get MongoDB URI from environment variable
        mongodb_uri = os.getenv('MONGODB_URI')
        if not mongodb_uri:
            raise ValueError("MONGODB_URI environment variable is not set")
        
        # Connect to MongoDB Atlas
        client = MongoClient(mongodb_uri)
        db = client['uapply']  # Create database named 'uapply'

        # Create collections
        collections = ['users', 'saved_jobs', 'job_posting']
        for collection in collections:
            if collection not in db.list_collection_names():
                db.create_collection(collection)
                print(f"Created collection: {collection}")

        # Load job posting data if available
        job_data_path = os.path.join('..', 'notebooks', 'job_posting_data.csv')
        if os.path.exists(job_data_path):
            # Read the CSV file
            job_data = pd.read_csv(job_data_path)
            
            # Add required fields if they don't exist
            required_fields = ['company_name', 'location', 'formatted_work_type', 'linkedin_url', 'company_industry']
            for field in required_fields:
                if field not in job_data.columns:
                    job_data[field] = ''  # Add empty field
            
            # Convert DataFrame to list of dictionaries
            job_records = job_data.to_dict('records')
            
            # Clear existing data
            db.job_posting.delete_many({})
            
            # Insert job records
            if job_records:
                db.job_posting.insert_many(job_records)
                print(f"Loaded {len(job_records)} job postings into database")
            else:
                print("No job records to insert")
        else:
            print(f"Job data file not found at: {job_data_path}")

        print("Database initialization completed successfully!")
        
    except Exception as e:
        print(f"Error during database initialization: {str(e)}")
        raise

if __name__ == "__main__":
    init_database() 