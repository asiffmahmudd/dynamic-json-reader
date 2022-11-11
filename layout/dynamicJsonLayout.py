import PySimpleGUI as sg
import globalStore.globals as globals
from operations.readJsonFile import readJSONFile
from layout.createDynamicLayout.createDynamicLayout import createDynamicLayout
from operations.addData import addData
from operations.populateInputFields import populateInputFields
from operations.deleteData import deleteData
from operations.updateData import updateData
from operations.clearInputs import clearInputs

selectedIndex = -1
def handleEvents(event, values):
    global selectedIndex
    if event == '-ADD_BTN-':
        addData(values)
    elif event == '-UPDATE_BTN-':
        if selectedIndex > -1:
            isUpdated = updateData(selectedIndex)
            if isUpdated:
                sg.popup("Update successful!")
                selectedIndex = -1
        else:
            sg.popup("No row selected from the table")
    elif event == '-DELETE_BTN-':
        if selectedIndex > -1:
            deleteData(selectedIndex)
            clearInputs()
            sg.popup("Deleted successfully!")
        else:
            sg.popup("No row selected from the table")
        selectedIndex = -1
    elif event == '-INFO_TABLE-':
        try:
            selectedIndex = values['-INFO_TABLE-'][0]
            selectedData = globals.data[list(globals.data.keys())[0]][selectedIndex]
            populateInputFields(selectedData.values())
        except Exception as e:
            return

def dynamicJsonLayout(filePath):
    readJSONFile(filePath)
    layout = createDynamicLayout()
    globals.modalwindow = sg.Window("Dynamic Layout", layout, modal=True)
    while True:
        event, globals.values = globals.modalwindow.read()
        if event == "Exit" or  event == sg.WIN_CLOSED or event == 'Cancel':
            break
        handleEvents(event, globals.values)
        
    globals.modalwindow.close()