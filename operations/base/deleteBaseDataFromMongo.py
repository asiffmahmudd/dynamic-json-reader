import globalStore.globals as globals

def deleteBaseDataFromMongo(id):
    collection = globals.database[globals.config["app-params"]["baseRecordCollection"]]
    collection.delete_one({'_id': id})
    