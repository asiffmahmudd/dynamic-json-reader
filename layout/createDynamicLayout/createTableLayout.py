import PySimpleGUI as sg
import globalStore.globals as globals
from styles.defaultStyles import default_text_style
from operations.processDataForTable import processDataForTable
from operations.getStructFromMongo import getStructFromMongo
from operations.getHistory import getHistory
from operations.getDropDownValues import getDropDownValues

# [am-37] table layout main function
def createTableLayout():
    text_style = default_text_style()
    # get the structure for child from database
    record = getStructFromMongo(globals.config["app-params"]["historyStructCollection"])
    # removing id as we are not going to show it on the UI
    record.pop("_id")
    # headers for table columns
    data_headings = list(record.keys())
    # defining column widths based on number of fields
    col_width = int(100/len(globals.historyStruct)) + 2
    
    # getting the dropdown values for primary key
    values = getDropDownValues(globals.config["app-params"]["primaryKey"])
    if len(values) > 0:
        keyValue = values[0]
        data = getHistory(globals.config["app-params"]["primaryKey"], keyValue)
        tableData = processDataForTable(data)
    else:
        tableData = ""
    return [
        [
            sg.Table(
                values=tableData, 
                headings=data_headings,
                max_col_width=col_width,
                def_col_width=col_width,
                auto_size_columns=False,
                display_row_numbers=True,
                vertical_scroll_only=False,
                justification='center',
                enable_events=True,
                font=text_style['font'],
                size=text_style['size'],
                num_rows=6,
                key='-INFO_TABLE-',
            )
        ]
    ]