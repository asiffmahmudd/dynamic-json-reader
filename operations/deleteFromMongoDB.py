import globalStore.globals as globals

def deleteFromMongoDB(id):
    collection = globals.database[globals.historyCollection]
    collection.delete_one({'_id': id})
    