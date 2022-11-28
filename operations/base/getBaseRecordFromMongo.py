
import globalStore.globals as globals

def getBaseRecordFromMongo(collectionName):
    collection = globals.database[collectionName]
    return collection.find({})
