import globalStore.globals as globals
from operations.base.updateBaseTableData import updateBaseTableData
from operations.base.updateBaseInMongo import updateBaseInMongo
from validation.validation import isValid
from operations.base.clearBaseInputs import clearBaseInputs
from operations.base.updateDropdownSeeds import updateDropdownSeeds
import PySimpleGUI as sg
from operations.base.updateChildDataInMongo import updateChildDataInMongo
from operations.updateTableData import updateTableData

def updateBaseData(index):
    errorCode, errorMsg, validData = isValid(globals.values, globals.baseStruct, "base")
    if errorCode == 1:
        sg.popup(errorMsg)
    else:
        oldVal = globals.baseRecord[index][globals.primaryKey]
        for key,val in validData.items():
            globals.baseRecord[index][key] = val
        updateBaseInMongo(validData, index)
        for key, value in globals.baseStruct.items():
            if key != "_id" and value["type"] == "dropdown":
                new_values = getNewDropDownValues(key)
                updateDropdownSeeds(new_values, globals.config['seed-collection']['CollectionName'])
                if key == globals.primaryKey:
                    try:
                        updateChildDataInMongo(globals.historyCollection, key, oldVal, globals.baseRecord[index][key])
                        globals.window[key].Update(values=new_values, value=new_values[0])
                    except Exception as e:
                        globals.window[key].Update(values=new_values)
        updateGlobalHistoryData(oldVal, globals.baseRecord[index][globals.primaryKey])
        updateBaseTableData()
        updateTableData()
        clearBaseInputs("base")
        return True
        
def getNewDropDownValues(key):
    result =[record[key] for record in globals.baseRecord]
    return result

def updateGlobalHistoryData(oldVal, newVal):
    index = 0
    for doc in globals.data:
        if doc[globals.primaryKey] == oldVal:
            globals.data[index][globals.primaryKey] = newVal
        index += 1