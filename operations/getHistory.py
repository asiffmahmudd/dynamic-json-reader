import globalStore.globals as globals

def getHistory(key, value):
    collection = globals.database[globals.config["app-params"]["historyCollection"]]
    result = collection.find({key:value})
    for row in result:
        globals.data.append(row)
    return collection.find({key:value})