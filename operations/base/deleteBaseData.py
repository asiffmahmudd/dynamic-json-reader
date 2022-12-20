from globalStore import globals
from operations.base.updateBaseTableData import updateBaseTableData
from operations.base.deleteBaseDataFromMongo import deleteBaseDataFromMongo
from operations.base.deleteBaseDataFromDropdownSeed import deleteBaseDataFromDropdownSeed
from operations.base.deleteChildData import deleteChildData
import PySimpleGUI as sg

# [am-27] function: for deleting parent data
def deleteBaseData(index):
    # deleting it from the database using id
    deleteBaseDataFromMongo(globals.baseRecord[index]["_id"])
    # checking if cascade delete was active or not
    if globals.config['app-params']['CanCascadeDelete'] == '1':
        # deleting child data along with parents from database
        deleteChildData(globals.config["app-params"]["historyCollection"], globals.baseRecord[index][globals.config["app-params"]["primaryKey"]])
    # going through the structure of the parent to check for dropdown fields
    for key, value in globals.baseStruct.items():
        # filtering out id and checking if it's a dropdown
        if key != "_id" and value["control"] == "dropdown":
            # deleting parent data from dropdown seed collection
            deleteBaseDataFromDropdownSeed(globals.values[key+'base'], key, globals.config['seed-collection']['CollectionName'])
            # checking for primary key
            if key == globals.config["app-params"]["primaryKey"]:
                # removing it from the global variable for the parent
                globals.baseRecord.remove(globals.baseRecord[index])
                # getting the new values for dropdown
                new_values = getNewDropDownValues(key)
                try:
                    # updating UI and showing the first element by default
                    globals.window[key].Update(values=new_values, value=new_values[0])
                except:
                    globals.window[key].Update(values=new_values)
    # updating parent table data 
    updateBaseTableData()
    
# function for getting the new values for dropdown field
def getNewDropDownValues(key):
    result =[record[key] for record in globals.baseRecord]
    return result