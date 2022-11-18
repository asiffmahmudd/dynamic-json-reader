import globalStore.globals as globals
from validation.isEmpty import isEmpty
from validation.isInt import isInt
from validation.isDate import isDate

def isValid(values):
    fields = list(globals.historyStruct.keys())
    validData = {}
    errorMsg = ""
    errorCode = 0
    # print(values)
    for inputKey in fields:
        if inputKey == "_id":
            continue
        if globals.historyStruct[inputKey]["required"] == "true" and isEmpty(values[inputKey]):
            errorCode = 1
            errorMsg += inputKey + " cannot be empty!\n"
        elif globals.historyStruct[inputKey]["type"] == "textfield" and globals.historyStruct[inputKey]["isNumeric"] == "true":
            
            try:
                # Convert it into integer
                validData[inputKey] = int(values[inputKey])
            except ValueError:
                try:
                    # Convert it into float
                    validData[inputKey] = float(values[inputKey])
                except ValueError:
                    errorCode = 1
                    errorMsg += inputKey + " is invalid!\n"
    #     elif globals.dataTypes[inputKey] == 'date':
    #         if not isDate(values[inputKey]):
    #             errorCode = 1
    #             errorMsg += fields[i] + " is invalid!\n"
    #         else:
    #             validData[fields[i]] = values[inputKey]
        else:
            validData[inputKey] = values[inputKey]
    return [errorCode, errorMsg, validData]