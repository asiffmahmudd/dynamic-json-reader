import globalStore.globals as globals
# [am-16] function: for populating input fields with selected data
def populateInputFields(data):
    # going throught all the fields for updating the UI
    for inputField in data:
        # filtering out id as it's not included in the UI
        if inputField == "_id":
            continue
        # updating the UI with proper data using the input field's key
        globals.window[inputField].update(data[inputField])