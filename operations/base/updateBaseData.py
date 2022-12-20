import globalStore.globals as globals
from operations.base.updateBaseTableData import updateBaseTableData
from operations.base.updateBaseInMongo import updateBaseInMongo
from validation.validation import isValid
from operations.base.clearBaseInputs import clearBaseInputs
from operations.base.updateDropdownSeeds import updateDropdownSeeds
import PySimpleGUI as sg
from operations.base.updateChildDataInMongo import updateChildDataInMongo
from operations.updateTableData import updateTableData

# [am-25] function: for updating parent data
def updateBaseData(index):
    # checking for valid data
    errorCode, errorMsg, validData = isValid(globals.values, globals.baseStruct, "base")
    # checking for error
    if errorCode == 1:
        # showing error message in a popup window
        sg.popup(errorMsg)
    else:
        # storing old value for making the changes in child data
        oldVal = globals.baseRecord[index][globals.config["app-params"]["primaryKey"]]
        # getting the record from row using index
        for key,val in validData.items():
            globals.baseRecord[index][key] = val
        # update parent data on database
        updateBaseInMongo(validData, index)
        # going through all the fields for checking for dropdown fields and updating the seed values and child data
        for key, value in globals.baseStruct.items():
            # filtering out id and checking if it's a dropdown
            if key != "_id" and value["control"] == "dropdown":
                # getting the dropdown values from the global variable for the parent
                new_values = getNewDropDownValues(key)
                # invoking the function for updating seed data on database
                updateDropdownSeeds(new_values, globals.config['seed-collection']['CollectionName'])
                # checking if it's the primary key
                if key == globals.config["app-params"]["primaryKey"]:
                    try:
                        # using this function for updating child data
                        updateChildDataInMongo(globals.config["app-params"]["historyCollection"], key, oldVal, globals.baseRecord[index][key])
                        # updating the value on UI and setting the default value to the first element
                        globals.window[key].Update(values=new_values, value=new_values[0])
                    except Exception as e:
                        globals.window[key].Update(values=new_values)
        # updating the changed data in the global variable for children
        updateGlobalHistoryData(oldVal, globals.baseRecord[index][globals.config["app-params"]["primaryKey"]])
        # updating the changes on parent table data
        updateBaseTableData()
        # updating the changes on child table data
        updateTableData()
        # clearing the input fields for parent
        clearBaseInputs("base")
        return True

# getting all the values based on the passed key from the global variable of the parent    
def getNewDropDownValues(key):
    result =[record[key] for record in globals.baseRecord]
    return result

# updating the changed data in the global variable for children
def updateGlobalHistoryData(oldVal, newVal):
    index = 0
    # going through all child data to look for the field and apply change
    for doc in globals.data:
        if doc[globals.config["app-params"]["primaryKey"]] == oldVal:
            globals.data[index][globals.config["app-params"]["primaryKey"]] = newVal
        index += 1