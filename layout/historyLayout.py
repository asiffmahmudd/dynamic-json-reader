from layout.buttonMenu.buttonMenu import buttonM
from layout.structLayout.createStructLayout import createStructLayout
from layout.createDynamicLayout.createTableLayout import createTableLayout
import PySimpleGUI as sg
import globalStore.globals as globals
from operations.getStructFromMongo import getStructFromMongo
from operations.base.getBaseRecordFromMongo import getBaseRecordFromMongo
from layout.statusBar.createStatusBarLayout import createStatusBarLayout

# [am-33] history layout main function
def historyLayout():
    # getting the button menu layout
    buttonMenu = buttonM('')
    # getting the parent structure from database 
    baseStructRecord = getStructFromMongo(globals.config["app-params"]["baseStructCollection"])
    # getting data for the parent from database
    baseRecord = getBaseRecordFromMongo(globals.config["app-params"]["baseRecordCollection"])
    # storing data for parent in the global variable
    for record in baseRecord:
        globals.baseRecord.append(record)
    # saving the structure for parent in a global variable
    globals.baseStruct = saveStruct(baseStructRecord)

    # getting the structure for child 
    historyStructRecord = getStructFromMongo(globals.config["app-params"]["historyStructCollection"])
    # saving the structure for child in a global variable
    globals.historyStruct = saveStruct(historyStructRecord)
    # removing the primary key from the child as it will be a duplicate in the UI
    historyStructRecord.pop(globals.config["app-params"]["primaryKey"])

    # creating the structure for parent
    baseStructLayout = createStructLayout(baseStructRecord, "base")
    # creating the structure for child
    historyStructLayout = createStructLayout(historyStructRecord, "")
    # creating the table layout
    tableLayout = createTableLayout()
    # creating the statusbar layout
    statuBarLayout = createStatusBarLayout("Child")

    # putting all the layouts together
    layout = buttonMenu + [[sg.Frame('Parent',baseStructLayout)]] + [[sg.Frame('Child',historyStructLayout)]] + tableLayout + statuBarLayout
    return layout

# function for returning data in key, value format for global variables
def saveStruct(record):
    result = {}
    for inputKey, value in record.items():
        result[inputKey] = value
    return result