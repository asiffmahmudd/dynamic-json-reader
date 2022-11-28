
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
from operations.toggleCrud import toggleCrud
from layout.baseLayout import baseLayout
from operations.base.addBaseData import addBaseData

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
            selectedData = globals.data[selectedIndex]
            populateInputFields(selectedData)
        except Exception as e:
            return
    elif event == globals.primaryKey:
        globals.data = []
        getHistory(globals.primaryKey, values[event])
        temp = None
        for record in globals.baseRecord:
            if record[globals.primaryKey] == values[event]:
                temp = record
        populateInputFields(temp)
        clearInputs()
        selectedIndex = -1
        updateTableData()
    elif event == '-TOGGLE_CRUD-' or event == '-TOGGLE_CRUD-1':
        clearInputs()
        toggleCrud()
    elif event == '-ADD_BTN-base':
        addBaseData(values)
    elif event == '-UPDATE_BTN-base':
        print("update")
    elif event == '-DELETE_BTN-base':
        print("Delte")    

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
        print(globals.event)
        if globals.event == sg.WIN_CLOSED or globals.event == 'Cancel' or globals.event == 'Cancel0': # if user closes window or clicks cancel
            break
        handleEvents(globals.event, globals.values)
    globals.window.close()