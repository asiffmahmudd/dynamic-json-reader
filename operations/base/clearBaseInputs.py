import globalStore.globals as globals

def clearBaseInputs(actionOn):
    fields = list(globals.baseStruct.keys())
    fields.remove("_id")
    for inputKey in fields:
        try:
            globals.window[inputKey+actionOn].update('')
        except:
            globals.window[inputKey+actionOn].update(value = False)