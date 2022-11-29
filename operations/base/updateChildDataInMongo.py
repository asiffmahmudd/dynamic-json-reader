import globalStore.globals as globals

def updateChildDataInMongo(collection, key, old_val, new_val):
    coll = globals.database[collection]
    coll.update_many(
        {key: old_val},
        {
            "$set": {
                key: new_val
            }
        }
    )