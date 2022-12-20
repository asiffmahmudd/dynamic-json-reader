
import globalStore.globals as globals
from operations.processDataForTable import processDataForTable
import globalStore.globals as globals

# [am-24] function: for updating table data for the parent window
def updateBaseTableData():
    # processing the table data to show on the UI and updating the window
    tableData = processDataForTable(globals.baseRecord)
    globals.window['-INFO_TABLE-base'].update(tableData)