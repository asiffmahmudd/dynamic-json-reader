import globalStore.globals as globals

def writeToMongoDB(data):
    collection = globals.database[globals.historyCollection]
    collection.insert_one(data)