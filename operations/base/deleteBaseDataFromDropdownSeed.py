import globalStore.globals as globals

def deleteBaseDataFromDropdownSeed(data, docName, collection):
    collection = globals.database[collection]
    collection.update_one(
        {'name': docName},
        {'$pull':{ 'values': data } }
    )