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

# variable for changing table data of the child based on the selected parent 
selectedIndex = -1
# variable for changing the table data of the parent based on the selected parent
selectedIndexBase = -1
# [am-10] theme for the app
sg.theme('DarkBlack1')

# [am-18] method for updating table data and global variable for child
def updateGlobalsAndTableData(key, value):
    # invoking the function for getting child data from the database and assign them to the proper global variable
    getHistory(key, value)
    temp = None
    # looping through all the parent data and finding the selected one
    for record in globals.baseRecord:
        if record[globals.config["app-params"]["primaryKey"]] == value:
            temp = record
    # populating input fields for parent section on the child window
    populateInputFields(temp)
    # clearing the input fields
    clearInputs()
    # resetting the selected row
    selectedIndex = -1
    # updating table data for the child window
    updateTableData()

# [am-03] method for handling the user events
def handleEvents(event, values):
    global selectedIndex
    global selectedIndexBase

    # checking if the add button was clicked for child
    if event == '-ADD_BTN-':
        # invoking the add functionality for child
        addData(values)
    # checking if the update button was clicked for child
    elif event == '-UPDATE_BTN-':
        # checking if there's a table data row selected for updating
        if selectedIndex > -1:
            # if table data was selected invoking the update function for child and get the response
            isUpdated = updateData(selectedIndex)
            # checking if the update was successful or not
            if isUpdated:
                # showing a popup indicating that the update was successful
                sg.popup("Update successful!")
                # resetting the selected row
                selectedIndex = -1
        else:
            # showing error message if no row was selected for updating
            sg.popup("No row selected from the table")
    # checking if the delete button for the child was clicked
    elif event == '-DELETE_BTN-':
        # checking if there's a table data row selected for updating
        if selectedIndex > -1:
            # invoking the delete function for deleting a child data
            deleteData(selectedIndex)
            # clearing the input fields
            clearInputs()
            # showing a popup indicating that the delete was successful
            sg.popup("Deleted successfully!")
        else:
            # showing error message if no row was selected for deleting
            sg.popup("No row selected from the table")
        # resetting the selected index for child
        selectedIndex = -1
    # if the user clicks/selects a row from the table this event will be triggered
    elif event == '-INFO_TABLE-':
        try:
            # changing the global variable to selected row for retrieving data
            selectedIndex = values['-INFO_TABLE-'][0]
            # using the selected index for getting the data
            selectedData = globals.data[selectedIndex]
            # populating the input fields with selected data for next operation
            populateInputFields(selectedData)
        except Exception as e:
            return
    # on the child window, if the user changes the parent field this event will be triggered
    elif event == globals.config["app-params"]["primaryKey"]:
        # emptying the global variable for getting new child data according to parent
        globals.data = []
        # invoking the function for updating window data and global variable for child data when a new parent has been selected
        updateGlobalsAndTableData(globals.config["app-params"]["primaryKey"], values[event])
    # [am-19] event for changing the toggle button
    elif event == '-TOGGLE_CRUD-' or event == '-TOGGLE_CRUD-1':
        # clearing child input fields on the child window
        clearInputs()
        # clearing the base input fields on the base window
        clearBaseInputs("base")
        # resetting the selected index for the child window (incase anything was selected before toggling)
        selectedIndex = -1
        # resetting the selected index for the parent window (incase anything was selected before toggling)
        selectedIndexBase = -1
        # invoking the method for changing the layout
        toggleCrud()
    # add button clicked on the parent window
    elif event == '-ADD_BTN-base':
        # invoking the function for adding data to parent
        addBaseData(values)
        # getting the primary key from the config file
        primaryKey = globals.config["app-params"]["primaryKey"]
        # invoking the method for updating table data and global variable for child
        updateGlobalsAndTableData(primaryKey, globals.baseRecord[0][primaryKey])
    elif event == '-UPDATE_BTN-base':
        # checking if a row has been selected from the table
        if selectedIndexBase > -1:
            # invoking the function which returns a boolean about the update status
            isUpdated = updateBaseData(selectedIndexBase)
            # checking if it was updated
            if isUpdated:
                # showing pop up for successful update
                sg.popup("Update successful!")
                # getting the primary key from config
                primaryKey = globals.config["app-params"]["primaryKey"]
                # updating global variables and table data
                updateGlobalsAndTableData(primaryKey, globals.baseRecord[0][primaryKey])
                # resetting the selected data
                selectedIndexBase = -1
        else:
            # showing popup if no row was selected
            sg.popup("No row selected from the table")
    # checking if the delete button was clicked on parent window
    elif event == '-DELETE_BTN-base':
        # checking if a row was selected or not
        if selectedIndexBase > -1:
            # deleting parent data
            deleteBaseData(selectedIndexBase)
            # getting primary key from config
            primaryKey = globals.config["app-params"]["primaryKey"]
            # updating global variables and table data
            updateGlobalsAndTableData(primaryKey, globals.baseRecord[0][primaryKey])
            # clearing the input fields for base
            clearBaseInputs("base")
            # showing popup for successful update
            sg.popup("Deleted successfully!")
        else:
            # showing popup if no row was selected
            sg.popup("No row selected from the table")
        # resetting the selected row
        selectedIndexBase = -1 
    # this event triggers when a row is selected from the table on the parent window
    elif event == '-INFO_TABLE-base':
        try:
            # storing the selected index on the global variable
            selectedIndexBase = values['-INFO_TABLE-base'][0]
            # getting teh selected data from the global variable
            selectedDataBase = globals.baseRecord[selectedIndexBase]
            # populating the input fields for parent window
            populateInputFieldsBase(selectedDataBase, "base")
        except Exception as e:
            return

# [am-01] main function. the app starts here
if __name__ == "__main__":  
    # invoking the method for connecting to database
    connectToDatabase() 
    # creating the variable for layout
    layout = []
    # checking if the config file only allows to do CRUD on parent or not
    if globals.config["app-params"]["isParentChild"] == "1":
        # layout for CRUD on child and parent both
        layout = [
            [   
                # this column is visible by default you can change the UI toggling the toggle button
                sg.Column(historyLayout(), element_justification='center', visible=True, key='-HISTORY_LAYOUT-', scrollable=True,  vertical_scroll_only=False, size=(1400, 750)), 
                # this column is visible by default you can change the UI toggling the toggle button
                sg.Column(baseLayout(), element_justification='center', visible=False, key='-BASE_LAYOUT-', scrollable=True,  vertical_scroll_only=False, size=(1400, 750)),
            ]
        ]
    else:
        # layout for CRUD on only parent
        layout = [
            [   
                
                # this column is invisible
                sg.Column(historyLayout(), element_justification='center', visible=False, key='-HISTORY_LAYOUT-', scrollable=True,  vertical_scroll_only=False, size=(1400, 750)), 
                # this column is visible by default and you CAN NOT change the UI by toggling the toggle button because the config file won't allow to have a CRUD on child
                sg.Column(baseLayout(), element_justification='center', visible=True, key='-BASE_LAYOUT-', scrollable=True,  vertical_scroll_only=False, size=(1400, 750)),
            ]
        ]
    
    # setting the window using the layout
    globals.window = sg.Window('Dynamic CRUD', layout, size=(1400, 750), element_justification="center")
    
    while True:
        # reading the events and the values from the UI
        globals.event, globals.values = globals.window.read()
        # getting the close event from the UI
        if globals.event == sg.WIN_CLOSED or globals.event == 'Cancel' or globals.event == 'Cancel0': # if user closes window or clicks cancel
            break
        # method for handling events from the UI
        handleEvents(globals.event, globals.values)
    # closing the window after the loop ends
    globals.window.close()