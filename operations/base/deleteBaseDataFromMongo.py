import globalStore.globals as globals

def deleteBaseDataFromMongo(id):
    collection = globals.database[globals.baseRecordCollection]
    collection.delete_one({'_id': id})
    