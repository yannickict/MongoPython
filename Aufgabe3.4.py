from pymongo import MongoClient
from MongoConnection import client

db = client["db_restaurants"]
collection = db["restaurants"]


name_input = input("Name (optional): ").strip()
cuisine_input = input("Küche (optional): ").strip()

filter = {}
if name_input:
    filter["name"] = {"$regex": name_input, "$options": "i"}
if cuisine_input:
    filter["cuisine"] = {"$regex": cuisine_input, "$options": "i"}


ergebnisse = collection.find(filter)

count = 0
for restaurant in ergebnisse:
    print(f" {restaurant.get('name')}, Küche:{restaurant.get('cuisine')}")
    
    count += 1


if count == 0:
    print("keine Restarants gefunden.")
