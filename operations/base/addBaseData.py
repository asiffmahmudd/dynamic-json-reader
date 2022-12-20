from operations.base.clearBaseInputs import clearBaseInputs
from validation.validation import isValid
from operations.base.updateBaseTableData import updateBaseTableData
import PySimpleGUI as sg
import globalStore.globals as globals
from operations.writeToMongoDB import writeToMongoDB
from operations.base.writeToMongoDropDownSeed import writeToMongoDropDownSeed

# [am-21] function: for adding data for parent
def addBaseData(values):
    # checking if input data is valid
    errorCode, errorMsg, validData = isValid(values, globals.baseStruct, "base")
    # checking if there's any error
    if errorCode == 1:
        # showing error message
        sg.popup(errorMsg)
    else:
        # invoking method to write to database
        writeToMongoDB(validData, globals.config["app-params"]["baseRecordCollection"])
        # going through the parent structure to update the drop down seed values and child row value that's connected to the parent
        for key, value in globals.baseStruct.items():
            # checking if it's a drop down
            if key != "_id" and value["control"] == "dropdown":
                # writing into the database for dropdown seeds
                writeToMongoDropDownSeed(values[key+'base'], key, globals.config['seed-collection']['CollectionName'])
                # checking if it's the dropdown for the primary key
                if key == globals.config["app-params"]["primaryKey"]:
                    # adding the new data to the global variable for the parent
                    globals.baseRecord.append(validData)
                    # invoking the function for getting parent data from the global variable
                    new_values = getNewDropDownValues(key)
                    # updating the UI with the new values
                    globals.window[key].Update(values=new_values, value=new_values[0])
        # clearing the input fields for parent window
        clearBaseInputs("base")
        # invoking the function for updating the table data on parent window
        updateBaseTableData()
        # showing pop up message for successful addition
        sg.popup("Added Successfully!")

# function for getting parent data from the global variable
def getNewDropDownValues(key):
    result =[record[key] for record in globals.baseRecord]
    return result

