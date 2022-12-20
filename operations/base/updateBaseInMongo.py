import globalStore.globals as globals

# updating the new value on database
def updateBaseInMongo(data, index):
    # getting the parent collection from confi
    collection = globals.database[globals.config["app-params"]["baseRecordCollection"]]
    # new data to be updated
    newValue = data
    # updating data
    collection.update_one({'_id': globals.baseRecord[index]["_id"]}, {"$set": newValue}, upsert=False)