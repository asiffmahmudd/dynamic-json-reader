from globalStore import globals
from operations.updateTableData import updateTableData
from operations.updateInMongoDB import updateInMongoDB
from validation.validation import isValid
from operations.clearInputs import clearInputs
import PySimpleGUI as sg

def updateData(index):
    errorCode, errorMsg, validData = isValid(globals.values, globals.historyStruct)
    if errorCode == 1:
        sg.popup(errorMsg)
    else:
        for key,val in validData.items():
            globals.data[index][key] = val
        updateInMongoDB(validData, index)
        updateTableData()
        clearInputs()
        return True