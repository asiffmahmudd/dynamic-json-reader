from globalStore import globals
from operations.updateTableData import updateTableData
from operations.deleteFromMongoDB import deleteFromMongoDB
# from operations.updateInJSON import updateInJSON

def deleteData(index):
    globals.data.remove(globals.data[index])
    deleteFromMongoDB(globals.data[index]["_id"])
    updateTableData()
    
