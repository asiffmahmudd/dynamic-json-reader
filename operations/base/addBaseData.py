from operations.base.clearBaseInputs import clearBaseInputs
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
        writeToMongoDB(validData, globals.config["app-params"]["baseRecordCollection"])
        for key, value in globals.baseStruct.items():
            if key != "_id" and value["control"] == "dropdown":
                writeToMongoDropDownSeed(values[key+'base'], key, globals.config['seed-collection']['CollectionName'])
                if key == globals.config["app-params"]["primaryKey"]:
                    globals.baseRecord.append(validData)
                    new_values = getNewDropDownValues(key)
                    globals.window[key].Update(values=new_values, value=new_values[0])
        clearBaseInputs("base")
        updateBaseTableData()
        sg.popup("Added Successfully!")

def getNewDropDownValues(key):
    result =[record[key] for record in globals.baseRecord]
    return result

