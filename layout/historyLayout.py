from layout.buttonMenu.buttonMenu import buttonM
from layout.structLayout.createStructLayout import createStructLayout
from layout.createDynamicLayout.createTableLayout import createTableLayout
import PySimpleGUI as sg
import globalStore.globals as globals
from operations.getStructFromMongo import getStructFromMongo
from operations.base.getBaseRecordFromMongo import getBaseRecordFromMongo
from layout.statusBar.createStatusBarLayout import createStatusBarLayout

def historyLayout():
    buttonMenu = buttonM('')
    baseStructRecord = getStructFromMongo(globals.config["app-params"]["baseStructCollection"])
    baseRecord = getBaseRecordFromMongo(globals.config["app-params"]["baseRecordCollection"])
    for record in baseRecord:
        globals.baseRecord.append(record)

    globals.baseStruct = saveStruct(baseStructRecord)

    historyStructRecord = getStructFromMongo(globals.config["app-params"]["historyStructCollection"])
    globals.historyStruct = saveStruct(historyStructRecord)
    historyStructRecord.pop(globals.config["app-params"]["primaryKey"])

    baseStructLayout = createStructLayout(baseStructRecord, "base")
    historyStructLayout = createStructLayout(historyStructRecord, "")
    tableLayout = createTableLayout()
    statuBarLayout = createStatusBarLayout("Child")

    layout = buttonMenu + [[sg.Frame('Cathod-Base',baseStructLayout)]] + [[sg.Frame('Cathod-History',historyStructLayout)]] + tableLayout + statuBarLayout
    return layout

def saveStruct(record):
    result = {}
    # record.pop("_id")
    for inputKey, value in record.items():
        result[inputKey] = value
    return result