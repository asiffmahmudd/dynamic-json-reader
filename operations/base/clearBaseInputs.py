import globalStore.globals as globals

# [am-23] function: clearing the input fields for the parent window
def clearBaseInputs(actionOn):
    # getting the fields from the global variable for parent's structure
    fields = list(globals.baseStruct.keys())
    # filtering out id
    fields.remove("_id")
    # going through every field for the parent window to update the UI
    for inputKey in fields:
        try:
            # setting the field to empty string if it's a text input
            globals.window[inputKey+actionOn].update('')
        except:
            # setting the value to false if it's not a text input
            globals.window[inputKey+actionOn].update(value = False)