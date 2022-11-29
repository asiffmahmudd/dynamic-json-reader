import globalStore.globals as globals

def updateDropdownSeeds(data, coll):
    collection = globals.database[coll]
    newValue = data
    collection.update_one({'name': globals.primaryKey}, {"$set": {"values":newValue}}, upsert=False)