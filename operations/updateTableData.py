
import globalStore.globals as globals
from operations.processDataForTable import processDataForTable
import globalStore.globals as globals

# [am-08] updating table data for child based on the global variable for child
def updateTableData():
    # invoking the function for getting the processed table data for showing on the UI and storing it in a variable
    tableData = processDataForTable(globals.data)
    # updating the child table UI
    globals.window['-INFO_TABLE-'].update(tableData)