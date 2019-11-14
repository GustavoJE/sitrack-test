from pymongo import MongoClient 
import os

"""
Database configurations
"""

client = MongoClient(os.getenv('MONGO_HOST', "mongodb://admin:admin@localhost:27017/")) 
mydatabase = client[os.getenv("MONGO_DATABASE", "sitrack")]
mycollection = mydatabase[os.getenv("MONGO_COLLECTION","sitrackexam")]   
