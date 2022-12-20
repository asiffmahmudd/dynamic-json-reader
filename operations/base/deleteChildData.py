import globalStore.globals as globals

# [am-29] function: for deleting child data from the database
def deleteChildData(collection, key):
    coll = globals.database[collection]
    coll.delete_many({globals.config["app-params"]["primaryKey"]: key})