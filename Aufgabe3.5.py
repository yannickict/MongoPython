from pymongo import MongoClient
from MongoConnection import client
from datetime import datetime


db = client["db_restaurants"]
collection = db["restaurants"]


name_input = input("Name (optional): ").strip()
cuisine_input = input("Küche (optional): ").strip()


filter = {}
if name_input:
    filter["name"] = {"$regex": name_input, "$options": "i"}
if cuisine_input:
    filter["cuisine"] = {"$regex": cuisine_input, "$options": "i"}

#setzen der fileter und Suche nach restaurant aus Aufgabe3.4 übernommen


ergebnisse = list(collection.find(filter))

if not ergebnisse:
    print("Keine Restaurants gefunden.")
    exit()



for idx, restaurant in enumerate(ergebnisse, 1):
    print(f"{idx}. {restaurant.get('name')}, Küche: {restaurant.get('cuisine')}")


if len(ergebnisse) > 1:
    auswahl = input("Restaurant für Bewertung auswählen: ").strip()
    if not auswahl.isdigit() or not (1 <= int(auswahl) <= len(ergebnisse)):
        print("ungültige Wahl.")
        exit()
    restaurant = ergebnisse[int(auswahl) - 1]
else:
    restaurant = ergebnisse[0]



grade = (input("Bewertung: ").strip())



bewertung = {
    "date": datetime.now(),
    "score": grade
}

collection.update_one(
    {"_id": restaurant["_id"]},
    {"$push": {"grades": bewertung}}
)

print(f"Bewertung gespiechert ")
