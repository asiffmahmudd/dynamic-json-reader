from globalStore import globals
from operations.updateTableData import updateTableData
from operations.updateInJSON import updateInJSON
from validation.validation import isValid
from operations.clearInputs import clearInputs
import PySimpleGUI as sg

def updateData(index):
    errorCode, errorMsg, validData = isValid(globals.values)
    if errorCode == 1:
        sg.popup(errorMsg)
    else:
        listKey = list(globals.data.keys())[0]
        globals.data[listKey][index] = validData
        updateInJSON()
        updateTableData()
        clearInputs()
        return True