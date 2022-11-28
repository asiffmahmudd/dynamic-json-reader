
import globalStore.globals as globals
from operations.processDataForTable import processDataForTable
import globalStore.globals as globals

def updateBaseTableData():
    tableData = processDataForTable(globals.baseRecord)
    globals.window['-INFO_TABLE-base'].update(tableData)