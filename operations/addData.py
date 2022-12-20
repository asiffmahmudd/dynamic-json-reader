from operations.clearInputs import clearInputs
from validation.validation import isValid
from operations.updateTableData import updateTableData
import PySimpleGUI as sg
import globalStore.globals as globals
from operations.writeToMongoDB import writeToMongoDB

# [am-04] add functinality for child
def addData(values):
    # calling the function to check if the input values are valid or not
    errorCode, errorMsg, validData = isValid(values, globals.historyStruct)
    if errorCode == 1:
        # if there's an error show the error message on a popup window
        sg.popup(errorMsg)
    # if there's no error
    else:
        # calling the function for writing the data on the mongodb database with valid data and appropriate collection from the config file
        writeToMongoDB(validData, globals.config["app-params"]["historyCollection"])
        # clearing the input fields for the form
        clearInputs()
        # appending the data to the global variable for children for updating data on the UI
        globals.data.append(validData)
        # update the table on UI for showing the new data
        updateTableData()
        # showing a popup for successfull addition
        sg.popup("Added Successfully!")
