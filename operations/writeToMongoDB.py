import globalStore.globals as globals

def writeToMongoDB(data, collection):
    collection = globals.database[collection]
    collection.insert_one(data)