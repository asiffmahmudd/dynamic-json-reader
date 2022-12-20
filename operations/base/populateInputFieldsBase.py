import globalStore.globals as globals

# [am-31] function: for populating input fields for parent window
def populateInputFieldsBase(data, actionOn):
    for inputField in data:
        if inputField == "_id":
            continue
        globals.window[inputField+actionOn].update(data[inputField])