from pymongo import MongoClient, errors

def connect_db():
    try:
        client = MongoClient('mongodb+srv://bond1qdev:54Md4qkso7tCCiF@goitlearn.rkpgekc.mongodb.net/goit_hw?retryWrites=true&w=majority')
        db = client['goit_hw']
        return db.cats
    except errors.ConnectionFailure:
        print("Failed to server connect.")

def create_cat(cat):
    collection = connect_db()
    result = collection.insert_one(cat)
    print('One cat added with _id:', result.inserted_id)


def read_all_cats():
    collection = connect_db()
    for cat in collection.find():
        print(cat)


def find_cat_by_name(name):
    collection = connect_db()
    cat = collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print("No cat found with this name.")


def update_cat_age(name, new_age):
    collection = connect_db()
    result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
    if result.modified_count:
        print("Successfully updated the cat's age.")
    else:
        print("No updates made.")


def add_feature_to_cat(name, feature):
    collection = connect_db()
    result = collection.update_one({"name": name}, {"$addToSet": {"features": feature}})
    if result.modified_count:
        print("Feature added.")
    else:
        print("No features added or feature already exists.")


def delete_cat_by_name(name):
    collection = connect_db()
    result = collection.delete_one({"name": name})
    if result.deleted_count:
        print("Successfully deleted the cat.")
    else:
        print("No cat found with this name to delete.")


def delete_all_cats():
    collection = connect_db()
    result = collection.delete_many({})
    print("Deleted all cats:", result.deleted_count)

# Тестування функцій
if __name__ == "__main__":
    cat = {
        "name": "barsik",
        "age": 3,
        "features": ["ходить в капці", "дає себе гладити", "рудий"]
    }

    #create_cat(cat)
    #read_all_cats()
    #find_cat_by_name("barsik")
    #update_cat_age("barsik", 5)
    #add_feature_to_cat("barsik", "любить спати")
    #delete_cat_by_name("barsik")
    #delete_all_cats()
