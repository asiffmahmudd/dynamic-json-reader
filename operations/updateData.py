from globalStore import globals
from operations.updateTableData import updateTableData
from operations.updateInJSON import updateInJSON
from validation.validation import isValid
from operations.clearInputs import clearInputs

def updateData(index):
    if isValid(globals.values):
        data = {}
        data["name"] = globals.values["-NAME-"]
        data["salary"] = globals.values["-SALARY-"]
        data["birthday"] = globals.values["-BIRTHDAY-"]
        globals.info[index] = data
        updateInJSON()
        updateTableData()
        clearInputs()
        return True