
import globalStore.globals as globals

def getStructFromMongo(collectionName):
    collection = globals.database[collectionName]
    return collection.find({})[0]
