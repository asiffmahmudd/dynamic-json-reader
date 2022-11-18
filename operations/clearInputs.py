
import globalStore.globals as globals

def clearInputs():
    fields = list(globals.historyStruct.keys())
    fields.remove("_id")
    fields.remove(globals.primaryKey)
    for inputKey in fields:
        globals.window[inputKey].update('')