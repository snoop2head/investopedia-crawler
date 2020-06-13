import os
import pymongo
import string
from crawl_terms import listup_vocabs_under_alphabet, collect_term_json

# using dotenv to fetch MongoDB Atlas URL environment variable
MONGO_URL = os.getenv("MONGO_URL")
print("Connecting MongoDB Atlas to: " + MONGO_URL)

# accessing MongoDB Atlas with pymongo MongoClient
client = pymongo.MongoClient(MONGO_URL)

# connect to the mongodb atlas database and collection
vocab_db = client.get_database("vocab")
vocab_terms_collection = vocab_db.vocab_terms


def insert_one_alphabet_term_to_db(alphabet):
    # collect alphabet a terms, package to json documents
    alphabet_term_list = []
    alphabet_vocab_url_list = listup_vocabs_under_alphabet(alphabet)
    for url in alphabet_vocab_url_list:
        term_data_json = collect_term_json(url)
        print(term_data_json["vocabulary"] + " is crawled succesfully")
        alphabet_term_list.append(term_data_json)

    # insert alphabet a terms to mongodb atlas
    vocab_terms_collection.insert_many(alphabet_term_list)


def insert_with_looping(exception_alphabet):
    alphabet_list = list(string.ascii_lowercase)
    # print(alphabet_list)
    alphabet_list.remove(exception_alphabet)
    # print(alphabet_list)
    for alphabet in alphabet_list:
        insert_one_alphabet_term_to_db(alphabet)
        print(
            f"ALL TERMS CORRESPONDING TO ALPHABET {alphabet} ARE INSERTED TO DATABASE"
        )


# insert_one_alphabet_term_to_db("a")
insert_with_looping("a")
