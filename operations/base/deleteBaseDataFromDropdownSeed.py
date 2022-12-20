import globalStore.globals as globals

# [am-30] delete data from dropdown seeds from the database
def deleteBaseDataFromDropdownSeed(data, docName, collection):
    collection = globals.database[collection]
    collection.update_one(
        {'name': docName},
        {'$pull':{ 'values': data } }
    )