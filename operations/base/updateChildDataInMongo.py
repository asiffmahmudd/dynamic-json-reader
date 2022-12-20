import globalStore.globals as globals
# [am-26] function: for updating child data (dropdown data) when there's a change in parent 
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