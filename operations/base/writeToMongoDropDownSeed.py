import globalStore.globals as globals

def writeToMongoDropDownSeed(data, docName, collection):
    collection = globals.database[collection]
    collection.update_one(
        {'name': docName},
        {'$push':{ 'values': data } }
    )