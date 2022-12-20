import globalStore.globals as globals
# [am-22] function: for writing into the dropdown seed database
def writeToMongoDropDownSeed(data, docName, collection):
    # getting the collection
    collection = globals.database[collection]
    collection.update_one(
        {'name': docName},
        {'$push':{ 'values': data } }
    )