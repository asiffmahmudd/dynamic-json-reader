import globalStore.globals as globals

def writeToMongoDropDownSeed(data, docName, collection):
    collection = globals.database[collection]
    print(data, docName, collection)
    collection.update_one(
        {'name': docName},
        {'$push':{ 'values': data } }
    )