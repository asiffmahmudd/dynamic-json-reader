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

selectedIndex = -1
selectedIndexBase = -1
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
    elif event == '-UPDATE_BTN-base':
        if selectedIndexBase > -1:
            isUpdated = updateBaseData(selectedIndexBase)
            if isUpdated:
                sg.popup("Update successful!")
                selectedIndexBase = -1
        else:
            sg.popup("No row selected from the table")
    elif event == '-DELETE_BTN-base':
        if selectedIndexBase > -1:
            deleteBaseData(selectedIndexBase)
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
    layout = [
        [
            sg.Column(historyLayout(), visible=True, key='-HISTORY_LAYOUT-'), 
            sg.Column(baseLayout(), visible=False, key='-BASE_LAYOUT-')
        ]
    ]
    
    globals.window = sg.Window('Dynamic CRUD', layout)
    while True:

        globals.event, globals.values = globals.window.read()
        # print(globals.event)
        if globals.event == sg.WIN_CLOSED or globals.event == 'Cancel' or globals.event == 'Cancel0': # if user closes window or clicks cancel
            break
        handleEvents(globals.event, globals.values)
    globals.window.close()