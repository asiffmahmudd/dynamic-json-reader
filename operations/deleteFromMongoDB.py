import globalStore.globals as globals

# [am-15] delete from database using id 
def deleteFromMongoDB(id):
    # getting the collection from the config file
    collection = globals.database[globals.config["app-params"]["historyCollection"]]
    # deleting data from the collection
    collection.delete_one({'_id': id})
    