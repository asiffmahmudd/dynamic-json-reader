from layout.buttonMenu.buttonMenu import buttonM
from layout.structLayout.createStructLayout import createStructLayout
from layout.createDynamicLayout.createTableLayout import createTableLayout
import PySimpleGUI as sg
import globalStore.globals as globals
from operations.getStructFromMongo import getStructFromMongo

def dynamicLayout():
    buttonMenu = buttonM()

    baseStructRecord = getStructFromMongo(globals.baseStructCollection)
    globals.primaryKey = list(baseStructRecord.keys())[1]
    globals.baseStruct = saveStruct(baseStructRecord)

    historyStructRecord = getStructFromMongo(globals.historyStructCollection)
    globals.historyStruct = saveStruct(historyStructRecord)
    historyStructRecord.pop(globals.primaryKey)

    baseStructLayout = createStructLayout(baseStructRecord)
    historyStructLayout = createStructLayout(historyStructRecord)
    tableLayout = createTableLayout()

    layout = buttonMenu + baseStructLayout + [[sg.HSeparator(pad=(5,5))]] + historyStructLayout + tableLayout
    return layout

def saveStruct(record):
    result = {}
    # record.pop("_id")
    for inputKey, value in record.items():
        result[inputKey] = value
    return result