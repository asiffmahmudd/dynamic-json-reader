import globalStore.globals as globals

def updateBaseInMongo(data, index):
    collection = globals.database[globals.baseRecordCollection]
    newValue = data
    collection.update_one({'_id': globals.baseRecord[index]["_id"]}, {"$set": newValue}, upsert=False)