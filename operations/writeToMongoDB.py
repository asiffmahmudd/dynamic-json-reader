import globalStore.globals as globals

# [am-07] writing data on mongodb collection
def writeToMongoDB(data, collection):
    # getting the collection from the global variable
    collection = globals.database[collection]
    # adding data to the collection
    collection.insert_one(data)