
import PySimpleGUI as sg
from layout.dynamicLayout import dynamicLayout
from operations.connectToDatabase import connectToDatabase
import globalStore.globals as globals

selectedIndex = -1
def handleEvents(event, values):
    global selectedIndex
    if event == '-ADD_BTN-':
        # addData(values)
        print("add")
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


#function: main function. the app starts here
if __name__ == "__main__":  
    connectToDatabase()

    layout = dynamicLayout()
    
    window = sg.Window('Dynamic CRUD', layout)
    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        handleEvents(event, values)
    window.close()