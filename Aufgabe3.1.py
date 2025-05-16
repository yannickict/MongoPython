from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["db_restaurants"]
collection = db["neighborhoods"]


stadtbezirke = collection.distinct("borough")


for bezirk in stadtbezirke:
    print(bezirk)


