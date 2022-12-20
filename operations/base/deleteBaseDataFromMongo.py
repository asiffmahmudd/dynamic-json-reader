import globalStore.globals as globals

# [am-28] function: for deleting parent data from database using id
def deleteBaseDataFromMongo(id):
    collection = globals.database[globals.config["app-params"]["baseRecordCollection"]]
    collection.delete_one({'_id': id})
    