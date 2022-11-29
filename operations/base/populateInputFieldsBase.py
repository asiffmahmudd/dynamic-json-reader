import globalStore.globals as globals

def populateInputFieldsBase(data, actionOn):
    for inputField in data:
        if inputField == "_id":
            continue
        globals.window[inputField+actionOn].update(data[inputField])