from layout.buttonMenu.buttonMenu import buttonM
from layout.structLayout.createStructLayout import createStructLayout
from layout.createDynamicLayout.createTableLayout import createTableLayout
import PySimpleGUI as sg
import globalStore.globals as globals
from operations.getStructFromMongo import getStructFromMongo
from operations.base.getBaseRecordFromMongo import getBaseRecordFromMongo

def historyLayout():
    buttonMenu = buttonM('')
    baseStructRecord = getStructFromMongo(globals.baseStructCollection)
    baseRecord = getBaseRecordFromMongo(globals.baseRecordCollection)
    for record in baseRecord:
        globals.baseRecord.append(record)

    globals.primaryKey = list(baseStructRecord.keys())[1]
    globals.baseStruct = saveStruct(baseStructRecord)

    historyStructRecord = getStructFromMongo(globals.historyStructCollection)
    globals.historyStruct = saveStruct(historyStructRecord)
    historyStructRecord.pop(globals.primaryKey)

    baseStructLayout = createStructLayout(baseStructRecord, "base")
    historyStructLayout = createStructLayout(historyStructRecord, "")
    tableLayout = createTableLayout()

    layout = buttonMenu + [[sg.Frame('Cathod-Base',baseStructLayout)]] + [[sg.Frame('Cathod-History',historyStructLayout)]] + tableLayout
    return layout

def saveStruct(record):
    result = {}
    # record.pop("_id")
    for inputKey, value in record.items():
        result[inputKey] = value
    return result