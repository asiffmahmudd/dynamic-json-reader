import PySimpleGUI as sg
from layout.historyLayout import historyLayout
from operations.connectToDatabase import connectToDatabase
from operations.addData import addData
import globalStore.globals as globals
from operations.getHistory import getHistory
from operations.updateTableData import updateTableData
from operations.updateData import updateData
from operations.populateInputFields import populateInputFields
from operations.clearInputs import clearInputs
from operations.deleteData import deleteData
from operations.base.deleteBaseData import deleteBaseData
from operations.toggleCrud import toggleCrud
from layout.baseLayout import baseLayout
from operations.base.addBaseData import addBaseData
from operations.base.populateInputFieldsBase import populateInputFieldsBase
from operations.base.clearBaseInputs import clearBaseInputs
from operations.base.updateBaseData import updateBaseData
from layout.statusBar.createStatusBarLayout import createStatusBarLayout

selectedIndex = -1
selectedIndexBase = -1
sg.theme('DarkGrey5')

def handleEvents(event, values):
    global selectedIndex
    global selectedIndexBase
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
            selectedData = globals.data[selectedIndex]
            populateInputFields(selectedData)
        except Exception as e:
            return
    elif event == globals.config["app-params"]["primaryKey"]:
        globals.data = []
        getHistory(globals.config["app-params"]["primaryKey"], values[event])
        temp = None
        for record in globals.baseRecord:
            if record[globals.config["app-params"]["primaryKey"]] == values[event]:
                temp = record
        populateInputFields(temp)
        clearInputs()
        selectedIndex = -1
        updateTableData()

    elif event == '-TOGGLE_CRUD-' or event == '-TOGGLE_CRUD-1':
        clearInputs()
        clearBaseInputs("base")
        selectedIndex = -1
        selectedIndexBase = -1
        toggleCrud()

    elif event == '-ADD_BTN-base':
        addBaseData(values)
        selectedData = globals.data[0]
        populateInputFields(selectedData)
    elif event == '-UPDATE_BTN-base':
        if selectedIndexBase > -1:
            isUpdated = updateBaseData(selectedIndexBase)
            if isUpdated:
                sg.popup("Update successful!")
                selectedData = globals.data[0]
                populateInputFields(selectedData)
                selectedIndexBase = -1
        else:
            sg.popup("No row selected from the table")
    elif event == '-DELETE_BTN-base':
        if selectedIndexBase > -1:
            deleteBaseData(selectedIndexBase)
            selectedData = globals.data[0]
            populateInputFields(selectedData)
            clearBaseInputs("base")
            sg.popup("Deleted successfully!")
        else:
            sg.popup("No row selected from the table")
        selectedIndexBase = -1 
    elif event == '-INFO_TABLE-base':
        try:
            selectedIndexBase = values['-INFO_TABLE-base'][0]
            selectedDataBase = globals.baseRecord[selectedIndexBase]
            populateInputFieldsBase(selectedDataBase, "base")
        except Exception as e:
            return

#function: main function. the app starts here
if __name__ == "__main__":  
    connectToDatabase()
    layout = []
    if globals.config["app-params"]["isParentChild"] == "1":
        layout = [
            # [sg.Push()],
            [   
                # sg.Push(),
                sg.Column(historyLayout(), element_justification='center', visible=True, key='-HISTORY_LAYOUT-', scrollable=True,  vertical_scroll_only=True, size=(1400, 750)), 
                sg.Column(baseLayout(), element_justification='center', visible=False, key='-BASE_LAYOUT-', scrollable=True,  vertical_scroll_only=True, size=(1400, 750)),
            ],
            # [sg.Push()]
        ]
    else:
        layout = [
            # [sg.Push()],
            [   
                # sg.Push(),
                sg.Column(historyLayout(), element_justification='center', visible=False, key='-HISTORY_LAYOUT-', scrollable=True,  vertical_scroll_only=True, size=(1400, 750)), 
                sg.Column(baseLayout(), element_justification='center', visible=True, key='-BASE_LAYOUT-', scrollable=True,  vertical_scroll_only=True, size=(1400, 750)),
            ],
            # [sg.Push()]
        ]
    
    globals.window = sg.Window('Dynamic CRUD', layout, size=(1400, 750), element_justification="center")
    while True:

        globals.event, globals.values = globals.window.read()
        # print(globals.event)
        if globals.event == sg.WIN_CLOSED or globals.event == 'Cancel' or globals.event == 'Cancel0': # if user closes window or clicks cancel
            break
        handleEvents(globals.event, globals.values)
    globals.window.close()