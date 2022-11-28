from operations.base.clearBaseInputs import clearInputs
# from operations.writeToJSON import writeToJSON
from validation.validation import isValid
from operations.base.updateBaseTableData import updateBaseTableData
import PySimpleGUI as sg
import globalStore.globals as globals
from operations.writeToMongoDB import writeToMongoDB
from operations.base.writeToMongoDropDownSeed import writeToMongoDropDownSeed

def addBaseData(values):
    errorCode, errorMsg, validData = isValid(values, globals.baseStruct, "base")
    if errorCode == 1:
        sg.popup(errorMsg)
    else:
        writeToMongoDB(validData, globals.baseRecordCollection)
        for key, value in globals.baseStruct.items():
            if key != "_id" and value["type"] == "dropdown":
                writeToMongoDropDownSeed(values[key+'base'], key, globals.config['seed-collection']['CollectionName'])
                if key == globals.primaryKey:
                    globals.baseRecord.append(validData)
                    new_values = getNewDropDownValues(key)
                    globals.window[key].Update(values=new_values, value=new_values[0])
        clearInputs("base")
        updateBaseTableData()

def getNewDropDownValues(key):
    result =[record[key] for record in globals.baseRecord]
    return result

