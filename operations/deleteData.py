from globalStore import globals
from operations.updateTableData import updateTableData
from operations.deleteFromMongoDB import deleteFromMongoDB

# [am-14] delete function for child
def deleteData(index):
    # invoking function for deleting data from the database using id
    deleteFromMongoDB(globals.data[index]["_id"])
    # removing data from the global variable to make changes in the UI
    globals.data.remove(globals.data[index])
    # updating table data according to updated global variable to reflect teh changes on UI
    updateTableData()
    
