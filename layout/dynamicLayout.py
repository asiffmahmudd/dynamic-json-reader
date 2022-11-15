from layout.buttonMenu.buttonMenu import buttonM
from layout.structLayout.createStructLayout import createStructLayout
from layout.createDynamicLayout.createTableLayout import createTableLayout
import PySimpleGUI as sg
import globalStore.globals as globals

def dynamicLayout():
    buttonMenu = buttonM()
    baseStructLayout = createStructLayout(globals.baseStructCollection)
    historyStructLayout = createStructLayout(globals.historyStructCollection)
    tableLayout = createTableLayout()

    layout = buttonMenu + baseStructLayout + [[sg.HSeparator(pad=(5,5))]] + historyStructLayout + tableLayout
    return layout