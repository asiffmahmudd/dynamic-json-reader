from globalStore import globals
from operations.base.updateBaseTableData import updateBaseTableData
from operations.base.deleteBaseDataFromMongo import deleteBaseDataFromMongo
from operations.base.deleteBaseDataFromDropdownSeed import deleteBaseDataFromDropdownSeed
from operations.base.deleteChildData import deleteChildData
# from operations.updateInJSON import updateInJSON
import PySimpleGUI as sg

def deleteBaseData(index):
    deleteBaseDataFromMongo(globals.baseRecord[index]["_id"])
    if globals.config['app-params']['CanCascadeDelete'] == '1':
        deleteChildData(globals.config["app-params"]["historyCollection"], globals.baseRecord[index][globals.config["app-params"]["primaryKey"]])
    for key, value in globals.baseStruct.items():
        if key != "_id" and value["control"] == "dropdown":
            deleteBaseDataFromDropdownSeed(globals.values[key+'base'], key, globals.config['seed-collection']['CollectionName'])
            if key == globals.config["app-params"]["primaryKey"]:
                globals.baseRecord.remove(globals.baseRecord[index])
                new_values = getNewDropDownValues(key)
                try:
                    globals.window[key].Update(values=new_values, value=new_values[0])
                except:
                    globals.window[key].Update(values=new_values)
    updateBaseTableData()
    
def getNewDropDownValues(key):
    result =[record[key] for record in globals.baseRecord]
    return result