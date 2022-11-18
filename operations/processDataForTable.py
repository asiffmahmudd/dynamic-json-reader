def processDataForTable(data): 
    temp = []
    for row in data:
        if "_id" in list(row.keys()):
            row.pop("_id")
        rowData = []
        for val in row.values(): 
            rowData.append(val)
        temp.append(rowData)
    return temp