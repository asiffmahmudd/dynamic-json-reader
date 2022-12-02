import globalStore.globals as globals

def deleteFromMongoDB(id):
    collection = globals.database[globals.config["app-params"]["historyCollection"]]
    collection.delete_one({'_id': id})
    