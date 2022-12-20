
import globalStore.globals as globals

# [am-35] getting the structure from database
def getStructFromMongo(collectionName):
    collection = globals.database[collectionName]
    return collection.find({})[0]
