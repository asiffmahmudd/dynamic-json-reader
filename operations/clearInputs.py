
import globalStore.globals as globals

# [am-13] function for clearing input fields for child
def clearInputs():
    # getting the fields from the child structure that was stored in the global variable
    fields = list(globals.historyStruct.keys())
    # filtering out _id
    fields.remove("_id")
    # removing primary key as we won't need it on child
    fields.remove(globals.config["app-params"]["primaryKey"])
    # loop for going through all the input fields
    for inputKey in fields:
        # try to set the input field's value to empty string
        try:
            globals.window[inputKey].update('')
        # if it's not a textbox setting it's value to false, so that nothing is selected by default
        except:
            globals.window[inputKey].update(value = False)