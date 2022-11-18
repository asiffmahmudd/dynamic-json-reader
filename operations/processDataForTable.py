def processDataForTable(data): 
    temp = []
    for row in data:
        rowData = []
        for key, val in row.items(): 
            if key == '_id':
                continue
            rowData.append(val)
        temp.append(rowData)
    return temp