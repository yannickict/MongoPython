from pymongo import MongoClient

from MongoConnection import client  # assumes 'client' is already a MongoClient object


def list_db_names():
    dblist = client.list_database_names()
    print("Databases")
    for db in dblist:
        print(" - " + db)

def list_collection_names():
    collist = selectedDb.list_collection_names()
    print("Collections")
    for col in collist:
        print(" - " + col)

dblist = client.list_database_names()
list_db_names()
db_name = ""
while True:
    db_name = input()
    if db_name not in dblist:
        list_db_names()
    else:
        break

selectedDb = client[db_name]

list_collection_names()