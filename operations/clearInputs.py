
import globalStore.globals as globals

def clearInputs():
    fields = list(globals.historyStruct.keys())
    fields.remove("_id")
    fields.remove(globals.config["app-params"]["primaryKey"])
    for inputKey in fields:
        try:
            globals.window[inputKey].update('')
        except:
            globals.window[inputKey].update(value = False)