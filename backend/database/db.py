from pymongo import MongoClient
from dotenv import load_dotenv
import os
import certifi

def connect_to_mongodb():
    try:
        # Load environment variables
        load_dotenv()
        
        # Get MongoDB URI from environment variable
        mongodb_uri = os.getenv('MONGODB_URI')
        if not mongodb_uri:
            raise ValueError("MONGODB_URI environment variable is not set")
        
        # Connect to MongoDB with SSL certificate and additional options
        client = MongoClient(
            mongodb_uri,
            tlsCAFile=certifi.where(),
            tlsAllowInvalidCertificates=True,
            serverSelectionTimeoutMS=5000,
            connectTimeoutMS=5000,
            socketTimeoutMS=5000
        )
        
        # Test the connection
        client.admin.command('ping')
        print("Successfully connected to MongoDB!")
        
        return client.uapply
        
    except Exception as e:
        print(f"Error connecting to MongoDB: {str(e)}")
        raise
