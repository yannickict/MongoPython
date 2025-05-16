
# Aufgabe1.2
from pymongo import MongoClient
from MongoConnection import client

dblist = client.list_database_names()

for db in dblist:
    print(db)

dblist = client.list_database_names()

if "admin" in dblist:
    print("Database exists.")
else:
    print("Database does not exist.")

