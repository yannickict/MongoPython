from pymongo import MongoClient, GEOSPHERE
from MongoConnection import client

db = client["db_restaurants"]
collection = db["restaurants"]


collection.create_index([("address.coord", GEOSPHERE)])


restaurant = collection.find_one({"name": "Le Perigord"})
coord = restaurant["address"]["coord"]

near_restaurant = collection.find_one({
    "address.coord": {
        "$near": {
            "$geometry": {
                "type": "Point",
                "coordinates": coord
            }
        }
    },
    "name": {"$ne": "Le Perigord"}
})




if near_restaurant:
    print(f"{near_restaurant['name']}, {near_restaurant['address']['coord']}")


