from globalStore import globals
from operations.updateTableData import updateTableData
from operations.deleteFromMongoDB import deleteFromMongoDB
# from operations.updateInJSON import updateInJSON

def deleteData(index):
    deleteFromMongoDB(globals.data[index]["_id"])
    globals.data.remove(globals.data[index])
    updateTableData()
    
