from globalStore import globals
from operations.updateTableData import updateTableData
from operations.updateInJSON import updateInJSON

def deleteData(index):
    listKey = list(globals.data.keys())[0]
    globals.data[listKey].remove(globals.data[listKey][index])
    updateInJSON()
    updateTableData()
    
