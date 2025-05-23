
from pymongo import MongoClient
from MongoConnection import client

db = client["db_restaurants"]
collection = db["restaurants"]

stadtbezirke = collection.distinct("borough")

for bezirk in stadtbezirke:
    print(bezirk)
