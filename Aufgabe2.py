from MongoConnection import client


def list_databases():
    dbs = client.list_database_names()
    if not dbs:
        print("No Database")
        return None
    print("\nDatabases")
    for db in dbs:
        print(f" - {db}")
    return dbs


def list_collections(db_name):
    try:
        db = client[db_name]
        cols = db.list_collection_names()
        if not cols:
            print("No Collection")
            return None
        print(f"\n{db_name}\n")
        print("Collections")
        for col in cols:
            print(f" - {col}")
        return cols
    except Exception:
        print("Database not found.")
        return None


def list_documents(db_name, col_name):
    try:
        collection = client[db_name][col_name]
        docs = collection.find({}, {"_id": 1})
        doc_ids = [str(doc["_id"]) for doc in docs]
        if not doc_ids:
            print("No Document")
            return None
        print(f"\n{db_name}.{col_name}\n")
        print("Documents")
        for doc_id in doc_ids:
            print(f" - {doc_id}")
        return doc_ids
    except Exception:
        print("Collection not found.")
        return None


def show_document(db_name, col_name, doc_id):
    try:
        from bson import ObjectId
        collection = client[db_name][col_name]
        document = collection.find_one({"_id": ObjectId(doc_id)})
        print(f"\n{db_name}.{col_name}.{doc_id}\n")
        if document:
            for k, v in document.items():
                if k != "_id":
                    print(f"{k}: {v}")
        else:
            print("Document not found.")
        input("\nPress any button to return")
    except Exception:
        print("Invalid Document ID or error.")
        input("\nPress any button to return")


def main():
    while True:
        dbs = list_databases()
        if not dbs:
            input("\nPress any button to return")
            continue
        db_name = input("\nSelect Database: ")
        if db_name not in dbs:
            print("Database not found.")
            input("\nPress any button to return")
            continue

        cols = list_collections(db_name)
        if not cols:
            input("\nPress any button to return")
            continue
        col_name = input("\nSelect Collection: ")
        if col_name not in cols:
            print("Collection not found.")
            input("\nPress any button to return")
            continue

        doc_ids = list_documents(db_name, col_name)
        if not doc_ids:
            input("\nPress any button to return")
            continue
        doc_id = input("\nSelect Document: ")
        if doc_id not in doc_ids:
            print("Document not found.")
            input("\nPress any button to return")
            continue

        show_document(db_name, col_name, doc_id)


if __name__ == "__main__":
    main()
