import PySimpleGUI as sg
import globalStore.globals as globals
from styles.defaultStyles import default_text_style
from operations.processDataForTable import processDataForTable
from operations.getStructFromMongo import getStructFromMongo
from operations.getHistory import getHistory
from operations.getDropDownValues import getDropDownValues

#function: Edit tab layout for editing users
def createTableLayout(actionOn):
    text_style = default_text_style()
    record = getStructFromMongo(globals.config["app-params"]["baseStructCollection"])
    record.pop("_id")
    data_headings = list(record.keys())
    
    tableData = processDataForTable(globals.baseRecord)

    return [
        [
            sg.Table(
                values=tableData, 
                headings=data_headings,
                max_col_width=18,
                def_col_width=18,
                auto_size_columns=False,
                display_row_numbers=True,
                vertical_scroll_only=False,
                justification='center',
                enable_events=True,
                font=text_style['font'],
                size=text_style['size'],
                num_rows=6,
                key='-INFO_TABLE-'+actionOn,
            )
        ]
    ]