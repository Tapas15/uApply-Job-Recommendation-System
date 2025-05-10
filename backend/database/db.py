from pymongo import MongoClient
import os
from dotenv import load_dotenv

def connect_to_mongodb():
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
        return db
    except Exception as e:
        print(f"Error connecting to MongoDB: {str(e)}")
        raise
