import globalStore.globals as globals
from validation.isEmpty import isEmpty
from validation.isInt import isInt
from validation.isDate import isDate

def isValid(values):
    listObject = list(globals.data.keys())[0]
    fields = list(globals.data[listObject][0].keys())
    fieldLen = len(fields)
    validData = {}
    errorMsg = ""
    errorCode = 0
    for i in range(fieldLen):
        inputKey = "-input"+str(i)+"-"
        if isEmpty(values[inputKey]):
            errorCode = 1
            errorMsg += fields[i] + " cannot be empty!\n"
        elif globals.dataTypes[inputKey] is int:
            if not isInt(values[inputKey]):
                errorCode = 1
                errorMsg += fields[i] + " is invalid!\n"
        elif globals.dataTypes[inputKey] == 'date':
            if not isDate(values[inputKey]):
                errorCode = 1
                errorMsg += fields[i] + " is invalid!\n"
        
        if errorCode != 1:
            validData[fields[i]] = values[inputKey]
                

    return [errorCode, errorMsg, validData]