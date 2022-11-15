
import globalStore.globals as globals
from operations.processDataForTable import processDataForTable
import globalStore.globals as globals

def updateTableData():
    tableData = processDataForTable(globals.data[list(globals.data.keys())[0]])
    globals.modalwindow['-INFO_TABLE-'].update(tableData)