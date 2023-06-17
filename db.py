"""DB"""

from pymongo.mongo_client import MongoClient
from pymongo import errors

import sys

uri = "mongodb+srv://admin:admin@cluster0.n6pwm8d.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



class Client:

    def __init__(self, uri, database):
        self.uri = f'{uri}'
        client = MongoClient(self.uri)
        self.curr_database = f'{client}.{database}'

    def ping(self):
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    def use_collection(self, collection_name, func):
        def inner(*args, **kwargs):
            collection = cls.curr_database[f'{collection_name}']
            res = func(collection, *args, **kwargs)
            return res
        return inner
    
    def insert(self, documents, collection):
        try: 
            result = collection.insert_many(documents)
            return result
        # return a friendly error if the operation fails
        except errors.OperationFailure:
            print("An authentication error was received. Are you sure your database user is authorized to perform write operations?")
            sys.exit(1)
        # else:
        #     inserted_count = len(result.inserted_ids)
        #     return "I inserted %x documents." %(inserted_count)
    
    def find_one(self, document, collection):
        try:
            result = collection.find_one(document)
            return result
        except Exception as e:
            print(e)