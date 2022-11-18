import globalStore.globals as globals

def updateInMongoDB(data, index):
    collection = globals.database[globals.historyCollection]
    newValue = data
    collection.update_one({'_id': globals.data[index]["_id"]}, {"$set": newValue}, upsert=False)