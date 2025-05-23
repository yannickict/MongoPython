from pymongo import MongoClient
from MongoConnection import client

db = client["db_restaurants"]
collection = db["restaurants"]

pipeline = [
    {"$unwind": "$grades"},
    {"$group": {
        "_id": "$name",
        "avgScore": {"$avg": "$grades.score"}
    }},
    {"$sort": {"avgScore": -1}},
    {"$limit": 3}
]

restaurants = collection.aggregate(pipeline)


for r in restaurants:
    print(f"{r['_id']}, score: {r['avgScore']:.2f}")

