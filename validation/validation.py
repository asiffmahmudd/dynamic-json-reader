import globalStore.globals as globals
from validation.isEmpty import isEmpty
from validation.isInt import isInt
from validation.isDate import isDate

def isValid(values, struct, actionOn=""):
    fields = list(struct.keys())
    validData = {}
    errorMsg = ""
    errorCode = 0
    # print(values)
    for inputKey in fields:
        if inputKey == '_id':
            continue
        if struct[inputKey]["required"] == "true" and isEmpty(values[inputKey+actionOn]):
            errorCode = 1
            errorMsg += inputKey + " cannot be empty!\n"
        elif struct[inputKey]["type"] == "textfield" and struct[inputKey]["isNumeric"] == "true":
            
            try:
                # Convert it into integer
                validData[inputKey] = int(values[inputKey+actionOn])
            except ValueError:
                try:
                    # Convert it into float
                    validData[inputKey] = float(values[inputKey+actionOn])
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
            validData[inputKey] = values[inputKey+actionOn]
    return [errorCode, errorMsg, validData]