# [am-09] process table data so that all infos can be appended to table rows
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