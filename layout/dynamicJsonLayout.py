import PySimpleGUI as sg
from operations.readJsonFile import readJSONFile
from layout.createDynamicLayout.createDynamicLayout import createDynamicLayout
from layout.buttonMenu.buttonMenu import buttonM

def dynamicJsonLayout(filePath):
    readJSONFile(filePath)
    layout = createDynamicLayout()
    window = sg.Window("Dynamic Layout", layout, modal=True, size=(1000, 600))
    while True:
        event, values = window.read()
        if event == "Exit" or  event == sg.WIN_CLOSED or event == 'Cancel':
            break
        
    window.close()