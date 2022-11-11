from globalStore import globals
from operations.updateTableData import updateTableData
from operations.updateInJSON import updateInJSON

def deleteData(index):
    globals.info.remove(globals.info[index])
    updateInJSON()
    updateTableData()
    
