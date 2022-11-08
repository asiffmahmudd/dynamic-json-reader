def processDataForTable(data): 
    temp = []
    for row in data:
        rowData = []
        for val in row.values(): 
            rowData.append(val)
        temp.append(rowData)
    return temp