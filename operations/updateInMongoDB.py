import globalStore.globals as globals

# [am-12] function for updating data on the database for child
def updateInMongoDB(data, index):
    # getting the collection for the child from the config file
    collection = globals.database[globals.config["app-params"]["historyCollection"]]
    newValue = data
    # updating the data on the database
    collection.update_one({'_id': globals.data[index]["_id"]}, {"$set": newValue}, upsert=False)