from validation.isEmpty import isEmpty

# [am-05] function for checking for valid data
# the actionOn variable decides if the validation is for parent or child
def isValid(values, struct, actionOn=""):
    # getting the fields from the passed structure
    fields = list(struct.keys())
    # dictionary for returning valid data
    validData = {}
    # variable for returning error message, if there's any
    errorMsg = ""
    # variable for returning if there was any error found or not
    errorCode = 0
    # loop for checking each fields
    for inputKey in fields:
        # avoiding the '_id' field
        if inputKey == '_id':
            continue
        # checking if the field is required and if it's empty or not
        if struct[inputKey]["required"] == "true" and isEmpty(values[inputKey+actionOn]):
            # setting the error code
            errorCode = 1
            # setting the error message
            errorMsg += inputKey + " cannot be empty!\n"
        # checking if the structure had double variable for this particular field
        elif struct[inputKey]["type"] == "double":            
            try:
                # Convert it into float
                validData[inputKey] = float(values[inputKey+actionOn])
            except ValueError:
                errorCode = 1
                errorMsg += inputKey + " is invalid!\n"
        # checking if the structure had int variable for this particular field
        elif struct[inputKey]["type"] == "int":
            try:
                # Convert it into integer
                validData[inputKey] = int(values[inputKey+actionOn])
            except ValueError:
                errorCode = 1
                errorMsg += inputKey + " is invalid!\n"
        # this is for all string values
        else:
            validData[inputKey] = values[inputKey+actionOn]
    
    return [errorCode, errorMsg, validData]