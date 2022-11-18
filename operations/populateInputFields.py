import globalStore.globals as globals

def populateInputFields(data):
    for inputField in data:
        if inputField == "_id":
            continue
        globals.window[inputField].update(data[inputField])