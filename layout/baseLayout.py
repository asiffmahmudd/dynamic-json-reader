from layout.buttonMenu.buttonMenu import buttonM
from layout.createBaseLayout import createBaseLayout
from layout.createDynamicLayout.createTableLayout import createTableLayout
import PySimpleGUI as sg
import globalStore.globals as globals
from operations.getStructFromMongo import getStructFromMongo
from layout.createDynamicLayout.createBaseTableLayout import createTableLayout
from layout.statusBar.createStatusBarLayout import createStatusBarLayout

def baseLayout():
    buttonMenu = buttonM('base')
    baseStructRecord = getStructFromMongo(globals.config["app-params"]["baseStructCollection"])

    baseLayout = createBaseLayout(baseStructRecord, "base")
    tableLayout = createTableLayout('base')
    statuBarLayout = createStatusBarLayout("Parent")

    layout = buttonMenu + baseLayout + tableLayout + [[sg.Push()]] + statuBarLayout
    return layout

def saveStruct(record):
    result = {}
    # record.pop("_id")
    for inputKey, value in record.items():
        result[inputKey] = value
    return result