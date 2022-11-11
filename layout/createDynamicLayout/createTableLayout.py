import PySimpleGUI as sg
import globalStore.globals as globals
from styles.defaultStyles import default_text_style
from operations.processDataForTable import processDataForTable

#function: Edit tab layout for editing users
def createTableLayout():
    text_style = default_text_style()
    data = globals.data['info']

    data_headings = []
    if len(data) > 0:
        data_headings = list(data[0].keys())
        data = processDataForTable(data)

    return [
        [
            sg.Table(
                values=data, 
                headings=data_headings,
                max_col_width=10,
                def_col_width=10,
                auto_size_columns=False,
                display_row_numbers=True,
                vertical_scroll_only=False,
                justification='left',
                enable_events=True,
                font=text_style['font'],
                size=text_style['size'],
                num_rows=6, 
                key='-INFO_TABLE-',
            )
        ]
    ]