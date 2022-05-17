# pip install pymongo==3.12.0

import pymongo

client = pymongo.MongoClient("mongodb://18.193.110.9:27017")

print(client)

db = client.list_database_names()

print(db)