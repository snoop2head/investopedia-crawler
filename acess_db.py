import os
import pymongo
from crawl_terms import make_vocab_to_def_json

# using dotenv to fetch MongoDB Atlas URL environment variable
MONGO_URL = os.getenv("MONGO_URL")
print("Connecting MongoDB Atlas to: " + MONGO_URL)

# accessing MongoDB Atlas with pymongo MongoClient
client = pymongo.MongoClient(MONGO_URL)

# connect to the mongodb atlas database and collection
vocab_db = client.get_database("vocab")
vocab_terms_collection = vocab_db.vocab_terms

"""
# testing database connection
db = client.test
print(db)

# testing collection connection
db = client.get_database("vocab")
vocab_terms_mongodb = db.vocab_terms
all_documents_no = vocab_terms_mongodb.count_documents({})
print(all_documents_no)
"""

"""
# insert a test document at the collection
new_term = {"name": "namaewa?", "url": "localhost"}
vocab_terms_collection.insert_one(new_term)

# insert investopedia data to the mongodb atlas
test_json_document = make_vocab_to_def_json(
    "https://www.investopedia.com/terms/b/buyersmarket.asp"
)
vocab_terms_collection.insert_one(test_json_document)

# insert multiple test documents at the collection
new_terms = [
    {"name": "namaewa?", "url": "localhost"},
    {"name": "taki-kun!", "url": "localhost"},
]
vocab_terms_collection.insert_many(new_terms)
"""

"""
# find all documents from mongodb atlas
all_docs = list(vocab_terms_collection.find())
print(all_docs, type(all_docs))

# find individual documents from mongodb atlas
one_doc = vocab_terms_collection.find_one({"vocabulary": "buyersmarket"})
print(one_doc)
"""

"""
"""
