from layout.buttonMenu.buttonMenu import buttonM
from layout.createBaseLayout import createBaseLayout
from layout.createDynamicLayout.createTableLayout import createTableLayout
import PySimpleGUI as sg
import globalStore.globals as globals
from operations.getStructFromMongo import getStructFromMongo
from layout.createDynamicLayout.createBaseTableLayout import createTableLayout
from layout.statusBar.createStatusBarLayout import createStatusBarLayout

# [am-36] main layout function for parent window
def baseLayout():
    # getting the button manu layout
    buttonMenu = buttonM('base')
    # getting the parent structure from database
    baseStructRecord = getStructFromMongo(globals.config["app-params"]["baseStructCollection"])

    # getting the parent layout
    baseLayout = createBaseLayout(baseStructRecord, "base")
    # getting the table layout
    tableLayout = createTableLayout('base')
    # getting teh statusbar layout
    statuBarLayout = createStatusBarLayout("Parent")

    # putting all the layouts together
    layout = buttonMenu + baseLayout + tableLayout + [[sg.Push()]] + statuBarLayout
    return layout

