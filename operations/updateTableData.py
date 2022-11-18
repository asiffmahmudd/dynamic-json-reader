
import globalStore.globals as globals
from operations.processDataForTable import processDataForTable
import globalStore.globals as globals

def updateTableData():
    tableData = processDataForTable(globals.data)
    globals.window['-INFO_TABLE-'].update(tableData)