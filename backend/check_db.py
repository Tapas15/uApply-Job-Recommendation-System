from pymongo import MongoClient
import os
from dotenv import load_dotenv

def check_database():
    try:
        # Load environment variables
        load_dotenv()
        
        # Get MongoDB URI from environment variable
        mongodb_uri = os.getenv('MONGODB_URI')
        if not mongodb_uri:
            raise ValueError("MONGODB_URI environment variable is not set")
        
        # Connect to MongoDB Atlas
        client = MongoClient(mongodb_uri)
        
        # Test the connection
        client.admin.command('ping')
        print("Successfully connected to MongoDB Atlas!")
        
        # Get the database
        db = client['uapply']
        
        # Check collections
        collections = db.list_collection_names()
        print("\nExisting collections:")
        for collection in collections:
            count = db[collection].count_documents({})
            print(f"- {collection}: {count} documents")
            
        return True
    except Exception as e:
        print(f"Error checking database: {str(e)}")
        return False

if __name__ == "__main__":
    check_database() 