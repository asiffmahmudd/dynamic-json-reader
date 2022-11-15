import globalStore.globals as globals

def getHistory():
    collection = globals.database[globals.historyCollection]
    return collection.find({})