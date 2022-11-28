from operations.clearInputs import clearInputs
# from operations.writeToJSON import writeToJSON
from validation.validation import isValid
from operations.updateTableData import updateTableData
import PySimpleGUI as sg
import globalStore.globals as globals
from operations.writeToMongoDB import writeToMongoDB

def addData(values):
    # isValid(values)
    errorCode, errorMsg, validData = isValid(values, globals.historyStruct)
    if errorCode == 1:
        sg.popup(errorMsg)
    else:
        writeToMongoDB(validData, globals.historyCollection)
        clearInputs()
        # listKey = list(globals.data.keys())[0]
        globals.data.append(validData)
        updateTableData()
