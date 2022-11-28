from layout.buttonMenu.buttonMenu import buttonM
from layout.createBaseLayout import createBaseLayout
from layout.createDynamicLayout.createTableLayout import createTableLayout
import PySimpleGUI as sg
import globalStore.globals as globals
from operations.getStructFromMongo import getStructFromMongo
from operations.base.getBaseRecordFromMongo import getBaseRecordFromMongo
from layout.createDynamicLayout.createBaseTableLayout import createTableLayout

def baseLayout():
    buttonMenu = buttonM('base')
    baseStructRecord = getStructFromMongo(globals.baseStructCollection)

    baseLayout = createBaseLayout(baseStructRecord, "base")
    tableLayout = createTableLayout('base')
    layout = buttonMenu + baseLayout + tableLayout
    return layout

def saveStruct(record):
    result = {}
    # record.pop("_id")
    for inputKey, value in record.items():
        result[inputKey] = value
    return result