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
