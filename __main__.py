
import PySimpleGUI as sg
from layout.dynamicLayout import dynamicLayout
from operations.connectToDatabase import connectToDatabase
from operations.addData import addData
import globalStore.globals as globals
from operations.getHistory import getHistory
from operations.updateTableData import updateTableData
from operations.processDataForTable import processDataForTable

selectedIndex = -1
def handleEvents(event, values):
    global selectedIndex
    if event == '-ADD_BTN-':
        addData(values)
    elif event == '-UPDATE_BTN-':
        print("update")
        # if selectedIndex > -1:
        #     isUpdated = updateData(selectedIndex)
        #     if isUpdated:
        #         sg.popup("Update successful!")
        #         selectedIndex = -1
        # else:
        #     sg.popup("No row selected from the table")
    elif event == '-DELETE_BTN-':
        print("delete")
        # if selectedIndex > -1:
        #     deleteData(selectedIndex)
        #     clearInputs()
        #     sg.popup("Deleted successfully!")
        # else:
        #     sg.popup("No row selected from the table")
        # selectedIndex = -1
    elif event == '-INFO_TABLE-':
        print("table")
        # try:
        #     selectedIndex = values['-INFO_TABLE-'][0]
        #     selectedData = globals.data[list(globals.data.keys())[0]][selectedIndex]
        #     populateInputFields(selectedData.values())
        # except Exception as e:
        #     return
    elif event == globals.primaryKey:
        globals.data = []
        getHistory(globals.primaryKey, values[event])
        updateTableData()
        # for d in data:
        #     print(d)

#function: main function. the app starts here
if __name__ == "__main__":  
    connectToDatabase()

    layout = dynamicLayout()
    
    globals.window = sg.Window('Dynamic CRUD', layout)
    while True:

        globals.event, globals.values = globals.window.read()

        if globals.event == sg.WIN_CLOSED or globals.event == 'Cancel': # if user closes window or clicks cancel
            break
        handleEvents(globals.event, globals.values)
    globals.window.close()