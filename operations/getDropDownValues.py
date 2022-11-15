import globalStore.globals as globals
def getDropDownValues(key):
    collection = globals.database[globals.config['seed-collection']['CollectionName']]
    record = collection.find({})
    # print(record)
    for doc in record:
        if doc['name'] == key:
            return doc['values']