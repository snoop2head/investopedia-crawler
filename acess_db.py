import os
from pymongo import MongoClient
import pymongo

MONGO_URL = os.getenv("MONGO_URL")
print("Connecting MongoDB Atlas to: " + MONGO_URL)

client = pymongo.MongoClient(MONGO_URL)

"""
# testing database connection
db = client.test
print(db)

# testing collection connection
db = client.get_database("vocab")
retrieved_terms = db.vocab_terms
all_documents_no = retrieved_terms.count_documents({})
print(all_documents_no)
"""
