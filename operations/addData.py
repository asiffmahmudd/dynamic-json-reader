from operations.clearInputs import clearInputs
# from operations.writeToJSON import writeToJSON
from validation.validation import isValid
from operations.updateTableData import updateTableData
import PySimpleGUI as sg
import globalStore.globals as globals

def addData(values):
    errorCode, errorMsg, validData = isValid(values)
    if errorCode == 1:
        sg.popup(errorMsg)
    else:
        # writeToJSON(validData)
        clearInputs()
        listKey = list(globals.data.keys())[0]
        globals.data[listKey].append(validData)
        updateTableData()
