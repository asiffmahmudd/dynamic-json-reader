from globalStore import globals
from operations.updateTableData import updateTableData
from operations.updateInMongoDB import updateInMongoDB
from validation.validation import isValid
from operations.clearInputs import clearInputs
import PySimpleGUI as sg

# [am-11] function for updating child data
def updateData(index):
    # checking if the input data is valid or not
    errorCode, errorMsg, validData = isValid(globals.values, globals.historyStruct)
    # checking if there's an error
    if errorCode == 1:
        # if there's an error show the error message on a popup window
        sg.popup(errorMsg)
    else:
        # updating the selected data
        for key,val in validData.items():
            globals.data[index][key] = val
        # invoking the function for updating data on the database
        updateInMongoDB(validData, index)
        # updating the table data
        updateTableData()
        # clearing the input fields
        clearInputs()
        # return true for updating data successfully
        return True