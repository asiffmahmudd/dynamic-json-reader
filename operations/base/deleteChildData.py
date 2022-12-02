import globalStore.globals as globals

def deleteChildData(collection, key):
    coll = globals.database[collection]
    coll.delete_many({globals.config["app-params"]["primaryKey"]: key})