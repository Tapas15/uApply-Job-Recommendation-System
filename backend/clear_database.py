from pymongo import MongoClient
from dotenv import load_dotenv
import os

def clear_database():
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
        
        # List of collections to drop
        collections = ['users', 'saved_jobs', 'job_posting']
        
        # Drop each collection
        for collection in collections:
            if collection in db.list_collection_names():
                db[collection].drop()
                print(f"Dropped collection: {collection}")
            else:
                print(f"Collection {collection} does not exist")
        
        print("\nDatabase cleared successfully!")
        
    except Exception as e:
        print(f"Error clearing database: {str(e)}")
    finally:
        client.close()

if __name__ == "__main__":
    clear_database() 