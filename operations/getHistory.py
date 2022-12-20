import globalStore.globals as globals

# [am-17] function: for getting child data from the database and setting the global data for child
def getHistory(key, value):
    # getting the collection from the config file
    collection = globals.database[globals.config["app-params"]["historyCollection"]]
    # getting teh result from the collection
    result = collection.find({key:value})
    # setting the global variable with fetched data
    for row in result:
        globals.data.append(row)
    # returning found data (not necessary)
    return collection.find({key:value})