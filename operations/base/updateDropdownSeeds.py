import globalStore.globals as globals

# updating dropdown seed data on database
def updateDropdownSeeds(data, coll):
    collection = globals.database[coll]
    newValue = data
    collection.update_one({'name': globals.config["app-params"]["primaryKey"]}, {"$set": {"values":newValue}}, upsert=False)